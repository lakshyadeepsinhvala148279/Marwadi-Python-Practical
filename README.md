# Marwadi University – M.Sc. Computer Science Python Practicals

A collection of Python lab practicals, assignments, and supporting study material for M.Sc. Computer Science. Programs are grouped by unit and assignment for easier revision and practice.

> **Privacy note:** Student names and enrollment identifiers found in the original working files have been replaced with generic placeholders before public release.

## Repository structure

```text
.
├── assignments/
├── unit-1/
├── unit-2/
├── unit-3/
├── unit-4/
├── practicals-beyond-syllabus/
├── docs/
├── README.md
└── .gitignore
```

## Contents

| Folder | Contents |
|---|---|
| `unit-1/` | Introductory Python, strings, input/output, and basic operations |
| `unit-2/` | Collections, functions, classes, and database-related examples |
| `unit-3/` | Object-oriented programming, exceptions, files, and regular expressions |
| `unit-4/` | MySQL database practicals and pandas examples |
| `assignments/` | Numbered practical assignments and sample text files |
| `practicals-beyond-syllabus/` | Additional cybersecurity practicals |
| `docs/` | Supporting PDF notes, lab manuals, and index document |

## Requirements

- Python 3.10 or later.
- Optional packages for selected practicals: `mysql-connector-python` and `pandas`.
- A local MySQL server and a database configured for the database practicals.

Install optional dependencies:

```bash
pip install -r requirements.txt
```

Run a script from its own folder so relative sample files are found:

```bash
python 1.py
```

Some programs request terminal input. MySQL examples require a running server and suitable database/table setup. The original classroom connection defaults (`localhost`, `root`, empty password) are placeholders only; configure your own local environment and never use an empty password in production.

## Validation notes

- Python syntax compilation was checked for the 84 executable `.py` files.
- `unit-1/ex1-idle-session-transcript.txt` preserves an IDLE session transcript; it is not a standalone Python program.
- Database and file-I/O programs may need external services or sample files before they run.
- An unrelated file-comparison block was removed from the IP-address practical.

## Disclaimer

Educational lab examples. Review code and configure services safely before running it.
