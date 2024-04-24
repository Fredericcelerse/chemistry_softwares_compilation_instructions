#!/usr/bin/env python

import ase
import ase.io as aio
import qml
import numpy as np

mols = []
ncharges = []
attypes = []

mol = aio.read("system.xyz")
charges = mol.get_initial_charges()
attype = mol.get_chemical_symbols()
ncharges.append(charges)
attypes.append(attype)

uatoms_sym = np.unique(np.concatenate(attypes))
uatoms = ase.Atoms(uatoms_sym).get_atomic_numbers()

rep = qml.representations.generate_fchl_acsf(nuclear_charges=mol.get_atomic_numbers(),coordinates=mol.positions,rcut=3, acut=3, nRs2=24, nRs3=20,elements=uatoms)
print(rep)

