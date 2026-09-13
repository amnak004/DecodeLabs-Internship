# Phishing Awareness Analysis

## Description

A Python-based phishing awareness analyzer that examines sample emails or messages and identifies common indicators of phishing attempts.

The project focuses on threat identification and security awareness by detecting suspicious keywords, links, urgency, and requests for sensitive information.

## Features

* Analyzes sample emails and messages
* Detects suspicious keywords and phrases
* Identifies suspicious or shortened URLs
* Detects requests for sensitive information
* Identifies urgency and pressure tactics
* Lists detected red flags
* Classifies messages as Likely Phishing, Suspicious, or Likely Safe
* Provides security advice to the user

## Technologies Used

* Python
* Regular Expressions
* String Handling
* Lists
* Loops
* Conditional Statements
* Basic Threat Analysis Concepts

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Open the terminal inside the project folder.
4. Run:

```bash
python phishing_analysis.py
```

5. Enter a sample email or message.
6. Press Enter twice when you are finished.
7. The analyzer will display the verdict, detected red flags, and security advice.

## Example

### Sample Message

```text
URGENT! Your account has been suspended.
Verify your account immediately by clicking
https://bit.ly/example and confirm your password and OTP.
```

### Analysis Result

```text
Verdict: Likely Phishing

Red Flags Found:
- Suspicious keyword or phrase detected
- Suspicious or shortened URL detected
- Request for sensitive information detected
- Strong urgency or pressure detected
```

## Red Flag Checklist

The analyzer looks for common phishing indicators such as:

* Urgent or threatening language
* Suspicious links
* URL shorteners
* Requests for passwords or OTPs
* Requests for financial or personal information
* Account suspension or security warnings
* Pressure to act immediately
* Suspicious verification requests

## Security Advice

* Do not click suspicious links.
* Never share passwords or verification codes.
* Verify the sender through an official source.
* Do not respond to messages that create unnecessary urgency.
* Be cautious when a message asks for sensitive information.

## Security Note

This project is designed for cybersecurity education and awareness. It uses basic rule-based detection and should not be considered a replacement for professional email security systems or advanced phishing detection solutions.

## Project Structure

```text
Phishing-Awareness-Analysis/
├── phishing_analysis.py
└── README.md
```

## Author

Amna Ahmed
