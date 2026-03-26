# Universal Data Auditor 

A robust, Python-based auditing engine designed to process large-scale CSV transaction data. This tool moves away from hardcoded scripts by implementing dynamic column detection and professional error logging.

## Core Features

* **Dynamic Column Detection:** Automatically identifies the file structure from the header. The auditor adapts to any number of columns without manual code changes.
* **Business Logic Validation:** Implements strict data integrity rules. Transactions with zero or negative values are caught using custom `ValueError` raises.
* **Production-Grade Logging:** All anomalies, missing columns, and validation failures are recorded in a dedicated `production_audit.log` file for post-audit analysis.
* **Modular Architecture:** Built as a standalone function, making it easy to integrate into larger automation workflows or CI/CD pipelines.

## Project Structure

You can explore the core components of this project here:

* [main_processor.py](./main.py) – The primary auditing engine containing the dynamic logic and validation rules.
* [production_audit.log](./audit.log) – An example of the system-generated log file tracking data discrepancies.

## Technical Implementation

### 1. Data Integrity
The script uses a `try-except` block to ensure that the entire process doesn't crash due to a single corrupted row. By using `if amount <= 0: raise ValueError`, the system separates standard data-type errors from specific business-rule violations.

### 2. Efficiency
The auditor reads files line-by-line using `enumerate(file)`, ensuring low memory consumption even when processing files with 10,000+ rows.

## How to Use

1.  **Generate Data:** Run `python data_creator.py` to create a sample CSV file.
2.  **Run Auditor:** Execute `python main_processor.py`.
3.  **Review Results:** Check the console for the summary report and open `production_audit.log` for a detailed breakdown of skipped or failed rows.

## Future Roadmap

* [ ] Add support for Excel (.xlsx) and JSON formats.
* [ ] Integrate automated PDF report generation for audit summaries.
* [ ] Add a CLI (Command Line Interface) for easier file path input.

---
Developed by **Muhammad Antor** | Focus: Scalable AI & Automation Solutions.
