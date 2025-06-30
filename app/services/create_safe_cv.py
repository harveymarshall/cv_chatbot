
def create_safe_cv(cv_text: str) -> str:
    return str(cv_text).replace("{", "{{").replace("}", "}}")
