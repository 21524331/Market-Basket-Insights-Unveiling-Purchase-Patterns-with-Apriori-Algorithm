# -*- coding: utf-8 -*-
"""apriori.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p4_QTqiKytKVGzyRNLRmIDZNl-Jx4SuA

# "Market Basket Insights: Unveiling Purchase Patterns with Apriori Algorithm

## Importing the libraries
"""

!pip install apyori

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""The necessary libraries (numpy, matplotlib, pandas) are imported along with the installation of apyori, which is used for implementing the Apriori algorithm.

## Data Preprocessing
"""

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

"""The dataset 'Market_Basket_Optimisation.csv' is loaded into a Pandas DataFrame. It seems to be a transactional dataset with 20 columns. Each row represents a transaction, and each column represents an item.

## Training the Apriori model on the dataset
"""

from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

"""The Apriori algorithm is trained on the dataset with certain parameters like min_support, min_confidence, min_lift, min_length, and max_length. These parameters control the minimum support, confidence, lift, and length of the association rules generated.

## Visualising the results

### Displaying the first results coming directly from the output of the apriori function
"""

results = list(rules)

results

"""The results of the Apriori algorithm are visualized. The association rules generated are displayed, showing items that are frequently bought together along with their support, confidence, and lift.

### Putting the results well organised into a Pandas DataFrame
"""

def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

"""The results are organized into a Pandas DataFrame for better readability. A function inspect() is defined to extract relevant information from the results, and the DataFrame is created using this function.

### Displaying the results non sorted
"""

resultsinDataFrame

"""### Displaying the results sorted by descending lifts"""

resultsinDataFrame.nlargest(n = 10, columns = 'Lift')

"""The results are displayed, both unsorted and sorted by descending lift. This helps in identifying the most significant association rules based on lift."""