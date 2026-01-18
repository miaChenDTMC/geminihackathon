# AI_Act_skills - EU AI Act Compliance Skills Library

**Total Skills:** 73
**Categories:** 13
**Status:** ✅ Reorganized & Ready for Use

---

## 📂 Quick Navigation

| Category | Skills | Key Use Cases |
|----------|--------|---------------|
| [Technical](#technical) | 15 | ML development, testing, RAG, prompt engineering |
| [Third-Party](#third-party) | 8 | Security scanning, SBOM, vulnerability management |
| [EU AI Act Compliance](#eu-ai-act-compliance) | 8 | Model cards, QMS, transparency, certification |
| [Fundamental Rights](#fundamental-rights) | 7 | Fairness, bias detection, discrimination prevention |
| [Societal](#societal) | 7 | Content moderation, sentiment analysis |
| [Trust](#trust) | 7 | Explainability, interpretability |
| [Business](#business) | 5 | Governance, ethics, validation |
| [Environment](#environment) | 4 | Carbon tracking, energy consumption |
| [Health & Safety](#health--safety) | 4 | Risk assessment, safety planning |
| [GDPR Compliance](#gdpr-compliance) | 3 | Data protection regulations |
| [Legal](#legal) | 3 | License compliance, scanning |
| [Cybersecurity](#cybersecurity) | 1 | Prompt injection protection |
| [Privacy](#privacy) | 1 | Data classification |

---

## 📋 Categories & Skills

### Technical
**ML/AI Development & Testing (15 skills)**

- `agentic-workflow-design` - Design autonomous AI agent workflows
- `alibi-detect` - Outlier and drift detection for ML models
- `deepeval` - LLM evaluation framework
- `evidently-ai` - ML monitoring and data drift detection
- `hitl-design` - Human-in-the-loop system design
- `huggingface-evaluate` - Model evaluation metrics
- `langsmith` - LLM application monitoring
- `ml-project-lifecycle` - End-to-end ML project management
- `model-selection` - Choose optimal models for tasks
- `prompt-engineering` - Optimize prompts for LLMs
- `promptfoo` - LLM prompt testing
- `rag-architecture` - RAG pipeline design
- `ragas` - RAG system evaluation
- `token-budgeting` - Optimize token usage & costs
- `weights-and-biases` - Experiment tracking

**Location:** `technical/skills/`

---

### Third-Party
**Security & Supply Chain (8 skills)**

- `grype-vulnerability` - Container vulnerability scanning
- `npm-audit` - JavaScript dependency security
- `oss-scorecard` - Open source security health metrics
- `safety-pyup` - Python dependency security
- `sbom-management` - Software Bill of Materials
- `security-frameworks` - Security compliance frameworks
- `snyk-io` - Vulnerability scanning
- `syft-sbom` - SBOM generation

**Location:** `third-party/skills/`

---

### EU AI Act Compliance
**Mandatory Compliance (8 skills)**

- `ai-logging-system` - Comprehensive logging (Art. 61)
- `ai-system-registry` - EU database registration (Art. 60)
- `ai-transparency-labels` - Transparency labeling (Art. 13)
- `ce-marking-generator` - CE certification (Art. 49)
- `fria-assessment` - Fundamental Rights Impact Assessment (Art. 27)
- `model-card-generation` - Automated model documentation
- `model-cards-generator` - Model documentation (Art. 13)
- `qms-tracker` - Quality Management System (Art. 17)

**Location:** `eu-ai-act-compliance/skills/`

---

### Fundamental Rights
**Fairness & Bias Prevention (7 skills)**

- `aequitas` - Bias and fairness audit toolkit
- `ai-fairness-360` - Comprehensive fairness metrics
- `bias-assessment` - Systematic bias evaluation
- `disaggregated-evaluation` - Performance across subgroups
- `fairlearn` - Fairness assessment & mitigation
- `moderate-content-api` - Content moderation
- `perspective-api` - Toxicity detection

**Location:** `fundamental-rights/skills/`

---

### Societal
**Content & Social Impact (7 skills)**

- `ai-content-detector` - Detect AI-generated content
- `claimbuster-api` - Fact-checking & claim verification
- `detoxify` - Toxic comment classification
- `hate-speech-detector` - Hate speech detection
- `perspective-api-societal` - Toxicity for social impact
- `textblob-sentiment` - Simple sentiment analysis
- `vader-sentiment` - Social media sentiment

**Location:** `societal/skills/`

---

### Trust
**Explainability & Accessibility (7 skills)**

- `axe-accessibility` - Automated accessibility testing
- `captum` - PyTorch model interpretability
- `explainability-planning` - Design explainable systems
- `interpretml` - Interpretable ML models
- `lime` - Local interpretable explanations
- `shap-explainer` - SHAP values for interpretability
- `what-if-tool` - Interactive model investigation

**Location:** `trust/skills/`

---

### Business
**Governance & Ethics (5 skills)**

- `ai-ethics` - AI ethics frameworks
- `ai-ethics-advisor` - Ethics advisory
- `ai-governance` - AI governance structures
- `ethics-review` - Ethics review processes
- `validating-ai-ethics-and-fairness` - Ethics validation

**Location:** `business/skills/`

---

### Environment
**Carbon & Energy (4 skills)**

- `cloud-carbon-footprint` - Cloud infrastructure carbon
- `codecarbon` - Track ML training emissions
- `ml-co2-impact` - Calculate ML CO2 impact
- `watttime-carbon` - Real-time carbon intensity

**Location:** `environment/skills/`

---

### Health & Safety
**Risk & Safety Management (4 skills)**

- `ai-safety-planning` - Safety planning for AI systems
- `conformance-calibration` - Model calibration for safety
- `incident-responder` - AI incident response
- `risk-assessment` - Systematic risk assessment

**Location:** `health-safety/skills/`

---

### GDPR Compliance
**Data Protection Regulations (3 skills)**

- `gdpr-compliance` - GDPR compliance requirements
- `hipaa-compliance` - Healthcare data protection
- `pci-dss-compliance` - Payment card data security

**Location:** `gdpr-compliance/skills/`

---

### Legal
**License & Compliance (3 skills)**

- `license-checker` - License verification
- `license-compliance` - License compliance management
- `scancode-toolkit` - License & copyright scanning

**Location:** `legal/skills/`

---

### Cybersecurity
**Security Protection (1 skill)**

- `prompt-injection-detector` - Detect prompt injection attacks

**Location:** `cybersecurity/skills/`

---

### Privacy
**Data Privacy (1 skill)**

- `data-classification` - Classify and protect sensitive data

**Location:** `privacy/skills/`

---

## 🎯 EU AI Act Mapping

### High-Risk AI Systems Requirements

| Article | Requirement | Skills |
|---------|-------------|--------|
| Art. 9 | Risk Management | ai-safety-planning, risk-assessment, fria-assessment |
| Art. 10 | Data Governance | data-classification, gdpr-compliance |
| Art. 13 | Transparency | model-cards-generator, ai-transparency-labels |
| Art. 15 | Accuracy & Robustness | evidently-ai, alibi-detect, ragas, deepeval |
| Art. 17 | Quality Management | qms-tracker |
| Art. 27 | FRIA | fria-assessment |
| Art. 49 | CE Marking | ce-marking-generator |
| Art. 60 | EU Database | ai-system-registry |
| Art. 61 | Post-Market Monitoring | ai-logging-system, langsmith, weights-and-biases |

### GPAI Models (Chapter V)

| Article | Requirement | Skills |
|---------|-------------|--------|
| Art. 53 | Transparency | model-cards-generator, ai-transparency-labels |
| Art. 53 | Energy Consumption | codecarbon, cloud-carbon-footprint, ml-co2-impact |

---

## 🚀 Quick Start

### Find a Skill
```bash
cd AI_Act_skills
ls */skills/
```

### Use a Skill
```bash
cd <category>/skills/<skill-name>
cat SKILL.md
```

### Create New Skill
```bash
python3 skill-creator/scripts/init_skill.py <skill-name> --path <category>/skills
```

---

## 📚 Documentation

- **Reorganization Report:** `../AI_ACT_SKILLS_REORGANIZATION_REPORT.md`
- **Complete Summary:** `../AI_ACT_SKILLS_COMPLETE_SUMMARY.md`
- **Verification Report:** `../SKIPPED_TOOLS_VERIFICATION_REPORT.md`

---

## 🔧 Skill Structure

Each skill follows this structure:
```
<skill-name>/
├── SKILL.md           # Main documentation
├── scripts/           # Executable scripts
├── references/        # API docs & references
└── assets/           # Templates & resources
```

---

**Last Updated:** 2026-01-10
**Status:** Production Ready ✅
