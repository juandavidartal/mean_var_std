import numpy as np

#MEAN
def mean(matrix, axis):
  if axis == 0 or axis ==1:
    mean_res = np.mean(matrix, axis=axis)
    return mean_res.tolist()
  
  elif axis == "flattened":
    mean_res = np.mean(matrix)
    return mean_res.tolist()
  
  else:
    return None

#VARIANCE
def var(matrix, axis):
  if axis == 0 or axis ==1:
    var_res = np.var(matrix, axis=axis)
    return var_res.tolist()
  
  elif axis == "flattened":
    var_res = np.var(matrix)
    return var_res.tolist()
  else:
    return None

#Standard Deviation

def std(matrix, axis):
  if axis == 0 or axis ==1:
    std_res = np.std(matrix, axis=axis)
    return std_res.tolist()
  
  elif axis == "flattened":
    std_res = np.std(matrix)
    return std_res.tolist()
  else:
    return None

#MAX
def max(matrix, axis):
  if axis == 0 or axis ==1:
    max_res = np.max(matrix, axis=axis)
    return max_res.tolist()
  
  elif axis == "flattened":
    max_res = np.max(matrix)
    return max_res.tolist()
  else:
    return None

#MIN
def min(matrix, axis):
  if axis == 0 or axis ==1:
    min_res = np.min(matrix, axis=axis)
    return min_res.tolist()

  elif axis == "flattened":
    min_res = np.min(matrix)
    return min_res.tolist()
  else:
    return None

#SUM
def sum(matrix, axis):
  if axis == 0 or axis ==1:
    sum_res = np.sum(matrix, axis=axis)
    return sum_res.tolist()

  elif axis == "flattened":
    sum_res = np.sum(matrix)
    return sum_res.tolist()
  else:
    return None



def calculate(list):
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
    
    #List to matrix conversion
    matrix = np.array(list).reshape((3, 3))
  
    calculations = {
     'mean': [mean(matrix, 0), mean(matrix, 1), mean(matrix, "flattened")],
     'variance': [var(matrix, 0), var(matrix, 1), var(matrix, "flattened")],
     'standard deviation': [std(matrix, 0), std(matrix, 1), std(matrix, "flattened")],
     'max': [max(matrix, 0), max(matrix, 1), max(matrix, "flattened")],
     'min': [min(matrix, 0), min(matrix, 1), min(matrix, "flattened")],
     'sum': [sum(matrix, 0), sum(matrix, 1), sum(matrix, "flattened")]
    }

    return calculations