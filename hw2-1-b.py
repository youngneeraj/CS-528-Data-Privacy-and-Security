import pandas as pd
from scipy.stats import entropy

def recursive_cl_diversity_within_class(df, c, l, sensitive_column):
    if l == 1 or df[sensitive_column].nunique() < l:
        return df
    
    frequencies = df[sensitive_column].value_counts()
    vmax = frequencies.index[0]
    fmax = frequencies.iloc[0]
    sum_others = frequencies.iloc[1:].sum()
    fthreshold = c * sum_others

    if fmax <= fthreshold:
        return df  # The group satisfies (c, l)-diversity.
    else:
        # Remove the most frequent value and check (c, l-1)-diversity for the rest.
        df = df[df[sensitive_column] != vmax]
        return recursive_cl_diversity_within_class(df, c, l - 1, qi_columns, sensitive_column)

def apply_generalization(df, generalization_func, column, level):
    df[column] = df[column].apply(lambda x: generalization_func(x, level))
    return df


    

    # Apply generalizations based on your generalization levels.
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
    
   
    generalization_levels = {
    'age': {'current': 2, 'max': 4},
    'education': {'current': 0, 'max': 3},
    'marital-status': {'current': 1, 'max': 3},
    'race': {'current': 0, 'max': 2},

}

if __name__ == "__main__":
    # Load your datasets
    df = pd.read_csv(r"C:\Users\neera\OneDrive\Desktop\DPA Assignments\get_anonymized_dataset.csv")
    c = 2  # The 'c' parameter for recursive (c, l)-diversity.
    l = 3  # The 'l' parameter for diversity.
    qi_columns = ['age', 'education', 'marital-status', 'race']  # Quasi-identifier columns.
    sensitive_column = 'occupation'  # Sensitive column.


    df = apply_generalization(df, generalize_age, 'age', 2)
    df = apply_generalization(df, generalize_education, 'education', 1)
    df = apply_generalization(df, generalize_marital_status, 'marital-status', 1)
    df = apply_generalization(df, generalize_race, 'race', 1)
    

    
    # Now apply recursive (c, l)-diversity.
    anonymized_df = recursive_cl_diversity_within_class(df, c, l, sensitive_column)
    

    # Save the anonymized data
    anonymized_df.to_csv('generalized_dataset_for_Recursive_c_l_diversity.csv', index=False)

    print(anonymized_df.head())  # Correct: This executes the head() method and prints its result

