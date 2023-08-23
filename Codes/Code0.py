import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns   

data = pd.read_csv("Dataset\Instagram data.csv", encoding = 'latin1')

plt.figure(figsize=(10, 8))
plt.style.use('ggplot')
plt.title("Distribution of Impressions From Home Page")
sns.distplot(data['From Hashtags'])
plt.show()


# Other possible parameters for plt.style.use()
#
# [‘Solarize_Light2’, 
#  ‘_classic_test_patch’, 
#  ‘bmh’, 
#  ‘classic’, 
#  ‘dark_background’, 
#  ‘fast’, 
#  ‘fivethirtyeight’, 
#  ‘ggplot’,
#  ’grayscale’,
#  ’seaborn’,
#  ’seaborn-bright’,
#  ’seaborn-colorblind’, 
#  ‘seaborn-dark’, 
# ]