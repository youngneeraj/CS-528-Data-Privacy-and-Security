import pandas as pd

# Adjust the path as necessary
dataset_path = (r"C:\Users\neera\OneDrive\Desktop\DPA Assignments\generalized_dataset_for_l_diversity.csv")
data = pd.read_csv(dataset_path)

from scipy.stats import entropy
import numpy as np

def calculate_entropy(series):
    """Calculate entropy of a Pandas series."""
    value_counts = series.value_counts()
    probabilities = value_counts / value_counts.sum()
    return entropy(probabilities, base=2)

# Group the data by the quasi-identifiers and calculate entropy for each group
grouped = data.groupby(['age', 'education', 'marital-status', 'race'])
entropy_values = grouped['occupation'].apply(calculate_entropy)


# Define your L value here
L = 3
min_entropy = np.log2(L)

# Check if all groups meet the L-diversity criteria
all_diverse = all(entropy_values >= min_entropy)
if all_diverse:
    print("All equivalence classes satisfy Entropy L-diversity.")
else:
    print("Some equivalence classes do not satisfy Entropy L-diversity.")


non_diverse_groups = entropy_values[entropy_values < min_entropy]
print("Non-diverse groups:")
print(non_diverse_groups)

