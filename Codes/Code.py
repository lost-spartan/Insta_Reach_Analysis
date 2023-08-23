import pandas as pd #pip install pandas
import numpy as np
import matplotlib.pyplot as plt #pip install matplotlib
import seaborn as sns   #pip install seaborn

data = pd.read_csv("Dataset\Instagram data.csv", encoding = 'latin1')
# To read data file fromm the location present with respect to the project folder

print(data) 


data.info()
# Tells Coloumn name, Non null element count and the data type of those element

data = data['From Hashtags']
# Takes the complete list of the quoted field

print(data)