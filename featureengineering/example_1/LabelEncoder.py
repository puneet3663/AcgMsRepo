from sklearn.preprocessing import LabelEncoder

# Sample categorical labels
labels = ['apple', 'banana', 'cherry', 'banana', 'apple']

# Create and fit the encoder
encoder = LabelEncoder()
encoded_labels = encoder.fit_transform(labels)

print(encoded_labels)
