def add_to_file(text: str):
    with open("notes.txt", "a") as f:
        f.write(text)
