import numpy as np

def convert_to_numpy_array(lst):
    """Convierte una lista en un array de NumPy de 3x3."""
    return np.array(lst).reshape(3, 3)

def calculate_axis_parameters(arr):
    """Calcula los parámetros estadísticos para los ejes."""
    axis_mean = np.mean(arr, axis=0).tolist()
    axis_variance = np.var(arr, axis=0).tolist()
    axis_std = np.std(arr, axis=0).tolist()
    axis_max = np.max(arr, axis=0).tolist()
    axis_min = np.min(arr, axis=0).tolist()
    axis_sum = np.sum(arr, axis=0).tolist()

    return [axis_mean, axis_variance, axis_std, axis_max, axis_min, axis_sum]

def calculate_flattened_parameters(arr):
    """Calcula los parámetros estadísticos para el array aplanado."""
    flattened_mean = np.mean(arr)
    flattened_variance = np.var(arr)
    flattened_std = np.std(arr)
    flattened_max = np.max(arr)
    flattened_min = np.min(arr)
    flattened_sum = np.sum(arr)

    return [flattened_mean, flattened_variance, flattened_std, flattened_max, flattened_min, flattened_sum]

def calculate(list):
    """Calcula parámetros estadísticos para diferentes ejes y el array aplanado."""
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    list = convert_to_numpy_array(list)

    axis1_params = calculate_axis_parameters(list.reshape(3, 3))
    axis2_params = calculate_axis_parameters(list.T)  # Transpuesta para obtener los parámetros para el segundo eje
    flattened_params = calculate_flattened_parameters(list.flatten())

    calculations = {
        'mean': [axis1_params[0], axis2_params[0], flattened_params[0]],
        'variance': [axis1_params[1], axis2_params[1], flattened_params[1]],
        'standard deviation': [axis1_params[2], axis2_params[2], flattened_params[2]],
        'max': [axis1_params[3], axis2_params[3], flattened_params[3]],
        'min': [axis1_params[4], axis2_params[4], flattened_params[4]],
        'sum': [axis1_params[5], axis2_params[5], flattened_params[5]]
    }

    return calculations

