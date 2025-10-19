# AI Email Automation Agent 🤖✉️

An **AI-powered email automation agent** built with **Python**, **Gmail API**, and **Google AI Studio**. This tool automatically generates and sends personalized emails to recipients, making professional communication faster and smarter.  

---

## Features

- 💌 **Automated Email Generation** – AI generates professional, personalized email content.  
- 👥 **Recipient Customization** – Reads recipient data from a CSV file and replaces placeholders automatically.  
- 📧 **Gmail Integration** – Sends emails directly through Gmail using secure API access.  
- 📝 **Template Management** – Supports multiple email templates for different use cases.  
- 🔒 **Secure Authentication** – OAuth2 ensures safe Gmail access without exposing passwords.  

---
## Demo

**Example CSV file (`recipients.csv`):**  
```csv
Name,Email
John Doe,john@example.com
Jane Smith,jane@example.co
```

## Installation:

-Clone the repository:
```
   git clone https://github.com/blackdragon101/AI-Email-Automation
   cd AI-Email-Automation
```
-Set up Gmail API credentials:

  Go to Google Cloud Console
  Create a new project.
  Enable the Gmail API.
  Create OAuth credentials and download credentials.json.
  Place credentials.json in the project root directory.
  
## Usage

-- Prepare your recipient CSV file (Book1.csv in my case).
-- Customize your email template in test1.py.
-- Run the script:
  ```
  python test1.py
```

## Technologies Used
```text
* Python – Core language for scripting and automation
* Gmail API – Sending emails securely
* Google AI Studio – AI-generated email content
* CSV – Recipient data management
```
## Screenshot:
<img width="757" height="335" alt="AI generated email" src="https://github.com/user-attachments/assets/9375eafa-3e31-4165-b2d1-13b1ebcb5b5b" />


The AI agent will generate personalized emails and send them automatically to all recipients listed in your CSV file.

🙌 Credits
Created by Fatima Masood — passionate about development, AI, and automation.
