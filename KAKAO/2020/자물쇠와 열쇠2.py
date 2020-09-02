import pandas as pd
import numpy as np

def solution(key, lock):
    key_df = pd.DataFrame(key)
    lock_df = pd.DataFrame(lock)
    key_np = np.array(key)
    lock_np = np.array(lock)
    print(key_np[0:1][1:2])
    print(lock_np)
    print(np.logical_xor(key_np, lock_np))
    # print(key_np * lock_np)
solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])