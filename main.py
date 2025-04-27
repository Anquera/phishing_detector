# phishing_detector/main.py

import os
from phishing_detector.scanner import scan_email
from phishing_detector.utils import read_email_file, print_report, save_report

def main():
    tests_dir = os.path.join(os.path.dirname(__file__), '.', 'tests')
    outputs_dir = os.path.join(os.path.dirname(__file__), '.', 'outputs')

    # Make sure outputs directory exists
    os.makedirs(outputs_dir, exist_ok=True)

    # Loop through all email files
    # Ensure this script is run from the project root directory
    # relative to the 'phishing_detector' package
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(current_dir, '..')
    tests_abs_dir = os.path.join(project_root, 'tests')
    outputs_abs_dir = os.path.join(project_root, 'outputs')


    os.makedirs(outputs_abs_dir, exist_ok=True)


    print(f"Scanning emails in: {tests_abs_dir}")

    # List files correctly relative to the script execution point or use absolute paths
    # Adjusted path logic for clarity if running main.py directly
    # Assuming main.py is in the root, and phishing_detector/tests is where tests are
    tests_dir_relative_to_main = './tests'
    outputs_dir_relative_to_main = './outputs'

    os.makedirs(outputs_dir_relative_to_main, exist_ok=True)


    if os.path.exists(tests_dir_relative_to_main):
        for filename in os.listdir(tests_dir_relative_to_main):
            if filename.endswith('.txt'):
                filepath = os.path.join(tests_dir_relative_to_main, filename)
                try:
                    subject, sender, body = read_email_file(filepath)

                    report = scan_email(subject, sender, body)

                    print(f"\n📄 Scanning {filename}:")
                    print_report(report)

                    output_path = os.path.join(outputs_dir_relative_to_main, f"{filename}_report.txt")
                    save_report(report, output_path)
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

    else:
        print(f"Error: 'tests' directory not found at {tests_dir_relative_to_main}")


if __name__ == "__main__":
    main()
