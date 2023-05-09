import re

def get_snakecase_header(header: str):
    return re.sub(r"\s+", "_", re.sub(r"\W", " ", header.lower()).strip())

def format_text_value(text: str):
    return re.sub(r"\s+", " ", re.sub(r"[\r\n\s]", " ", text.strip()))
