import numpy as np
from sklearn.metrics import roc_curve

# a sheet is a 2d boolean matrix, TOTAL_GENES x TOTAL_GENES
TOTAL_GENES = 1432

# take 2 2d matrices,

# check_against_test_sheet(sheet_orig, sheet_generated)
# get True Positive, False Positive, True Negative, False Negative as tp, fp, tn, fn

def check_against_test_sheet(sheet_orig, sheet_generated, threshold):
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for i in range(TOTAL_GENES):
        for j in range(TOTAL_GENES):
            if sheet_orig[i, j] == True and sheet_generated[i, j] >= threshold:
                tp += 1
            elif sheet_orig[i, j] == False and sheet_generated[i, j] >= threshold:
                fp += 1
            elif sheet_orig[i, j] == True and sheet_generated[i, j] < threshold:
                fn += 1
            elif sheet_orig[i, j] == False and sheet_generated[i, j] < threshold:
                tn += 1

    return tp, fp, tn, fn

# find_float_threshold(sheet_orig, sheet_generated)
# make equal number of False Positives and False Negatives 
# return the threshold

def find_float_threshold(sheet_orig, sheet_generated):
    # Flatten the 2D matrices into 1D arrays
    sheet_orig_flat = sheet_orig.flatten()
    sheet_generated_flat = sheet_generated.flatten()

    # Compute ROC curve
    fpr, tpr, thresholds = roc_curve(sheet_orig_flat, sheet_generated_flat)

    # Find the optimal threshold (Youden's J statistic)
    J = tpr - fpr
    optimal_idx = np.argmax(J)
    optimal_threshold = thresholds[optimal_idx]

    return optimal_threshold

# Example usage:
# Assuming sheet_orig and sheet_generated are 2D numpy arrays
# optimal_threshold = find_float_threshold(sheet_orig, sheet_generated)
# print(f'Optimal Threshold: {optimal_threshold}')
