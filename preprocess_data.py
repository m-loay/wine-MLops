import pandas as pd

df = pd.read_csv("wine_quality.csv")

# features that we expect are uninformative
keep_list = [
    "alcohol",
    "sulphates",
    "volatile acidity",  
    "chlorides",         
    "pH",               
    "fixed acidity", 
    "residual sugar", 
    "free sulfur dioxide", 
    "density", 
    "citric acid"
]

# Select only those columns
df = df[keep_list]

# save it
df.to_csv("data_processed_wine_quality.csv", index=False)
