"""
KEY POINTS
- Just nest the models
"""
import re
from typing import List, Any, Optional, Union
import numpy as np
from pydantic import BaseModel, validator, AnyUrl, EmailStr


"""
Contributor:
Name: str
URL: URL or mailing url
Org: str
"""


class MailTo(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        if not isinstance(v, str):
            raise TypeError("Not a valid mailto Email format")
        v = v.strip()
        if not re.match(r"mailto:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", v):
            raise ValueError("mailto URL is not a valid mailto link")


class Contributor(BaseModel):
    name: str
    url: Optional[Union[AnyUrl, MailTo]]
    organization: Optional[str]


class Molecule(BaseModel):
    name: str
    charge: float
    symbols: List[str]
    coordinates: Any
    contributor: Optional[Contributor]

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


mol_data = {"name": "water",
            "charge": 0.0,
            "symbols": ["H", "H", "O"],
            "coordinates": [[0, 0, 0],
                            [1, 1, 1],
                            [2, 2, 2]]
            }
contributor_data = {"name": "Levi Naden",
                    "url": "i_make_waffles@somewhere.com",
                    "organization": "Tasty Buttery Waffles Inc."
                    }
mol_data["contributor"] = contributor_data
mol1 = Molecule(**mol_data)
