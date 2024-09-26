import numpy as np

# DTFT实现
def DTFT(x, xn=0):
    """
    返回一个计算DTFT的函数，输入是一个序列x
    """
    def dtft_func(w):
        """
        计算给定频率w的DTFT
        """
        n = np.arange(len(x)) - xn  # 调整时间索引以考虑零点对齐
        if isinstance(w, (list, np.ndarray)):  # 如果 w 是列表或数组
            return [np.sum(x * np.exp(-1j * wi * n)) for wi in w]
        else:  # 如果 w 是单个值
            return [np.sum(x * np.exp(-1j * w * n))]
    
    return dtft_func