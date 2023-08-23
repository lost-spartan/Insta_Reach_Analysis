#   Number of Impressions(Reach) from each Section

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns   

data = pd.read_csv("Dataset\Instagram data.csv", encoding = 'latin1')

home = data['From Home'].sum()
hasht = data['From Hashtags'].sum()
expl = data['From Explore'].sum()
others = data['From Other'].sum() 

value = [home, hasht, expl, others]
indices = ["From Home", "From Hashtags", "From Explore", "From Others"]

plt.bar(indices, value, color='c')
plt.title("Number of Impressions(Reach) from each Section")
plt.show()