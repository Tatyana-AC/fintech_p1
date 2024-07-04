import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()


# s = pd.Series([1,3,5,np.nan,6,8])

# print(s)

# Read the CSV file
nasdaq_data = pd.read_csv('https://example.com/passkey=wedsmdjsjmdd')

# View the first 5 rows
print(nasdaq_data.head())

# This will display "Hello, World!" in the terminal
print("Hello, World!")

# This will display your system version in the terminal
import sys
print(sys.version)