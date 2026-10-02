# Pull Request (PR) Submission Guide — New Lunar Accord (NLA)

Thank you for contributing to the **New Lunar Accord (NLA)**! This guide outlines the steps for developers, scientists, and sci-fi enthusiasts worldwide to submit code, mathematical calculations, CAD models, or lore expansions.

---

## 🚀 Step-by-Step Contribution Workflow

### 1. Fork & Clone
1. Fork the `LunarAccord-NLA` repository to your personal GitHub account.
2. Clone your fork locally:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/LunarAccord-NLA.git](https://github.com/YOUR_USERNAME/LunarAccord-NLA.git)
   cd LunarAccord-NLA2. Create a Feature Branch
Use a descriptive branch name reflecting your contribution type:

Code/Scripts: feat/script-radiation-model

Calculations: calc/helium3-yield

Documentation/Lore: docs/sector-expansion

Assets/CAD: assets/rover-3d-model

Bash
git checkout -b feat/your-feature-name
3. Local Verification
Ensure Python scripts adhere to PEP 8 standards and execute without errors (python3 scripts/your_script.py).

Verify Markdown files render correctly with proper headers and tables.

Validate SVG/CAD files for compatibility and clean vector paths.

4. Commit & Push
Write clear, structured commit messages:

Bash
git commit -m "feat(scripts): add bio-dome humidity control algorithm"
git push origin feat/your-feature-name
5. Submit the Pull Request
Go to the main repository on GitHub and click New Pull Request. Complete the PR template checklist below in your pull request description.

📋 Pull Request Template (Copy into PR Description)
Markdown
### 🌌 Contribution Summary
Provide a concise overview of what this PR introduces (e.g., new calculation script, documentation update, CAD asset).

### 🛠️ Type of Change
- [ ] 🐍 **Python / C++ Script** (Simulation, resource calculation, telemetry)
- [ ] 📄 **Documentation / Lore** (Treaty update, sector spec, safety protocol)
- [ ] 📐 **3D Model / CAD / Vector** (.STL, FreeCAD, SVG, maps)
- [ ] 🐛 **Bug Fix / Refactoring** (Optimization, script correction)

### 🧪 Testing & Verification
- [ ] Script tested locally with expected CLI output.
- [ ] Math formulas independently verified.
- [ ] Markdown files formatted and checked for typos.

### 📜 Related Issue
Fixes/Addresses Issue # (if applicable).

---

### 2. `.github/ISSUE_TEMPLATE.md`
Salve este arquivo no diretório `.github/ISSUE_TEMPLATE.md` ou na raiz do projeto:

```markdown
# Issue & Proposal Templates — New Lunar Accord (NLA)

Select the relevant template structure below when opening a new issue in the repository.

---

## Template 1: Feature or Calculation Proposal

```markdown
---
name: Feature / Calculation Proposal
about: Propose a new simulation script, mathematical model, or lunar module
title: '[PROPOSAL] '
labels: enhancement, proposal
assignees: ''
---

### 💡 Proposed Concept
A clear and concise description of the new feature, script, or calculation module you are proposing (e.g., "Add a lunar soil sintering energy calculator").

### 📊 Scientific or Technical Basis
Provide the underlying logic, equations, or parameters (e.g., energy required per kg of regolith melted by microwave/laser).

### 🛰️ Targeted Sector / Scope
- [ ] Sector US (Republic Logistics)
- [ ] Sector CN/RU (Empire Mining & Energy)
- [ ] Sector BR (Life Support & Agriculture)
- [ ] Universal / Inter-Sector Protocol

### 🛠️ Implementation Plan
- [ ] Describe the intended language/format (Python, Markdown, CAD, SVG).
- [ ] Willing to submit a PR for this proposal? (Yes / No)
Template 2: Bug Report or Script Error
Markdown
---
name: Bug Report / Calculation Error
about: Report a broken script, incorrect math, or documentation flaw
title: '[BUG] '
labels: bug, triage
assignees: ''
---

### 🐛 Problem Description
A clear description of what the error is or which calculation yields incorrect results.

### 🔄 Steps to Reproduce
1. Run script `python3 scripts/lunar_resource_calc.py -c 50 -d 100`
2. Observe error or unexpected value at line XX.

### 🎯 Expected Behavior
What output or result was expected based on physics/biology calculations.

### 💻 System Info
- OS: Linux (Debian) / macOS / Windows
- Python Version: 3.x

---

### Estrutura Final Recomendada do Repositório:

```text
LunarAccord-NLA/
├── README.md
├── CONTRIBUTING.md
├── PULL_REQUEST_TEMPLATE.md
├── LICENSE
├── .github/
│   └── ISSUE_TEMPLATE.md
├── assets/
│   └── br_sector_tree_of_life.svg
├── docs/
│   ├── NEW_LUNAR_ACCORD.md
│   ├── BRAZIL_AGRO_BIOSPHERE.md
│   └── SAFETY_PROTOCOLS.md
└── scripts/
    └── lunar_resource_calc.py
