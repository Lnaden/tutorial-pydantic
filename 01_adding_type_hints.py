"""
KEY POINTS
- Type hints
- Typing Library for indicating nested types
- Type hints are suggestions
- Why bother with hints/typing? Alot of what we do has strict type requirements
- We colloquially extend "typing" to include shape
- Can feed BS and still work, even if IDE complains

"""
from typing import List


class Molecule:
    def __init__(self, name: str, charge: float, symbols: List[str], coordinates: List[List[float]]):
        self.name = name
        self.charge = charge
        self.symbols = symbols
        self.coordinates = coordinates
        self.num_atom = len(symbols)

    def __str__(self) -> str:
        return f"name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}"


mol1 = Molecule("water", 0.0, ["H", "H", "O"], [0, 0, 0])
mol2 = Molecule("water", 0.0, "SOOOOOUUUUUPPPP!", [0, 0, 0])
print(mol1)
print(mol2)
