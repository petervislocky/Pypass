import secrets
import string


def generate_pswd(
    length: int = 16,
    *,
    letters: bool = True,
    digits: bool = False,
    punctuation: bool = False,
) -> str:
    """Generates a password using secrets library for secure, random generation.
    Default is a letters only password with a length of 16.

    Args:
        length: Length of the password, default is 16.
        letters: Whether to include letters or not, default is True.
        digits: Whether to include numbers or not, default is False.
        punctuation: Whether to include punctuation or not, default is False.
    """
    characters = ""
    # disallowing some commonly rejected chars that appear in `string.punctuation`
    disallowed = "\"'|`\\<>()[]{};:,"

    if letters:
        characters += string.ascii_letters
    if digits:
        characters += string.digits
    if punctuation:
        characters += "".join(i for i in string.punctuation if i not in disallowed)

    return "".join(secrets.choice(characters) for _ in range(length))
