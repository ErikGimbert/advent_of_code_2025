def file_to_commands(file_path: str) -> list[str]:
    """Read a file and return a list of commands."""
    with open(file_path, "r") as file:
        commands = [line.strip() for line in file if line.strip()]
    return commands
