                    # 📄 Task 3: Automate Email Extraction from a Text File

import re  # For regular expressions
import os  # For file handling

def extract_emails_from_file(input_path, output_path):
    # ✅ Step 1: Check if input file exists
    if not os.path.exists(input_path):
        print(f"❌ Error: File '{input_path}' does not exist.")
        return

    # ✅ Step 2: Read content from the input file
    with open(input_path, 'r') as file:
        content = file.read()

    # ✅ Step 3: Use regex to extract all emails
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

    # ✅ Step 4: Remove duplicates using set
    unique_emails = sorted(set(emails))

    # ✅ Step 5: Write the emails to output file
    with open(output_path, 'w') as file:
        for email in unique_emails:
            file.write(email + '\n')

    print(f"✅ {len(unique_emails)} email(s) extracted and saved to '{output_path}'.")

# 🧪 Example usage
input_file = 'input_text.txt'
output_file = 'extracted_emails.txt'

extract_emails_from_file(input_file, output_file)
