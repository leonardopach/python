import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv("credit.csv")
print(base_credit.head(10))
print(base_credit.describe())
print(base_credit[base_credit["person_age"] >= 144])
sns.countplot(x=base_credit["person_age"])
np.unique(base_credit["person_age"])
