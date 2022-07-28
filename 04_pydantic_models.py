"""
KEY POINTS
- Libraries do this
- Pydantic is one of the first, and certainly most powerful to leverage existing type hints
- Build models within models
- Auto data validation on whole models
- Auto data coercion
- Add validators
- Add dependent validators

STAGES
- Add Pydantic Base Model, show coords is wrong
- Show invalid data are wrong
- Show validator
- Show data coercion
- Show validators relying on other validators
"""
from typing import List, Any
import numpy as np
from pydantic import BaseModel, validator


class Molecule(BaseModel):
    name: str
    charge: float
    symbols: List[str]
    # coordinates: List[List[float]]
    coordinates: Any

    @property
    def num_atoms(self):
        return len(self.symbols)

    @validator("coordinates", pre=True)
    def coord_validator(cls, v):
        try:
            v = np.asarray(v)
        except ValueError:
            raise ValueError(f"Could not cast {v} to numpy array")
        return v

    @validator("coordinates")
    def coords_length_of_symbols(cls, v, values):
        symbols = values["symbols"]
        if len(v.shape) != 2 or len(symbols) != v.shape[0] or v.shape[1] != 3:
            raise ValueError("Coordinates must be of shape [Number Symbols, 3]")
        return v

    # def __str__(self):
    #     return f"name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}"


# mol1 = Molecule(name="water",
#                 charge=0.0,
#                 symbols=["H", "H", "O"],
#                 coordinates=[[0, 0, 0]])
mol1 = Molecule(name="water",
                charge=0.0,
                symbols=["H", "H", "O"],
                coordinates=[[0, 0, 0],
                             [1, 1, 1],
                             [2, 2, 2]])

print("\n")
print(mol1)
mol_data = mol1.dict()
print("\n\n")
# mol2 = Molecule(name="water",
#                 charge=0.0,
#                 symbols="SOOOOOUUUUUPPPP!",
#                 coordinates=[[0, 0, 0]])
mol_data.update(name="TIP3P")
mol2 = Molecule(**mol_data)
print(mol2)
