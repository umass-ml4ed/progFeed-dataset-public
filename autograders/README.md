# autograders/

Per-lab autograder code used for grading and AI feedback generation.

## Naming Convention

| Suffix | Meaning |
|--------|---------|
| (none) | Basic autograder, no AI |
| `_github` | GitHub Actions-based autograder |
| `_github_ai` | GitHub Actions + AI test case feedback (group 1) |
| `_github_ai_abc` | GitHub Actions + AI feedback with A/B/C experimental conditions (groups 0/1/2) |

## Directories

| Directory | Labs | Notes |
|-----------|------|-------|
| `lab00_autograder` | lab00 | Basic hello world check |
| `lab01_autograder_github` | lab01 | No AI feedback |
| `lab02_autograder_github_ai` | lab02 | AI test case feedback only |
| `lab03_autograder_github_ai` | lab03 | AI test case feedback only |
| `lab05_autograder_github_ai_abc` | lab05 | Full A/B/C experiment |
| `lab06_autograder_github_ai_abc` | lab06 | Full A/B/C experiment |
| `lab07_autograder_github_ai_abc` | lab07 | Full A/B/C experiment |
| `lab09_autograder_github_ai_abc` | lab09 | Full A/B/C experiment |
| `lab10_autograder_github_ai_abc` | lab10 | Full A/B/C experiment |
| `lab11_autograder_github` | lab11 | No AI feedback |
| `preLab01–08_autograder_github` | pre-labs | No AI feedback |

## Key Files Per Autograder

- **`test.py`** — unittest file defining test cases per problem
- **`consent.csv`** — student email → `ExpGroup` mapping (0=control, 1=TC, 2=NL, 3=opt-out)
- **`*_desc.txt`** — problem description files (used by NL feedback generation)
