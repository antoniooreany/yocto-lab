# yocto-lab

A small learning sandbox for Yocto/BitBake, created to understand the fundamentals of custom layers, recipes, and build configuration.

This repository serves as a companion project to [embedded-ci-lab](https://github.com/antoniooreany/embedded-ci-lab), where the focus is on robust CI tooling. Here, the focus is on the Yocto/BitBake metadata domain.

## What this repo contains
- **Minimal Layer Structure:** A clean directory layout demonstrating a custom layer (`meta-example`).
- **Hello World Recipe:** A simple `hello_1.0.bb` recipe showing basic metadata and file installation.
- **Config Examples:** Sample `bblayers.conf` and `local.conf` files for learning.
- **Validation Tool:** A tiny Python script (`tools/check_layer.py`) to validate the expected directory structure.

## What is this repo (and what it isn't)
- **It is:** An educational playground for Yocto metadata and an educational template for beginners.
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
