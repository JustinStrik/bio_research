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

def get_edge_list_files():
    # directory "edge lists ints"
    # files = [f for f in listdir("edge lists ints") if isfile(join("edge lists ints", f)) and f.endswith(".xlsm")]
    # # make absolute path
    # files = [join("edge lists ints", f) for f in files]

    # 50_900_updated - Copy (2)/1_COHP_46966_502__F_D.xlsm 50_900_updated - Copy (2)/2_COHP_46939_477__F_B.xlsm 50_900_updated - Copy (2)/3_COHP_46983_512__F_D.xlsm 50_900_updated - Copy (2)/4_COHP_44940_480__F_B.xlsm 50_900_updated - Copy (2)/5_COHP_47000_507__F_D.xlsm 50_900_updated - Copy (2)/6_COHP_49264_513__F_D.xlsm 50_900_updated - Copy (2)/7_COHP_49205_487__F_B.xlsm 50_900_updated - Copy (2)/8_COHP_46903_483__F_A.xlsm 50_900_updated - Copy (2)/9_COHP_46891_482__F_A.xlsm 50_900_updated - Copy (2)/10_COHP_49224_542__F_B.xlsm 50_900_updated - Copy (2)/11_COHP_47017_508__F_D.xlsm 50_900_updated - Copy (2)/12_COHP_44997_541__F_B.xlsm 50_900_updated - Copy (2)/13_COHP_46915_545__F_A.xlsm 50_900_updated - Copy (2)/14_COHP_44978_490__N_C.xlsm 50_900_updated - Copy (2)/15_COHP_49241_514__F_D.xlsm 50_900_updated - Copy (2)/16_COHP_44959_489__N_C.xlsm 50_900_updated - Copy (2)/17_COHP_46879_476__F_A.xlsm 50_900_updated - Copy (2)/18_COHP_46927_484__F_B.xlsm 50_900_updated - Copy (2)/19_COHP_46947_488__N_C.xlsm 50_900_updated - Copy (2)/20_COHP_49252_511__F_D.xlsm 
    # # make above into a list but replace 50_900_updated - Copy (2)/ with edge lists ints/
    # keep in that order
    files = ["edge lists ints/COHP_46966_502__F_D.xlsm", "edge lists ints/COHP_46939_477__F_B.xlsm", "edge lists ints/COHP_46983_512__F_D.xlsm", "edge lists ints/COHP_44940_480__F_B.xlsm", "edge lists ints/COHP_47000_507__F_D.xlsm", "edge lists ints/COHP_49264_513__F_D.xlsm", "edge lists ints/COHP_49205_487__F_B.xlsm", "edge lists ints/COHP_46903_483__F_A.xlsm", "edge lists ints/COHP_46891_482__F_A.xlsm", "edge lists ints/COHP_49224_542__F_B.xlsm", "edge lists ints/COHP_47017_508__F_D.xlsm", "edge lists ints/COHP_44997_541__F_B.xlsm", "edge lists ints/COHP_46915_545__F_A.xlsm", "edge lists ints/COHP_44978_490__N_C.xlsm", "edge lists ints/COHP_49241_514__F_D.xlsm", "edge lists ints/COHP_44959_489__N_C.xlsm", "edge lists ints/COHP_46879_476__F_A.xlsm", "edge lists ints/COHP_46927_484__F_B.xlsm", "edge lists ints/COHP_46947_488__N_C.xlsm", "edge lists ints/COHP_49252_511__F_D.xlsm"]
    return files



