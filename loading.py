from enum import Enum

# response reduction factor
class RF(Enum):
    RC_OMRF = 3.0
    RC_SMRF = 5.0
    STEEL_OMRF = 3.0
    STEEL_SMRF = 5.0

# seismic zone
class Zone(Enum):
    II = 0.1
    III = 0.16
    IV = 0.24
    V = 0.36

# importance factor
class IMF(Enum):
    Important = 1.5
    Residential_or_commercial = 1.2
    All_other = 1.0

# soil type
class Soil(Enum):
    Hard = 1
    Medium = 2
    Soft = 3

# structure type
class ST(Enum):
    RC_MRF = 1
    RC_STEEL_COMPOSITE_MRF = 2
    STEEL_MRF = 3
    RC_STRUCTURAL_WALLS = 4
    ALL_OTHER = 5

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

    def add_definition_IS1893_16(self, zone: Zone, rf: RF, imf:IMF, soil:Soil, st: ST, dm:float=0.05):
        self.definitions += (
            "DEFINE IS1893 2016 LOAD\n"
            f"ZONE {zone.value} RF {rf.value} I {imf.value} SS {soil.value} ST {st.value} DM {dm}\n"
            "SELFWEIGHT 1\n\n"
            # todo: add seismic weights after adding Dl, LL
        )

    def generate(self):
        return self.definitions + self.load_text
