def generate_email(subject, purpose):
    email = f"""
Subject: {subject}

Dear Sir/Madam,

I hope you are doing well.

I am writing this email regarding {purpose}. I would like to request your support and consideration on this matter.

Thank you for your time and attention. I look forward to your response.

Sincerely,
Your Name
"""
    return email


def main():
    print("========== AI Email Writer (Version 1) ==========\n")

    subject = input("Enter Email Subject: ")
    purpose = input("Enter the purpose of the email: ")

    email = generate_email(subject, purpose)

    print("\n========== Generated Email ==========\n")
    print(email)


if __name__ == "__main__":
    main()