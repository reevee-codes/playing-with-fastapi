class utils():

    @staticmethod
    def addToFile(text: str):
        with open("notes.txt", "a") as f:
            f.write(text)



