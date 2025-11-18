import pandas as pd

# Create a sample DataFrame
data = {'DogName': ['Luna', 'Bella', 'Daisy'],
        'Age': [2, 3, 1],
        'Color': ['Black', 'White', 'Brown']}
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

print("Successfully written to output.csv")