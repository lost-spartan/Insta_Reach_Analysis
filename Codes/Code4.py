#   Relationship of comments wrt sources

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns   

data = pd.read_csv("Dataset\Instagram data.csv", encoding = 'latin1')

home = data['From Home']
hasht = data['From Hashtags']
expl = data['From Explore']

comments = data['Comments']


slope1 = np.polyfit(comments, home, 1)
line1 = np.polyval(slope1, comments)
plt.plot(comments, line1, label="From Home")

slope2 = np.polyfit(comments, hasht, 1)
line2 = np.polyval(slope2, comments)
plt.plot(comments, line2, label="From Hashtags")

slope3 = np.polyfit(comments, expl, 1)
line3 = np.polyval(slope3, comments)
plt.plot(comments, line3, label="From Explore")

plt.title("Relationship of comments wrt sources")
plt.xlabel("Number of comments")
plt.ylabel("Source Reach")
plt.legend()
plt.show()