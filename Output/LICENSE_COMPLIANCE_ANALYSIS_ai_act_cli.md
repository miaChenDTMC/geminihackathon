# Open Source License Compliance Analysis
## AI Act CLI Tool (`ai_act_cli.py`)

**Analysis Date:** 2026-01-10
**Analyzed File:** `ai_act_cli.py`
**Tool Version:** 1.0.0
**Analysis Type:** Dependency License Compliance

---

## Executive Summary

The EU AI Act Query Assistant (`ai_act_cli.py`) is a Limited Risk AI system that uses multiple open source dependencies. This analysis evaluates license compliance, identifies potential risks, and provides recommendations for distribution.

**Overall Compliance Status:** ✓ COMPLIANT
**Distribution Model:** Desktop/CLI Application
**Project License:** Not explicitly specified (Recommended: MIT or Apache-2.0)

---

## 1. Dependency Analysis

### 1.1 Direct Dependencies

| Package | License | Category | SPDX ID | Status |
|---------|---------|----------|---------|--------|
| **google-genai** | Apache-2.0 | Permissive | Apache-2.0 | ✓ Approved |
| **rich** | MIT | Permissive | MIT | ✓ Approved |
| **Python (Runtime)** | PSF-2.0 | Permissive | Python-2.0 | ✓ Approved |

### 1.2 Indirect Dependencies (Key Libraries)

Through `rich`:
- **markdown-it-py** (MIT)
- **Pygments** (BSD-2-Clause)
- **typing-extensions** (PSF-2.0)

Through `google-genai`:
- **google-auth** (Apache-2.0)
- **protobuf** (BSD-3-Clause)
- **requests** (Apache-2.0)
- **urllib3** (MIT)

---

## 2. License Compatibility Assessment

### 2.1 Inbound Licenses

All dependencies use permissive licenses:
- **MIT**: Minimal obligations (attribution only)
- **Apache-2.0**: Attribution + NOTICE file requirements
- **BSD-2-Clause/BSD-3-Clause**: Attribution requirements
- **PSF-2.0**: Python-specific permissive license

### 2.2 Compatibility Matrix

```text
Inbound → Outbound Compatibility:

FROM          | TO: MIT | TO: Apache-2.0 | TO: GPL-3.0 | TO: Proprietary
--------------|---------|----------------|-------------|------------------
MIT           |    ✓    |       ✓        |      ✓      |        ✓
Apache-2.0    |    ✗    |       ✓        |      ✓*     |        ✓
BSD-2/3       |    ✓    |       ✓        |      ✓      |        ✓
PSF-2.0       |    ✓    |       ✓        |      ✓      |        ✓

* GPL-3.0 only (incompatible with GPL-2.0)
```

### 2.3 Recommended Outbound Licenses

Given the dependency mix (including Apache-2.0):

1. **Apache-2.0** (Recommended) - Compatible with all dependencies, provides patent grant
2. **MIT** (Alternative) - Requires relicensing Apache-2.0 code attribution
3. **GPL-3.0+** (If open source required) - Compatible but restricts commercial use

**Incompatible:**
- GPL-2.0 (Apache-2.0 incompatibility)
- Proprietary without attribution (violates all dependency licenses)

---

## 3. License Obligations

### 3.1 Attribution Requirements

**Required for ALL distributions:**

```markdown
THIRD-PARTY SOFTWARE NOTICES
============================

This software uses the following third-party components:

1. google-genai (Apache-2.0)
   Copyright Google LLC
   https://github.com/googleapis/python-genai

2. rich (MIT License)
   Copyright 2020-present Will McGugan
   https://github.com/Textualize/rich

3. Python Standard Library (PSF-2.0)
   Copyright © 2001-2025 Python Software Foundation
   https://www.python.org/
```

### 3.2 Apache-2.0 Specific Requirements

For `google-genai` and related Google libraries:

1. **NOTICE File:** Include Google's NOTICE file if one exists
2. **State Changes:** Document any modifications to Google library code
3. **Patent Grant:** Users receive patent license from Google
4. **Trademark:** Cannot use Google trademarks without permission

### 3.3 Distribution Obligations by Type

#### Desktop/CLI Distribution (Current Model)
- ✓ Include LICENSE file (your project license)
- ✓ Include NOTICE.txt or THIRD-PARTY-NOTICES.txt
- ✓ Include dependency license texts (recommended in `licenses/` directory)
- ✗ No source code disclosure required (all permissive licenses)

#### SaaS/Web Service Distribution
- ✓ Attribution in UI or `/licenses` endpoint
- ✗ No source code disclosure (no AGPL dependencies)

#### PyPI Package Distribution
- ✓ Set `License` metadata in setup.py/pyproject.toml
- ✓ Include `LICENSE` and `NOTICE.txt` in package
- ✓ Use `license_files` to include dependency licenses

---

## 4. Security & Legal Considerations

### 4.1 Dependency Security

**google-genai:**
- Maintained by Google LLC
- Regular security updates
- Enterprise-grade support
- Risk: Medium (API changes may break compatibility)

**rich:**
- Community-maintained (Will McGugan)
- Active development
- Wide adoption (100M+ downloads)
- Risk: Low

**Recommendations:**
- Pin dependency versions in `requirements.txt`
- Use `pip-audit` or `safety` for vulnerability scanning
- Review Google AI Terms of Service for API usage rights

### 4.2 Data Privacy & GDPR

While not strictly a license issue, note:

- **google-genai** sends data to Google's API servers
- User queries and EU AI Act text are processed externally
- Consider GDPR Article 28 (data processor agreement) requirements
- Inform users that data is sent to Google (Article 50 compliance already implemented)

### 4.3 Patent Considerations

**Apache-2.0 Patent Grant:**
- Google grants patent license for `google-genai` use
- Protection against patent litigation from Google
- Does NOT cover patents from other parties

**MIT/BSD/PSF Licenses:**
- No explicit patent grant
- Implicit license under some jurisdictions
- Lower risk for established libraries like `rich`

---

## 5. Compliance Checklist

### Pre-Distribution

- [ ] **Choose project license** (Recommended: Apache-2.0 or MIT)
- [ ] **Create LICENSE file** with full license text
- [ ] **Generate NOTICE.txt** with all attributions
- [ ] **Review Google AI Terms** for commercial use restrictions
- [ ] **Document dependencies** in requirements.txt with versions
- [ ] **Run license audit** using `pip-licenses` or `pipdeptree`

### Distribution Package

- [ ] **Include in repository:**
  - `LICENSE` (project license)
  - `NOTICE.txt` (third-party attributions)
  - `licenses/` directory (optional but recommended)
  - `requirements.txt` (with pinned versions)

- [ ] **Update setup.py/pyproject.toml:**
  ```python
  license="Apache-2.0",
  license_files=["LICENSE", "NOTICE.txt"],
  classifiers=[
      "License :: OSI Approved :: Apache Software License",
  ]
  ```

### CI/CD Integration

- [ ] **Add license check to CI pipeline**
  ```bash
  pip install pip-licenses
  pip-licenses --format=markdown --with-urls --output-file=LICENSES.md
  ```

- [ ] **Add security scanning**
  ```bash
  pip install pip-audit
  pip-audit --require-hashes --format=json
  ```

---

## 6. Recommendations

### 6.1 Immediate Actions

1. **Add LICENSE file**
   - Recommended: Apache-2.0 (compatible with all dependencies + patent grant)
   - Alternative: MIT (simpler but no patent protection)

2. **Create NOTICE.txt**
   - Include attributions for google-genai, rich, and Python
   - Add Google's NOTICE file content if available

3. **Document license in code**
   - Add SPDX identifier to ai_act_cli.py header:
     ```python
     # SPDX-License-Identifier: Apache-2.0
     # Copyright [Year] [Your Name/Organization]
     ```

### 6.2 Long-Term Best Practices

1. **Automate license tracking**
   - Use `pip-licenses` in CI/CD
   - Fail builds on prohibited licenses (if policy defined)

2. **Establish license policy**
   - Approved: MIT, Apache-2.0, BSD, PSF
   - Requires Review: LGPL, MPL
   - Prohibited: GPL (if proprietary distribution planned), AGPL

3. **Monitor dependency updates**
   - License changes are rare but possible
   - Review before major version upgrades

4. **Legal review for commercial use**
   - If distributing commercially, have legal review:
     - Google AI API Terms of Service
     - Export control requirements (cryptography in dependencies)
     - Industry-specific compliance (HIPAA, PCI-DSS if applicable)

### 6.3 EU AI Act Considerations

As a **Limited Risk AI System**, additional requirements:

1. **Article 50 Compliance:**
   - ✓ Already implemented (transparency notice in code)
   - Ensure license permits required disclosures

2. **Technical Documentation (Article 11):**
   - Include dependency licenses in technical documentation
   - Document data flows (user query → Google API → response)

3. **Third-Party Provider Obligations:**
   - Google acts as AI model provider
   - Review Google's AI Act compliance statements
   - Include in risk assessment documentation

---

## 7. Risk Assessment

| Risk Area | Level | Mitigation |
|-----------|-------|------------|
| **License Violation** | Low | All dependencies use approved permissive licenses |
| **Patent Litigation** | Low | Apache-2.0 provides patent grant from Google |
| **Dependency Vulnerabilities** | Medium | Implement automated security scanning |
| **API ToS Violation** | Medium | Review Google AI Terms, add usage limits if needed |
| **GDPR Non-Compliance** | Medium | Already disclosed AI usage; add data processing agreement |
| **Supply Chain Attack** | Medium | Pin versions, verify checksums, use lock files |

---

## 8. Tooling Recommendations

### 8.1 License Scanning

```bash
# Install license checker
pip install pip-licenses

# Generate license report
pip-licenses --format=markdown --with-urls --output-file=LICENSES_REPORT.md

# Check for GPL contamination (if prohibited)
pip-licenses --format=json | grep -i "gpl"
```

### 8.2 Security Scanning

```bash
# Install security audit tool
pip install pip-audit safety

# Run vulnerability scan
pip-audit --format=json --output=vulnerabilities.json

# Alternative: safety check
safety check --json --output=safety-report.json
```

### 8.3 SBOM Generation

```bash
# Install SBOM generator
pip install cyclonedx-bom

# Generate Software Bill of Materials
cyclonedx-py -r -i requirements.txt -o sbom.json --format json
```

---

## 9. Conclusion

**Compliance Status:** ✓ COMPLIANT

The EU AI Act Query Assistant uses only permissive open source licenses (MIT, Apache-2.0, BSD, PSF-2.0), making it compatible with most distribution models. No copyleft restrictions apply.

**Key Actions Required:**
1. Add project LICENSE file (Apache-2.0 or MIT recommended)
2. Create NOTICE.txt with third-party attributions
3. Review Google AI API Terms for commercial use
4. Implement automated license and security scanning

**EU AI Act Alignment:**
- Article 50 transparency requirements: ✓ Implemented
- No license conflicts with required disclosures
- Google API dependency requires ongoing ToS compliance monitoring

---

## Appendices

### Appendix A: Full Dependency Tree

```text
ai_act_cli.py
├── google-genai (Apache-2.0)
│   ├── google-auth (Apache-2.0)
│   ├── google-api-core (Apache-2.0)
│   ├── protobuf (BSD-3-Clause)
│   ├── requests (Apache-2.0)
│   └── urllib3 (MIT)
├── rich (MIT)
│   ├── markdown-it-py (MIT)
│   ├── Pygments (BSD-2-Clause)
│   └── typing-extensions (PSF-2.0)
└── Python stdlib (PSF-2.0)
    ├── sys
    ├── pathlib
    ├── datetime
    └── os
```

### Appendix B: SPDX License Identifiers

- **MIT**: https://spdx.org/licenses/MIT.html
- **Apache-2.0**: https://spdx.org/licenses/Apache-2.0.html
- **BSD-2-Clause**: https://spdx.org/licenses/BSD-2-Clause.html
- **BSD-3-Clause**: https://spdx.org/licenses/BSD-3-Clause.html
- **PSF-2.0**: https://spdx.org/licenses/Python-2.0.html

### Appendix C: Resources

- SPDX License List: https://spdx.org/licenses/
- Choose A License: https://choosealicense.com/
- OSI Approved Licenses: https://opensource.org/licenses/
- Google Open Source: https://opensource.google/
- Python Packaging Guide: https://packaging.python.org/

---

**Document Control:**
- Version: 1.0
- Date: 2026-01-10
- Analyst: AI Compliance Assessment Tool
- Next Review: 2026-04-10 (or upon major dependency update)
