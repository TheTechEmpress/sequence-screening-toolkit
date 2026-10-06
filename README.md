# sequence-screening-toolkit

Reusable Python utilities for sequence obfuscation, screening calls, and detection-rate analysis.

Extracted from [screening-evasion-eval](https://github.com/TheTechEmpress/screening-evasion-eval), where these utilities were used to evaluate the robustness of a sequence-based screening baseline against adversarial evasion.

## Why this exists

Evaluating biological screening tools requires repeatable, transparent tooling. This repository packages the pieces so anyone can reproduce, extend, or reuse them without rewriting the plumbing.

## Modules

| Module | Purpose |
|---|---|
| `obfuscate.py` | Generate evasive variants of DNA sequences (substitution, fragmentation, padding, reverse-complement) |
| `screen.py` | Call a screening function against a sequence and return a detection result |
| `compare.py` | Compare detection results across techniques and produce summary statistics |
| `visualise.py` | Plot detection rates and export charts |

## Installation

```bash
git clone https://github.com/TheTechEmpress/sequence-screening-toolkit
cd sequence-screening-toolkit
pip install -r requirements.txt
