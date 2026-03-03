class Loading:
    def __init__(self):
        self.definitions = "" 
        self.load_text = ""
        self.load_label = 1

    def add_selfweight(self):
        self.load_text += (
            f"LOAD {self.load_label} LOADTYPE DEAD TITLE DL\n"
            "SELFWEIGHT Y -1.1\n\n"
        )
        self.load_label += 1

    def add_roof_udl(self, member_range: str, load_value: float):
        pass

    def add_load_combination(self):
        pass 

    def add_definition_IS1893_16(self):
        self.definitions += (
            ""
        )

    def generate(self):
        return self.definitions + self.load_text
