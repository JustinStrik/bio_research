import numpy as np
TOTAL_GENES = 1432

def score_mouse_at_time(A, time, mouse, predicted_matrix):
    """
    Scores the mouse at the given time in the matrix.
    Uses the following formula:
    P = TP / (TP + FN)
    N = TN / (TN + FP)
    Score = P / 2 + N / 2

    A is a 3d matrix where the first dimension is the gene index,
    the second dimension is the gene index * mouse index,
    and the third dimension is the time index.
    """

    # get the mouse at the given time
    # !! CHECK TO SEE IF INCLUDES THE MAX MOUSE INDEX
    mouse_matrix = A[:, mouse * TOTAL_GENES: (mouse + 1) * TOTAL_GENES, time]

    return score_matrix(predicted_matrix, mouse_matrix)


# params: predicted mouse matrix, original mouse matrix
def score_matrix(predicted_matrix, original_matrix):
    """
    Scores the given matrix.
    Uses the following formula:
    P = TP / (TP + FN)
    N = TN / (TN + FP)
    Score = P / 2 + N / 2

    A is a 2d matrix where the first dimension is the gene index
    and the second dimension is the gene index * mouse index.
    """

    TP = 0
    FP = 0
    TN = 0
    FN = 0
    for predicted_val, original_val in zip(predicted_matrix.flatten(), original_matrix.flatten()):
        TP += 1 if predicted_val == 1 and original_val == 1 else 0
        FP += 1 if predicted_val == 1 and original_val == 0 else 0
        TN += 1 if predicted_val == 0 and original_val == 0 else 0
        FN += 1 if predicted_val == 0 and original_val == 1 else 0

    P = TP / (TP + FN) if TP + FN != 0 else 0
    N = TN / (TN + FP) if TN + FP != 0 else 0
    score = P / 2 + N / 2

    return score

    