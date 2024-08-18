import pandas as pd
import numpy as np

# Your provided k-anonymity function
def apply_k_anonymity(df, k=5):
    grouped = df.groupby(['age', 'education', 'marital-status', 'race'])
    anonymized_df = grouped.filter(lambda x: len(x) >= k)
    return anonymized_df



# Your recursive (c, l)-diversity function
def recursive_cl_diversity_within_class(df, c, l, sensitive_column):
    if l == 3 or df[sensitive_column].nunique() < l:
        return df
    
    frequencies = df[sensitive_column].value_counts()
    vmax = frequencies.index[0]
    fmax = frequencies.iloc[0]
    sum_others = frequencies.iloc[1:].sum()
    fthreshold = c * sum_others

    if fmax <= fthreshold:
        return df  # The group satisfies (c, l)-diversity.
    else:
        df = df[df[sensitive_column] != vmax]
        return recursive_cl_diversity_within_class(df, c, l - 1, sensitive_column)
    






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




# Placeholder for actual distortion calculation
def calculate_distortion(original_df, anonymized_df):
    original_count = len(original_df)
    generalized_count = len(anonymized_df)
    distortion = (original_count - generalized_count) / original_count
    return distortion




# Placeholder for actual precision calculation
def calculate_precision(original_df, generalized_df, current_generalization_levels, max_generalization_levels):
    N_A = len(max_generalization_levels)
    PT = len(generalized_df)
    sum_h_over_depth = sum(current_generalization_levels[attribute] / max_generalization_levels[attribute] for attribute in max_generalization_levels)
    precision = 1 - (sum_h_over_depth / (N_A * PT))
    return precision



if __name__ == "__main__":
    # Load your datasets
    original_df = pd.read_csv(r"C:\Users\neera\OneDrive\Desktop\DPA Assignments\adult.data")
    generalized_df = pd.read_csv(r"C:\Users\neera\OneDrive\Desktop\DPA Assignments\generalized_dataset_for_Recursive_c_l_diversity.csv")

    k = 5
    l = 3
    sensitive_column = "occupation"  # Replace with your actual sensitive column

    # User input for c
    c = float(input("Please enter the value for c (e.g., 0.5, 1, 2): "))





    # Apply k-anonymity
    anonymized_df = apply_k_anonymity(generalized_df, k)
    print(f"DataFrame after (c, l)-diversity for c={c}: {anonymized_df.shape}")

    # Apply recursive (c, l)-diversity
    anonymized_df = recursive_cl_diversity_within_class(anonymized_df, c, l, sensitive_column)
    print(f"DataFrame after (c, l)-diversity for c={c}: {anonymized_df.shape}")



      # Apply generalizations based on your generalization levels.
max_generalization_levels = {
    'age': 4,  # Max generalization level provided for age
    'education': 3,  # Max generalization level provided for education
    'marital-status': 3,  # Max generalization level provided for marital-status
    'race': 2,  # Max generalization level provided for race
}

# Define the current generalization level for each quasi-identifier
current_generalization_levels = {
    'age': 2,
    'education': 0,
    'marital-status': 1,
    'race': 0,
}



print(f"Current generalization levels: {current_generalization_levels}")
    # Calculate distortion and precision
distortion = calculate_distortion(original_df, anonymized_df)
precision = calculate_precision(original_df, anonymized_df, current_generalization_levels, max_generalization_levels)

print(f"Distortion for c={c}: {distortion}")
print(f"Precision for c={c}: {precision}")


