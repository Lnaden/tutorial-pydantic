"""
KEY POINTS:
- Compress large collections of data as a "Dataclass"
- Distinction between CLASS variable and Instance variable
- Dataclass overwrites this
- Can augment class to add other methods
- Still just a typing suggestion
- Critically, dangerously wrong here with args as kwargs
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Molecule:
    name: str
    charge: float
    symbols: List[str]
    coordinates: List[List[float]]

    @property
    def num_atoms(self):
        return len(self.symbols)

    def __str__(self) -> str:
        return f"name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}"


mol1 = Molecule("water", 0.0, ["H", "H", "O"], [0, 0, 0])
mol2 = Molecule("water", 0.0, "SOOOOOUUUUUPPPP!", [0, 0, 0])
print(mol1)
print("\n\n")
print(mol2)
