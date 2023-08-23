#   Share of Impressions(Reach) from each Section

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns   

data = pd.read_csv("Dataset\Instagram data.csv", encoding = 'latin1')

home = data['From Home'].sum()
hasht = data['From Hashtags'].sum()
expl = data['From Explore'].sum()
others = data['From Other'].sum()

labels = ['From Home', 'From Hashtags', 'From Explore', 'From Other']
values = [home, hasht, expl, others]

explode_val = [0.1, 0.1, 0.1, 0.1]  # It pops up the segment in the chart 

plt.pie( values, labels = labels, explode=explode_val, shadow=True, startangle=90, autopct='%1.2f%%')
plt.legend(title = "Reach Source : ")
plt.title("Share of Impressions(Reach) from each Section")
plt.show()


# startangle -> By default the pie chart starts from x axis, to make it start from y axis you can use this.
# autopct -> This helps you to show the percentage of the segment on the figure