# End User Guide

This guide provides an audit of your project requirements and instructions on how to use the generated code.

---

## 1. Project Requirements Audit

The following is a summary of the project goals and deliverables derived from your input:

### Project Title
**Web Scraping Proof of Concept for Firmographic Data**

### Project Description
Develop a proof of concept for web scraping techniques that effectively address challenges such as blocking, timeouts, and reverse API changes. The project will focus on gathering firmographic information from five selected companies, ensuring compliance with legal and ethical standards.

### Key Goals
* Identify and address common web scraping challenges.
* Gather accurate and relevant firmographic data from selected companies.
* Ensure the web scraping techniques comply with legal and ethical standards.
* Develop a proof of concept using a widely-used programming language, such as Python.

### Deliverables
* Examples of at least three challenging web scraping techniques and solutions.
* Proof of concept code that successfully scrapes data from five companies.
* Demonstration of solutions to common web scraping challenges like blocking, timeouts, and reverse API changes.
* Collected firmographic information for each of the five companies.
* Functional and error-free code execution.

### Decomposed Tasks
The project has been broken down into the following atomic tasks for execution:

**1. Web Scraping Solution Blueprint**
* **Task ID**: `57c42195`
* **Description**: Create a technical blueprint for the core web scraping logic to obtain customer contact information from 5 specified companies in India, including strategies for handling dynamic content and CAPTCHAs.
* **Assigned to**: Senior_engineer Agent
* **Output Format**: Json

**2. Scraping Core - Data Extraction Logic (Company-Specific)**
* **Task ID**: `2c0b45e6`
* **Description**: Generate Python code for company-specific data extraction logic to pull addresses with all details from the 5 specified Indian companies, adhering to the 'Web Scraping Solution Blueprint' blueprint.
* **Assigned to**: Technical Agent
* **Output Format**: Code

**3. Scalability Strategy Document**
* **Task ID**: `1ac61e6a`
* **Description**: Generate a document outlining the strategy to scale the web scraping solution for 5 million customers, including distributed processing and rate limiting.
* **Assigned to**: Content Agent
* **Output Format**: Text

**4. Compliance & Legal Standards Report**
* **Task ID**: `e8f3faa6`
* **Description**: Generate a report on compliance and legal standards for web scraping in India and internationally, focusing on data privacy laws.
* **Assigned to**: Content Agent
* **Output Format**: Text

**5. Output Formatting Blueprint**
* **Task ID**: `32a20d6f`
* **Description**: Create a technical blueprint to format, clean, and store the scraped data in a structured and normalized format (e.g., CSV, JSON), including data validation rules.
* **Assigned to**: Senior_engineer Agent
* **Output Format**: Json

**6. Output Formatting and Storage Script**
* **Task ID**: `1ca38083`
* **Description**: Generate a Python script to format and store the scraped data in a structured format (CSV/JSON), performing data cleaning and validation as defined in the 'Output Formatting Blueprint' blueprint.
* **Assigned to**: Technical Agent
* **Output Format**: Code

**7. LLM API configuration check**
* **Task ID**: `341f7088`
* **Description**: Ensure the LLM API key is correctly configured.
* **Assigned to**: Validation Agent
* **Output Format**: Text

---

## 2. Instructions for Use

The generated output is in the `./integrated_output/scripts` directory.

The following files were generated for the **python** tech stack:
* `web_scraping_solution_blueprint_57c42195.txt`
* `scraping_core_data_extraction_logic_company_specif_2c0b45e6.py`
* `scalability_strategy_document_1ac61e6a.txt`
* `compliance_legal_standards_report_e8f3faa6.txt`
* `output_formatting_blueprint_32a20d6f.txt`
* `output_formatting_and_storage_script_1ca38083.py`
* `llm_api_configuration_check_341f7088.txt`
* `main.py`
* `main_file_name`
* `scripts_dir`

### Setup and Execution
1.  **Navigate** to the output scripts folder: `cd integrated_output/scripts`
2.  **Ensure** all necessary LLM API keys are set as environment variables (e.g., `OPENAI_API_KEY`).
3.  **Run** the main file from your terminal. The LLM has identified the main entry point as **`main.py`**.
```bash
python main.py --prompt "Your prompt here"
```

This will run the full end-to-end workflow and print the final response to your terminal.
