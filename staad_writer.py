from typing import List, Tuple

class StaadModel:
    def __init__(self, unit: str = "METER KN"):
        self.unit = unit
        self.nodes: List[Tuple[int, float, float, float]] = []
        self.members: List[Tuple[int, int, int]] = []
        self.member_property_block = ""
        self.support_block = ""
        self.load_block = ""

    # Geometry

    def add_node(self, node_id: int, x: float, y: float, z: float):
        self.nodes.append((node_id, x, y, z))

    def add_member(self, member_id: int, start: int, end: int):
        self.members.append((member_id, start, end))

    # Properties

    def set_prismatic_property(self, member_range: str, yd: float, zd: float):
        self.member_property_block = (
            f"MEMBER PROPERTY\n"
            f"{member_range} PRIS YD {yd} ZD {zd}\n"
        )

    # Supports

    def set_fixed_supports(self, node_list: List[int]):
        nodes = " ".join(str(n) for n in node_list)
        self.support_block = f"SUPPORTS\n{nodes} FIXED\n"

    # Loads

    def add_selfweight(self):
        self.load_block += (
            "LOAD 1 LOADTYPE DEAD TITLE DL\n"
            "SELFWEIGHT Y -1.1\n"
        )

    # Write File

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
                f.write(f"{node[0]} {node[1]} {node[2]} {node[3]}\n")
            f.write("\n")

            f.write("MEMBER INCIDENCES\n")
            for mem in self.members:
                f.write(f"{mem[0]} {mem[1]} {mem[2]}\n")
            f.write("\n")

            f.write(self.member_property_block + "\n")

            f.write(self.support_block + "\n")

            f.write(self.load_block + "\n")

            f.write("PERFORM ANALYSIS\n")
            f.write("FINISH\n")
