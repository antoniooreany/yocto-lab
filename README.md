# yocto-lab

   ![Metadata Validation](https://github.com/antoniooreany/yocto-lab/actions/workflows/validate.yml/badge.svg)
   ![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
   ![License](https://img.shields.io/badge/license-MIT-green.svg)

   `yocto-lab` is a small learning sandbox designed to master the fundamentals of Yocto/BitBake metadata architecture, custom layers, and build
   configurations.

   ## Table of Contents
   - [Portfolio Highlights](#portfolio-highlights)
   - [Getting Started](#getting-started)
   - [Usage](#usage)
   - [Yocto/BitBake Integration Ecosystem](#yoctobitbake-integration-ecosystem)
   - [Project structure](#project-structure)
   - [Engineering Decisions](#engineering-decisions)
   - [Future Work](#future-work)

   ## Portfolio Highlights

   This project serves as a domain-specific extension to my CI/CD portfolio, focusing on the complex metadata structures typical of embedded Linux
   environments.

   ### Why this project matters
   It demonstrates the ability to not only build CI tools but also to deeply understand the **domain metadata** (Yocto/BitBake) that these tools
   are designed to serve. It serves as a proof-of-contact project for understanding layers, recipes, and configs.

   ### Skills demonstrated
   - **Yocto Architecture**: Mastering layers, recipes, and configuration file hierarchy.
   - **Metadata as Code**: Applying professional naming conventions and directory structures (`meta-yocto-lab`, `recipes-apps`).
   - **Tooling Integration**: Creating Python-based inspection tools (`check_layer.py`) to bridge the gap between build systems and CI runners.
   - **Quality Assurance**: Automated validation via GitHub Actions.


   ## Getting Started

   ### Prerequisites
    - Python 3.10+
    - Make (optional, for convenience targets)
    - Basic understanding of BitBake (optional)

   ## Usage

   > **Engineering Note:** To orchestrate real-world builds and automated validation for `yocto-lab`, I use
   [embedded-ci-lab](https://github.com/antoniooreany/embedded-ci-lab) as the CI/CD framework.

   You can view the detailed Usage instructions here: https://github.com/antoniooreany/embedded-ci-lab/#usage



   ## Yocto/BitBake Integration Ecosystem

   > **Engineering Note:** To demonstrate how [embedded-ci-lab](https://github.com/antoniooreany/embedded-ci-lab) manages real-world build
   metadata, I developed this companion repository, `yocto-lab`, which serves as a hands-on domain-learning sandbox.

   You can view the detailed Yocto/BitBake Integration Ecosystem instructions here: https://github.com/antoniooreany/embedded-ci-lab/#yoctobitbake-integration-ecosystem


   ## Project structure

   ```text
   yocto-lab/
   ├── .github/workflows/validate.yml
   ├── CHANGELOG.md
   ├── LICENSE
   ├── README.md
   ├── .gitignore
   ├── meta-yocto-lab/
   │   ├── conf/
   │   └── recipes-apps/
   │       └── hello/
   │           └── files/
   ├── samples/
   └── tools/
   ```

   ## Engineering Decisions

   - **Naming Conventions**: Transitioned from `meta-example` to `meta-yocto-lab` to mirror industry-standard naming.
   - **Semantic Versioning**: Strict adherence to SemVer and [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) for project history.
   - **Minimalism**: Intentionally kept small to focus on structural integrity rather than build times.

   ## Future Work

   We aim to evolve `yocto-lab` into a more comprehensive domain-learning platform. Planned improvements include:

   ### 1. Advanced Metadata
   - **Complex Layer Integration**: Integrate `meta-security` or `meta-virtualization` to explore cross-layer dependencies and security-hardened
   configurations.
   - **Hardware Platform Support**: Extend configuration samples to include real-world boards (e.g., Raspberry Pi 4) beyond the QEMU emulator.

   ### 2. Automation & Compliance
   - **SDK Automation**: Implement CI steps to automatically generate and validate extensible SDKs (eSDK) for developer onboarding.
   - **Compliance & SBOM**: Add automated SPDX/CycloneDX generation to demonstrate software supply chain transparency for embedded Linux.

   ### 3. CI Optimization
   - **Environment Automation**: Transition environment setup to `kas` to provide a more standardized and reproducible build entry point.
   - **Multi-distro Validation**: Test metadata compatibility across different Yocto LTS releases (e.g., Kirkstone vs. Scarthgap) within the CI
   pipeline.

   ## License
   MIT