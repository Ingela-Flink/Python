import random

class lotteri:

    def __init__(self):

        self.list_vinster = [
            "Harpoon",
            "Guld pump",
            "MK seven",
            "Flnit",
            "Scar",
            "Tac",
            "Boogie",
            "P90",
            "Hunting",
            "Grappler",
        ]
    

    def get_vinst(self):
        slumptal = random.randint(0, len(self.list_vinster)-1 )

        return self.list_vinster[slumptal]