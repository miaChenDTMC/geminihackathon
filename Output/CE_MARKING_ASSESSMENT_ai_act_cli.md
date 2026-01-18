# CE Marking Applicability Assessment
## EU AI Act Query Assistant (`ai_act_cli.py`)

**Assessment Date:** 2026-01-10
**System:** AI Act CLI Tool v1.0.0
**Regulation:** Regulation (EU) 2024/1689 (EU AI Act)
**Assessment Standard:** Annex VII - Conformity Assessment Procedures

---

## Executive Summary

This assessment evaluates whether the EU AI Act Query Assistant requires CE marking under the EU AI Act. CE marking is mandatory for high-risk AI systems before market placement, indicating conformity with regulatory requirements.

**Assessment Conclusion:** ❌ **CE MARKING NOT REQUIRED**

**Risk Classification:** Limited Risk (Article 50)
**CE Marking Obligation:** Not Applicable (only high-risk systems require CE marking)
**Compliance Pathway:** Transparency obligations under Article 50

---

## 1. Risk Classification Analysis

### 1.1 System Description

**Product Name:** EU AI Act Query Assistant
**Type:** Conversational AI chatbot for regulatory information
**Technology:** Google Gemini 3 Pro (general-purpose AI model)
**Use Case:** Legal research and information retrieval
**Deployment:** Desktop/CLI application

**Key Characteristics:**
- Retrieval-augmented generation (RAG) architecture
- Read-only information provision
- No decision-making authority
- No direct impact on fundamental rights
- No critical infrastructure control

### 1.2 Annex III High-Risk Use Cases Assessment

| Annex III Category | Description | Applicable? | Justification |
|-------------------|-------------|-------------|---------------|
| **1. Biometrics** | Biometric identification/categorization | ❌ No | System does not process biometric data |
| **2. Critical Infrastructure** | Safety components for utilities, transport | ❌ No | System is informational only |
| **3. Education/Employment** | Educational admissions, recruitment tools | ❌ No | Not used for hiring or education decisions |
| **4. Essential Services** | Creditworthiness, emergency dispatch | ❌ No | No access to financial or emergency systems |
| **5. Law Enforcement** | Risk assessment, polygraph, crime prediction | ❌ No | Not used by law enforcement |
| **6. Migration/Asylum** | Asylum application assessment | ❌ No | Not used for immigration purposes |
| **7. Justice** | Court decision assistance | ❌ No | Informational only, no binding legal effect |
| **8. Democratic Processes** | Electoral influence | ❌ No | Not used in electoral processes |

**Conclusion:** ❌ **NOT A HIGH-RISK AI SYSTEM**

### 1.3 Article 6 Risk Classification

The system is classified under **Article 50 (Limited Risk)** because:

1. **It is a chatbot** interacting with natural persons
2. **No Annex III use cases** apply
3. **No fundamental rights impact** (informational only)
4. **No safety-critical function**

**Applicable Requirements:**
- ✅ Article 50(1): Transparency obligations (disclosure that user is interacting with AI)
- ✅ Article 50(2): AI-generated content labeling (implemented in code)

**Not Applicable:**
- ❌ Title III Chapter 2: High-risk system requirements (Articles 8-15)
- ❌ Article 43: Conformity assessment
- ❌ Article 48: CE marking

---

## 2. CE Marking Requirements (For Reference)

### 2.1 When CE Marking is Required

**Article 48 - CE Marking:**
> "High-risk AI systems that have been found to be in conformity with the requirements set out in Chapter 2 shall bear the CE marking to indicate such conformity."

**Applicable To:**
- ✅ High-risk AI systems (Annex III use cases)
- ✅ AI systems with safety components under harmonized standards

**Not Applicable To:**
- ❌ Limited risk AI systems (Article 50) ← **This system**
- ❌ Minimal risk AI systems
- ❌ General-purpose AI models (GPAIs) - separate transparency obligations

### 2.2 Conformity Assessment Procedures (If High-Risk)

If this system were high-risk, the following would apply:

| Risk Level | Procedure | Authority | Annex Reference |
|------------|-----------|-----------|-----------------|
| **High-risk (internal control)** | Provider self-assessment | Provider's QMS | Annex VI |
| **High-risk (notified body)** | Third-party assessment | Notified body | Annex VII |
| **High-risk (post-market)** | Ongoing monitoring | Provider + notified body | Article 61 |

**Current System:** None required (not high-risk)

---

## 3. Compliance Pathway for Limited Risk Systems

### 3.1 Article 50 Transparency Obligations

**Requirement:** Providers of AI systems that interact with natural persons shall inform users that they are interacting with an AI system.

**Implementation Status:** ✅ COMPLIANT

**Evidence from Code (`ai_act_cli.py:105-119`):**
```python
# EU AI Act Article 50 Compliance: Chatbot Disclosure
self.console.print()
self.console.print(Panel.fit(
    "🤖 [bold yellow]AI Assistant Disclosure (EU AI Act Article 50)[/bold yellow]\n\n"
    f"You are interacting with an AI-powered system using [bold]Google {MODEL_NAME}[/bold].\n"
    "This system analyzes the EU AI Act and GDPR regulation text to provide information.\n\n"
    "[bold]Important Notices:[/bold]\n"
    "[dim]• Responses are AI-generated and should be verified with official sources\n"
    "• This is NOT legal advice - consult qualified legal counsel for compliance decisions\n"
    "• Information is based on Regulation (EU) 2024/1689 (EU AI Act) and GDPR\n"
    f"• System Classification: {EU_AI_ACT_RISK_LEVEL} AI System\n"
    f"• Model: {MODEL_NAME} | Version: {VERSION} | Classified: {EU_AI_ACT_CLASSIFICATION_DATE}[/dim]",
    title="⚠️  Transparency Notice",
    border_style="yellow"
))
```

**Compliance Elements:**
- ✅ Clear disclosure of AI usage
- ✅ Model identification (Google Gemini 3 Pro)
- ✅ Risk classification stated (Limited Risk)
- ✅ Disclaimer about AI-generated content
- ✅ Prominent display at session start

### 3.2 Additional Transparency Measures

**Beyond Article 50 minimum requirements:**

1. **Response-level disclosure** (line 206):
   ```python
   self.console.print("\n[dim italic]⚠️  AI-generated response - Verify with official sources and legal counsel for compliance decisions[/dim italic]")
   ```

2. **Version and classification tracking:**
   - System version: `VERSION = "1.0.0"`
   - Risk level: `EU_AI_ACT_RISK_LEVEL = "Limited Risk"`
   - Classification date: `EU_AI_ACT_CLASSIFICATION_DATE = "2025-01-07"`

3. **Model transparency:**
   - Explicit model name: `gemini-3-pro-preview`
   - Google attribution

**Compliance Rating:** ✅ **EXCEEDS MINIMUM REQUIREMENTS**

---

## 4. If System Were High-Risk: Required Documentation

### 4.1 Technical Documentation (Annex IV)

If this system were high-risk, the following documentation would be required:

- [ ] General description of AI system
- [ ] Detailed description of elements and development process
- [ ] Detailed information on monitoring, functioning, and control
- [ ] Description of risk management system
- [ ] Description of changes to the system through its lifecycle
- [ ] List of harmonized standards applied
- [ ] Copy of EU declaration of conformity
- [ ] Detailed description of system capabilities and limitations

**Current Status:** Not required (not high-risk)
**Recommendation:** Maintain technical documentation as best practice

### 4.2 Quality Management System (Annex V)

If high-risk, would require:

- [ ] Compliance strategy
- [ ] Design, design control, and design verification techniques
- [ ] Testing, validation, and verification procedures
- [ ] Technical specifications and standards applied
- [ ] Data management systems
- [ ] Risk management procedures
- [ ] Post-market monitoring system
- [ ] Incident reporting procedures
- [ ] Communication with authorities

**Current Status:** Not required
**Recommendation:** Implement lightweight QMS for internal quality assurance

### 4.3 Conformity Assessment (Annex VI/VII)

If high-risk, provider would:

1. Prepare technical documentation (Annex IV)
2. Implement quality management system (Annex V)
3. Conduct conformity assessment:
   - **Annex VI** (internal control) - self-assessment by provider, OR
   - **Annex VII** (third-party) - assessment by notified body
4. Draw up EU declaration of conformity
5. Affix CE marking
6. Register in EU database (Article 60)

**Current Status:** Not required

---

## 5. Hypothetical CE Marking Process (Educational)

### 5.1 If System Were Reclassified as High-Risk

**Scenario:** Hypothetically, if the system were used by courts for legal research assistance, it might fall under **Annex III, point 8 (Administration of Justice)** and require CE marking.

**Required Steps:**

#### Step 1: Prepare Technical Documentation
- Complete Annex IV documentation
- Document training data, model architecture, validation procedures
- Describe risk management system

#### Step 2: Choose Conformity Assessment Route

**Option A: Annex VI (Internal Control) - For most high-risk systems**
- Provider conducts self-assessment
- Implement QMS per Annex V
- Document compliance with Articles 8-15
- No notified body required

**Option B: Annex VII (Third-Party) - For biometrics & critical infrastructure**
- Engage notified body
- Submit technical documentation
- Undergo assessment by accredited body
- Obtain conformity certificate

#### Step 3: EU Declaration of Conformity
```
EU DECLARATION OF CONFORMITY
Regulation (EU) 2024/1689 (EU AI Act)

We, [Provider Name],
declare under our sole responsibility that the AI system:

Product: EU AI Act Query Assistant
Model: ai_act_cli v1.0.0
Type: Limited Risk Conversational AI
Serial Number: [Unique identifier]

to which this declaration relates is in conformity with:
- Regulation (EU) 2024/1689, Title III, Chapter 2
- [List harmonized standards applied]

[Place, Date]
[Signature of authorized representative]
```

#### Step 4: Affix CE Marking
- Physical CE mark on packaging (if applicable)
- Digital CE mark in software metadata
- Minimum height: 5mm (if physical)

#### Step 5: Register in EU Database
- Submit system to EU AI system database (Article 60)
- Include technical summary
- Update upon substantial modifications

**Timeline:** 6-12 months
**Cost:** €10,000 - €100,000 (depending on notified body involvement)

---

## 6. Current Compliance Status

### 6.1 Mandatory Requirements

| Requirement | Status | Evidence |
|-------------|--------|----------|
| **Risk Classification** | ✅ Complete | Documented as Limited Risk (Article 50) |
| **Article 50 Disclosure** | ✅ Compliant | Transparency notice implemented |
| **AI-Generated Content Labeling** | ✅ Compliant | Disclaimers on all outputs |
| **CE Marking** | ✅ N/A | Not required for Limited Risk systems |

### 6.2 Best Practice Recommendations

While CE marking is not required, the following are recommended:

1. **Maintain Technical Documentation**
   - Even without CE marking requirement, document system design
   - Useful for internal quality, updates, and potential future regulatory changes

2. **Implement Lightweight QMS**
   - Version control
   - Change management
   - User feedback tracking
   - Incident logging

3. **Self-Assessment Against High-Risk Requirements**
   - Periodic review of Annex III use cases
   - Monitor for changes in system use that could trigger reclassification
   - Document risk assessments

4. **EU Database Registration (Optional)**
   - Not mandatory for Limited Risk
   - Consider voluntary registration for transparency

5. **Prepare for Future Regulations**
   - EU AI Act will evolve
   - GPAI provider (Google) transparency obligations may cascade
   - National implementations may vary

---

## 7. Decision Tree: Does Your AI System Need CE Marking?

```
START
  │
  ├─→ Is your AI system listed in Annex III (high-risk use cases)?
  │     YES → CE MARKING REQUIRED
  │     NO → Continue
  │
  ├─→ Is it a safety component covered by EU harmonized legislation?
  │     YES → CE MARKING REQUIRED (under that legislation)
  │     NO → Continue
  │
  ├─→ Is it a general-purpose AI model (GPAI)?
  │     YES → Article 53 transparency obligations (not CE marking)
  │     NO → Continue
  │
  ├─→ Does it interact with natural persons (chatbot, emotion recognition)?
  │     YES → Article 50 transparency obligations (not CE marking) ← THIS SYSTEM
  │     NO → Minimal risk (no obligations)
```

**Conclusion for ai_act_cli.py:** Article 50 obligations only, no CE marking

---

## 8. GPAI Provider Obligations (Upstream)

### 8.1 Google as GPAI Provider

The system uses Google's Gemini 3 Pro model, which is a **General-Purpose AI Model (GPAI)** under Article 53.

**Google's Obligations (not provider of ai_act_cli):**
- Article 53(1)(a): Technical documentation
- Article 53(1)(b): Information to downstream providers (you)
- Article 53(1)(c): Copyright compliance policy
- Article 53(1)(d): Energy consumption documentation

**Your Obligations as Downstream Provider:**
- ✅ Comply with Article 50 (transparency) - DONE
- ⚠️ Review Google's GPAI documentation for compliance
- ⚠️ Ensure Google provides required information (Article 53(1)(b))

### 8.2 Systemic Risk Models (Article 55)

If Google's model were classified as **systemic risk GPAI** (>10^25 FLOPs):
- Additional evaluation requirements
- Red teaming and adversarial testing
- Incident reporting

**Not your direct obligation**, but important for supply chain transparency.

---

## 9. Monitoring for Reclassification

### 9.1 Scenarios Requiring Reassessment

The system should be **reclassified as high-risk** (requiring CE marking) if:

| Scenario | New Risk Level | CE Required? |
|----------|---------------|--------------|
| **Deployed in court systems** for legal research | High-risk (Annex III, point 8) | YES |
| **Used for creditworthiness assessment** | High-risk (Annex III, point 4) | YES |
| **Integrated into critical infrastructure** | High-risk (Annex III, point 2) | YES |
| **Used for biometric identification** | High-risk (Annex III, point 1) | YES |
| **Substantially modified** (new risk assessment) | Depends on modification | TBD |

**Current Use Case:** Informational chatbot for general public → Limited Risk → No change

### 9.2 Substantial Modification Triggers

**Article 43(4):** Changes to AI system requiring new conformity assessment:

- Change in intended purpose (e.g., from info retrieval to decision support)
- New training data that changes system behavior
- Architecture changes (e.g., adding reasoning capabilities)
- Deployment in new high-risk context

**Recommendation:** Document all changes and reassess risk classification annually.

---

## 10. Comparative Analysis: CE Marking vs. Article 50

| Aspect | CE Marking (High-Risk) | Article 50 (Limited Risk - This System) |
|--------|------------------------|------------------------------------------|
| **Legal Basis** | Article 48 | Article 50 |
| **Applicability** | High-risk AI systems | Chatbots, emotion recognition, deepfakes |
| **Conformity Assessment** | Required (Annex VI/VII) | Not required |
| **Notified Body** | Sometimes required | Not required |
| **Technical Documentation** | Mandatory (Annex IV) | Not mandatory (recommended) |
| **EU Database Registration** | Mandatory | Not mandatory |
| **CE Mark Affixing** | Required | Not applicable |
| **Transparency Disclosure** | Required | **Required** ✅ |
| **QMS** | Mandatory (Annex V) | Not mandatory |
| **Post-Market Monitoring** | Mandatory (Article 61) | Not mandatory |
| **Estimated Cost** | €10k-€100k+ | <€1k (disclosure only) |
| **Timeline** | 6-12 months | Immediate (if properly implemented) |

**Current System:** Article 50 pathway (right column)

---

## 11. Recommendations

### 11.1 Immediate Actions (Current Limited Risk Status)

- ✅ **Maintain Article 50 compliance** (already implemented)
- ✅ **Document risk classification** (this assessment serves as documentation)
- ⚠️ **Monitor use case changes** (annual review recommended)
- ⚠️ **Track GPAI provider compliance** (verify Google's Article 53 documentation)

### 11.2 If Considering High-Risk Deployment

If planning to deploy in courts, law enforcement, or other Annex III contexts:

1. **Conduct full risk assessment** (6-12 months before deployment)
2. **Engage legal counsel** specializing in EU AI Act
3. **Budget for conformity assessment** (€10k-€100k)
4. **Identify notified body** (if Annex VII required)
5. **Develop technical documentation** (Annex IV)
6. **Implement QMS** (Annex V)
7. **Plan for EU database registration**

**Timeline:** 12-18 months from decision to market placement

### 11.3 Best Practices (Even Without CE Marking)

1. **Maintain "shadow" technical documentation**
   - Easier to achieve CE compliance if needed later
   - Demonstrates due diligence

2. **Implement change control**
   - Version tracking
   - Risk reassessment triggers

3. **User feedback loop**
   - Monitor for unintended uses
   - Address misclassification risks

4. **Annual compliance review**
   - Reassess risk classification
   - Review regulatory updates
   - Check GPAI provider documentation

---

## 12. Conclusion

**CE Marking Required:** ❌ **NO**

**Rationale:**
- System is classified as **Limited Risk** under Article 50
- Not listed in **Annex III** (high-risk use cases)
- No safety component requiring CE marking under other EU legislation
- Transparency obligations (Article 50) are the applicable requirement

**Compliance Status:** ✅ **FULLY COMPLIANT**

**Key Compliance Elements:**
- Article 50 transparency disclosure: ✅ Implemented
- AI-generated content labeling: ✅ Implemented
- Risk classification documented: ✅ This assessment
- GPAI supply chain awareness: ⚠️ Monitor Google compliance

**Future Monitoring:**
- Annual risk classification review
- Track use case changes that could trigger Annex III
- Monitor EU AI Act implementation (effective dates: 2025-2027)
- Follow GPAI provider transparency updates

**No Action Required:** System is compliant with current classification. CE marking is not applicable.

---

## 13. Appendices

### Appendix A: EU AI Act Timeline

| Date | Milestone |
|------|-----------|
| **2024-08-01** | EU AI Act enters into force |
| **2025-02-02** | Prohibited AI practices ban (Article 5) |
| **2025-08-02** | GPAI obligations (Articles 53-55) |
| **2026-08-02** | Obligations for deployers |
| **2027-08-02** | **High-risk system obligations (CE marking)** ← If applicable |

**Current System:** Article 50 already in effect

### Appendix B: Notified Bodies for AI (Informational)

If high-risk assessment were required:

- TÜV SÜD (Germany)
- BSI (UK - if mutual recognition)
- DEKRA (Germany)
- Bureau Veritas (France)

**Note:** Notified body list for EU AI Act still being established (as of 2026).

### Appendix C: Relevant Articles

- **Article 6:** Classification of high-risk AI systems
- **Article 43:** Conformity assessment
- **Article 48:** CE marking
- **Article 50:** Transparency obligations (chatbots)
- **Article 53:** GPAI provider obligations
- **Annex III:** High-risk AI systems list
- **Annex IV:** Technical documentation
- **Annex V:** Quality management system
- **Annex VI/VII:** Conformity assessment procedures

### Appendix D: Resources

- **EU AI Act Full Text:** https://eur-lex.europa.eu/eli/reg/2024/1689
- **European Commission AI Act Page:** https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- **Notified Bodies Database:** https://ec.europa.eu/growth/tools-databases/nando/
- **GPAI Code of Practice:** In development (Article 56)

---

**Document Control:**
- Version: 1.0
- Date: 2026-01-10
- Assessed By: EU AI Act Compliance Team
- Next Review: 2027-01-10 (annual review)
- Classification: PUBLIC
