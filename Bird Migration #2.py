
# First, use `groupby()` to group the data by "bird_name".
import pandas as pd
import numpy as np
birddata = pd.read_csv()

grouped_birds = birddata.groupby("Sanne")
# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds.speed_2d.mean()
print(mean_speeds)