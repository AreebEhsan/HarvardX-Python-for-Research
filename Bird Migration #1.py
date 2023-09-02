import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

birddata = pd.read_csv("bird_tracking.csv")
print(birddata)




bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize=(7, 7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name

    x, y = birddata.longitude[ix], birddata.latitude[ix]

    plt.plot(x, y , ".", label = bird_name)   # "." dotted line
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc= "lower right")

plt.show()


