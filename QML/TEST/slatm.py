#!/usr/bin/env python

import ase
import ase.io as aio
import qml
from qml.representations import get_slatm_mbtypes
from qml.representations import generate_slatm
import numpy as np

mols = []
ncharges = []
attypes = []
atnums = []
natoms = []

mol = aio.read("system.xyz")
charges = mol.get_initial_charges()
attype = mol.get_chemical_symbols()
ncharges.append(charges)
attypes.append(attype)
atnums.append(mol.get_atomic_numbers())
natoms.append(len(mol.get_atomic_numbers()))

uatoms_sym = np.unique(np.concatenate(attypes))
uatoms = ase.Atoms(uatoms_sym).get_atomic_numbers()

mbtypes = qml.representations.get_slatm_mbtypes(atnums)
maxsize = np.max(natoms)

rep = generate_slatm(mol.positions, atnums, mbtypes, local=False)
print(rep)

