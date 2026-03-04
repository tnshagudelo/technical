# Accelerators for Developers and QA

This directory contains pre-built templates, best practices, and artifacts designed to accelerate
the day-to-day work of development and quality assurance teams.

## Structure

```
accelerators/
├── dev/                  # Developer accelerators
│   ├── templates/        # Project and code templates
│   ├── best-practices/   # Guidelines and standards
│   └── artifacts/        # Pre-built configuration files and scripts
└── qa/                   # QA accelerators
    ├── templates/        # Test plan, case, and bug-report templates
    ├── best-practices/   # Testing guidelines and standards
    └── artifacts/        # Pre-built test scripts and configuration
```

## How to Use

1. Browse the relevant section (`dev/` or `qa/`).
2. Copy the template or artifact you need into your project.
3. Customise placeholders (marked with `<REPLACE_*>`) for your context.
4. Follow the best-practice guides to keep quality high across the team.

## Contributing

- Keep templates generic and reusable.
- Document every placeholder clearly.
- Validate artifacts before committing (e.g. run `docker build`, execute scripts locally).
