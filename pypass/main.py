import click
import pyperclip
import importlib.metadata
from rich import print
from rich.markup import escape

from pypass.generator import generate_pswd


__version__ = importlib.metadata.version("Pypass")


def display_title() -> None:
    name_str = r"""
__________
\______   \___.__.___________    ______ ______
 |     ___<   |  |\____ \__  \  /  ___//  ___/
 |    |    \___  ||  |_> > __ \_\___ \ \___ \
 |____|    / ____||   __(____  /____  >____  >
           \/     |__|       \/     \/     \/
    """
    print(f"[green]{name_str}[/green]")
    print("[turquoise4]A Python password generator for your terminal![/turquoise4]")


@click.command()
@click.option(
    "-l",
    "--letters",
    is_flag=True,
    help="Specify to include standard ascii letters in password.",
)
@click.option(
    "-n",
    "--numbers",
    is_flag=True,
    help="Specify to include numeric values to password.",
)
@click.option(
    "-p",
    "--punctuation",
    is_flag=True,
    help="Specify to include punctuation in the password.",
)
@click.option(
    "-L",
    "--length",
    default=16,
    help="Specify the length of the password to generate. Default is 16. Must be >= 4",
)
@click.option(
    "--no-copy",
    is_flag=True,
    help="Include to stop the program from auto copying to clipboard.",
)
@click.option(
    "--version",
    is_flag=True,
    help="Show the version info for the program.",
)
def main(
    letters: bool, numbers: bool, punctuation: bool, length: int, no_copy: bool, version: bool
) -> None:
    if version:
        display_title()
        print(f"Version: {__version__}")
        return

    if not letters and not numbers and not punctuation:
        raise click.UsageError("Must include at least one set of chars to include.")

    if length <= 4:
        raise click.UsageError("Cannot create a password shorter than 4 chars.")

    password = generate_pswd(
        length=length, letters=letters, digits=numbers, punctuation=punctuation
    )
    print(f"[red]Generated password -> [/red] {escape(password)}")

    if not no_copy:
        pyperclip.copy(password)
        print("[turquoise4]Password copied to clipboard.[/turquoise4]")


if __name__ == "__main__":
    main()
