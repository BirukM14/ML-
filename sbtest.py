import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rollno = [1, 2, 3, 4, 5, 6, 7, 8, 9]
marks = [23, 25, 27, 20, 4, 60, 7, 8, 9]

# Correct DataFrame creation
sample_df = pd.DataFrame({"rollno": rollno, "marks": marks})

print(sample_df)
