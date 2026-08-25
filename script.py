import re
import subprocess

# Only allow letters, digits, spaces, dots, dashes and underscores in package names.
# This keeps input safe to pass to winget
# and avoids accidental flag injection via leading dashes.
SAFE_NAME = re.compile(r"^[A-Za-z0-9 ._\-]+$")


def ask(prompt):
    """Prompt the user and return a stripped, non-empty response."""
    value = input(prompt).strip()
    while not value:
        value = input("input cannot be empty, try again:\n").strip()
    return value


def safe_name(prompt):
    """Prompt until the user supplies a name that passes validation."""
    while True:
        name = ask(prompt)
        if SAFE_NAME.fullmatch(name):
            return name
        print("invalid name: use letters, digits, spaces, '.', '_' or '-' only.\n")


# Main menu loop — only accept 1, 2 or 3.
while True:
    choice = ask(
        "what would you like to do?\n" "1. install\n" "2. uninstall\n" "3. upgrade\n"
    )
    if choice in ("1", "2", "3"):
        break
    print("error! enter 1, 2, or 3\n")

match int(choice):
    case 1:
        safe_name("pls give a name for software to search:\n")
        name = safe_name("pls give a name for software to install:\n")
        subprocess.run(
            [
                "winget",
                "search",
                "-q",
                name,
            ]
        )
        subprocess.run(
            [
                "winget",
                "install",
                name,
                "--silent",
                "--accept-source-agreements",
                "--accept-package-agreements",
            ]
        )
    case 2:
        name = safe_name("pls give a name for software to uninstall:\n")
        subprocess.run(
            [
                "winget",
                "uninstall",
                name,
                "--silent",
                "--all-versions",
                "--purge",
                "--force",
            ]
        )
    case 3:
        subprocess.run(["winget", "upgrade", "--include-unknown"])
        update_all = ask("would you like to update all apps [y/n]\n").lower()
        if update_all == "y":
            subprocess.run(
                ["winget", "upgrade", "--all", "--silent", "--include-unknown"]
            )
        elif update_all == "n":
            name = safe_name("please enter an app name\n")
            force = ask("would you like to force an upgrade? [y/n]\n").lower()
            command = [
                "winget",
                "upgrade",
                name,
                "--silent",
                "--include-unknown",
            ]
            if force == "y":
                command.append("--force")
            subprocess.run(command)
