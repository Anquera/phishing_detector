# Phishing Detector

A simple command-line tool to scan email files for potential phishing indicators using heuristic and pattern-matching techniques. This project serves as a midterm deliverable to demonstrate software security tool development for threat detection.

## Project Overview

This tool analyzes email content stored in plain text files to identify characteristics commonly found in phishing attempts. It focuses on analyzing the subject line, sender address, and URLs found within the email body.

## Features Implemented

The current version of the Phishing Detector implements the following detection features:

1. Subject Keyword Scan: Checks the email subject line for the presence of predefined suspicious keywords often used in phishing attacks (e.g., "urgent", "security alert").
2. Suspicious Sender Domain Check: Evaluates the sender's email address domain against a list of known or commonly mimicked suspicious domain patterns (e.g., domains containing typos or extra words mimicking legitimate brands).
3. URL Domain Check: Extracts URLs found within the email body and checks if the domain of these URLs matches any of the predefined suspicious domain patterns.

These features contribute to identifying potential phishing emails by flagging specific patterns and anomalies.

## Prerequisites

To run this tool, you need:

*   Python 3.6 or higher

## How to Use

1. Prepare Email Files: Place the email content you want to scan into plain text files (e.g., test_email.txt) within the tests/ directory. Each file should contain the email headers and body. A simple format with Subject: and From: lines is expected by the current utils.py.

2. Run the Scanner: Open your terminal or command prompt, navigate to the project's root directory (where main.py is located), and run the main script:
    python main.py

3. View Reports: After the script finishes execution, it will print a report for each scanned email to the console. Additionally, a detailed report for each email will be saved as a .txt file in the outputs/ directory. The output file name will correspond to the input file name with _report.txt appended.

## Understanding the Report

The generated report for each email will list the results of each implemented scan feature.

*   It will indicate whether the subject line contained suspicious keywords.
*   It will state if the sender's email domain matched any suspicious patterns.
*   It will list any URLs found in the body that contained suspicious domain patterns, or indicate if none were found or matched.

If any feature flags the email, it suggests that the email exhibits characteristics consistent with known phishing techniques.

## Project Structure

PHISHING_DETECTOR/
├── .venv/                  # Python virtual environment (optional)
├── outputs/                # Directory to store scan reports
│   ├── test_sample1.txt_report.txt
│   └── test_sample2.txt_report.txt
├── phishing_detector/
│   ├── __init__.py
│   ├── ml_model.py         # Placeholder for potential ML features
│   ├── scanner.py          # Contains the core scanning logic
│   └── utils.py            # Helper functions (reading emails, reporting)
├── tests/                  # Directory to place email files for scanning
│   ├── test_sample1.txt
│   └── test_sample2.txt
├── main.py                 # Entry point to run the scanner
├── README.md               # This file
└── requirements.txt        # Project dependencies (if any)

## Definition of Done (Midterm Scope)

For the purpose of this midterm project, the "Definition of Done" is achieved when:
*   The main.py script successfully iterates through and processes all .txt files in the tests/ directory.
*   The scanner.py file contains implemented logic for at least 3 distinct phishing detection features (Subject Keyword Scan, Suspicious Sender Domain Check, URL Domain Check).
*   For each scanned email, a report is generated in the outputs/ directory detailing the findings of each implemented feature.
*   The tool can be demonstrated to correctly flag test emails designed to trigger its specific features and not flag legitimate emails within the constraints of the chosen heuristic methods.

## Testing and Assurance

Testing is performed by preparing a diverse set of test emails in the tests/ directory, including both simulated phishing examples targeting the implemented features and legitimate email examples. Running the main.py script and verifying that the generated reports accurately reflect the expected outcomes for these test cases provides assurance that the implemented detection logic functions as intended within the scope of the project's features.

## Future Enhancements (Beyond Midterm)

Possible areas for future development include:

*   More sophisticated URL analysis (typosquatting, IP address checks, fetching and analyzing page content in a sandbox).
*   Full email header parsing and analysis (SPF/DKIM/DMARC checks, hop analysis).
*   Integration of machine learning models trained on larger datasets (ml_model.py is a placeholder for this).
*   Attachment analysis (checking file types, potentially scanning content safely).
*   Handling different email formats (MIME, HTML parsing).
*   A graphical user interface.
