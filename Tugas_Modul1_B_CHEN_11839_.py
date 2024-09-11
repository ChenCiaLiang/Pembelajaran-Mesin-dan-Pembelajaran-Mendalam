import pandas as pd
import numpy as np

#Load data
diabetes_csv = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documents\K\S 5\PMdPM\Pembelajaran-Mesin-dan-Pembelajaran-Mendalam\diabetes.csv')

#Load dataset ke dalam dataframe
df_diabetes = pd.DataFrame(data = diabetes_csv, index = None)
df_diabetes

#mengecek data kosong, null, dan nan
print("data null\n", df_diabetes.isnull().sum())
print("\n")
print("data kosong \n", df_diabetes.empty)
print("\n")
print("data nan \n", df_diabetes.isna().sum())

df_diabetes.describe()