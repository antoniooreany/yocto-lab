# yocto-lab
![Metadata Validation](https://github.com/antoniooreany/yocto-lab/actions/workflows/validate.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A small learning sandbox for Yocto/BitBake, created to understand the fundamentals of custom layers, recipes, and build configuration.

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
