# Test Agents

This folder contains test implementations of AI agents for EU AI Act compliance and assistance.

## Structure

```
test-agents/
├── ai-act-cli/           # AI Act CLI tools and governance agent
│   ├── ai_act_cli.py              # Main CLI interface
│   ├── ai_act_provider.py         # AI Act provider implementation
│   ├── ai_risk_classifier.py      # Risk classification tool
│   ├── query_ai_act.py            # Query AI Act regulations
│   ├── setup_ai_act_store.py      # Setup AI Act knowledge store
│   └── governance-agent/          # Governance AI Agent
│       ├── cli.py                 # Agent CLI
│       ├── governance_agent.py    # Core agent implementation
│       ├── config.yaml            # Configuration
│       ├── requirements.txt       # Python dependencies
│       └── examples/              # Usage examples
└── lisa-agent/           # LISA (Legal Information Support Assistant)
    ├── autofill_ai.py             # AI autofill functionality
    ├── form_analyzer.py           # Form analysis tools
    ├── gemini_client.py           # Gemini API client
    ├── lisa_rag.py                # RAG implementation
    ├── run_mock_tests.py          # Test runner
    ├── test_form_fields.py        # Form field tests
    └── README.md                  # LISA agent documentation
```

## AI Act CLI

The AI Act CLI provides tools for:
- Risk classification of AI systems
- Querying EU AI Act regulations
- Governance plan generation
- Compliance checking

### Quick Start - Governance Agent

```bash
cd ai-act-cli/governance-agent
pip install -r requirements.txt
python cli.py --help
```

See [governance-agent/QUICKSTART.md](ai-act-cli/governance-agent/QUICKSTART.md) for detailed instructions.

## LISA Agent

LISA (Legal Information Support Assistant) provides:
- Automated form filling for AI Act compliance
- RAG-based document analysis
- Form field validation
- EU AI Act knowledge retrieval

### Quick Start - LISA Agent

```bash
cd lisa-agent
# See README.md for setup instructions
python autofill_ai.py
```

See [lisa-agent/README.md](lisa-agent/README.md) for detailed instructions.

## Usage

Both agents can be used independently or integrated into larger compliance workflows. Refer to the individual README files in each subdirectory for specific usage instructions and examples.
