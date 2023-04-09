import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    t_statistic, p_value = ttest_1samp(x, 300)
    
    if (p_value < 0.06).all():
        return True  
    else:
        return False
    
