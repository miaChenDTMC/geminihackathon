# HITL Design: ai_act_cli.py (EU AI Act Query Assistant)

**Generated:** 2026-01-10  
**System:** EU AI Act Query Assistant v1.0.0  
**Skill Applied:** hitl-design

---

## 1. System Overview

| Attribute | Value |
|-----------|-------|
| **AI Function** | Legal/regulatory query answering using LLM (Gemini 3 Pro) |
| **Decision Impact** | **Medium** - Informational guidance on legal compliance |
| **Volume** | Low-Medium (individual user queries) |
| **Deployment** | CLI-based interactive system |
| **EU AI Act Classification** | Limited Risk (Article 50) |

### Current State Analysis

```text
┌─────────────────────────────────────────────────────────────────┐
│                    CURRENT HITL STATE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  User Query ──► AI Response ──► Display to User                 │
│                     │                                            │
│                     └──► Disclaimer: "Verify with legal counsel" │
│                                                                  │
│  Pattern: AI ONLY with Transparency Disclaimer                  │
│  Human Oversight: NONE (warning-based only)                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Current HITL Level:** 4 (Human-out-of-loop with post-hoc review only)

---

## 2. HITL Pattern Recommendation

### Recommended Pattern: **Human-on-the-Loop (Monitoring)**

```text
                    ┌─────────────────────────────┐
                    │     Admin Dashboard         │
                    │  • Query Analytics          │
                    │  • Response Quality Audit   │
                    │  • Flag Patterns            │
                    └─────────────┬───────────────┘
                                  │ Monitors
                                  ▼
    User Query ──► AI Response ──► Display ──► User Action
                        │
                        └──► Logging System
                                  │
                              ┌───┴───┐
                              │ Audit │
                              │ Trail │
                              └───────┘
```

### Justification

| Factor | Assessment | Recommendation |
|--------|------------|----------------|
| Stakes | Medium (legal guidance, not decisions) | Human-on-the-Loop |
| Reversibility | Fully reversible (information only) | Allow automation |
| Volume | Low-medium | Can support monitoring |
| Regulatory | Limited Risk (Art. 50) | Transparency + monitoring |
| Liability | User warned about AI limitations | Monitoring sufficient |

---

## 3. Routing Strategy

### Current State: No Routing (All Auto-Response)

### Recommended Routing Design

```python
class QueryRouter:
    """Route queries based on risk and complexity."""
    
    # Thresholds
    AUTO_RESPOND_CONFIDENCE = 0.85  # High confidence = auto-respond
    FLAG_FOR_REVIEW_CONFIDENCE = 0.60  # Low confidence = flag
    
    # High-risk query patterns (require flagging)
    HIGH_RISK_PATTERNS = [
        r"can I (legally|safely) deploy",    # Deployment decisions
        r"is (this|my) system (prohibited|banned)",  # Classification
        r"what are the (penalties|fines)",    # Enforcement
        r"how to avoid compliance",           # Potential evasion
        r"(GDPR|EU AI Act) (fine|penalty)",   # Legal consequences
    ]
    
    # Regulated categories requiring audit trail
    REGULATED_CATEGORIES = [
        "high_risk_classification",
        "prohibited_practices",
        "enforcement_penalties",
        "fundamental_rights",
        "biometric_systems",
    ]
    
    def route(self, query: str, confidence: float, category: str) -> RoutingDecision:
        # Always log all queries
        self.log_query(query)
        
        # Check for high-risk patterns
        if self.matches_high_risk_pattern(query):
            return RoutingDecision.FLAG_FOR_AUDIT
        
        # Check if regulated category
        if category in self.REGULATED_CATEGORIES:
            return RoutingDecision.FLAG_FOR_AUDIT
        
        # Low confidence responses should be flagged
        if confidence < self.FLAG_FOR_REVIEW_CONFIDENCE:
            return RoutingDecision.FLAG_FOR_REVIEW
        
        # Auto-respond with audit trail
        return RoutingDecision.AUTO_RESPOND_WITH_LOG
```

### Routing Decision Matrix

| Query Type | Confidence | Action | Audit Level |
|------------|------------|--------|-------------|
| General information | High (>85%) | Auto-respond | Standard log |
| General information | Medium (60-85%) | Auto-respond | Enhanced log |
| General information | Low (<60%) | Auto-respond + Flag | Review queue |
| High-risk patterns | Any | Auto-respond + Flag | Priority review |
| Regulated categories | Any | Auto-respond + Flag | Compliance audit |

---

## 4. Review Queue Design (For Flagged Queries)

### Queue Architecture

```python
class AuditQueue:
    """Queue for flagged queries requiring human review."""
    
    def __init__(self):
        self.queue = []
        
    def add_to_queue(self, item: AuditItem):
        item.priority = self.calculate_priority(item)
        item.sla_deadline = self.calculate_sla(item.priority)
        self.queue.append(item)
        
    def calculate_priority(self, item: AuditItem) -> str:
        if item.category == "prohibited_practices":
            return "CRITICAL"
        elif item.matches_high_risk_pattern:
            return "HIGH"
        elif item.confidence < 0.60:
            return "MEDIUM"
        else:
            return "LOW"

@dataclass
class AuditItem:
    id: str
    query: str
    response: str
    confidence: float
    category: str
    flags: List[str]
    timestamp: datetime
    priority: str = "LOW"
    sla_deadline: datetime = None
    reviewed_by: str = None
    review_outcome: str = None
```

### Prioritization

| Priority | SLA | Criteria | Action Required |
|----------|-----|----------|-----------------|
| **Critical** | 24 hours | Prohibited practices queries | Verify response accuracy |
| **High** | 48 hours | High-risk patterns detected | Review for misuse potential |
| **Medium** | 7 days | Low confidence responses | Quality check |
| **Low** | 30 days | Routine sampling | Random audit |

---

## 5. Review Interface Requirements

### Admin Dashboard Components

```markdown
## Audit Dashboard Layout

### 1. Queue Overview
┌─────────────────────────────────────────────────────────────────┐
│  PENDING REVIEWS                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Critical: [X]  │  High: [X]  │  Medium: [X]  │  Low: [X]       │
│  Oldest: [X days/hours]  │  SLA Breaches: [X]                   │
└─────────────────────────────────────────────────────────────────┘

### 2. Query Details View
┌─────────────────────────────────────────────────────────────────┐
│  Query ID: [UUID]              Priority: [CRITICAL/HIGH/...]    │
├─────────────────────────────────────────────────────────────────┤
│  User Query:                                                     │
│  ─────────────────────────────────────────────────────────────  │
│  [Full query text]                                               │
├─────────────────────────────────────────────────────────────────┤
│  AI Response:                                                    │
│  ─────────────────────────────────────────────────────────────  │
│  [Full response text with article citations highlighted]         │
├─────────────────────────────────────────────────────────────────┤
│  Flags: [HIGH_RISK_PATTERN] [LOW_CONFIDENCE]                    │
│  Confidence: [X%]                                                │
│  Category: [Classification/Enforcement/etc.]                    │
├─────────────────────────────────────────────────────────────────┤
│  Actions:                                                        │
│  [ Approve ] [ Flag Inaccurate ] [ Escalate ] [ Add Note ]      │
└─────────────────────────────────────────────────────────────────┘

### 3. Metrics Panel
- Daily query volume
- Response accuracy (sampled)
- Common query categories
- Flag frequency trends
```

### Reviewer Actions

| Action | Description | Effect |
|--------|-------------|--------|
| **Approve** | Response is accurate | Mark reviewed, update metrics |
| **Flag Inaccurate** | Response contains errors | Add to training data, alert |
| **Escalate** | Needs expert review | Route to legal/compliance |
| **Add Note** | Add context for future | Store annotation |

---

## 6. Escalation Path

```text
Level 1: Automated Flagging
    │
    ▼
Level 2: Admin Review (SLA: per priority)
    │
    ├──► Approve ──► Close
    │
    ├──► Flag Inaccurate ──► Model Improvement Queue
    │
    └──► Escalate
            │
            ▼
Level 3: Compliance Officer (SLA: 48 hours)
    │
    ├──► Resolution ──► Close + Document
    │
    └──► Escalate
            │
            ▼
Level 4: Legal Counsel (SLA: 5 business days)
    │
    └──► Final Resolution + Policy Update
```

### Escalation Triggers

| Trigger | Description | Target Level |
|---------|-------------|--------------|
| **Misinformation** | Response contradicts regulation | Level 3 |
| **Harmful advice** | Could lead to non-compliance | Level 3 |
| **Repeated pattern** | Same issue multiple times | Level 3 |
| **Legal interpretation** | Complex regulatory question | Level 4 |
| **Policy gap** | No clear guidance exists | Level 4 |

---

## 7. Feedback Loop

### Implementation for Model Improvement

```python
class FeedbackCollector:
    """Collect feedback from human reviews for improvement."""
    
    def record_feedback(self, audit_item: AuditItem, decision: str, notes: str):
        feedback = {
            "query": audit_item.query,
            "response": audit_item.response,
            "decision": decision,  # approve/inaccurate/escalate
            "notes": notes,
            "reviewer": audit_item.reviewed_by,
            "timestamp": datetime.now()
        }
        
        # Store for analysis
        self.store_feedback(feedback)
        
        # If inaccurate, add to training correction set
        if decision == "inaccurate":
            self.add_to_correction_set(feedback)
            
        # Check for patterns
        self.analyze_patterns()
    
    def analyze_patterns(self):
        """Detect systematic issues."""
        recent = self.get_recent_feedback(days=7)
        
        # Calculate disagreement rate
        disagreement_rate = len([f for f in recent if f["decision"] == "inaccurate"]) / len(recent)
        
        if disagreement_rate > 0.10:  # >10% inaccuracy
            self.alert_high_error_rate(disagreement_rate)
```

### Feedback Types

| Type | Collection Method | Use |
|------|-------------------|-----|
| **Accuracy** | Admin review decisions | Response quality tracking |
| **Usability** | User feedback (optional) | UX improvement |
| **Coverage gaps** | Escalated queries | Knowledge base expansion |
| **Patterns** | Automated analysis | System prompt refinement |

---

## 8. Metrics & Monitoring

### Key Performance Indicators

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Query volume | N/A | Not tracked | ⚠️ Needs implementation |
| Response latency | <5s | Not measured | ⚠️ Needs implementation |
| Flag rate | <10% | Not tracked | ⚠️ Needs implementation |
| Review accuracy | >95% | Not measured | ⚠️ Needs implementation |
| SLA compliance | >95% | N/A | ⚠️ Needs implementation |
| User satisfaction | >4/5 | Not collected | ⚠️ Needs implementation |

### Dashboard Metrics

```python
@dataclass
class HITLMetrics:
    """Dashboard metrics for HITL monitoring."""
    
    # Volume
    total_queries_today: int
    total_queries_week: int
    queries_flagged_today: int
    
    # Queue health
    pending_reviews: int
    pending_by_priority: Dict[str, int]
    oldest_pending_hours: float
    sla_breaches: int
    
    # Quality
    reviews_completed_today: int
    accuracy_rate_7day: float
    inaccuracy_rate_7day: float
    escalation_rate_7day: float
    
    # Trends
    volume_trend: List[int]  # Daily for last 30 days
    accuracy_trend: List[float]  # Weekly for last 12 weeks
```

### Alerting Thresholds

| Alert | Threshold | Severity |
|-------|-----------|----------|
| High error rate | >10% inaccurate in 24h | Critical |
| Queue backlog | >50 pending | High |
| SLA breach | Any critical item | High |
| Unusual volume | >3x normal | Medium |
| Low confidence spike | >20% low conf | Medium |

---

## 9. Implementation Roadmap

### Phase 1: Logging Foundation (Week 1-2)

```python
# Add to ai_act_cli.py
class QueryLogger:
    def __init__(self, log_path: str = "logs/queries.jsonl"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(exist_ok=True)
        
    def log(self, query: str, response: str, metadata: dict):
        entry = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "response_length": len(response),
            "response_preview": response[:500],
            **metadata
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
```

**Deliverables:**
- [ ] Query logging to JSONL file
- [ ] Basic metadata capture (timestamp, query length, response length)
- [ ] Log rotation (daily files)

### Phase 2: Query Classification (Week 3-4)

**Deliverables:**
- [ ] Pattern matching for high-risk queries
- [ ] Category classification (prohibition, high-risk, limited, minimal)
- [ ] Confidence scoring (if available from model)
- [ ] Flagging logic

### Phase 3: Admin Dashboard (Week 5-8)

**Deliverables:**
- [ ] Web-based admin interface
- [ ] Query review workflow
- [ ] Metrics visualization
- [ ] Export capabilities

### Phase 4: Feedback Integration (Week 9-12)

**Deliverables:**
- [ ] Feedback collection from reviews
- [ ] Pattern analysis automation
- [ ] System prompt improvement process
- [ ] Monthly quality reports

---

## 10. Validation Checklist

### HITL Design Checklist

- [ ] HITL pattern selected: **Human-on-the-Loop (Monitoring)**
- [ ] Routing criteria defined: **Confidence + Risk Pattern based**
- [ ] Review queue designed: **Priority-based with SLAs**
- [ ] Escalation path established: **4-level escalation**
- [ ] Interface requirements specified: **Admin dashboard design**
- [ ] SLAs defined: **24h Critical to 30d Low**
- [ ] Feedback loop implemented: **TBD**
- [ ] Metrics dashboard created: **TBD**
- [ ] Reviewer training planned: **TBD**
- [ ] Capacity planning completed: **TBD**

### Current Implementation Status

| Component | Status | Priority |
|-----------|--------|----------|
| Query Logging | ❌ Not implemented | **P0 - Critical** |
| Pattern Detection | ❌ Not implemented | **P1 - High** |
| Flagging System | ❌ Not implemented | **P1 - High** |
| Admin Dashboard | ❌ Not implemented | **P2 - Medium** |
| Metrics Collection | ❌ Not implemented | **P2 - Medium** |
| Feedback Loop | ❌ Not implemented | **P3 - Low** |

---

## 11. Integration with Other Skills

### Inputs From
- **ai-safety-planning** → Oversight requirements, risk thresholds
- **explainability-planning** → Review explanation formats
- **EU AI Act Article 14** → Human oversight legal requirements

### Outputs To
- **ml-project-lifecycle** → Feedback for model improvement
- **Application code** → Logging and flagging implementation
- **Operations** → Review staffing requirements

---

## 12. Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| HITL Design Lead | | | |
| Development Lead | | | |
| Operations Manager | | | |
| Compliance Officer | | | |

---

*This HITL Design was generated using the hitl-design skill based on analysis of ai_act_cli.py*
