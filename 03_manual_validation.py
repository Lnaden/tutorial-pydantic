"""
KEY POINTS
- Lets add data validation
- Well this got complicated, especially since we already defined the data struct once
- Hard to iterate over everything which we can accept, e.g. list vs tuple, int vs float
  - Concept of strict vs flexible, and can you just coerce the data?
- There are tools like `Iterable` which can simplify some of this
- Quickly becomes unreadable.
- Have to engineer data error collection
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Molecule:
    name: str
    charge: float
    symbols: List[str]
    coordinates: List[List[float]]

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise ValueError(f"{self.name} must be a str")
        if not isinstance(self.charge, float):
            raise ValueError(f"{self.charge} must be a float")
        if not (isinstance(self.symbols, list) or isinstance(self.symbols, tuple)) or \
                any(not isinstance(x, str) for x in self.symbols):
            raise ValueError(f"{self.symbols} must be a list of str")
        if (not (isinstance(self.coordinates, list) or isinstance(self.coordinates, tuple)) or
            any(not (isinstance(y, list) or isinstance(y, tuple)) for y in self.coordinates) or
            any(any(not (isinstance(z, float) or isinstance(z, int)) for z in sub) for sub in self.coordinates)
        ):
            raise ValueError(f"{self.coordinates} must be a list of list of float")

    @property
    def num_atoms(self):
        return len(self.symbols)

    def __str__(self) -> str:
        return f"name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}"


mol1 = Molecule("water", 0.0, ["H", "H", "O"], [[0, 0, 0]])
mol2 = Molecule("water", 0.0, "SOOOOOUUUUUPPPP!", [0, 0, 0])
print(mol1)
print(mol2)
