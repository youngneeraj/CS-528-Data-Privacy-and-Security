import pandas as pd

def load_and_prepare_data(file_path):
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ]
    df = pd.read_csv(file_path, names=column_names, skipinitialspace=True, na_values="?")
    return df[['age', 'education', 'marital-status', 'race', 'occupation', 'salary']]

def generalize_data(df):
    df['age'] = pd.cut(df['age'], bins=[0, 20, 40, 60, 80, 100], right=False, labels=['0-20', '20-40', '40-60', '60-80', '80-100'])
    education_order = ['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', 
                       '11th', '12th', 'HS-grad', 'Some-college', 'Assoc-voc', 'Assoc-acdm', 
                       'Bachelors', 'Masters', 'Prof-school', 'Doctorate', 'Unknown']
    df['education'] = pd.Categorical(df['education'], categories=education_order, ordered=True)
    df['education'] = df['education'].fillna('Unknown')
    df['marital-status'] = df['marital-status'].replace(['Married-spouse-absent', 'Married-civ-spouse', 'Married-AF-spouse'], 'Married').fillna('Unknown')
    df['race'] = df['race'].fillna('Unknown')
    return df

def apply_k_anonymity(df, k1=10, k2=5):
    # First, create a copy of the df to retain the 'salary' column for processing
    df_with_salary = df.copy()

    # Calculate the count for each group based on QIs and 'salary'
    grouped = df_with_salary.groupby(['age', 'education', 'marital-status', 'race', 'salary'], observed=True)
    counts = grouped.transform('size')

    # Calculate the k-values for each row based on the 'salary' column
    k_values = df_with_salary['salary'].apply(lambda x: k1 if x == '<=50K' else k2)

    # Create a mask for rows that do not meet the k-anonymity requirement
    mask = counts < k_values

    # Apply the mask to filter rows that do not meet the k-anonymity requirement
    df_anonymized = df_with_salary[~mask]

    # Drop the 'salary' column from the final dataset as it's not required to be shared in the output
    df_anonymized = df_anonymized.drop(columns=['salary'])
    
    return df_anonymized

def main(file_path):
    df = load_and_prepare_data(file_path)
    df = generalize_data(df)
    df = apply_k_anonymity(df)
    print("Data after generalization (sample):")
    print(df.head())
    df.to_csv('get_anonymized_dataset.csv', index=False)

# Replace 'file_path' with the actual path to your dataset
file_path = 'C:\\Users\\neera\\OneDrive\\Desktop\\DPA Assignments\\adult.data' 


main(file_path)

def main(file_path):
    df = load_and_prepare_data(file_path)
    df_generalized = generalize_data(df)
    initial_count = len(df_generalized)
    df_anonymized = apply_k_anonymity(df_generalized, k1=10, k2=5)
    final_count = len(df_anonymized)
    
    print(f"Initial record count: {initial_count}")
    print(f"Final record count after applying (k1, k2)-anonymity: {final_count}")
    print("Data after generalization and (k1, k2)-anonymity enforcement (sample):")
    print(df_anonymized.head())
    
    # Save the anonymized dataset without the 'salary' attribute
    df_anonymized.to_csv(r'C:\Users\neera\OneDrive\Desktop\DPA Assignments\get_anonymized_dataset.csv', index=False)


# Make sure to use the correct and existing file path
file_path = r'C:\Users\neera\OneDrive\Desktop\DPA Assignments\adult.data' 
main(file_path)



