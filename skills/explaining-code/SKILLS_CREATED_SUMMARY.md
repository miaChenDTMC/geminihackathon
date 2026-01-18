# AI Act Skills Creation Summary

**Date:** 2026-01-10
**Source:** GitHub Download Folder
**Total Skills Created:** 47
- **uncertainty-toolbox** (Health & Safety)
- **urlhaus-malware** (Cybersecurity)
- **carbon-emissions** (Environment)
- **perspective-api** (Societal)
- **fhir-validator** (Health & Safety)
- **ai-logging-system** (EU AI Act Compliance)
- **spdx-license-checker** (Legal) - *Created but directory check failed*
---

## Overview

This document summarizes the creation of 47 Claude Code skills based on the tools downloaded from GitHub. Each skill follows the standard skill-creator template and is organized by EU AI Act compliance category.

---

## Skills by Category

### 1. Cybersecurity (1 skill)
- `prompt-injection-detector` - Detect and prevent prompt injection attacks in AI systems

### 2. Environment (4 skills)
- `codecarbon` - Track and reduce carbon emissions from ML training
- `cloud-carbon-footprint` - Measure cloud infrastructure carbon footprint
- `ml-co2-impact` - Calculate ML model CO2 impact
- `watttime-carbon` - Real-time carbon intensity data for optimal scheduling

### 3. Technical (8 skills)
- `evidently-ai` - ML model monitoring and data drift detection
- `alibi-detect` - Outlier and drift detection for ML models
- `ragas` - RAG system evaluation framework
- `deepeval` - LLM evaluation framework
- `huggingface-evaluate` - Model evaluation metrics from Hugging Face
- `langsmith` - LLM application development and monitoring
- `weights-and-biases` - ML experiment tracking and visualization
- `promptfoo` - LLM prompt testing and evaluation

### 4. Trust (6 skills)
- `shap-explainer` - SHAP values for model interpretability
- `lime` - Local interpretable model-agnostic explanations
- `captum` - Model interpretability for PyTorch
- `interpretml` - Interpretable ML models and explanations
- `what-if-tool` - Interactive model investigation
- `axe-accessibility` - Automated accessibility testing

### 5. Fundamental Rights (6 skills)
- `ai-fairness-360` - Comprehensive fairness metrics and mitigation
- `fairlearn` - Fairness assessment and unfairness mitigation
- `aequitas` - Bias and fairness audit toolkit
- `perspective-api` - Toxicity and comment quality API
- `moderate-content-api` - Content moderation API
- `disaggregated-evaluation` - Disaggregated model performance evaluation

### 6. Societal (7 skills)
- `detoxify` - Toxic comment classification
- `claimbuster-api` - Fact-checking and claim detection
- `textblob-sentiment` - Simple sentiment analysis
- `vader-sentiment` - Social media sentiment analysis
- `hate-speech-detector` - Hate speech detection
- `ai-content-detector` - Detect AI-generated content
- `perspective-api-societal` - Toxicity detection for societal impact

### 7. Third-Party (7 skills)
- `snyk-io` - Security vulnerability scanning
- `safety-pyup` - Python dependency security checker
- `npm-audit` - JavaScript dependency security
- `syft-sbom` - Software Bill of Materials generator
- `grype-vulnerability` - Vulnerability scanner for containers
- `oss-scorecard` - Security health metrics for open source
- `license-checker` - License compliance verification

### 8. Health & Safety (1 skill)
- `conformance-calibration` - Model calibration for safety-critical applications

### 9. EU AI Act Compliance (7 skills)
- `model-cards-generator` - Generate model documentation cards
- `ai-system-registry` - Register and track AI systems
- `model-card-generation` - Automated model card creation
- `ai-transparency-labels` - Generate transparency labels for AI systems
- `qms-tracker` - Quality Management System tracking
- `ai-logging-system` - Comprehensive AI system logging
- `ce-marking-generator` - Generate CE marking for AI systems

---

## Skill Structure

Each skill includes:
- **SKILL.md** - Main skill documentation with:
  - Name and description
  - Overview and when to use
  - Placeholder sections for customization

- **scripts/** - Directory for executable helper scripts
  - `example.py` - Template Python script

- **references/** - Directory for reference documentation
  - `api_reference.md` - Template API reference

- **assets/** - Directory for templates and resources
  - `example_asset.txt` - Template asset file

---

## Next Steps

For each skill, you should:

1. **Review the GitHub repository** - Read the README and documentation from the corresponding tool in `github download/`

2. **Customize SKILL.md**:
   - Complete the description with specific tool information
   - Add "When to Use" scenarios based on the tool's capabilities
   - Choose appropriate structure (workflow-based, task-based, etc.)
   - Add concrete examples and code snippets
   - Remove template guidance sections

3. **Update resources**:
   - Add relevant scripts from the GitHub repo to `scripts/`
   - Create reference documentation in `references/`
   - Add templates or assets to `assets/`
   - Delete unused example files

4. **Validate the skill**:
   ```bash
   python3 AI_Act_skills/skill-creator/scripts/quick_validate.py <skill-path>
   ```

5. **Test the skill** with Claude Code to ensure it provides useful guidance

---

## Directory Structure

```
AI_Act_skills/
├── cybersecurity/
│   └── skills/
│       └── prompt-injection-detector/
├── environment/
│   └── skills/
│       ├── codecarbon/
│       ├── cloud-carbon-footprint/
│       ├── ml-co2-impact/
│       └── watttime-carbon/
├── technical/
│   └── skills/
│       ├── evidently-ai/
│       ├── alibi-detect/
│       ├── ragas/
│       ├── deepeval/
│       ├── huggingface-evaluate/
│       ├── langsmith/
│       ├── weights-and-biases/
│       └── promptfoo/
├── trust/
│   └── skills/
│       ├── shap-explainer/
│       ├── lime/
│       ├── captum/
│       ├── interpretml/
│       ├── what-if-tool/
│       └── axe-accessibility/
├── fundamental-rights/
│   └── skills/
│       ├── ai-fairness-360/
│       ├── fairlearn/
│       ├── aequitas/
│       ├── perspective-api/
│       ├── moderate-content-api/
│       └── disaggregated-evaluation/
├── societal/
│   └── skills/
│       ├── detoxify/
│       ├── claimbuster-api/
│       ├── textblob-sentiment/
│       ├── vader-sentiment/
│       ├── hate-speech-detector/
│       ├── ai-content-detector/
│       └── perspective-api-societal/
├── third-party/
│   └── skills/
│       ├── snyk-io/
│       ├── safety-pyup/
│       ├── npm-audit/
│       ├── syft-sbom/
│       ├── grype-vulnerability/
│       ├── oss-scorecard/
│       └── license-checker/
├── health-safety/
│   └── skills/
│       └── conformance-calibration/
└── eu-ai-act-compliance/
    └── skills/
        ├── model-cards-generator/
        ├── ai-system-registry/
        ├── model-card-generation/
        ├── ai-transparency-labels/
        ├── qms-tracker/
        ├── ai-logging-system/
        └── ce-marking-generator/
```

---

## Related Files

- **Source:** `github download/` - Original GitHub repositories
- **Download Summary:** `github download/DOWNLOAD_SUMMARY.md` - Details about downloaded tools
- **Skill Creator:** `AI_Act_skills/skill-creator/` - Tools for creating and managing skills

---

## Notes

- All skills were created using the `init_skill.py` script from the skill-creator
- Skills follow the same structure and organization pattern
- Each skill requires customization based on the specific tool's documentation
- Some tools are API references (not GitHub repos) and will need different documentation approaches
