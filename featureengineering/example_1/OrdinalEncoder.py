from sklearn.preprocessing import OrdinalEncoder
import numpy as np

# Sample categorical data
data = np.array([['low'], ['medium'], ['high'], ['medium'], ['low']])

# Create and fit the encoder
encoder = OrdinalEncoder()
encoded_data = encoder.fit_transform(data)

print(encoded_data)
