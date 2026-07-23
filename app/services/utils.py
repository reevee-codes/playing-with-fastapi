def add_to_file(text: str) -> None:
    with open("../../notes.txt", "a") as f:
        f.write(text)
