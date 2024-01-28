import re


def extract_session_id(session_str: str):

    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""


if __name__ == "__main__":
    print(extract_session_id(
        "projects/project-chatbot-tkl9/agent/sessions/ba0b21cd-0895-0258-5f04-e7fd18e438be/contexts/ongoing-order"))
