# Marwadi University – M.Sc. Computer Science Python Practicals

A structured collection of Python lab practicals, assignments, and supporting study material for M.Sc. Computer Science.

## Repository structure

```text
.
├── assignments/
├── docs/
├── practicals-beyond-syllabus/
├── unit-1/
├── unit-2/
├── unit-3/
├── unit-4/
├── FILE_MANIFEST.md
├── README.md
├── requirements.txt
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

## Requirements and setup

- Python 3.10 or later.
- Optional packages used by selected practicals are listed in `requirements.txt`.
- Some database practicals require a local MySQL server and a database/table configured for the example.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run a program from its own folder when it uses relative sample-file paths:

```bash
python 1.py
```

Some programs require terminal input. MySQL examples need a running server and suitable database/table setup. Configure credentials in your local environment; do not commit real passwords or use an empty password in production.

## Validation and notes

- Python syntax compilation was checked for all 84 executable Python files.
- `unit-1/ex1-idle-session-transcript.txt` is a preserved IDLE transcript, not a standalone Python program.
- Syntax validation does not guarantee that every program will run without its required database, packages, input files, or external services.
- Student-identifying details in the source material were replaced with generic placeholders for public sharing.

See [FILE_MANIFEST.md](FILE_MANIFEST.md) for the complete file listing.

## Disclaimer

These materials are intended for educational practice. Review each program and configure external services safely before running it.
