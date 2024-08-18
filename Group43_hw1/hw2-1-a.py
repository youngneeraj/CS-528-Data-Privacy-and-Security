import pandas as pd
import numpy as np
from scipy.stats import entropy

# Load the dataset
anonymized_data = pd.read_csv(r"C:\Users\neera\OneDrive\Desktop\DPA Assignments\get_anonymized_dataset.csv")

# Define the maximum generalization levels for each quasi-identifier
max_generalization_levels = {
    'age': 4,  # Max generalization level provided for age
    'education': 3,  # Max generalization level provided for education
    'marital-status': 3,  # Max generalization level provided for marital-status
    'race': 2,  # Max generalization level provided for race
}

# Define the current generalization level for each quasi-identifier
current_generalization_levels = {
    'age': 1,
    'education': 0,
    'marital-status': 1,
    'race': 0,
}

# Define the function to calculate entropy
def calculate_entropy(series):
    probabilities = series.value_counts(normalize=True)
    return entropy(probabilities, base=2)

# Generalization functions for each QI based on provided levels
def generalize_education(value, level):
    if level == 1:
        if value in ['Preschool', '1st-4th', '5th-6th']:
            return 'Elementary'
        elif value in ['7th-8th', '9th', '10th']:
            return 'Intermediate'
        elif value in ['11th', '12th', 'HS-grad']:
            return 'Secondary'
    elif level == 2:
        if value in ['Some-college', 'Assoc-voc', 'Assoc-acdm']:
            return 'Non-degree Postsecondary'
        elif value == 'Bachelors':
            return 'Undergraduate'
        elif value in ['Masters', 'Prof-school', 'Doctorate']:
            return 'Graduate'
    elif level == 3:
        return '*'

def generalize_age(value, level):
    # Directly return the generalized category based on the level
    # This approach assumes 'value' is a category like '20-40' and matches it to the correct generalization
    if level == 1:
        return value  # Assuming value is already in the initial binned format
    elif level == 2:
        if value in ['11-20', '21-30', '31-40']:
            return '20-40'
        else:
            return '41-60'
    elif level == 3:
        if value in ['11-20', '21-30', '31-40']:
            return '<40'
        else:
            return '>=40'
    elif level == 4:
        return '*'


def generalize_marital_status(value, level):
    if level == 1:
        if value in ['Married-civ-spouse', 'Married-spouse-absent', 'Married-AF-spouse']:
            return 'Married'
        else:
            return value  # Keeping other categories as is for level 1
    elif level == 2:
        if value in ['Married']:
            return 'Married'
        elif value in ['Divorced', 'Separated', 'Widowed']:
            return 'Previously Married'
        else:
            return 'Single'
    elif level == 3:
        return '*'

def generalize_race(value, level):
    if level == 1:
        if value == 'White':
            return 'Caucasian'
        elif value == 'Black':
            return 'African Descent'
        elif value == 'Asian-Pac-Islander':
            return 'Asian/Pacific Islander'
        elif value == 'Amer-Indian-Eskimo':
            return 'Indigenous Peoples'
        else:
            return 'Other/Unknown'
    elif level == 2:
        return '*'
    # Update the enforce_entropy_l_diversity function to use these generalization functions
def enforce_entropy_l_diversity(df, l_value, qi_columns, sensitive_column, generalization_levels):
    generalized_df = pd.DataFrame(columns=df.columns)
    groups = df.groupby(qi_columns)
    
    for _, group in groups:
        group_entropy = calculate_entropy(group[sensitive_column])
        
        if group_entropy < np.log2(l_value):
            # Increase generalization level and apply generalization
            for qi_column in qi_columns:
                current_level = generalization_levels[qi_column]['current']
                max_level = generalization_levels[qi_column]['max']
                
                # Check if further generalization is possible
                if current_level < max_level:
                    # Apply generalization based on the QI
                    generalization_func = globals()[f'generalize_{qi_column.replace("-", "_")}']
                    group[qi_column] = group[qi_column].apply(generalization_func, args=(current_level + 1,))
                    generalization_levels[qi_column]['current'] += 1
        
        generalized_df = pd.concat([generalized_df, group], ignore_index=True)
    
    return generalized_df

# Generalization levels dict
generalization_levels = {
    'age': {'current': 2, 'max': 4},
    'education': {'current': 0, 'max': 3},
    'marital-status': {'current': 1, 'max': 3},
    'race': {'current': 0, 'max': 2},
}

# Apply the L-diversity enforcement
generalized_data = enforce_entropy_l_diversity(anonymized_data, 3, ['age', 'education', 'marital-status', 'race'], 'occupation', generalization_levels)


# Save the generalized data
generalized_data.to_csv(r'C:\Users\neera\OneDrive\Desktop\DPA Assignments\generalized_dataset_for_l_diversity.csv', index=False)
