
# 🛠️ Operations & Developer Guide

## 1. Executive Overview

This project leverages **Task** (`Taskfile.yml`) as its canonical automation orchestrator. The decision to standardize on Task—over traditional `Makefile`s or a collection of disparate shell scripts—is a deliberate architectural choice designed to enforce clarity, discoverability, and maintainability across all development and CI/CD workflows.

### Core Principles
The primary goals of this system are to:
-   **Eliminate Ambiguity:** Provide a single, authoritative entry point (`task <command>`) for all operational tasks.
-   **Maximize Discoverability:** Enable any developer to instantly see all available workflows with `task --list-all`.
-   **Enforce Separation of Concerns:** Isolate domain-specific logic (e.g., infrastructure vs. testing) into modular, self-contained files.
-   **Ensure Reproducibility:** Guarantee that automation behaves identically on developer machines and in CI pipelines.

### Task Hierarchy & Modular Design
Our automation architecture is not monolithic. It is composed of a central orchestrator and several domain-specific modules, promoting scalability and ease of maintenance.

-   **The Root `Taskfile.yml` (The Orchestrator):** This file serves as the public API for developers. It defines high-level, user-facing commands (e.g., `setup`, `run-v2`) and global project variables. It uses the `includes` directive to delegate the low-level implementation details to specialized modules.

-   **The Modular Taskfiles (`tasks/*.yml`):** Each file within the `tasks/` directory encapsulates the logic for a single operational domain. This design prevents the root Taskfile from becoming bloated and makes it easier to modify or debug specific parts of the automation pipeline without affecting others.

The relationship is as follows:

| Namespace | Responsibility | Source File |
| :--- | :--- | :--- |
| `infra:` | Manages Dockerized test harnesses (Allure Bridges). | `tasks/Taskfile.infra.yml` |
| `audit:` | Executes Pytest suites against FIPS containers. | `tasks/Taskfile.audit.yml` |
| `report:` | Generates and serves static HTML test artifacts. | `tasks/Taskfile.report.yml` |

This layered architecture ensures that our automation is scalable, maintainable, and easy for new developers to navigate.




## 2. Architecture & Orchestration

The automation layer is engineered as a decoupled, modular ecosystem. Rather than a linear script, it functions as an orchestration engine where specialized modules interact through well-defined interfaces (shared directories and environment variables).

### 2.1 Modular Design Philosophy
The system is partitioned into four primary domains, each isolated within its own namespace. This separation ensures that changes in the reporting logic do not inadvertently break the infrastructure or auditing logic.

*   **`infra` (The Environment Layer):** Encapsulates the "Bridge" architecture. It treats reporting tools (Allure) as ephemeral infrastructure, containerizing them to ensure version consistency across all developer environments.
*   **`audit` (The Execution Layer):** The core engine of the project. It handles the invocation of the Pytest suite. It is designed to be "Image Agnostic," meaning it can inject different container targets (`distroless` vs. `standard`) into the same test logic.
*   **`report` (The Visualization Layer):** Responsible for transforming raw JSON/XML test results into human-readable insights. It abstracts the complexity of Docker volume mounting and port mapping, providing a seamless "Serve" experience.
*   **`docs` (The Knowledge Layer):** The final stage of the pipeline. It aggregates performance data, test metrics, and GitHub metadata to synchronize the project's documentation (`README.md` and `docs/`) with the actual state of the code.

### 2.2 Orchestration & Dependency Graph
To maintain system integrity, the `Taskfile` enforces a strict execution order. While many tasks can be run in isolation for debugging, the production pipeline follows a **Directed Acyclic Graph (DAG)** to ensure prerequisites are met.

#### The Core Dependency Chain:
1.  **Provisioning Phase (`infra`):** Before any audit can occur, the `setup` task ensures that the Allure Bridge images exist.
2.  **Validation Phase (`audit`):** Once the infrastructure is ready, the audit engine executes. It generates raw data artifacts in the `allure-results/` directory.
3.  **Synthesis Phase (`report` / `docs`):** These tasks depend on the presence of the audit artifacts. They consume the raw data to produce the final HTML reports and Markdown documentation.

#### Visualizing the Flow:
```mermaid
graph LR
    subgraph Initialization
        infra[Task: setup] --> |Builds Bridges| D[(Docker Images)]
    end

    subgraph Verification
        D --> audit[Task: audit:run]
        audit --> |Writes| R[(allure-results)]
    end

    subgraph Presentation
        R --> report[Task: report:serve]
        R --> docs[Task: docs:generate]
        docs --> |Updates| MD[README.md]
    end

    style infra fill:#f9f,stroke:#333,stroke-width:2px
    style audit fill:#bbf,stroke:#333,stroke-width:2px
    style MD fill:#dfd,stroke:#333,stroke-width:4px
```

### 2.3 Variable Propagation & State
State is managed across modules using two primary mechanisms:
*   **Static Variables:** Defined in the root `vars:` section (e.g., `registry`, `owner`), ensuring a "Single Source of Truth" for project-wide constants.
*   **Dynamic Artifacts:** Modules communicate by passing files through standardized directories (`allure-results/`, `allure-report/`). This allows the `report` module to remain independent of the `audit` module’s internal logic—it only cares that the results directory exists and contains valid data.






---

## 3. Stage 01: Environment Bootstrapping

Before executing the verification suites, the local environment must be provisioned with the necessary "Bridges." These are containerized versions of our reporting and auditing tools, ensuring we don't pollute the host system with specific version dependencies.

### 3.1 Local Toolchain Prerequisites
To interface with the automation engine, ensure the following are installed on your host:
- **Task (Go-Task):** The orchestrator (`brew install go-task`).
- **Docker:** Required for running the Wolfi images and the Allure Bridges.
- **Python 3.10+ & Pipenv:** Required for the metadata generation and README update scripts.

### 3.2 Infrastructure as Code: The Allure Bridges
We utilize a "Bridge Architecture" for our reporting. Instead of requiring you to install Java or the Allure CLI locally, we encapsulate these in lightweight Docker images:
- **`allure2-bridge`**: Optimized for standard reporting.
- **`allure3-bridge`**: Used for advanced visualization and analytics.

To build these harnesses, run the primary setup command:
```bash
# Orchestrates the building of both Allure v2 and v3 bridge images
task setup
```

### 3.3 Dependency Management (Python)
Our documentation and benchmarking logic rely on specialized Python scripts. We use `pipenv` to manage a deterministic virtual environment.

```bash
# Initialize the Python environment and install locked dependencies
pipenv install
```

### 3.4 Why This Stage is Critical
1. **Version Pinning:** By building the bridges locally via `infra:build-all`, we guarantee that the report generation logic is identical across the entire team.
2. **Isolation:** No Allure or Java binaries are needed on your host machine; everything runs within an isolated Docker context.
3. **Readiness:** Once this stage is complete, the system enters a "Ready" state, allowing for the execution of the `audit:` and `report:` tasks.

---

> [!NOTE]
> *   **Infrastructure-as-Tooling:** We treat our reporting tools as part of the infrastructure. If the bridge doesn't exist, the pipeline shouldn't proceed.
> *   **Idempotency:** The `setup` task is idempotent; you can run it multiple times, and it will only rebuild images if the underlying Dockerfiles or context have changed.
>
> 


---

## 4. Stage 02: Verification & Auditing

The auditing engine is built on top of `pytest` and is designed to be completely decoupled from the container lifecycle. It treats the target image as an external dependency, allowing for high-velocity testing across multiple environments.

### 4.1 Single Image Audit (Default Workflow)
This is the standard entry point for developers. It executes the full suite of FIPS compliance tests against the pre-defined production-grade image (usually the `distroless` variant).

```bash
# Executes tests against the image defined in DEFAULT_IMAGE
task audit:run
```

**What happens under the hood:**
1.  The system identifies the target image.
2.  A temporary environment is provisioned to execute `pytest`.
3.  Test results and an `environment.properties` file are generated inside the `allure-results/` directory for downstream reporting.

### 4.2 Multi-Variant Testing (The Matrix)
In high-assurance environments, we must ensure that security properties are consistent across all distribution flavors. The `multi` task automates the validation of both the hardened `distroless` image and the `standard` (shell-enabled) image in a single execution loop.

```bash
# Validates both image variants sequentially
task audit:multi
```

**Technical Rationale:**
*   **Standard Image:** Validates that the FIPS module works in interactive/CI environments.
*   **Distroless Image:** Validates the final production artifact where the attack surface is minimized.

### 4.3 Runtime Overrides & CLI Flexibility
The audit system is engineered for "Injection." You can point the audit suite at any image—whether it’s a local build or a remote staging image—without modifying the `Taskfile`.

**Pattern: Overriding via Environment Variables**
```bash
# Run the audit against a specific local tag or remote registry
task audit:run IMAGE="ghcr.io/your-org/wolfi-openssl:debug-feat-x"
```

**The `SAFE_NAME` Logic (Technical Detail):**
To prevent data collision when testing multiple images, the Taskfile employs a sanitization logic:
```yaml
SAFE_NAME: '{{.IMG_SAFE | replace "/" "_" | replace ":" "_" | replace "." "_"}}'
```
This ensures that results for `ghcr.io/repo:latest` are stored in `allure-results/audit_ghcr_io_repo_latest/`. This allows you to run audits for multiple versions and compare them in a single Allure report without overwriting data.

### 4.4 Result Persistence
Every audit run generates a structured output:
*   **`allure-results/`**: Contains the raw JSON/XML data.
*   **`environment.properties`**: Dynamically generated during the run to inject the exact Image ID into the final report, ensuring full traceability from "Test Result" to "Container Binary."

---
## 5. Stage 03: Reporting & Observability

In high-compliance environments (FIPS 140-3), a "passed test" is only as good as its documentation. This stage abstracts the complexity of data visualization using a **Bridge Architecture**, allowing us to generate high-fidelity reports without host-side dependencies.

### 5.1 The Reporting Philosophy: "Data vs. Insights"
Our pipeline generates massive amounts of raw JSON and XML artifacts during the `audit` stage. Stage 03 is responsible for the **Synthesis** of this data. We treat our reporting infrastructure as ephemeral; the reports are generated on-demand inside isolated containers to ensure that the visualization logic remains consistent regardless of where the developer is working.

### 5.2 Dual-Engine Support: Allure v2 vs. Allure v3
We provide two distinct reporting engines to cater to different operational needs:

*   **Allure v2 (The Industry Standard):** Best for stable, daily compliance checks. It provides a proven, highly-compatible UI that security auditors are familiar with.
    *   *Command:* `task run-v2` (Orchestrates Audit + Serve)
*   **Allure v3 (Advanced Analytics):** Leveraged for deep-dive performance analysis and complex multi-test trend visualization. It offers a more modern reactive UI for inspecting cryptographic execution timings.
    *   *Command:* `task run-v3` (Orchestrates Audit + Serve)

### 5.3 The Bridge Abstraction (Containerized Reporting)
To maintain a "Zero-Install" policy on host machines, we use **Dockerized Bridges**. These bridges handle the complex Java/Node environments required by Allure:
1.  **Mounting:** The `allure-results/` directory is mounted as a read-only volume into the bridge container.
2.  **Transformation:** The bridge binary parses the raw results and compiles a static, single-page application (SPA).
3.  **Serving:** A micro-web server is spawned inside the container, mapped to host ports (`8080` or `8081`), allowing the developer to interact with the report via a local browser.

### 5.4 Multi-Audit Aggregation (The "Single Pane of Glass")
One of the most powerful features of our orchestration is the ability to aggregate results from different image variants (`standard` vs. `distroless`) into a single report.

By using the globbing pattern `{{.RESULTS_DIR}}/audit_*`, the reporting engine automatically discovers every test session executed in the current workspace. This allows auditors to:
*   Compare FIPS compliance across different base OS versions side-by-side.
*   Identify if a specific vulnerability or failure is restricted to the `distroless` environment or is a core `OpenSSL` issue.

### 5.5 Critical Observability Metrics
Our reports are configured to highlight the following **KPIs (Key Performance Indicators)**:
*   **Cryptographic Boundary Integrity:** Did the FIPS provider load correctly?
*   **Algorithm Blocking:** Confirmation that non-approved algorithms (e.g., MD5 in FIPS mode) were successfully rejected.
*   **KAT (Known Answer Tests) Latency:** Timing metrics for self-tests to ensure no performance regressions in the cryptographic engine.

### 5.6 Manual Lifecycle Management
While `task run-v2` is the standard "one-shot" command, senior engineers can control the lifecycle manually:
```bash
# Generate the report without opening a browser (useful for CI artifacts)
task report:v2:gen

# Serve existing results from a previous CI run downloaded locally
task report:v2:serve
```

---



>[!IMPORTANT]
>"By decoupling the Audit (Data Generation) from the Report (Data Visualization), we create a 'Tamper-Evident' workflow. The reporting bridge ensures that the data is presented exactly as it was captured, providing a reliable 'Chain of Custody' for our FIPS compliance artifacts."



---

## 6. Stage 04: Performance & Benchmarking

The benchmarking pipeline is designed to provide empirical evidence of the operational efficiency of the Wolfi-OpenSSL FIPS stack. We move beyond "it works" to "it performs at scale," ensuring that security hardening does not become a bottleneck for cloud-native workloads.

### 6.1 The Benchmarking Philosophy: "Quantifying the FIPS Tax"
Running OpenSSL in FIPS mode involves additional entropy gathering and algorithmic constraints. Our goal is to benchmark the **Delta** between standard execution and FIPS-validated execution across various ciphers (AES-GCM, RSA, ECDSA, etc.).

### 6.2 The Profiling Engine (`run_benchmark.sh`)
The core workload is driven by the `docs:benchmark` task. This engine executes a series of `openssl speed` commands within the target container environment. 
*   **Parallelism Control:** Benchmarks are executed in controlled environments to minimize "Noisy Neighbor" interference.
*   **Standardization:** We measure throughput (bytes per second) and latency (operations per second) for varying buffer sizes (16b to 16kb) to simulate real-world packet sizes.

### 6.3 Automated Data Parsing (`parser.py`)
Raw OpenSSL output is notoriously difficult to consume (ASCII tables). Our `docs:parse-benchmark` task utilizes a specialized Python-based parser to:
1.  **Extract:** Scrape the raw logs for specific algorithmic metrics.
2.  **Normalize:** Convert various units (kibi-bytes vs kilo-bytes) into a standardized SI format.
3.  **Structure:** Transform the unstructured text into a machine-readable JSON/CSV intermediate state. This allows us to track performance regressions over time across different versions of the FIPS provider.

### 6.4 Statistical Synthesis & Reporting
The final phase, `docs:all-report-benchmark`, aggregates the parsed data and invokes a Python-based reporting engine (`generate_report.py`) to produce high-fidelity visualizations.

*   **Regression Analysis:** The system is designed to compare the current build's performance against historical baselines.
*   **Heatmaps & Throughput Curves:** Instead of single data points, we generate curves that show how the FIPS provider scales with larger data chunks—critical for high-throughput TLS termination proxies.

### 6.5 Operational Commands
To trigger the full performance profiling and reporting pipeline:

```bash
# Complete End-to-End Pipeline: Run -> Parse -> Report
task docs:all-report-benchmark
```

For granular control, you can execute individual stages:
```bash
# Step 1: Execute the raw benchmark workloads
task docs:benchmark

# Step 2: Transform raw logs into structured data
task docs:parse-benchmark
```

### 6.6 Performance Metadata
Every benchmark report is tagged with:
*   **CPU Instruction Sets:** (e.g., AES-NI, AVX-512) to verify if the FIPS provider is correctly utilizing hardware acceleration.
*   **Kernel Version:** To account for syscall overhead in the containerized environment.
*   **OpenSSL Build Flags:** To ensure the performance is reflective of the production configuration.

---

> [!TIP]
> "We don't benchmark to see how fast we are; we benchmark to detect **Regressions**. In the world of FIPS, a sudden 5% drop in throughput often points to a change in the cryptographic boundary or a loss of hardware acceleration—both of which have security and cost implications at scale."



## 6. Stage 04: Performance & Benchmarking

The benchmarking pipeline is designed to provide empirical evidence of the operational efficiency of the Wolfi-OpenSSL FIPS stack. We move beyond "it works" to "it performs at scale," ensuring that security hardening does not become a bottleneck for cloud-native workloads.

### 6.1 The Benchmarking Philosophy: "Quantifying the FIPS Tax"
Running OpenSSL in FIPS mode involves additional entropy gathering and algorithmic constraints. Our goal is to benchmark the **Delta** between standard execution and FIPS-validated execution across various ciphers (AES-GCM, RSA, ECDSA, etc.).

### 6.2 The Profiling Engine (`run_benchmark.sh`)
The core workload is driven by the `docs:benchmark` task. This engine executes a series of `openssl speed` commands within the target container environment. 
*   **Parallelism Control:** Benchmarks are executed in controlled environments to minimize "Noisy Neighbor" interference.
*   **Standardization:** We measure throughput (bytes per second) and latency (operations per second) for varying buffer sizes (16b to 16kb) to simulate real-world packet sizes.

### 6.3 Automated Data Parsing (`parser.py`)
Raw OpenSSL output is notoriously difficult to consume (ASCII tables). Our `docs:parse-benchmark` task utilizes a specialized Python-based parser to:
1.  **Extract:** Scrape the raw logs for specific algorithmic metrics.
2.  **Normalize:** Convert various units (kibi-bytes vs kilo-bytes) into a standardized SI format.
3.  **Structure:** Transform the unstructured text into a machine-readable JSON/CSV intermediate state. This allows us to track performance regressions over time across different versions of the FIPS provider.

### 6.4 Statistical Synthesis & Reporting
The final phase, `docs:all-report-benchmark`, aggregates the parsed data and invokes a Python-based reporting engine (`generate_report.py`) to produce high-fidelity visualizations.

*   **Regression Analysis:** The system is designed to compare the current build's performance against historical baselines.
*   **Heatmaps & Throughput Curves:** Instead of single data points, we generate curves that show how the FIPS provider scales with larger data chunks—critical for high-throughput TLS termination proxies.

### 6.5 Operational Commands
To trigger the full performance profiling and reporting pipeline:

```bash
# Complete End-to-End Pipeline: Run -> Parse -> Report
task docs:all-report-benchmark
```

For granular control, you can execute individual stages:
```bash
# Step 1: Execute the raw benchmark workloads
task docs:benchmark

# Step 2: Transform raw logs into structured data
task docs:parse-benchmark
```

### 6.6 Performance Metadata
Every benchmark report is tagged with:
*   **CPU Instruction Sets:** (e.g., AES-NI, AVX-512) to verify if the FIPS provider is correctly utilizing hardware acceleration.
*   **Kernel Version:** To account for syscall overhead in the containerized environment.
*   **OpenSSL Build Flags:** To ensure the performance is reflective of the production configuration.

---


> [!TIP]
> We don't benchmark to see how fast we are; we benchmark to detect **Regressions**. In the world of FIPS, a sudden 5% drop in throughput often points to a change in the cryptographic boundary or a loss of hardware acceleration—both of which have security and cost implications at scale.
>
> 






In a "High-Assurance" ecosystem, documentation that is manually updated is considered a liability. If the documentation does not reflect the exact state of the last cryptographic audit, it is misleading at best and a compliance failure at worst. 

**Stage 05** is the "Final Assembly" of our knowledge base, where we treat documentation as a compiled artifact.

---

## 7. Stage 05: Auto-Documentation Pipeline

This project employs a **"Living Documentation" (Docs-as-Code)** philosophy. The final stage of our automation pipeline ensures that our public-facing technical specifications, security badges, and compliance metrics are mathematically and operationally synchronized with the latest build artifacts.

### 7.1 The Single Source of Truth (SSoT)
Instead of static Markdown files, our `README.md` and `docs/` are treated as templates. The pipeline consumes raw data from three upstream stages to "render" the final documentation:
1.  **Metadata Layer:** GitHub Actions environment variables (SHA, Run ID, Actor).
2.  **Audit Layer:** Pytest execution results (Pass/Fail rates, Compliance status).
3.  **Performance Layer:** Parsed benchmark results (Throughput and Latency metrics).

### 7.2 Automated Metadata Ingestion
The task `docs:generate_docs_tests` serves as the primary data aggregator. It invokes a Python-based ingestion engine that scrapes the `allure-results/` and the host environment to build a comprehensive **Metadata Manifest**.

*   **Jinja2 Templating:** We use the Jinja2 engine to inject these variables into our Markdown files. This ensures that the "Service Integrity Dashboard" at the top of the README always displays the real-time status of the `FIPS 140-3` validation.
*   **Dynamic Badges:** Our badges aren't just images; they are data-driven indicators that reflect the `test_stats.passed` vs `test_stats.failed` metrics of the most recent audit.

### 7.3 The Synchronization Loop
The documentation pipeline is split into two distinct operational tasks to allow for granular updates:

#### A. Full Documentation Re-Sync
This task is executed after a full `multi-variant` audit. It processes the entire test suite output and regenerates the detailed technical logs.
```bash
# Aggregates multi-audit results and renders the full documentation suite
task docs:generate_docs_tests
```

#### B. README Hot-Update
For rapid iterations or metadata-only changes (like updating a version tag), this task focuses specifically on the `README.md`.
```bash
# Specifically regenerates the README.md using the latest available metadata
task docs:generate_readme"
```

### 7.4 Operational Traceability & Audit Trail
As a Tech Lead, I prioritize **Traceability**. Every time the documentation is generated, the pipeline injects an **"Audit Note"**:
*   **Commit Linking:** The documentation is bound to a specific `GITHUB_SHA`, ensuring that an auditor can match the docs to the exact line of code.
*   **Run Linking:** We inject the `GITHUB_RUN_ID` into the `README`, creating a direct clickable link from the documentation back to the tamper-evident logs of the GitHub Actions runner.

### 7.5 Supply Chain Transparency (SBOM & Attestations)
The final step of the documentation pipeline ensures that links to the **Software Bill of Materials (SBOM)** and **SLSA Provenance** are updated. By automating this, we guarantee that users are always downloading the correct `CycloneDX` or `SPDX` manifests associated with the current image digest, eliminating "Version Mismatch" risks in the supply chain.

---


>[!TIP]
>
> In the Google SRE model, we say: 'If a human has to touch it, it’s a bug.' By automating our documentation, we remove the human element from the compliance narrative. The README isn't a promise of what the software should* do; it is a verifiable report of what the software *actually did* during its last audit.
>



## 8. Variable Reference & Configuration

Our Taskfiles are built on the principle of **"Global Defaults, Local Overrides."** This section provides a comprehensive reference of the variables that control the behavior of the infrastructure, auditing, and reporting layers.

### 8.1 Core Project Identity (Global Scope)
Defined in the root `Taskfile.yml`, these variables establish the project's namespace and source control identity. They are used across all modules to ensure consistency.

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `owner` | `taha2samy` | The GitHub organization or user owning the repository. |
| `registry` | `ghcr.io` | The authoritative container registry for artifact distribution. |
| `repo_of_code` | `openssl_fips` | The internal name of the source code repository. |
| `repo_url` | `https://github.com/...` | The canonical URL used for metadata injection and links. |

### 8.2 Operational Overrides (The Injection Layer)
These variables are designed to be overridden at runtime via the Command Line Interface (CLI). This is the primary mechanism for testing new images or changing the scope of an audit.

| Variable | Scope | Description |
| :--- | :--- | :--- |
| `IMAGE` | `audit` | **Primary Override:** Directs the test suite to a specific container tag (e.g., `IMAGE=my-local-tag`). |
| `DEFAULT_IMAGE` | `global` | The fallback image used if the `IMAGE` variable is not provided. |
| `RESULTS_ROOT` | `global` | The parent directory for all test artifacts (Default: `allure-results`). |

### 8.3 Path & Workspace Management
These variables define the filesystem structure of the automation artifacts. **Do not modify these** unless you are refactoring the entire project structure.

*   **`RESULTS_DIR`**: Within specific modules, this points to the subdirectory where raw Allure data is stored.
*   **`REPORT_DIR`**: The destination for compiled, static HTML reports (Default: `allure-report`).
*   **`USER_WORKING_DIR`**: A dynamic Task variable used to map local paths into Dockerized bridges correctly.

### 8.4 How to Override Variables
Task allows for flexible variable injection. As a Tech Lead, I recommend using the **CLI Argument pattern** for ad-hoc testing and **Environment Variables** for CI/CD pipelines.

#### A. CLI Override (Recommended for Developers)
This method is transient and perfect for one-off tests.
```bash
# Testing a specific development build
task audit:run IMAGE="ghcr.io/taha2samy/wolfi-openssl-fips:beta-test"
```

#### B. Global Shell Export
Useful when you are working on a specific image for an entire session.
```bash
export IMAGE="my-dev-image"
task audit:run
task run-v2
```

### 8.5 Sanitization & Collision Avoidance
A critical feature of our variable management is the **`SAFE_NAME`** logic. When you override the `IMAGE` variable, the Taskfile automatically generates a sanitized string to use as a directory name.

*   **Logic:** `IMAGE` -> `ghcr.io/repo:tag`
*   **Safe Name:** `ghcr_io_repo_tag`

This allows the system to store results for multiple different images simultaneously in the `allure-results/` directory without data corruption, enabling side-by-side comparisons in the final report.

---

>[!TIP]
> "We treat our variables as a **Contract**. By exposing specific variables like `IMAGE` for overrides, we allow the automation to be flexible enough for local development while remaining rigid enough for production-grade CI/CD. The use of `SAFE_NAME` is particularly vital; it transforms a volatile string (the image tag) into a stable filesystem identifier, ensuring our 'Audit Trail' remains organized even when testing dozens of image variants."



## 9. Troubleshooting & Maintenance

A robust automation system requires periodic maintenance and a clear path for resolving execution anomalies. This section outlines the procedures for resetting the workspace state and diagnosing common failure modes in the pipeline.

### 9.1 System Hygiene (The "Clean Slate" Policy)
Automated testing and reporting generate significant disk artifacts over time (container images, log files, and HTML reports). To prevent "State Drift" or disk exhaustion, we provide a tiered cleanup strategy.

*   **Audit Cleanup:** Wipes raw test results and generated reports.
    ```bash
    task audit:clean
    ```
*   **Infrastructure Cleanup:** Removes the Allure Bridge Docker images to force a fresh build.
    ```bash
    task infra:clean
    ```
*   **The "Nuclear" Option:** Resets the entire environment to its original state. Use this if you encounter inexplicable behavior in the reporting or audit logic.
    ```bash
    task clean-all
    ```

### 9.2 Common Failure Modes & Resolutions

#### A. Bridge Build Failures (`infra:build-v2/v3`)
*   **Symptom:** Docker fails to build the Allure bridge images.
*   **Root Cause:** Usually an expired Docker cache or a temporary network failure reaching the Alpine/Allure repositories.
*   **Resolution:** Run `task infra:clean` followed by `task setup`. Ensure your Docker daemon has at least 4GB of allocated memory.

#### B. Permission Denied on Scripts
*   **Symptom:** `task` fails when trying to execute `.sh` or `.py` files.
*   **Root Cause:** Execution bits (`+x`) are sometimes lost during git operations or environment migrations.
*   **Resolution:** The Taskfile includes `chmod +x` commands in the `docs:` tasks, but you can manually fix the entire directory with:
    ```bash
    chmod +x scripts/*.py benchmark/*.sh
    ```

#### C. Allure Port Collisions
*   **Symptom:** `task report:v2:serve` fails with `port 8080 is already in use`.
*   **Root Cause:** An orphaned bridge container is still running from a previous session.
*   **Resolution:** Find and kill the container:
    ```bash
    docker ps | grep allure
    docker stop <container_id>
    ```

#### D. Missing Metadata in README
*   **Symptom:** The README displays `manual-repo-name` or `0` instead of real data.
*   **Root Cause:** The `update_readme.py` script is falling back to defaults because environment variables are missing or the `allure-results` are empty.
*   **Resolution:** Ensure you have run `task audit:run` at least once before generating documentation.

### 9.3 Diagnostic Log Inspection
When a task fails, always inspect the **primary log stream**. Our Taskfile is configured to pipe standard error (`stderr`) directly to your terminal.

1.  **Pytest Logs:** Check `reports/` (if generated) or the terminal output for cryptographic rejection messages (e.g., `Provider failed to load`).
2.  **Docker Logs:** If a bridge fails to serve, use `docker logs <container_id>` to see the internal Allure server status.
3.  **Task Trace:** For deep debugging of the task execution itself, run Task in verbose mode:
    ```bash
    task <task_name> --verbose
    ```

### 9.4 Maintenance Schedule
As a Tech Lead, I recommend the following maintenance cadence:
- **Weekly:** Run `task clean-all` to ensure you are testing against the latest Wolfi base images and Allure binaries.
- **Per Release:** Run `task docs:all-report-benchmark` to ensure the performance baseline hasn't shifted significantly.

---

>[!TIP]
> "Maintenance isn't just about cleaning up files; it's about **Predictability**. By enforcing a 'Clean Slate' policy via `task clean-all`, we ensure that our CI/CD results are not influenced by artifacts from previous runs. In a FIPS-compliant project, 'Leftover State' is a security risk. If you can't reproduce a failure from a clean state, it wasn't a failure—it was a ghost in the machine."

---
**License:** Apache-2.0  
**Security Contact:** See [SECURITY.md](../SECURITY.md) for vulnerability disclosure protocols.