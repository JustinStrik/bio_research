from os import listdir
from os.path import isfile, join, isdir

def get_adj_matrix_files():
    # all folders in /Adjacency Matrices/
    folders = [f for f in listdir("Adjacency Matrices") if isdir(join("Adjacency Matrices", f))]

    # names of files will be results_adj_COHP_46947_488__N_C_w0.csv
    # where 488 is the mouse id and w{i} is the week number
    files = [] # absolute path to files
    for folder in folders:
        files += [join("Adjacency Matrices", folder, f) for f in listdir(join("Adjacency Matrices", folder)) if isfile(join("Adjacency Matrices", folder, f))]

    return files



