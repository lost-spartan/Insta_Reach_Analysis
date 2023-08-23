#   Relationship of likes wrt sources

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns   

data = pd.read_csv("Dataset\Instagram data.csv", encoding = 'latin1')

home = data['From Home']
hasht = data['From Hashtags']
expl = data['From Explore']

likes = data['Likes']

plt.scatter(likes, home, alpha= 0.5, label='From Home')
plt.scatter(likes, hasht, alpha= 0.5, label='From Hashtags')
plt.scatter(likes, expl, alpha= 0.5, label='From Explore') 


slope1 = np.polyfit(likes, home, 1)
line1 = np.polyval(slope1, likes)
plt.plot(likes, line1, label="From Home", color='blue')

slope2 = np.polyfit(likes, hasht, 1)
line2 = np.polyval(slope2, likes)
plt.plot(likes, line2, label="From Hashtags", color='brown')

slope3 = np.polyfit(likes, expl, 1)
line3 = np.polyval(slope3, likes)
plt.plot(likes, line3, label="From Explore", color='green')

plt.legend()

plt.title("Relationship of likes wrt sources")
plt.xlabel("Number of likes")
plt.ylabel("Source Reach")
plt.show()