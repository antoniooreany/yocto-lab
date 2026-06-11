# yocto-lab
![Metadata Validation](https://github.com/antoniooreany/yocto-lab/actions/workflows/validate.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A small learning sandbox for Yocto/BitBake, created to understand the fundamentals of custom layers, recipes, and build configuration.

## Table of Contents
- [Yocto/BitBake Integration Ecosystem](#yoctobitbake-integration-ecosystem)
- [Relationship to embedded-ci-lab](#relationship-to-embedded-ci-lab)
- [What this repo contains](#what-this-repo-contains)
- [What is this repo (and what it isn't)](#what-is-this-repo-and-what-it-isnt)
- [CI Integration Ideas](#ci-integration-ideas)
- [Commands explored](#commands-explored)
- [License](#license)

## Yocto/BitBake Integration Ecosystem
**Engineering Note:** To demonstrate how [embedded-ci-lab](https://github.com/antoniooreany/embedded-ci-lab) manages real-world build metadata, I developed this companion repository, **yocto-lab**, which serves as a hands-on learning sandbox for Yocto/BitBake.

This ecosystem highlights my experience with both CI/CD tooling and build system internals:
- **embedded-ci-lab**: Python-based framework for reliable CI automation, observability, and resource-aware execution.
- **yocto-lab (this repo)**: Proof-of-contact with BitBake/Yocto metadata, featuring a professional layer structure, recipes, and build configurations.

**Integration:** `embedded-ci-lab` uses the `yocto_validate_artifacts` step to perform automated "Sanity Checks" on Yocto metadata. While `yocto-lab` is provided as a hands-on learning sandbox, this framework is fully environment-agnostic. You can validate any Yocto-compatible directory structure anywhere on your file system by configuring the `artifacts_root` in your pipeline definition, or by using environment variables (e.g., `${ARTIFACTS_ROOT}`) for maximum portability across different CI/CD environments (mirroring professional gate-checks like those in Zuul CI).

### Workflow Setup (for yocto-lab demo)
For integration tests and demos, ensure `yocto-lab` is cloned in the same parent directory:
```text
/projects/
├── embedded-ci-lab/
└── yocto-lab/
```

### Running the Integration Demo
By default, the demo expects `yocto-lab` to be in the parent directory. You can override this using the `ARTIFACTS_ROOT` environment variable:

**Option 1: Use the default (../yocto-lab)**
```bash
embedded-ci run --pipeline pipelines/yocto_lab_integration_demo.yaml
```

**Option 2: Override with custom path**
- **On Linux/macOS (Bash):**
  ```bash
  ARTIFACTS_ROOT=/custom/path/to/artefacts embedded-ci run --pipeline pipelines/yocto_lab_integration_demo.yaml
  ```
- **On Windows (PowerShell):**
  ```powershell
  $env:ARTIFACTS_ROOT="/custom/path/to/artefacts"; embedded-ci run --pipeline pipelines/yocto_lab_integration_demo.yaml
  ```
This flexibility is achieved using Bash-style variable expansion (`${ARTIFACTS_ROOT:-../yocto-lab}`) supported natively by the `embedded-ci-lab` pipeline loader.

## Relationship to embedded-ci-lab
This repository is a domain-learning companion to [embedded-ci-lab](https://github.com/antoniooreany/embedded-ci-lab).
- **yocto-lab**: Focuses on Yocto/BitBake metadata (layers, recipes, and configs).
- **embedded-ci-lab**: Focuses on Python-based CI automation, resource guarding, and reporting.

Concepts learned here (such as metadata structure and configuration) provide the foundation for automated validation and inspection tasks implemented in [embedded-ci-lab].

## What this repo contains
- **Professional Layer Structure:** A clean directory layout demonstrating a custom layer (`meta-yocto-lab`).
- **Hello World Recipe:** A simple `hello_1.0.bb` recipe within `recipes-apps` showing basic metadata and file installation.
- **Config Samples:** Provided `samples/` directory with `bblayers.conf` and `local.conf` for quick environment setup.
- **Validation Tool:** A tiny Python script (`tools/check_layer.py`) to validate the expected professional directory structure.

## What is this repo (and what it isn't)
- **It is:** An educational playground for Yocto metadata and an architectural template for beginners.
- **It is NOT:** A full Yocto distribution, a production-ready layer, or a CI system.

## CI Integration Ideas
While this is not a CI project, this layer/recipe sandbox could be validated in a CI environment using:
- `bitbake -p`: To parse the configuration and recipes.
- `bitbake-layers show-layers`: To verify layer inclusion.
- `kas` (or shell-based checks): To automate structural validation.

## Commands explored
### Already run
- `bitbake-layers show-layers`: To verify the layer is correctly parsed.
- `python3 tools/check_layer.py`: Locally validate the expected directory structure (lightweight check).

### Planned
- `bitbake -p`: To check for parsing errors.
- `bitbake hello`: To build the recipe.

## License
MIT
