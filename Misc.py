import pandas as pd
import numpy as np

# Create a sample dataset with 50 rows and 5 columns
data = {
    'Column1': np.random.randint(1, 100, 50),
    'Column2': np.random.choice(['A', 'B', 'C', 'D'], 50),
    'Column3': np.random.random(50),
    'Column4': np.random.normal(0, 1, 50),
    'Column5': pd.date_range(start='2023-01-01', periods=50)
}

df = pd.DataFrame(data)

# Save the dataset as a Feather file
df.to_feather('sample_dataset.feather')

print("Dataset created and saved as 'sample_dataset.feather'")