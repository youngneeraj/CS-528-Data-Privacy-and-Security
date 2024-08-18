import pandas as pd
import numpy as np
from scipy.stats import entropy
import pandas as pd

# Load your datasets
original_df = pd.read_csv(r"C:\Users\neera\OneDrive\Desktop\DPA Assignments\adult.data")
generalized_df = pd.read_csv(r"C:\Users\neera\OneDrive\Desktop\DPA Assignments\generalized_dataset_for_l_diversity.csv")

# Function to enforce k=5 anonymity on the generalized dataset
def apply_k_anonymity(df, k=5):
    grouped = df.groupby(['age', 'education', 'marital-status', 'race'])
    anonymized_df = grouped.filter(lambda x: len(x) >= k)
    return anonymized_df

# Function to calculate entropy for enforcing l-diversity
def calculate_entropy(series):
    probabilities = series.value_counts(normalize=True)
    return entropy(probabilities, base=2)

# Calculating distortion
def calculate_distortion(original_df, generalized_df):
    original_count = len(original_df)
    generalized_count = len(generalized_df)
    distortion = (original_count - generalized_count) / original_count
    return distortion

# Calculating precision
def calculate_precision():
    depth_vgh = {'age': 4, 'education': 3, 'marital-status': 3, 'race': 2}
    height = {'age': 2, 'education': 1, 'marital-status': 1, 'race': 0}
    N_A = len(depth_vgh)
    PT = len(generalized_df)
    sum_h_over_depth = sum(height[attribute] / depth_vgh[attribute] for attribute in depth_vgh)
    precision = 1 - (sum_h_over_depth / (N_A * PT))
    return precision

# Main execution
if __name__ == "__main__":
    anonymized_df = apply_k_anonymity(generalized_df, k=5)
    distortion = calculate_distortion(original_df, anonymized_df)
    precision = calculate_precision()
    print(f"Distortion: {distortion}, Precision: {precision}")

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

generalized_data = enforce_entropy_l_diversity(generalized_df, 3, ['age', 'education', 'marital-status', 'race'], 'occupation', generalization_levels)
