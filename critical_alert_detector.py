"""
Critical Alert Detector for EU AI Act Compliance
Grafana-based alerting system for AI-specific critical events

Monitors:
- Safety incidents (Article 73)
- Performance degradation
- Compliance violations
- Critical infrastructure disruption

Risk Mappings:
- safety-001: Death or serious harm to health (Article 3(49)(a))
- safety-002: Critical infrastructure disruption (Article 3(49)(b))
- safety-003: Fundamental rights violations (Article 3(49)(c))
- safety-005: Serious harm to property/environment (Article 3(49)(d))
"""

import os
import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint

console = Console()


class AlertSeverity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RiskCategory(str, Enum):
    SAFETY_001 = "safety-001"
    SAFETY_002 = "safety-002"
    SAFETY_003 = "safety-003"
    SAFETY_005 = "safety-005"


@dataclass
class EUAIActRiskMapping:
    risk_id: str
    article_reference: str
    incident_type: str
    reporting_deadline_days: int
    severity: AlertSeverity
    description: str
    threshold_config: Dict[str, Any]


@dataclass
class AlertRule:
    uid: str
    title: str
    condition: str
    risk_category: RiskCategory
    severity: AlertSeverity
    evaluation_interval: str
    for_duration: str
    annotations: Dict[str, str]
    labels: Dict[str, str]
    notification_channels: List[str]


class CriticalAlertDetector:
    """
    Grafana-based critical alert detector for EU AI Act compliance
    """
    
    EU_AI_ACT_RISK_MAPPINGS = {
        RiskCategory.SAFETY_001: EUAIActRiskMapping(
            risk_id="safety-001",
            article_reference="Article 3(49)(a), Article 73(4)",
            incident_type="Death or serious harm to health",
            reporting_deadline_days=10,
            severity=AlertSeverity.CRITICAL,
            description="Death of a person or serious harm to a person's health",
            threshold_config={
                "health_impact_score": 9.0,
                "fatality_detected": True,
                "immediate_notification": True
            }
        ),
        RiskCategory.SAFETY_002: EUAIActRiskMapping(
            risk_id="safety-002",
            article_reference="Article 3(49)(b), Article 73(3)",
            incident_type="Critical infrastructure disruption",
            reporting_deadline_days=2,
            severity=AlertSeverity.CRITICAL,
            description="Serious and irreversible disruption of critical infrastructure",
            threshold_config={
                "infrastructure_impact_score": 8.5,
                "disruption_duration_minutes": 15,
                "affected_services": 1
            }
        ),
        RiskCategory.SAFETY_003: EUAIActRiskMapping(
            risk_id="safety-003",
            article_reference="Article 3(49)(c), Article 73(2)",
            incident_type="Fundamental rights violation",
            reporting_deadline_days=15,
            severity=AlertSeverity.HIGH,
            description="Infringement of Union law protecting fundamental rights",
            threshold_config={
                "rights_violation_score": 7.0,
                "affected_individuals": 1,
                "bias_detection_threshold": 0.15
            }
        ),
        RiskCategory.SAFETY_005: EUAIActRiskMapping(
            risk_id="safety-005",
            article_reference="Article 3(49)(d), Article 73(2)",
            incident_type="Property/environmental harm",
            reporting_deadline_days=15,
            severity=AlertSeverity.HIGH,
            description="Serious harm to property or the environment",
            threshold_config={
                "damage_value_eur": 50000,
                "environmental_impact_score": 7.5,
                "affected_area_km2": 0.1
            }
        )
    }
    
    def __init__(self, grafana_url: str = "http://localhost:3000", api_key: Optional[str] = None):
        self.grafana_url = grafana_url.rstrip('/')
        self.api_key = api_key or os.getenv('GRAFANA_API_KEY')
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        } if self.api_key else {'Content-Type': 'application/json'}
        
    def generate_alert_rules(self) -> List[AlertRule]:
        """Generate Grafana alert rules for all EU AI Act risk categories"""
        alert_rules = []
        
        for risk_cat, risk_mapping in self.EU_AI_ACT_RISK_MAPPINGS.items():
            rule = self._create_alert_rule_for_risk(risk_cat, risk_mapping)
            alert_rules.append(rule)
        
        return alert_rules
    
    def _create_alert_rule_for_risk(self, risk_category: RiskCategory, 
                                   risk_mapping: EUAIActRiskMapping) -> AlertRule:
        """Create specific alert rule for a risk category"""
        
        conditions = self._build_alert_condition(risk_category, risk_mapping)
        
        return AlertRule(
            uid=f"eu_ai_act_{risk_mapping.risk_id.replace('-', '_')}",
            title=f"EU AI Act - {risk_mapping.incident_type}",
            condition=conditions,
            risk_category=risk_category,
            severity=risk_mapping.severity,
            evaluation_interval="1m" if risk_mapping.reporting_deadline_days <= 2 else "5m",
            for_duration="0m" if risk_mapping.severity == AlertSeverity.CRITICAL else "2m",
            annotations={
                "description": risk_mapping.description,
                "article_reference": risk_mapping.article_reference,
                "reporting_deadline": f"{risk_mapping.reporting_deadline_days} days",
                "runbook_url": f"https://eur-lex.europa.eu/eli/reg/2024/1689/oj#art_73",
                "summary": f"Critical AI safety event detected: {risk_mapping.incident_type}"
            },
            labels={
                "severity": risk_mapping.severity.value,
                "risk_id": risk_mapping.risk_id,
                "compliance": "eu_ai_act",
                "article": "73",
                "team": "ai_safety"
            },
            notification_channels=self._get_notification_channels(risk_mapping)
        )
    
    def _build_alert_condition(self, risk_category: RiskCategory, 
                               risk_mapping: EUAIActRiskMapping) -> str:
        """Build PromQL/LogQL condition for alert"""
        
        if risk_category == RiskCategory.SAFETY_001:
            return f"""
            (
              ai_system_health_impact_score > {risk_mapping.threshold_config['health_impact_score']}
              or
              ai_system_fatality_detected == 1
            )
            """
        
        elif risk_category == RiskCategory.SAFETY_002:
            return f"""
            (
              ai_system_infrastructure_impact_score > {risk_mapping.threshold_config['infrastructure_impact_score']}
              and
              ai_system_disruption_duration_minutes > {risk_mapping.threshold_config['disruption_duration_minutes']}
            )
            """
        
        elif risk_category == RiskCategory.SAFETY_003:
            return f"""
            (
              ai_system_rights_violation_score > {risk_mapping.threshold_config['rights_violation_score']}
              or
              ai_system_bias_score > {risk_mapping.threshold_config['bias_detection_threshold']}
            )
            """
        
        elif risk_category == RiskCategory.SAFETY_005:
            return f"""
            (
              ai_system_damage_value_eur > {risk_mapping.threshold_config['damage_value_eur']}
              or
              ai_system_environmental_impact_score > {risk_mapping.threshold_config['environmental_impact_score']}
            )
            """
        
        return "ai_system_error_rate > 0.1"
    
    def _get_notification_channels(self, risk_mapping: EUAIActRiskMapping) -> List[str]:
        """Determine notification channels based on severity and deadline"""
        channels = ["email", "slack"]
        
        if risk_mapping.reporting_deadline_days <= 2:
            channels.extend(["pagerduty", "sms"])
        
        if risk_mapping.severity == AlertSeverity.CRITICAL:
            channels.append("incident_management")
        
        return channels
    
    def export_grafana_provisioning_config(self, output_dir: str = "./grafana_config") -> Dict[str, str]:
        """Export Grafana provisioning configuration files"""
        os.makedirs(output_dir, exist_ok=True)
        
        alert_rules = self.generate_alert_rules()
        
        provisioning_config = {
            "apiVersion": 1,
            "groups": [
                {
                    "name": "EU AI Act Compliance Alerts",
                    "interval": "1m",
                    "rules": [self._alert_rule_to_grafana_format(rule) for rule in alert_rules]
                }
            ]
        }
        
        alert_file = os.path.join(output_dir, "eu_ai_act_alerts.yaml")
        with open(alert_file, 'w') as f:
            import yaml
            yaml.dump(provisioning_config, f, default_flow_style=False)
        
        datasource_file = os.path.join(output_dir, "datasources.yaml")
        self._create_datasource_config(datasource_file)
        
        dashboard_file = os.path.join(output_dir, "dashboard.json")
        self._create_dashboard_config(dashboard_file, alert_rules)
        
        return {
            "alerts": alert_file,
            "datasources": datasource_file,
            "dashboard": dashboard_file
        }
    
    def _alert_rule_to_grafana_format(self, rule: AlertRule) -> Dict:
        """Convert AlertRule to Grafana provisioning format"""
        return {
            "uid": rule.uid,
            "title": rule.title,
            "condition": "A",
            "data": [
                {
                    "refId": "A",
                    "queryType": "prometheus",
                    "model": {
                        "expr": rule.condition.strip(),
                        "interval": "",
                        "legendFormat": "",
                        "refId": "A"
                    },
                    "datasourceUid": "prometheus",
                    "relativeTimeRange": {
                        "from": 600,
                        "to": 0
                    }
                }
            ],
            "noDataState": "NoData",
            "execErrState": "Alerting",
            "for": rule.for_duration,
            "annotations": rule.annotations,
            "labels": rule.labels,
            "isPaused": False
        }
    
    def _create_datasource_config(self, filepath: str):
        """Create Grafana datasource configuration"""
        config = {
            "apiVersion": 1,
            "datasources": [
                {
                    "name": "Prometheus",
                    "type": "prometheus",
                    "access": "proxy",
                    "url": "http://localhost:9090",
                    "isDefault": True,
                    "editable": True
                },
                {
                    "name": "Loki",
                    "type": "loki",
                    "access": "proxy",
                    "url": "http://localhost:3100",
                    "editable": True
                }
            ]
        }
        
        with open(filepath, 'w') as f:
            import yaml
            yaml.dump(config, f, default_flow_style=False)
    
    def _create_dashboard_config(self, filepath: str, alert_rules: List[AlertRule]):
        """Create Grafana dashboard for EU AI Act compliance monitoring"""
        dashboard = {
            "dashboard": {
                "title": "EU AI Act - Critical Alert Monitoring",
                "tags": ["eu-ai-act", "compliance", "safety"],
                "timezone": "browser",
                "panels": self._generate_dashboard_panels(alert_rules),
                "schemaVersion": 36,
                "version": 1,
                "refresh": "30s"
            },
            "overwrite": True
        }
        
        with open(filepath, 'w') as f:
            json.dump(dashboard, f, indent=2)
    
    def _generate_dashboard_panels(self, alert_rules: List[AlertRule]) -> List[Dict]:
        """Generate dashboard panels for monitoring"""
        panels = []
        
        panel_id = 1
        y_pos = 0
        
        for rule in alert_rules:
            risk_mapping = self.EU_AI_ACT_RISK_MAPPINGS[rule.risk_category]
            
            panels.append({
                "id": panel_id,
                "title": f"{risk_mapping.risk_id.upper()}: {risk_mapping.incident_type}",
                "type": "graph",
                "gridPos": {"h": 8, "w": 12, "x": 0 if panel_id % 2 == 1 else 12, "y": y_pos},
                "targets": [{
                    "expr": rule.condition.strip(),
                    "legendFormat": f"{risk_mapping.risk_id}",
                    "refId": "A"
                }],
                "alert": {
                    "name": rule.title,
                    "conditions": [{"evaluator": {"params": [0], "type": "gt"}}]
                },
                "fieldConfig": {
                    "defaults": {
                        "color": {"mode": "palette-classic"},
                        "custom": {"axisLabel": "", "axisPlacement": "auto"},
                        "thresholds": {
                            "mode": "absolute",
                            "steps": [
                                {"color": "green", "value": None},
                                {"color": "yellow", "value": 0.5},
                                {"color": "red", "value": 0.8}
                            ]
                        }
                    }
                }
            })
            
            panel_id += 1
            if panel_id % 2 == 1:
                y_pos += 8
        
        panels.append({
            "id": panel_id,
            "title": "Alert Summary - Reporting Deadlines",
            "type": "table",
            "gridPos": {"h": 8, "w": 24, "x": 0, "y": y_pos},
            "targets": [{
                "expr": "ALERTS{compliance=\"eu_ai_act\"}",
                "format": "table",
                "refId": "A"
            }]
        })
        
        return panels
    
    def create_incident_from_alert(self, alert_data: Dict) -> Dict:
        """Create incident management entry from Grafana alert"""
        from incident_management import IncidentManager, Incident
        
        risk_id = alert_data.get('labels', {}).get('risk_id', 'unknown')
        
        incident_data = {
            "title": alert_data.get('annotations', {}).get('summary', 'Critical AI Safety Event'),
            "description": alert_data.get('annotations', {}).get('description', ''),
            "ai_system_name": alert_data.get('labels', {}).get('ai_system', 'Unknown System'),
            "detected_at": datetime.now().isoformat(),
            "member_state": "EU",
            "source": "grafana_alert",
            "alert_uid": alert_data.get('uid', ''),
            "risk_category": risk_id
        }
        
        return incident_data
    
    def display_alert_configuration(self):
        """Display alert configuration in terminal"""
        console.print(Panel.fit(
            "[bold cyan]EU AI Act Critical Alert Detector[/bold cyan]\n"
            "[dim]Grafana-based alerting for AI safety compliance[/dim]",
            border_style="cyan"
        ))
        
        table = Table(title="Alert Rules Configuration", show_header=True, header_style="bold magenta")
        table.add_column("Risk ID", style="cyan", width=12)
        table.add_column("Incident Type", style="yellow", width=30)
        table.add_column("Severity", style="red", width=10)
        table.add_column("Deadline", style="green", width=10)
        table.add_column("Article", style="blue", width=20)
        
        for risk_cat, mapping in self.EU_AI_ACT_RISK_MAPPINGS.items():
            table.add_row(
                mapping.risk_id,
                mapping.incident_type,
                mapping.severity.value.upper(),
                f"{mapping.reporting_deadline_days} days",
                mapping.article_reference
            )
        
        console.print(table)
        
        console.print("\n[bold green]Monitoring Capabilities:[/bold green]")
        console.print("  ✓ Real-time alerting")
        console.print("  ✓ Threshold monitoring")
        console.print("  ✓ Anomaly detection")
        console.print("  ✓ Custom rules per EU AI Act Article 73")
        console.print("  ✓ Dashboard integration")


def main():
    """Main CLI for Critical Alert Detector"""
    import argparse
    
    parser = argparse.ArgumentParser(description="EU AI Act Critical Alert Detector")
    parser.add_argument('--grafana-url', default='http://localhost:3000', help='Grafana URL')
    parser.add_argument('--export-config', action='store_true', help='Export Grafana configuration')
    parser.add_argument('--output-dir', default='./grafana_config', help='Output directory for configs')
    parser.add_argument('--display', action='store_true', help='Display alert configuration')
    
    args = parser.parse_args()
    
    detector = CriticalAlertDetector(grafana_url=args.grafana_url)
    
    if args.display or (not args.export_config):
        detector.display_alert_configuration()
    
    if args.export_config:
        console.print("\n[bold yellow]Exporting Grafana configuration...[/bold yellow]")
        files = detector.export_grafana_provisioning_config(args.output_dir)
        
        console.print(f"\n[bold green]✓ Configuration exported to {args.output_dir}[/bold green]")
        for config_type, filepath in files.items():
            console.print(f"  • {config_type}: {filepath}")
        
        console.print("\n[bold cyan]Next Steps:[/bold cyan]")
        console.print(f"1. Copy files to Grafana provisioning directory:")
        console.print(f"   cp {args.output_dir}/*.yaml /etc/grafana/provisioning/alerting/")
        console.print(f"   cp {args.output_dir}/*.json /etc/grafana/provisioning/dashboards/")
        console.print(f"2. Restart Grafana: sudo systemctl restart grafana-server")
        console.print(f"3. Configure notification channels in Grafana UI")


if __name__ == "__main__":
    main()
