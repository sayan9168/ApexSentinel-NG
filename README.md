# ApexSentinel-NG

### Autonomous network intelligence & reconnaissance engine

High-speed scanning · Service intelligence · CVE mapping · Remote API control

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-yellow)](#disclaimer)

> Inspired by the speed goals of tools like Nmap, Masscan, and RustScan — with a focus on **authorized** security research.

---

## Features

| Feature | Description |
|---------|-------------|
| **Fast scanning core** | Async / high-concurrency port scanning |
| **Service intelligence** | Banner / pattern-based identification |
| **CVE mapping** | Link findings to known vulnerability references |
| **Remote API** | FastAPI control plane for mobile / dashboard use |
| **Auth-aware design** | Intended for systems you own or are authorized to test |

---

## Project layout

```text
ApexSentinel-NG/
├── main.py              # CLI entry
├── scanner_engine.py    # High-speed core
├── vuln_scanner.py      # CVE / exploit mapping helpers
├── api_core.py          # FastAPI remote control
└── requirements.txt
```

---

## Install & run

```bash
git clone https://github.com/sayan9168/ApexSentinel-NG.git
cd ApexSentinel-NG

pip install -r requirements.txt

# CLI scanner
python main.py

# Optional API hub
python api_core.py
```

---

## Disclaimer

**Authorized use only.**  
Scan only systems you own or have explicit written permission to test.  
The author assumes no liability for misuse.

---

## Author

[Sayan Mahata](https://github.com/sayan9168) — 2026
