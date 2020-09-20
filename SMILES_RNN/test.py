from utils.data_structs import extract_vanadium_data, draw_molecule
import os


sdfs = ['/'.join(['.','data', 'sdfs', sdf]) for sdf in os.listdir('./data/sdfs') 
        if sdf.endswith(sdf)]
mols = [extract_vanadium_data(sdf) for sdf in sdfs 
        if extract_vanadium_data(sdf) is not None] 
for idx, mol in enumerate(mols):
    draw_molecule(idx, mol)