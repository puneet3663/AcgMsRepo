from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Sample categorical data
data = np.array([['red'], ['green'], ['blue'], ['green'], ['red']])

# Create and fit the OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)  # Setting sparse_output=False returns a NumPy array
encoded_data = encoder.fit_transform(data)

print(encoded_data)
