import secrets
import string


def generate_pswd(
    length: int = 16,
    *,
    letters: bool = True,
    digits: bool = True,
    punctuation: bool = True,
) -> str:
    """Generates a password using secrets library for secure, random generation."""
    characters = ""
    if letters:
        characters += string.ascii_letters
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation

    password = [secrets.choice(characters) for _ in range(length)]
    return "".join(password)


if __name__ == "__main__":
    print(generate_pswd())
