# yocto-lab

![Metadata Validation](https://github.com/antoniooreany/yocto-lab/actions/workflows/validate.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

`yocto-lab` is a small learning sandbox designed to master the fundamentals of Yocto/BitBake metadata architecture, custom layers, and build configurations.

## Table of Contents
- [Portfolio Highlights](#portfolio-highlights)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Yocto/BitBake Integration](#yoctobitbake-integration)
  - [Integration Scenarios (Demos)](#integration-scenarios-demos)
  - [Real-world Yocto Build Guide](#real-world-yocto-build-guide)
- [Project structure](#project-structure)
- [Engineering Decisions](#engineering-decisions)
- [Future Work](#future-work)
- [License](#license)

## Portfolio Highlights

This project serves as a domain-specific extension to my CI/CD portfolio, focusing on the complex metadata structures typical of embedded Linux environments.

### Why this project matters
It demonstrates the ability to not only build CI tools but also to deeply understand the **domain metadata** (Yocto/BitBake) that these tools are designed to serve. It serves as a proof-of-contact project for understanding layers, recipes, and configs.

### Motivation
Modern embedded/automotive development (e.g., at BMW) relies on hundreds of layers and thousands of recipes. Understanding how to structure, version, and validate this metadata is critical. `yocto-lab` was created to explore these patterns in a controlled, minimalist environment.

### Features
- **Professional Layer Structure**: Follows Yocto standards with `meta-yocto-lab`.
- **Application-Layer Focused Recipes**: Organized under `recipes-apps`.
- **Versioned Metadata**: Demonstrates standard naming (`hello_1.0.bb`).
- **Sample Configurations**: Pre-configured `samples/` for `local.conf` and `bblayers.conf`.
- **Automated Validation**: 
  - Local Python-based structure checker (`tools/check_layer.py`).
  - GitHub Actions CI for immediate feedback.
- **Project Hygiene**: MIT Licensed, Yocto-specific `.gitignore`, and detailed `CHANGELOG.md`.

## Getting Started

### Prerequisites
- Python 3.10+
- Basic understanding of BitBake (optional)

### Installation
```bash
git clone https://github.com/antoniooreany/yocto-lab.git
cd yocto-lab
```

## Usage

### Local Validation (Quick Start)
Run the lightweight Python inspector to verify the layer structure:
```bash
python3 tools/check_layer.py
```

### Exploring Commands
Practical commands explored in this sandbox:
- `bitbake-layers show-layers`: Verify layer parsing.
- `bitbake -p`: (Planned) Simulate full parsing checks.
- `bitbake hello`: (Planned) Simulate individual recipe builds.

## Yocto/BitBake Integration

> **Engineering Note:** To demonstrate how [embedded-ci-lab](https://github.com/antoniooreany/embedded-ci-lab) manages real-world build metadata, I developed this companion repository, `yocto-lab`, which serves as a hands-on domain-learning sandbox.

### Integration Scenarios (Demos)

By default, the demo expects `yocto-lab` to be in the parent directory. You can override this using the `ARTIFACTS_ROOT` environment variable:

```bash
# Run integration pipeline
ARTIFACTS_ROOT=~/yocto-work/poky/yocto-lab embedded-ci run --pipeline pipelines/full-yocto-integration.yaml
```

### Real-world Yocto Build Guide

While the default integration scenarios use mocked artifacts for portability, you can use this metadata to orchestrate real Yocto builds and verify them in an emulator.

#### Prerequisites & Environment
Ensure your host system (e.g., Ubuntu 22.04 on WSL2) has the required Yocto build dependencies:
```bash
sudo apt update && sudo apt install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev zstd liblz4-tool -y
```

> **Important Note on Performance:** Always perform BitBake build operations within your native Linux filesystem (e.g., `~/yocto-work/...`). Building on Windows-mounted directories (`/mnt/c/`) will lead to severe performance degradation and permission errors.

#### Infrastructure Recommendations
- **Storage**: Minimum 100GB of free space. To minimize disk usage, we recommend adding `INHERIT += "rm_work"` to your `local.conf`.
- **RAM**: Minimum 16GB (32GB recommended for high-performance parallel builds).

#### Manual Build & Deployment
1.  **Initialize Environment**: Within your Poky directory:
    ```bash
    source oe-init-build-env
    ```
2.  **Add Layer**: Register this layer with BitBake:
    ```bash
    bitbake-layers add-layer path/to/yocto-lab/meta-yocto-lab
    ```
3.  **Configure Image**: Add the following to `conf/local.conf`:
    ```bitbake
    IMAGE_INSTALL:append = " hello"
    ```
4.  **Execute Build**:
    ```bash
    bitbake core-image-minimal
    ```
5.  **Run & Verify (QEMU)**: Launch the emulator and run the custom command:
    ```bash
    runqemu qemux86-64 nographic
    # Log in as root, then run:
    hello
    # Expected output: Hello, Yocto World!
    ```

#### Testing & Troubleshooting
To verify your setup without waiting for a full build:
- **Dry-run**: Use `bitbake -n core-image-minimal`. The `-n` flag simulates execution, allowing you to verify parsing and metadata integrity in seconds.
- **Duration**: The first build will take significant time as it compiles the entire toolchain. Keep the laptop plugged in.

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
│   │   └── layer.conf
│   └── recipes-apps/
│       └── hello/
│           ├── files/
│           │   └── hello.sh
│           └── hello_1.0.bb
├── samples/
│   ├── bblayers.conf
│   └── local.conf
└── tools/
    └── check_layer.py
```

## Engineering Decisions

- **Naming Conventions**: Transitioned from `meta-example` to `meta-yocto-lab` to mirror industry-standard naming.
- **Semantic Versioning**: Strict adherence to SemVer and [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) for project history.
- **Minimalism**: Intentionally kept small to focus on structural integrity rather than build times.

## Future Work

We aim to evolve `yocto-lab` into a more comprehensive domain-learning platform. Planned improvements include:

### 1. Advanced Metadata
- **Complex Layer Integration**: Integrate `meta-security` or `meta-virtualization` to explore cross-layer dependencies and security-hardened configurations.
- **Hardware Platform Support**: Extend configuration samples to include real-world boards (e.g., Raspberry Pi 4) beyond the QEMU emulator.

### 2. Automation & Compliance
- **SDK Automation**: Implement CI steps to automatically generate and validate extensible SDKs (eSDK) for developer onboarding.
- **Compliance & SBOM**: Add automated SPDX/CycloneDX generation to demonstrate software supply chain transparency for embedded Linux.

### 3. CI Optimization
- **Environment Automation**: Transition environment setup to `kas` to provide a more standardized and reproducible build entry point.
- **Multi-distro Validation**: Test metadata compatibility across different Yocto LTS releases (e.g., Kirkstone vs. Scarthgap) within the CI pipeline.

## License
MIT
