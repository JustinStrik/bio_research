import numpy as np
from read_input import read_full_matrix_with_alignment
# folder manipulate_data, get function get_times_with_mouse_alignment from file test_alignments
from manipulate_data.test_alignments import get_times_with_mouse_alignment

TOTAL_GENES = 1432

# args: mouse_index, time, mask
def mask_mouse_index_at_time(index, time, mask):
    """
    Masks the mouse at the given index at the given time in the matrix.
    """

    # to mask mouse, remember that each mouse at a time 
    # represents the TOTAL_GENES x TOTAL_GENES matrix at that time
    # the y TOTAL_GENES begins at index * TOTAL_GENES
    
    # remove values from mask that meet these conditions: tuple[2] == time)
                            #    and (tuple[1] > (index * TOTAL_GENES + TOTAL_GENES) and tuple[1] < (index * TOTAL_GENES + TOTAL_GENES))
                            #    for tuple in mask]

    filtered_mask = [
        t for t in mask
        if not (t[2] == time and (t[1] > (index * TOTAL_GENES) and t[1] < (index * TOTAL_GENES + TOTAL_GENES)))
    ]
    return filtered_mask


def mask_n_mice_at_time(n, mask):
    """
    Masks n mice at the given time in the matrix.
    """
    
    alignment_times = get_times_with_mouse_alignment()

    # pick 5 random time-mouse pairs, cannot duplicate times
    times = np.random.choice(list(alignment_times.keys()), n, replace=False)

    # choose mouse index at random at each time
    mice = [np.random.choice(alignment_times[time]) for time in times]
    # rewrite to not duplicate mice

    # make array of pairs of time and mouse index
    pairs = zip(times, mice)

    # mask the mice at the given times
    for time, mouse in pairs:
        mask = mask_mouse_index_at_time(mouse, time, mask)

if __name__ == "__main__":
    # returns tuples where the value is 1 in the matrix
    A = read_full_matrix_with_alignment()
    mask = A

    # returns time_index->mouse_index_array
    alignment_times = get_times_with_mouse_alignment()

    # pick 5 random time-mouse pairs, cannot duplicate times
    mask_n_mice_at_time(5, mask)