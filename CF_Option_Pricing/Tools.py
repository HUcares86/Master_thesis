import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy


def n_th_moment(x, counts, c, n):
    return np.sum(counts*(x-c)**n) / np.sum(counts)
