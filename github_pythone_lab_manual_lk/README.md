# Marwadi University – M.Sc. Computer Science Python Practicals

A collection of Python practical programs, assignments, cybersecurity exercises, and supporting lab documents. The original assignment numbering and program contents are retained, with student-identifying details replaced by placeholders for public sharing.

## Repository structure

```text
.
├── unit-1/
├── unit-2/
├── unit-3/
├── unit-4/
├── assignments/
├── practicals-beyond-syllabus/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Contents

- **Unit 1–4:** Unit-wise Python practicals.
- **Assignments:** Numbered assignments 28–51 and their sample text files.
- **Practicals beyond syllabus:** Eight additional cybersecurity-oriented exercises.
- **Docs:** Original PDF assignment/lab notes and DOCX lab-manual index.

## Requirements

- Python 3.10 or later.
- Optional packages: `mysql-connector-python` and `pandas`.
- MySQL server for database exercises.

Install optional dependencies:

```bash
pip install -r requirements.txt
```

Run a program from its folder, for example:

```bash
python unit-1/1.py
```

Some scripts require terminal input, sample files, third-party packages, or a locally configured MySQL database. Review each script before running it. Database examples use local-development connection settings; set the `MYSQL_PASSWORD` environment variable before running database examples. Never publish real passwords.

## Validation

- 84 `.py` program files are syntax-compilable.
- `unit-1/ex1-idle-session-transcript.txt` is a preserved IDLE shell transcript, not an executable Python script.
- Syntax compilation does not guarantee runtime success when a script depends on external services, files, packages, or user input.

## Privacy

Student name and enrollment-number occurrences in source files and supporting documents have been redacted/replaced with placeholders for public publication.

## Disclaimer

For educational use. Verify commands, inputs, and external-service settings before execution.
