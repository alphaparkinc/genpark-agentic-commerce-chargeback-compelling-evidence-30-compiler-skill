# Visa CE 3.0 Compelling Evidence Chargeback Remedy Pack Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Visa Compelling Evidence 3.0 qualifying historical transactions matching, automated pre-arbitration representation, and friendly fraud reverser. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `match_ce30_qualifying_historical_transactions`: Match 2 historical undisputed transactions (> 120 days old) sharing device IP, fingerprint, or login credentials.
- `generate_ce30_vrol_pre_arbitration_packet`: Generate Visa Resolve Online (VROL) formatted response for liability shift under Rule 10.4.

## 🚀 Installation & Usage
```bash
python -m genpark_agentic_commerce_chargeback_compelling_evidence_30_compiler_skill.server --test
```
