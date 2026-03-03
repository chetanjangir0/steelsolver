from typing import List, Tuple

class StaadModel:
    def __init__(self, unit: str = "METER KN"):
        self.unit = unit
        self.nodes: List[Tuple[int, float, float, float]] = []
        self.members: List[Tuple[int, int, int]] = []
        self.member_property_block = ""
        self.support_block = ""
        self.load_block = ""
        self.material_block = (
            "DEFINE MATERIAL START\n"
            "ISOTROPIC STEEL\n"
            "E 2.05e+08\n"
            "POISSON 0.3\n"
            "DENSITY 76.8195\n"
            "ALPHA 1.2e-05\n"
            "DAMP 0.03\n"
            "G 7.88462e+07\n"
            "TYPE STEEL\n"
            "STRENGTH FY 250000 FU 400000 RY 1.5 RT 1.2\n"
            "END DEFINE MATERIAL\n"
        )
        self.constant_block = (
            "CONSTANTS\n"
            "MATERIAL STEEL ALL\n"
        )

    def add_node(self, node_id: int, x: float, y: float, z: float):
        self.nodes.append((node_id, x, y, z))

    def add_member(self, member_id: int, start: int, end: int):
        self.members.append((member_id, start, end))

    def set_load_block(self, load_text: str):
        self.load_block = load_text

    def set_prismatic_property(self, member_range: str, yd: float, zd: float):
        self.member_property_block = (
            f"MEMBER PROPERTY\n"
            f"{member_range} PRIS YD {yd} ZD {zd}\n"
        )

    def set_fixed_supports(self, node_list: List[int]):
        nodes = " ".join(str(n) for n in node_list)
        self.support_block = f"SUPPORTS\n{nodes} FIXED\n"

    def write(self, filename: str):
        with open(filename, "w") as f:

            f.write("STAAD SPACE\n")
            f.write("START JOB INFORMATION\n")
            f.write("ENGINEER DATE\n")
            f.write("END JOB INFORMATION\n\n")
            f.write("INPUT WIDTH 79\n\n")

            f.write(f"UNIT {self.unit}\n\n")

            f.write("JOINT COORDINATES\n")
            for node in self.nodes:
                f.write(f"{node[0]} {node[1]} {node[2]} {node[3]};\n")
            f.write("\n")

            f.write("MEMBER INCIDENCES\n")
            for mem in self.members:
                f.write(f"{mem[0]} {mem[1]} {mem[2]};\n")
            f.write("\n")

            f.write(self.material_block + "\n")
            
            f.write(self.member_property_block + "\n")

            f.write(self.constant_block + "\n")

            f.write(self.support_block + "\n")

            f.write(self.load_block + "\n")

            f.write("PERFORM ANALYSIS\n")
            f.write("FINISH\n")
