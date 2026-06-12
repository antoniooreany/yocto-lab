# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.2] - 2026-06-10

### Fixed
- **Documentation:** Corrected typographical errors ("artefacts" -> "artifacts") in README integration examples.

## [0.3.1] - 2026-06-10

### Changed
- **Major Documentation Refactor:**
    - Consolidated all ecosystem integration narratives into a single, cohesive README.
    - Synchronized documentation style and structure with the `embedded-ci-lab` repository.
    - Added a clickable Table of Contents and "Project Scope" section.
    - Expanded "Running the Integration Demo" guide with multi-platform (Bash/PowerShell) support.
    - Integrated "Integration Concept" ASCII diagram to visualize project synergy.
- **Project Positioning:** Refined "Portfolio Highlights" and "Motivation" sections to better target automotive/embedded CI roles.

## [0.3.0] - 2026-06-10

### Changed
- **Professional Naming Refactor:**
    - Renamed `meta-example` to `meta-yocto-lab`.
    - Renamed `recipes-example` to `recipes-apps` (Application Layer focus).
    - Renamed `conf-examples` to `samples`.
- **Infrastructure Updates:**
    - Updated `layer.conf` with new collection name (`yocto-lab`) and priority.
    - Updated `tools/check_layer.py` validation logic for the new structure.
    - Fixed `samples/bblayers.conf` to point to the correct layer path.
- **Documentation:** Updated README.md to reflect the professional architectural changes.

## [0.2.0] - 2026-06-10

### Added
- **MIT License:** Project now explicitly licensed under MIT.
- **GitHub Actions CI:** Automated metadata validation on every push/PR via `tools/check_layer.py`.
- **Yocto-specific .gitignore:** Properly handles BitBake build artifacts and Python cache.
- **Project Badges:** Build status, Python version, and License badges in README.

### Changed
- **Documentation Refinement:** Improved README with project positioning, "Relationship to embedded-ci-lab" section, and detailed command exploration notes.

## [0.1.1] - 2026-06-10

### Added
- **Commands Explored:** Detailed section in README documenting BitBake and local tool usage.
- **Interview Positioning:** Refined project narrative for better professional visibility.

## [0.1.0] - 2026-06-10

### Added
- **Minimal Layer Structure:** Custom layer `meta-example`.
- **Hello World Recipe:** `hello_1.0.bb` and supporting shell script.
- **Config Examples:** `bblayers.conf` and `local.conf` samples.
- **Validation Tool:** Initial Python-based structural check.
