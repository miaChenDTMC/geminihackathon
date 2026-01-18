# GDPR Compliance Assessment
## EU AI Act Query Assistant (`ai_act_cli.py`)

**Assessment Date:** 2026-01-10
**Regulation:** GDPR (Regulation EU 2016/679)
**System:** AI Act CLI Tool v1.0.0
**Data Controller:** [Your Organization]
**Assessment Type:** Privacy Impact Assessment

---

## Executive Summary

This assessment evaluates GDPR compliance for the EU AI Act Query Assistant, a conversational AI chatbot that processes user queries about EU regulations.

**Overall GDPR Compliance:** ⚠️ **PARTIALLY COMPLIANT**
**Risk Level:** MEDIUM (personal data processing without full safeguards)
**Critical Gaps:** 5 HIGH, 8 MEDIUM
**DPIA Required:** YES (Article 35 - automated decision-making with legal effects potential)

**Key Findings:**
- User queries may contain personal data (company names, roles, projects)
- Data sent to Google Gemini API (third-party processor)
- No Data Processing Agreement (DPA) with Google
- No privacy notice provided to users
- Session-only storage but no clear retention policy

---

## 1. Data Processing Overview

### 1.1 Personal Data Processed

**Data Categories:**

| Data Type | Source | Examples | GDPR Category | Sensitivity |
|-----------|--------|----------|---------------|-------------|
| **User Queries** | Direct input | "My company XYZ wants to deploy facial recognition..." | Personal data | MEDIUM-HIGH |
| **Company Information** | User queries | Company names, projects, AI systems being developed | Personal/Commercial | MEDIUM |
| **Job Roles** | User queries | "I'm a compliance officer at..." | Personal data | LOW |
| **Technical Metadata** | System logs | Timestamps, session IDs (if implemented) | Personal data | LOW |
| **IP Address** | Network layer | User's IP (if logged) | Personal data | MEDIUM |
| **No Storage** | - | System does NOT persistently store queries | - | - |

**Special Categories (Article 9 - Prohibited without explicit consent):**
- ❌ Racial/ethnic origin: Not collected
- ❌ Political opinions: Not collected
- ❌ Religious beliefs: Not collected
- ❌ Health data: Not collected
- ❌ Biometric data: Not collected
- ❌ Genetic data: Not collected
- ⚠️ **Trade union membership:** Could appear in queries (e.g., "Our union is concerned about...")

**Criminal Convictions (Article 10):**
- ⚠️ Users might mention legal cases or compliance issues
- Not systematically processed but could appear in queries

### 1.2 Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                         USER                                 │
│  (Data Subject - may include personal data in queries)       │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         │ Enters query (HTTPS in terminal)
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                  AI ACT CLI (Local)                          │
│  Controller: [Your Organization]                             │
│  Processing: Query received, no persistent storage           │
│  Data: User query text (may contain personal data)           │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         │ Sends query via HTTPS API
                         ▼
┌──────────────────────────────────────────────────────────────┐
│              GOOGLE GEMINI API (Cloud)                       │
│  Processor: Google LLC (USA - adequacy decision)             │
│  Processing: AI model inference                              │
│  Retention: Per Google AI ToS (~30 days typical)             │
│  Location: Google Cloud (likely USA or EU)                   │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         │ Returns AI-generated response
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                  AI ACT CLI (Local)                          │
│  Processing: Display response                                │
│  Data: Response text (may reference query data)              │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         │ Session ends (data cleared)
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                    DATA DELETION                             │
│  Local: Session data cleared on exit                         │
│  Google: Retained per Google's policy (30 days?)             │
└──────────────────────────────────────────────────────────────┘
```

### 1.3 Roles & Responsibilities

**Data Controller:** [Your Organization]
- Determines purposes and means of processing
- Responsible for GDPR compliance
- Must provide privacy notice
- Handles data subject rights requests

**Data Processor:** Google LLC
- Processes data on behalf of controller
- Bound by Data Processing Agreement (DPA)
- ⚠️ **MISSING: No DPA currently in place**

**Data Subjects:** End users of ai_act_cli.py
- Individuals making queries
- Have rights under GDPR Articles 12-22

---

## 2. Lawful Basis Assessment (Article 6)

### 2.1 Legal Basis Analysis

**Article 6(1) - Lawfulness of Processing:**

| Basis | Applicable? | Justification |
|-------|-------------|---------------|
| **a) Consent** | ⚠️ Possible | User voluntarily uses system, but no explicit consent mechanism |
| **b) Contract** | ❌ No | No contractual relationship with users |
| **c) Legal Obligation** | ❌ No | No legal obligation to provide this service |
| **d) Vital Interests** | ❌ No | Not necessary to protect life |
| **e) Public Interest** | ⚠️ Possible | Facilitating EU AI Act compliance (public interest) |
| **f) Legitimate Interest** | ✅ **RECOMMENDED** | Providing regulatory guidance is legitimate interest |

**Recommended Legal Basis:** **Article 6(1)(f) - Legitimate Interests**

**Justification:**
- **Legitimate Interest:** Helping organizations understand and comply with EU AI Act
- **Necessity:** Processing queries necessary to provide this service
- **Balancing Test:**
  - Controller interest: Provide compliance assistance
  - Data subject interest: Privacy of query data
  - Balance: Use session-only storage, transparency disclosures, no profiling
  - **Verdict:** Legitimate interest outweighs privacy risks with proper safeguards

**Alternative:** **Article 6(1)(a) - Consent** if you implement explicit opt-in

### 2.2 Legitimate Interest Assessment (LIA)

**Purpose:** Provide AI-powered EU AI Act information service

**Necessity Test:**
- ✅ Can the purpose be achieved without processing personal data? **NO** - queries inherently contain user context
- ✅ Is the processing proportionate? **YES** - only process what's necessary for response
- ✅ Are there less intrusive means? **PARTIALLY** - could anonymize but reduces utility

**Balancing Test:**

| Factor | Controller | Data Subject | Winner |
|--------|------------|--------------|--------|
| **Interest** | Provide regulatory guidance | Privacy of queries | Tie |
| **Impact** | High (business service) | Low-Medium (no sensitive data collection) | Controller |
| **Expectation** | Users expect AI processing | Users expect privacy | Data Subject |
| **Safeguards** | Session-only, no profiling | Strong if implemented | Data Subject |
| **Alternatives** | No viable alternative | Could use non-AI service | Controller |

**LIA Conclusion:** ✅ Legitimate interest is valid legal basis, **subject to implementing proper safeguards**

---

## 3. GDPR Principles Compliance (Article 5)

### 3.1 Principles Assessment

#### Principle 1: Lawfulness, Fairness, Transparency

| Requirement | Status | Evidence / Gap |
|-------------|--------|----------------|
| **Lawful basis** | ⚠️ Partial | Legitimate interest applicable, but not documented |
| **Fair processing** | ✅ Yes | System provides useful service, no deception |
| **Transparent** | ❌ NO | **No privacy notice provided** |

**Gap:** CRITICAL - No privacy notice explaining:
- What data is collected
- Why it's processed
- Who it's shared with (Google)
- User rights

---

#### Principle 2: Purpose Limitation

| Requirement | Status | Evidence / Gap |
|-------------|--------|----------------|
| **Specified purpose** | ⚠️ Partial | Purpose is regulatory Q&A, not formally documented |
| **Explicit purpose** | ❌ NO | No privacy notice with explicit purpose statement |
| **Legitimate purpose** | ✅ Yes | Providing legal information is legitimate |
| **No further processing** | ✅ Yes | Queries not used for other purposes (no analytics, marketing) |

**Gap:** Document purpose in privacy notice

---

#### Principle 3: Data Minimization

| Requirement | Status | Evidence / Gap |
|-------------|--------|----------------|
| **Adequate** | ✅ Yes | Need user query to provide response |
| **Relevant** | ✅ Yes | Only process query text, no extra data |
| **Limited** | ⚠️ Partial | Full query sent to Google (could redact PII first) |

**Score:** 2/3 - Good but could improve with PII redaction

---

#### Principle 4: Accuracy

| Requirement | Status | Evidence / Gap |
|-------------|--------|----------------|
| **Accurate data** | ✅ Yes | User provides own data, no stored profiles to become inaccurate |
| **Up to date** | ✅ Yes | Session-only, no stale data |
| **Rectification** | ✅ N/A | No persistent storage |
| **Erasure** | ✅ Yes | Data cleared on session end |

**Score:** 4/4 - Excellent (benefit of no storage)

---

#### Principle 5: Storage Limitation

| Requirement | Status | Evidence / Gap |
|-------------|--------|----------------|
| **Time-limited** | ✅ Yes | Session-only storage |
| **Periodic review** | ⚠️ Partial | No retention schedule documented |
| **Archiving** | ✅ N/A | No archiving for public interest |
| **Google retention** | ❌ Unknown | **Google's retention policy unclear** |

**Gap:** Need to document:
- Local retention: Session-only (documented in privacy notice)
- Google retention: Request clarification from Google (likely 30 days)

---

#### Principle 6: Integrity & Confidentiality (Security)

| Requirement | Status | Evidence / Gap |
|-------------|--------|----------------|
| **Appropriate security** | ⚠️ Partial | HTTPS encryption, but prompt injection vulnerabilities |
| **Confidentiality** | ⚠️ Partial | No encryption at rest (session only, so acceptable) |
| **Availability** | ⚠️ Partial | No rate limiting (DoS risk) |
| **Resilience** | ⚠️ Partial | No backup system (acceptable for stateless service) |

**Score:** 2/4 - See security assessment for details

---

#### Principle 7: Accountability

| Requirement | Status | Evidence / Gap |
|-------------|--------|----------------|
| **Demonstrate compliance** | ❌ NO | No GDPR compliance documentation |
| **Records of processing** | ❌ NO | No Article 30 register |
| **DPIA (if required)** | ❌ NO | **This document is the first DPIA** |
| **DPO (if required)** | ⚠️ Unknown | Depends on organization size/type |
| **Policies** | ❌ NO | No privacy policy, data protection policy |

**Score:** 0/5 - **CRITICAL GAP**

---

## 4. Data Subject Rights (Articles 12-22)

### 4.1 Rights Assessment

#### Right to Information (Articles 13-14)

**Status:** ❌ **NON-COMPLIANT**

**Required Information (Article 13):**

| Info Required | Status | Notes |
|---------------|--------|-------|
| **Controller identity** | ❌ Missing | Not stated in UI |
| **DPO contact** | ❌ Missing | Not stated |
| **Processing purpose** | ❌ Missing | Not stated (implied from context) |
| **Legal basis** | ❌ Missing | Not stated |
| **Recipients** | ❌ Missing | Google not mentioned in privacy context |
| **International transfers** | ❌ Missing | USA (Google) not mentioned |
| **Retention period** | ❌ Missing | Session-only not stated |
| **Data subject rights** | ❌ Missing | Rights not listed |
| **Right to withdraw** | ❌ Missing | Not applicable if using legitimate interest |
| **Right to complain** | ❌ Missing | No supervisory authority contact |
| **Automated decision-making** | ⚠️ Partial | Article 50 notice mentions AI, but not GDPR-specific |

**Compliance:** 0/11 - **CRITICAL GAP**

**Remediation:** Create privacy notice (template in Section 9)

---

#### Right of Access (Article 15)

**Status:** ⚠️ **PARTIALLY COMPLIANT**

| Requirement | Status | Feasibility |
|-------------|--------|-------------|
| **Confirm processing** | ✅ Can do | Check if query in Google's retention period |
| **Provide copy** | ⚠️ Difficult | Would need to request from Google |
| **Supplementary info** | ✅ Can do | Can provide: purpose, categories, recipients, retention |

**Implementation:** Need process to handle access requests (likely: "No data stored locally, contact Google for API retention data")

---

#### Right to Rectification (Article 16)

**Status:** ✅ **COMPLIANT (N/A)**

**Justification:** No persistent data stored, nothing to rectify. If Google retains query, user would need to contact Google (though this is impractical).

---

#### Right to Erasure (Article 17)

**Status:** ⚠️ **PARTIALLY COMPLIANT**

| Scenario | Status | Feasibility |
|----------|--------|-------------|
| **Local data** | ✅ Auto-erased | Session ends, data cleared |
| **Google data** | ❌ Cannot erase | No mechanism to request deletion from Google |
| **Grounds for erasure** | ⚠️ Debatable | Data processed under legitimate interest (can be challenged) |

**Gap:** No process to facilitate erasure from Google's systems

---

#### Right to Restriction (Article 18)

**Status:** ⚠️ **PARTIALLY COMPLIANT**

**Scenarios:**
- Accuracy contested: N/A (user provides own data)
- Unlawful processing: Could stop using system
- No longer needed but user wants to keep: N/A
- Legitimate interest objected to: See Article 21

**Implementation:** If user objects, stop processing (don't use system)

---

#### Right to Data Portability (Article 20)

**Status:** ✅ **COMPLIANT (N/A)**

**Justification:**
- Portability applies to data "provided by data subject" under consent or contract
- This system uses legitimate interest (not consent/contract)
- No persistent storage
- **Conclusion:** Right not applicable

---

#### Right to Object (Article 21)

**Status:** ⚠️ **REQUIRES IMPLEMENTATION**

| Objection Type | Status | Response |
|----------------|--------|----------|
| **General objection** | ⚠️ Possible | User can stop using system |
| **Direct marketing** | ✅ N/A | No marketing |
| **Profiling** | ✅ N/A | No profiling |
| **Legitimate interest** | ⚠️ Required | Must provide mechanism to object |

**Implementation:** Add notice: "If you object to this processing, please discontinue use and contact [email]"

---

#### Automated Decision-Making & Profiling (Article 22)

**Status:** ✅ **COMPLIANT**

| Requirement | Status | Justification |
|-------------|--------|---------------|
| **Solely automated decision** | ❌ NO | System provides information, not decisions |
| **Legal/significant effects** | ❌ NO | No legal binding effects (disclaimers clear) |
| **Profiling** | ❌ NO | No user profiling |
| **Safeguards (if applicable)** | ✅ N/A | Article 22 does not apply |

**Conclusion:** Article 22 NOT applicable (informational system with no legal effects)

**However:** Article 35 DPIA may still be required due to "systematic monitoring" if used at scale

---

## 5. International Data Transfers (Chapter V)

### 5.1 Transfer Assessment

**Transfer:** User data → Google Gemini API (USA)

**Legal Basis Options:**

| Mechanism | Status | Notes |
|-----------|--------|-------|
| **Adequacy Decision** | ✅ **APPLICABLE** | EU-US Data Privacy Framework (2023) |
| **Standard Contractual Clauses (SCCs)** | ⚠️ Backup | Google provides SCCs |
| **Binding Corporate Rules** | ⚠️ Possible | Google may have BCRs |
| **Derogations (Art 49)** | ❌ Not relied upon | Not necessary with adequacy decision |

**Current Status:**
- ✅ USA has adequacy decision (EU-US DPF)
- ⚠️ Google must be self-certified under DPF (likely yes, but verify)
- ⚠️ Should still execute SCCs as supplementary measure

**Compliance Actions:**
1. ✅ Verify Google is DPF-certified: https://www.dataprivacyframework.gov/s/participant-search
2. ⚠️ Execute Google's Standard Contractual Clauses
3. ⚠️ Conduct Transfer Impact Assessment (TIA) per Schrems II
4. ⚠️ Document in privacy notice: "Data may be transferred to USA (Google)"

### 5.2 Transfer Impact Assessment (TIA)

**Schrems II Requirements:**

| Factor | Assessment | Risk |
|--------|------------|------|
| **US surveillance laws** | FISA 702, EO 12333 | MEDIUM |
| **Google's legal obligations** | Subject to US law | MEDIUM |
| **Technical safeguards** | Encryption in transit (TLS) | Good |
| **Contractual safeguards** | SCCs (if executed) | Good |
| **Practical access** | Query data may be accessible to US authorities | MEDIUM |

**TIA Conclusion:**
- **Risk Level:** MEDIUM
- **Mitigation:** Execute SCCs, document transfers, implement PII redaction before sending to API
- **Adequacy:** Transfers permissible under DPF + SCCs

---

## 6. Data Protection Impact Assessment (DPIA) - Article 35

### 6.1 DPIA Requirement Assessment

**Article 35(1) - DPIA Required if:**

| Criterion | Applicable? | Analysis |
|-----------|-------------|----------|
| **Systematic & extensive automated processing** | ⚠️ Possibly | If used at scale (thousands of users) |
| **Special category data (Art 9)** | ❌ No | Not processing sensitive data systematically |
| **Large-scale systematic monitoring** | ⚠️ Possibly | If monitoring query patterns |
| **Profiling with legal effects** | ❌ No | No profiling |
| **Innovative technology** | ⚠️ Yes | LLM chatbot is relatively new tech |
| **Impedes data subject rights** | ❌ No | Rights can still be exercised |
| **High risk to rights & freedoms** | ⚠️ Possibly | Depends on usage scale |

**DPIA Conclusion:** ⚠️ **RECOMMENDED** (Precautionary measure, especially if scaling)

**This document serves as the initial DPIA.**

### 6.2 DPIA Summary

**Processing Description:**
- Receive user queries about EU AI Act
- Send to Google Gemini API for AI-powered response
- Display response with disclaimers
- Session-only storage, no persistent data

**Necessity & Proportionality:**
- **Necessary:** Yes, to provide AI-powered regulatory guidance
- **Proportionate:** Yes, minimal data (query text only), session-only retention

**Risks to Data Subjects:**

| Risk | Likelihood | Impact | Severity | Mitigation |
|------|------------|--------|----------|------------|
| **Google data breach** | Low | Medium | **MEDIUM** | Google's security, encryption |
| **Unauthorized access (prompt injection)** | High | Medium | **HIGH** | Implement input validation |
| **Query contains sensitive data** | Medium | High | **HIGH** | Warning to users, PII redaction |
| **US government access** | Low | Medium | **MEDIUM** | SCCs, encryption |
| **No privacy notice** | High | Medium | **HIGH** | Create privacy notice (urgent) |
| **Lack of erasure mechanism** | Medium | Low | **MEDIUM** | Document limitation, Google contact |

**Overall Risk:** MEDIUM-HIGH (before mitigations), MEDIUM (after mitigations)

**Mitigation Measures:**
1. Create privacy notice (CRITICAL)
2. Execute DPA with Google (HIGH)
3. Implement PII redaction (HIGH)
4. Add prompt injection protection (HIGH)
5. Document Google retention policy (MEDIUM)

**Residual Risk:** LOW-MEDIUM (acceptable with mitigations)

**DPIA Approval:** [DPO or Senior Management sign-off required]

---

## 7. Data Processing Agreement (DPA) - Article 28

### 7.1 DPA Requirement

**Article 28 - Processor Obligations:**

**Status:** ❌ **NON-COMPLIANT** - No DPA with Google

**Required DPA Clauses:**

| Clause | Required? | Google Provides? | Status |
|--------|-----------|------------------|--------|
| **Subject matter** | ✅ Yes | ✅ Yes | Document in DPA |
| **Duration** | ✅ Yes | ✅ Yes | API service agreement |
| **Nature & purpose** | ✅ Yes | ⚠️ Generic | Specify AI query processing |
| **Type of personal data** | ✅ Yes | ⚠️ Generic | Specify: query text |
| **Categories of data subjects** | ✅ Yes | ⚠️ Generic | Specify: end users |
| **Controller obligations** | ✅ Yes | ✅ Yes | In Google Cloud ToS |
| **Processor obligations** | ✅ Yes | ✅ Yes | Article 28(3) compliance |
| **Sub-processors** | ✅ Yes | ✅ Yes | Google uses sub-processors (list available) |
| **Security measures** | ✅ Yes | ✅ Yes | ISO 27001, SOC 2 |
| **International transfers** | ✅ Yes | ✅ Yes | SCCs included |
| **Data subject rights assistance** | ✅ Yes | ⚠️ Limited | Google provides tools, but limited for API |
| **Audits** | ✅ Yes | ⚠️ Limited | SOC 2 reports, limited direct audit |
| **Deletion on termination** | ✅ Yes | ✅ Yes | Specified in ToS |

**Google's DPA Availability:**
- ✅ Google Cloud Data Processing Addendum: https://cloud.google.com/terms/data-processing-addendum
- ⚠️ Google AI ToS: May have separate/additional terms

**Action Required:**
1. Review Google AI API Terms of Service
2. Execute Google Cloud DPA (if not already in place)
3. Ensure DPA covers Gemini API usage specifically
4. Review sub-processor list
5. Document DPA execution date

### 7.2 Sub-Processor Management

**Google's Sub-Processors:**
- Google may use sub-contractors for infrastructure (e.g., data centers)
- List available at: https://cloud.google.com/terms/subprocessors

**Controller Obligations:**
- ✅ Be informed of sub-processors (Google provides list)
- ✅ Right to object to new sub-processors (check Google's terms)
- ✅ Ensure sub-processors have same obligations (Google's responsibility)

---

## 8. Compliance Checklist

### 8.1 GDPR Compliance Status

| Article | Requirement | Status | Priority |
|---------|-------------|--------|----------|
| **Art 5** | Lawfulness, fairness, transparency | ❌ NO | **CRITICAL** |
| **Art 6** | Legal basis (legitimate interest) | ⚠️ Partial | **HIGH** |
| **Art 13** | Privacy notice | ❌ NO | **CRITICAL** |
| **Art 28** | Data Processing Agreement | ❌ NO | **CRITICAL** |
| **Art 30** | Records of processing activities | ❌ NO | **HIGH** |
| **Art 32** | Security measures | ⚠️ Partial | **HIGH** |
| **Art 33** | Breach notification (72h) | ⚠️ No process | **MEDIUM** |
| **Art 35** | DPIA | ⚠️ This doc | **MEDIUM** |
| **Art 44** | International transfers | ⚠️ Partial | **HIGH** |

**Compliance Score:** 15% (2/15 fully compliant)

### 8.2 Action Items by Priority

**CRITICAL (0-7 days):**
1. ❌ Create and display privacy notice (Article 13)
2. ❌ Execute DPA with Google (Article 28)
3. ❌ Document legal basis (Article 6)

**HIGH (7-30 days):**
4. ⚠️ Create Article 30 register of processing activities
5. ⚠️ Implement security improvements (see security assessment)
6. ⚠️ Verify Google DPF certification
7. ⚠️ Execute Standard Contractual Clauses with Google

**MEDIUM (30-90 days):**
8. ⚠️ Develop data subject rights request process
9. ⚠️ Create breach notification procedure
10. ⚠️ Implement PII redaction before sending to API
11. ⚠️ Conduct Transfer Impact Assessment
12. ⚠️ Document Google's data retention policy

---

## 9. Templates & Implementation

### 9.1 Privacy Notice Template

**To display in CLI or documentation:**

```markdown
# PRIVACY NOTICE
## EU AI Act Query Assistant

**Effective Date:** [Date]
**Controller:** [Your Organization Name]
**Contact:** privacy@example.com
**DPO:** dpo@example.com (if applicable)

### 1. What Data We Collect

When you use this AI assistant, we process:
- **Your Queries:** The text questions you ask about EU AI Act and GDPR
- **Session Data:** Temporary data during your interaction (cleared on exit)
- **Technical Data:** IP address (if logged), timestamps

### 2. Why We Process Your Data

**Purpose:** To provide AI-powered answers to your regulatory questions.

**Legal Basis:** Legitimate interest (Article 6(1)(f) GDPR)
- Our legitimate interest: Helping organizations understand EU regulations
- Your interest: Receiving accurate regulatory guidance
- Balance: We use minimal data, session-only storage, no profiling

### 3. Who We Share Your Data With

**Google LLC (USA):** We use Google's Gemini AI API to generate responses.
Your queries are sent to Google's servers for processing.

**International Transfer:** Your data may be transferred to the USA.
This is permitted under the EU-US Data Privacy Framework and Standard
Contractual Clauses.

**Retention:**
- **Our system:** Session-only (deleted when you exit)
- **Google:** Up to 30 days (per Google AI API data retention policy)

### 4. Your Rights

You have the right to:
- **Access:** Request a copy of your data (contact Google for API retention data)
- **Rectification:** Correct inaccurate data (N/A - session only)
- **Erasure:** Request deletion (local data auto-deleted; contact Google for API data)
- **Restriction:** Limit how we process your data (stop using the system)
- **Object:** Object to processing (discontinue use, contact us)
- **Complaint:** Lodge a complaint with your data protection authority

**To exercise your rights:** Contact privacy@example.com

### 5. Data Security

We protect your data using:
- HTTPS encryption for all API communication
- No persistent local storage
- Google's enterprise-grade security (ISO 27001, SOC 2)

### 6. Important Notices

⚠️ **Do not include sensitive personal data in your queries**
   (e.g., health data, racial/ethnic origin, political opinions)

⚠️ **This is an AI system - responses may be inaccurate**
   Always verify information and consult legal counsel for compliance decisions.

⚠️ **Your queries are sent to Google LLC**
   By using this system, you acknowledge data transfer to Google's API.

### 7. Contact & Complaints

**Privacy Questions:** privacy@example.com
**Data Protection Officer:** dpo@example.com
**Supervisory Authority:** [Your country's DPA, e.g., ICO (UK), CNIL (France)]

---

**By using this system, you acknowledge this privacy notice.**
To opt out, discontinue use and contact privacy@example.com.
```

### 9.2 Implementation in Code

**Add to `ai_act_cli.py` startup:**

```python
def show_privacy_notice(self):
    """Display GDPR-compliant privacy notice."""
    self.console.print()
    self.console.print(Panel.fit(
        "📋 [bold]PRIVACY NOTICE[/bold]\n\n"
        "[bold]Your Privacy Matters[/bold]\n"
        "• Your queries are sent to Google Gemini API (USA)\n"
        "• Session-only storage (deleted on exit)\n"
        "• Do NOT include sensitive personal data in queries\n\n"
        "Full privacy notice: https://example.com/privacy\n"
        "Contact: privacy@example.com\n\n"
        "[dim]By using this system, you acknowledge our privacy notice.[/dim]",
        title="🔒 GDPR Privacy Notice",
        border_style="blue"
    ))

    # Optional: Require explicit consent
    consent = Prompt.ask(
        "\n[bold]Do you consent to your queries being sent to Google API?[/bold]",
        choices=["yes", "no"],
        default="yes"
    )

    if consent.lower() == "no":
        self.console.print("[yellow]You have declined. Exiting...[/yellow]")
        sys.exit(0)

# Call in __init__ or chat_loop
def initialize_agent(self):
    # ... existing code ...
    self.show_privacy_notice()
```

### 9.3 Article 30 Record of Processing Activities

**Template:**

| Field | Value |
|-------|-------|
| **Controller** | [Your Organization] |
| **DPO Contact** | dpo@example.com |
| **Processing Activity** | AI-powered EU AI Act query assistant |
| **Purpose** | Provide regulatory information and guidance |
| **Legal Basis** | Legitimate interest (Article 6(1)(f)) |
| **Categories of Data** | User queries (may contain personal data: names, companies) |
| **Categories of Data Subjects** | End users (legal professionals, compliance officers, developers) |
| **Recipients** | Google LLC (processor - Gemini API) |
| **International Transfers** | USA (Google) - EU-US DPF + SCCs |
| **Retention Period** | Session-only (local); ~30 days (Google) |
| **Security Measures** | HTTPS encryption, session-only storage, Google's security (ISO 27001, SOC 2) |
| **Data Subject Rights** | Access, erasure, objection (see privacy notice) |

---

## 10. Recommendations

### 10.1 Immediate Actions (Week 1)

1. **Create Privacy Notice** (Template in 9.1)
   - Add to CLI startup
   - Publish on website
   - Include in documentation

2. **Execute Google DPA**
   - Review Google AI API Terms
   - Execute Google Cloud DPA
   - Document execution date

3. **Document Legal Basis**
   - Complete Legitimate Interest Assessment
   - Store in compliance records

### 10.2 Short-Term Actions (Month 1)

4. **Create Article 30 Register** (Template in 9.3)
5. **Develop Data Subject Rights Process**
   - Create email template for requests
   - Document how to facilitate Google data access/deletion
   - Train support team (if applicable)

6. **Verify International Transfers**
   - Check Google DPF certification
   - Execute SCCs if not in DPA
   - Document Transfer Impact Assessment

### 10.3 Long-Term Actions (Months 2-3)

7. **Implement PII Redaction**
   - Detect names, emails, company names in queries
   - Anonymize before sending to Google (or warn user)

8. **Create Breach Notification Procedure**
   - Define breach scenarios
   - Identify notification authority
   - 72-hour notification process

9. **DPO Assignment** (if required)
   - Assess if DPO is mandatory (public authority, large-scale monitoring, special categories)
   - Appoint DPO if needed

10. **Regular GDPR Audits**
    - Annual privacy review
    - Update privacy notice
    - Review Google's terms for changes

---

## 11. Conclusion

**Overall GDPR Compliance:** ⚠️ **PARTIALLY COMPLIANT**

**Strengths:**
- ✅ Session-only storage (minimal data retention)
- ✅ No profiling or automated decision-making
- ✅ Encryption in transit (HTTPS)
- ✅ No special category data processing

**Critical Gaps:**
- ❌ No privacy notice (Article 13)
- ❌ No DPA with Google (Article 28)
- ❌ No Article 30 register
- ⚠️ Unclear Google retention policy
- ⚠️ No data subject rights process

**Risk Level:** MEDIUM-HIGH (before remediation), LOW-MEDIUM (after)

**Timeline to Compliance:**
- **Basic Compliance:** 1-2 weeks (privacy notice + DPA)
- **Full Compliance:** 2-3 months (all procedures, monitoring, audits)

**Investment Required:**
- **Legal:** €5k-€15k (lawyer review, DPA negotiation)
- **Technical:** 40-60 hours (implementation, testing)
- **Ongoing:** 10-20 hours/year (audits, updates)

**Recommendation:** Implement privacy notice and execute Google DPA within 7 days (CRITICAL).

---

## 12. Appendices

### Appendix A: GDPR Articles Referenced

- Article 5: Principles
- Article 6: Lawfulness of processing
- Articles 13-14: Information to data subjects
- Articles 15-22: Data subject rights
- Article 28: Processors
- Article 30: Records of processing
- Article 32: Security
- Article 35: DPIA
- Chapter V (44-50): International transfers

### Appendix B: Resources

- **GDPR Full Text:** https://gdpr-info.eu/
- **ICO Guidance:** https://ico.org.uk/for-organisations/guide-to-data-protection/
- **EDPB Guidelines:** https://edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en
- **EU-US DPF:** https://www.dataprivacyframework.gov/
- **Google Cloud DPA:** https://cloud.google.com/terms/data-processing-addendum

### Appendix C: Google Documentation

- Google AI Terms: [Check Google AI website]
- Google Cloud DPA: https://cloud.google.com/terms/data-processing-addendum
- Google Sub-processors: https://cloud.google.com/terms/subprocessors
- Google Security: https://cloud.google.com/security

---

**Document Control:**
- Version: 1.0
- Date: 2026-01-10
- Regulation: GDPR (EU 2016/679)
- Next Review: 2026-04-10 (quarterly)
- Classification: INTERNAL - Privacy Sensitive
- Approval: [DPO/Legal/Management signature required]
