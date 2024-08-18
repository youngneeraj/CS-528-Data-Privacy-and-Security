import pandas as pd

# Load your anonymized data
anonymized_data = pd.read_csv('get_anonymized_dataset.csv')

# Define the maximum generalization levels for each quasi-identifier
max_generalization_levels = {
    'age': 4, # Max generalization level provided for age
    'education': 3, # Max generalization level provided for education
    'marital-status': 3, # Max generalization level provided for marital-status
    'race': 2, # Max generalization level provided for race
}

# Define the current generalization level for each quasi-identifier
current_generalization_levels = {
    'age': 1,
    'education': 0,
    'marital-status': 1,
    'race': 0,
}

# Calculate distortion using the provided levels
distortion = sum(current_generalization_levels[qi] / max_generalization_levels[qi] for qi in max_generalization_levels) / len(max_generalization_levels)



# Print the distortion 
print("Distortion:", distortion)



# Define the maximum generalization levels for each quasi-identifier
depth_vgh = {
    'age': 4,  # Depth of VGH for age
    'education': 3,  # Depth of VGH for education
    'marital-status': 3,  # Depth of VGH for marital-status
    'race': 2,  # Depth of VGH for race
}

# Define the current generalization level for each quasi-identifier
height = {
    'age': 1,  # Height of generalization for age
    'education': 0,  # Height of generalization for education
    'marital-status': 1,  # Height of generalization for marital-status
    'race': 0,  # Height of generalization for race
}

# The number of attributes and the number of records
N_A = 4  # Number of attributes
PT = 5  # Dataset size (number of records)

# Calculate the sum of the height of generalized values divided by the depth of VGH for each attribute
sum_h_over_depth = sum(height[attribute] / depth_vgh[attribute] for attribute in depth_vgh)

# Calculate precision using the provided formula
precision = 1 - (sum_h_over_depth / (PT * N_A))
print("Precision:", precision)

