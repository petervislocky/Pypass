from rich import print


def display_title() -> None:
    name_str = r"""
__________
\______   \___.__.___________    ______ ______
 |     ___<   |  |\____ \__  \  /  ___//  ___/
 |    |    \___  ||  |_> > __ \_\___ \ \___ \
 |____|    / ____||   __(____  /____  >____  >
           \/     |__|       \/     \/     \/
    """
    print(f"[green] {name_str} [/green]")
    print("[turquoise4] A Python password generator for your terminal! [/turquoise4]")


def main():
    display_title()


if __name__ == "__main__":
    main()
