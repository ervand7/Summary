from typing import List


# my solution
def num_unique_emails(emails: List[str]) -> int:
    result = set()
    for email in emails:
        local_name, domain = email.split("@")
        s = ""
        for letter in local_name:
            if letter == "+":
                break
            if letter != ".":
                s += letter
        result.add(f"{s}@{domain}")

    return len(result)
