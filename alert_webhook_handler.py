"""
Webhook handler for Grafana alerts
Integrates with incident management system for EU AI Act compliance
"""

from flask import Flask, request, jsonify
from datetime import datetime
from typing import Dict, Any
import json
from rich.console import Console

console = Console()

app = Flask(__name__)


class AlertWebhookHandler:
    """
    Handles incoming Grafana alerts and creates incidents
    """
    
    def __init__(self):
        self.incident_manager = None
        self._load_incident_manager()
    
    def _load_incident_manager(self):
        """Load incident manager if available"""
        try:
            from incident_management import IncidentManager
            self.incident_manager = IncidentManager()
        except ImportError:
            console.print("[yellow]Warning: incident_management module not available[/yellow]")
    
    def process_alert(self, alert_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process incoming Grafana alert"""
        
        if alert_data.get('status') == 'firing':
            return self._handle_firing_alert(alert_data)
        elif alert_data.get('status') == 'resolved':
            return self._handle_resolved_alert(alert_data)
        
        return {'status': 'ignored', 'reason': 'unknown alert status'}
    
    def _handle_firing_alert(self, alert_data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a firing alert"""
        
        alerts = alert_data.get('alerts', [])
        results = []
        
        for alert in alerts:
            labels = alert.get('labels', {})
            annotations = alert.get('annotations', {})
            
            risk_id = labels.get('risk_id', 'unknown')
            severity = labels.get('severity', 'medium')
            
            console.print(f"\n[bold red]🚨 ALERT FIRING[/bold red]")
            console.print(f"Risk ID: {risk_id}")
            console.print(f"Severity: {severity}")
            console.print(f"Description: {annotations.get('description', 'N/A')}")
            
            if self.incident_manager and risk_id.startswith('safety-'):
                incident_data = self._create_incident_from_alert(alert)
                
                try:
                    from incident_management import Incident
                    incident = Incident(**incident_data)
                    self.incident_manager.save_incident(incident)
                    
                    if self.incident_manager.client:
                        severity, incident_type, days = self.incident_manager.classify_severity(incident)
                        
                        results.append({
                            'status': 'incident_created',
                            'incident_id': incident.incident_id,
                            'risk_id': risk_id,
                            'reporting_deadline_days': days,
                            'severity': severity.value if severity else 'unknown'
                        })
                    else:
                        results.append({
                            'status': 'incident_created_manual_classification_required',
                            'incident_id': incident.incident_id,
                            'risk_id': risk_id
                        })
                    
                    console.print(f"[green]✓ Incident created: {incident.incident_id}[/green]")
                    
                except Exception as e:
                    console.print(f"[red]Error creating incident: {e}[/red]")
                    results.append({
                        'status': 'error',
                        'error': str(e),
                        'risk_id': risk_id
                    })
            else:
                results.append({
                    'status': 'logged',
                    'risk_id': risk_id,
                    'note': 'No incident manager available or non-safety alert'
                })
        
        return {
            'status': 'processed',
            'alerts_processed': len(alerts),
            'results': results
        }
    
    def _handle_resolved_alert(self, alert_data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a resolved alert"""
        
        alerts = alert_data.get('alerts', [])
        
        for alert in alerts:
            labels = alert.get('labels', {})
            risk_id = labels.get('risk_id', 'unknown')
            
            console.print(f"\n[bold green]✓ ALERT RESOLVED[/bold green]")
            console.print(f"Risk ID: {risk_id}")
        
        return {
            'status': 'resolved',
            'alerts_resolved': len(alerts)
        }
    
    def _create_incident_from_alert(self, alert: Dict[str, Any]) -> Dict[str, Any]:
        """Create incident data structure from alert"""
        
        labels = alert.get('labels', {})
        annotations = alert.get('annotations', {})
        
        return {
            'title': annotations.get('summary', labels.get('alertname', 'Unknown Alert')),
            'description': f"{annotations.get('description', '')}\n\nAlert Details:\n{json.dumps(alert, indent=2)}",
            'ai_system_name': labels.get('ai_system', 'Unknown System'),
            'detected_at': datetime.now().isoformat(),
            'member_state': 'EU',
            'source': 'grafana_alert',
            'alert_uid': alert.get('fingerprint', ''),
            'risk_category': labels.get('risk_id', 'unknown'),
            'severity_level': labels.get('severity', 'medium')
        }


webhook_handler = AlertWebhookHandler()


@app.route('/api/alerts/webhook', methods=['POST'])
def handle_webhook():
    """Webhook endpoint for Grafana alerts"""
    
    try:
        alert_data = request.get_json()
        
        if not alert_data:
            return jsonify({'error': 'No data received'}), 400
        
        result = webhook_handler.process_alert(alert_data)
        
        return jsonify(result), 200
        
    except Exception as e:
        console.print(f"[red]Webhook error: {e}[/red]")
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'eu-ai-act-alert-webhook',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/api/alerts/test', methods=['POST'])
def test_alert():
    """Test endpoint to simulate an alert"""
    
    test_alert = {
        'status': 'firing',
        'alerts': [
            {
                'labels': {
                    'alertname': 'Test Alert',
                    'severity': 'critical',
                    'risk_id': 'safety-001',
                    'ai_system': 'test_system'
                },
                'annotations': {
                    'summary': 'Test critical safety alert',
                    'description': 'This is a test alert for safety-001',
                    'article_reference': 'Article 3(49)(a), Article 73(4)',
                    'reporting_deadline': '10 days'
                },
                'fingerprint': 'test123456',
                'startsAt': datetime.now().isoformat()
            }
        ]
    }
    
    result = webhook_handler.process_alert(test_alert)
    return jsonify(result), 200


if __name__ == '__main__':
    console.print("[bold cyan]Starting Alert Webhook Handler[/bold cyan]")
    console.print("Listening on http://localhost:8002")
    app.run(host='0.0.0.0', port=8002, debug=True)
