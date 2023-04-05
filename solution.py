import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 16
    n = len(x)
    sum = 0
    for i in range(n):
      sum += x[i]
    res = sum / (16 * n)
    return res
