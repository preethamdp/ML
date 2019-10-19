import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fectch data and format it
data = fetch_movielens(min_rating=4.0)

print(data['train'])