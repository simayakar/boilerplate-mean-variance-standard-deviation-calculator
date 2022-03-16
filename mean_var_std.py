import numpy as np

def calculate(list):


    if len(list)<9:
      raise ValueError( "List must contain nine numbers.")
    else:
      arr = np.array(list)
      arr = arr.reshape(3,3)
      
    

    #MEAN CALCULATIONS
    mean_flattened = np.mean(arr).tolist()#flattened
    mean_axis1 = np.mean(arr, axis=0).tolist() #axis1
    mean_axis2 = np.mean(arr, axis=1).tolist() #axis2

    #VARIANCE CALCULATIONS
    var_flattened = np.var(arr).tolist() #flattened
    var_axis1 = np.var(arr, axis=0).tolist() #axis1
    var_axis2 = np.var(arr, axis=1).tolist() #axis2

    #STD DEV CALCULATIONS
    std_dev_flattened = np.std(arr).tolist() #flattened
    std_dev_axis1 = np.std(arr, axis=0).tolist() #axis1
    std_dev_axis2 = np.std(arr, axis=1).tolist() #axis2

    #MAX CALCULATIONS
    max_flattened = np.max(arr).tolist()
    max_axis1 = np.max(arr, axis=0).tolist()
    max_axis2 = np.max(arr, axis=1).tolist()

    #MIN CALCULATIONS
    min_flattened = np.min(arr).tolist()
    min_axis1 = np.min(arr, axis=0).tolist()
    min_axis2 = np.min(arr, axis=1).tolist()

    #SUM CALCULATIONS 
    sum_flattened = np.sum(arr).tolist()
    sum_axis1 = np.sum(arr, axis=0).tolist()
    sum_axis2 = np.sum(arr, axis=1).tolist()

    calculations = {
      'mean' : [mean_axis1, mean_axis2, mean_flattened],
      'variance' : [var_axis1, var_axis2, var_flattened],
      'standard deviation' : [std_dev_axis1, std_dev_axis2, std_dev_flattened],
      'max' : [max_axis1, max_axis2, max_flattened],
      'min' : [min_axis1, min_axis2, min_flattened],
      'sum' : [sum_axis1, sum_axis2, sum_flattened]
    }

    return calculations