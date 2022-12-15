def convert_code_to_markdown(code: str, language: str = "python") -> str:
    return f"""```{language}\n{code}\n```"""
