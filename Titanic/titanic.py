import os
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = '/data'
TRAIN_FILE = '/train.csv'
TEST_FILE = '/test.csv'

train = pd.read_csv(ROOT + DATA_FOLDER + TRAIN_FILE)
print(train.head())
