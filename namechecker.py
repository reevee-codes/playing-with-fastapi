class namechecker():

    @staticmethod
    def checkname(name: str) -> bool:
        imiona = ["kasia", "basia", "ela", "marcelina", "martyna"]
        print("podales " + name)
        if name in imiona:
            print("jest")
        return name.lower() in imiona