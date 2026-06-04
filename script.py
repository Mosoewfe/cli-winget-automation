import subprocess

choice = input(
    "what would you like to do?\n"
    "1. install\n"
    "2. uninstall\n"
    "3. upgrade\n"
)

while True:
    match int(choice):
        case 1:
            name = input("pls give a name for software:\n")
            subprocess.run(["winget", "search", "-q", name])
            name = input("pls give a name for software to install:\n")
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
            break
        case 2:
            name = input("pls give a name for software:\n")
            subprocess.run(
                ["winget", "uninstall", name, "--silent", "--purge", "--force"]
            )
            break
        case 3:
            subprocess.run(["winget", "upgrade", "--include-unknown"])
            choice = input("would you like to update all apps [y/n]\n")
            if choice.lower() == "y":
                subprocess.run(
                    ["winget", "upgrade", "--all", "--silent", "--include-unknown"]
                )
            elif choice.lower() == "n":
                name = input("please enter an app name\n")
                force = input("would you like to force an upgrade? [y/n]\n")
                command = [
                    "winget",
                    "upgrade",
                    name,
                    "--silent",
                    "--include-unknown",
                ]
                if force.lower() == "y":
                    command.append("--force")
                subprocess.run(command)
            break
        case _:
            choice = input("error! enter 1, 2, or 3\n")