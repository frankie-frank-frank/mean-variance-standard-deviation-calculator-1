import numpy as np

def calculate(list):
    if(len(list)!=9):
        raise ValueError("List must contain nine numbers.")
    ls = np.array(list)
    mean_row = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
    mean_column = [ls[[0,3,6]].mean(), ls[[1,4,7]].mean(),ls[[2,5,8]].mean()]
    mean_flat = ls.mean()
    
    variance_row = [ls[[0,1,2]].var(), ls[[3,4,5]].var(), ls[[6,7,8]].var()]
    variance_column = [ls[[0,3,6]].var(), ls[[1,4,7]].var(),ls[[2,5,8]].var()]
    var_flat = ls.var()
    
    std_row = [ls[[0,1,2]].std(), ls[[3,4,5]].std(), ls[[6,7,8]].std()]
    std_column = [ls[[0,3,6]].std(), ls[[1,4,7]].std(),ls[[2,5,8]].std()]
    std_flat = ls.std()
    
    max_row = [ls[[0,1,2]].max(), ls[[3,4,5]].max(), ls[[6,7,8]].max()]
    max_column = [ls[[0,3,6]].max(), ls[[1,4,7]].max(),ls[[2,5,8]].max()]
    max_flat = ls.max()
    
    min_row = [ls[[0,1,2]].min(), ls[[3,4,5]].min(), ls[[6,7,8]].min()]
    min_column = [ls[[0,3,6]].min(), ls[[1,4,7]].min(),ls[[2,5,8]].min()]
    min_flat = ls.min()
    
    sum_row = [ls[[0,1,2]].sum(), ls[[3,4,5]].sum(), ls[[6,7,8]].sum()]
    sum_column = [ls[[0,3,6]].sum(), ls[[1,4,7]].sum(),ls[[2,5,8]].sum()]
    sum_flat = ls.sum()
    return {'mean': [mean_column, mean_row, mean_flat],'variance': [variance_column, variance_row, var_flat], 'standard deviation':[std_column, std_row, std_flat],'max':[max_column, max_row, max_flat],'min':[min_column,min_row, min_flat],'sum':[sum_column, sum_row, sum_flat]
    }