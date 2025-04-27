# phishing_detector/utils.py

def read_email_file(filepath):
    """Reads an email file and returns subject, sender, and body."""
    subject = ''
    sender = ''
    body_lines = []
    in_body = False # Flag to track when we are in the body

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file: # Added errors='ignore' for robustness
            lines = file.readlines()

        for line in lines:
            # Simple approach: Assume headers come first, then body after a blank line
            # A more robust parser would handle MIME
            if not in_body:
                if line.strip() == '':
                    in_body = True
                    continue # Skip the blank line separating headers and body

                line_lower = line.strip().lower()
                if line_lower.startswith('subject:'):
                    subject = line[len('subject:'):].strip()
                elif line_lower.startswith('from:'):
                    sender = line[len('from:'):].strip()
                # Add parsing for other headers here if needed for future features
            else:
                body_lines.append(line)

        body = "".join(body_lines).strip() # Join body lines and remove leading/trailing whitespace
        return subject, sender, body

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None, None, None # Return None for failure
    except Exception as e:
        print(f"Error reading email file {filepath}: {e}")
        return None, None, None


def print_report(report):
    """Prints the scan report."""
    print("-" * 30)
    if report:
        for item in report:
            print(f"• {item}")
    else:
        print("• No findings.")
    print("-" * 30)


def save_report(report, output_path):
    """Saves the scan report to a file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write("Phishing Scan Report\n")
            file.write("-" * 30 + "\n")
            if report:
                for item in report:
                    file.write(f"• {item}\n")
            else:
                 file.write("• No findings.\n")
            file.write("-" * 30 + "\n")
        print(f"Report saved to {output_path}")
    except Exception as e:
        print(f"Error saving report to {output_path}: {e}")
