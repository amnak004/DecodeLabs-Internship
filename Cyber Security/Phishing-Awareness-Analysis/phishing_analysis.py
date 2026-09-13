import re


SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify your account",
    "verify your identity",
    "account suspended",
    "account locked",
    "click immediately",
    "act now",
    "confirm your password",
    "reset your password",
    "claim your prize",
    "you have won",
    "limited time",
    "security alert",
    "payment failed",
    "update your information"
]


SUSPICIOUS_URL_PATTERNS = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "is.gd",
    "shorturl.at"
]


SENSITIVE_REQUESTS = [
    "password",
    "credit card",
    "bank account",
    "otp",
    "verification code",
    "social security",
    "personal information"
]


def extract_urls(message):
    return re.findall(r'https?://\S+|www\.\S+', message, re.IGNORECASE)


def analyze_message(message):
    red_flags = []

    message_lower = message.lower()

    # Check suspicious keywords
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in message_lower:
            red_flags.append(
                f"Suspicious keyword or phrase detected: '{keyword}'"
            )

    # Check suspicious URLs
    urls = extract_urls(message)

    for url in urls:
        for pattern in SUSPICIOUS_URL_PATTERNS:
            if pattern in url.lower():
                red_flags.append(
                    f"Suspicious or shortened URL detected: {url}"
                )
                break

    # Check sensitive information requests
    for item in SENSITIVE_REQUESTS:
        if item in message_lower:
            red_flags.append(
                f"Request for sensitive information detected: '{item}'"
            )

    # Check urgency
    urgency_words = ["urgent", "immediately", "now", "as soon as possible"]

    urgency_count = sum(
        word in message_lower for word in urgency_words
    )

    if urgency_count >= 2:
        red_flags.append(
            "The message creates strong urgency or pressure."
        )

    # Determine result
    if len(red_flags) >= 3:
        result = "Likely Phishing"
    elif len(red_flags) > 0:
        result = "Suspicious"
    else:
        result = "Likely Safe"

    return result, red_flags


print("=" * 55)
print("        PHISHING AWARENESS ANALYZER")
print("=" * 55)

print("\nEnter a sample email or message below.")
print("Press ENTER twice when you are finished.\n")

lines = []

while True:
    line = input()

    if line == "":
        break

    lines.append(line)

message = " ".join(lines)

if not message.strip():
    print("\nNo message was entered.")
else:
    result, red_flags = analyze_message(message)

    print("\n" + "=" * 55)
    print("ANALYSIS RESULT")
    print("=" * 55)

    print(f"\nVerdict: {result}")

    if red_flags:
        print("\nRed Flags Found:")

        for number, flag in enumerate(red_flags, start=1):
            print(f"{number}. {flag}")

        print("\nWhy is this message unsafe?")
        print(
            "The message contains characteristics commonly associated "
            "with phishing attacks, such as suspicious links, urgency, "
            "or requests for sensitive information."
        )
    else:
        print("\nNo major phishing indicators were detected.")

    print("\nSecurity Advice:")
    print("- Do not click suspicious links.")
    print("- Never share passwords or verification codes.")
    print("- Verify the sender through an official source.")
    print("- Do not respond to messages that create unnecessary urgency.")