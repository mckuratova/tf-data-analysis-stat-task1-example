import pandas as pd
import numpy as np


chat_id = 906914964 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return sum(x) / (16 * len(x))
