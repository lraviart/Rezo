import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyshark as ps

# Read the CSV file
df = pd.read_csv('App/rien_touche.csv')

# Filter rows with 'DNS' protocol
dns_df = df[df['Protocol'] == 'DNS']

# Create a new DataFrame with 'Protocol' and 'Info' columns
filtered_df = dns_df[['Protocol', 'Info']]

# Write the filtered DataFrame to a new CSV file
filtered_df.to_csv('rien_touche.csv', index=False)
