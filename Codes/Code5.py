#   Conversion Rate (From Profile visited to Followed)

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns   

data = pd.read_csv("Dataset\Instagram data.csv", encoding = 'latin1')

conversion_rate = (data["Follows"].sum() / data["Profile Visits"].sum()) * 100
print(conversion_rate)

plt.scatter(data['Follows'], data['Profile Visits'], alpha=0.5)
slope = np.polyfit(data['Follows'], data['Profile Visits'], 1)
line = np.polyval(slope, data['Follows'])
plt.plot(data['Follows'], line, color='g')
plt.xlim(-2,105)
plt.ylim(0,350)

plt.title("Conversion Rate (From Profile visited to Followed)")
plt.xlabel("Number of New Followers")
plt.ylabel("Number of Profile visits")
plt.show()