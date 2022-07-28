class Molecule:
    def __init__(self, name, charge, symbols, coordinates):
        self.name = name
        self.charge = charge
        self.symbols = symbols
        self.coordinates = coordinates
        self.num_atom = len(symbols)

    def __str__(self):
        return f"name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}"


mol1 = Molecule("water", 0.0, ["H", "H", "O"], [0, 0, 0])
print(mol1)
mol1.symbols = ["H", "O"]
print(mol1)
