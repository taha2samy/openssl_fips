
# 🛠 Task Execution Guide: Allure & Audit Workflow

This guide provides a detailed breakdown of all available tasks within the automated workflow. These tasks manage the building of environments, execution of tests, and serving of reports using Docker-based Allure bridges.

---

## 1. Infrastructure Tasks (`infra:`)
*Responsible for managing the Docker bridge images.*

| Task | Description | Command |
| :--- | :--- | :--- |
| **`infra:build-v2`** | Builds the Allure 2 image. Installs **Python 3.12**, **Java (JRE)**, and the **Allure 2.29 CLI**. | `task infra:build-v2` |
| **`infra:build-v3`** | Builds the Allure 3 image. Installs **Python 3.12**, **Node.js 20**, and the **Allure 3 CLI**. | `task infra:build-v3` |
| **`infra:build-all`** | A meta-task that triggers both `build-v2` and `build-v3` sequentially. | `task infra:build-all` |
| **`infra:clean`** | Force-removes the `allure2-bridge` and `allure3-bridge` Docker images from your local system. | `task infra:clean` |

---

## 2. Audit Tasks (`audit:`)
*Handles the execution of Pytest within the isolated bridge environment.*

| Task | Description | Command |
| :--- | :--- | :--- |
| **`audit:run`** | **The Core Execution Task.** It spawns an Allure 3 bridge container, mounts the current project directory to `/app`, and runs `pytest`. It also generates an `environment.properties` file for report metadata. | `task audit:run` |
| **`audit:multi`** | Runs the audit against multiple predefined image tags (e.g., `3.5.5-distroless` and `latest`) for comparison. | `task audit:multi` |
| **`audit:clean`** | Deletes the `allure-results/` directory to clear old test data. | `task audit:clean` |

**Variables for `audit:run`:**
*   **`IMAGE`**: (Optional) Pass a specific Docker image to test. 
    *   *Example:* `task audit:run IMAGE=ghcr.io/user/repo:tag`

---

## 3. Reporting Tasks (`report:`)
*Manages report generation and web serving for both Allure versions.*

### Allure 2 (Legacy)
| Task | Description | Command |
| :--- | :--- | :--- |
| **`report:v2:gen`** | Processes JSON results and generates a static HTML report in the `allure-report/` folder using the Allure 2 engine. | `task report:v2:gen` |
| **`report:v2:serve`** | Starts a local web server inside the container and maps it to **Port 8080**. Automatically opens the classic dashboard. | `task report:v2:serve` |

### Allure 3 (Modern)
| Task | Description | Command |
| :--- | :--- | :--- |
| **`report:v3:gen`** | Generates a static report using the Allure 3 Node-based engine. | `task report:v3:gen` |
| **`report:v3:serve`** | Starts a high-performance web server mapped to **Port 8081**. Opens the modern dashboard. | `task report:v3:serve` |

---

## 4. Global Aliases (The Workflow Shortcuts)
*High-level commands that combine multiple layers into a single execution.*

### `task setup`
*   **Action**: Runs `infra:build-all`.
*   **When to use**: Run this first to prepare the Docker images on a new machine.

### `task run-v3`
*   **Action**: `audit:run` ➡️ `report:v3:serve`.
*   **When to use**: The standard command for a full test cycle using the latest Allure 3 UI.

### `task run-v2`
*   **Action**: `audit:run` ➡️ `report:v2:serve`.
*   **When to use**: When you need to view results using the classic Allure 2 interface.

### `task clean-all`
*   **Action**: Wipes `allure-results`, `allure-report`, and removes the Docker images.
*   **When to use**: To completely reset the environment and free up space.

---

## 💡 Pro-Tips for Task Execution

1.  **Concurrent Serving**: You can run `task report:v2:serve` in one terminal and `task report:v3:serve` in another. Since they use ports **8080** and **8081** respectively, they will not conflict.
2.  **Mounting Logic**: All bridge tasks use `-v {{.USER_WORKING_DIR}}:/app`. This means the container sees your local files. If you change a test file on your host, the container uses the updated version immediately.
3.  **Permissions**: Tasks that require script execution (like `update-pkgs`) automatically apply `chmod +x` before running.



## 🔍 Technical Deep Dive & Advanced Usage

### 1. The Data Flow (How it works)
Understanding the lifecycle of a single test run is key to troubleshooting:
1.  **Source**: Your local code in `new_test/` is mounted into the container at `/app`.
2.  **Execution**: Pytest runs inside the container using the container's Python environment but writes results to your local `allure-results/` folder.
3.  **Persistence**: Because of the **Volume Mount (`-v`)**, the JSON files remain on your host machine even after the container is destroyed (`--rm`).
4.  **Rendering**: The Allure CLI reads these JSON files from your host, processes them, and outputs a static website in `allure-report/`.

### 2. Automatic Metadata Injection
One of the most powerful features in `audit:run` is the automatic creation of the `environment.properties` file. 
*   **Why?** Allure reports are often generic. By writing the `IMAGE` tag into this file, your report will explicitly show: `Image = ghcr.io/taha2samy/wolfi-openssl-fips:3.5.5-distroless`.
*   **Impact**: This makes your reports "Audit-Ready" and traceable to a specific build.

### 3. Passing Custom Arguments to Pytest
You don't always want to run all tests. You can pass extra arguments to the `audit:run` task using the Taskfile variables.
*   **Targeting a specific file**:
    ```bash
    task audit:run -- new_test/tests/test_01_core_policy.py
    ```
    *(Note: This requires adding `{{.CLI_ARGS}}` to your Taskfile command).*

### 4. Port Management & Conflicts
*   **Allure 2 (8080)**: This is the default port for most web dev tools. If it's occupied on your host, you can change the mapping in `Taskfile.report.yml` from `-p 8080:8080` to `-p 9090:8080`.
*   **Allure 3 (8081)**: Chosen specifically to avoid conflict with Allure 2, allowing you to run side-by-side comparisons.

### 5. Troubleshooting Common Issues
*   **"Permission Denied" on Linux**: If the container cannot write to `allure-results`, it’s usually a permission mismatch. Run `chmod -R 777 allure-results` to allow the container to write.
*   **Docker Build Hangs**: If `task setup` is slow, it's usually fetching the Debian/Python base image or the Node.js repository. This only happens during the first build.
*   **Report is Empty**: Ensure that `allure-results` contains `.json` files. If it's empty, it means Pytest failed to run or didn't find any tests in the provided path.

