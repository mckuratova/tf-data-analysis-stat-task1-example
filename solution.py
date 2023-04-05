import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    ni = {}
    for i in x:
        if i in ni:
            ni[i] += 1
        else:
            ni[i] = 1
    t = 16
    n = len(x)
    summa = 0
    for i in ni:
        summa += i * ni[i]
    res = summa / n
    return res
