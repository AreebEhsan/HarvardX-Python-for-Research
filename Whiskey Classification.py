import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

whisky = pd.read_csv("whiskies.csv")

whisky["Region"] = pd.read_csv("C:/Users/HP/Documents/regions.csv")

flavors = whisky.iloc[:, 2:14]
corr_flavors = pd.DataFrame.corr(flavors)
corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize = (10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")

plt.show()