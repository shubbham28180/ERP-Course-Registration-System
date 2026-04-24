import pandas as pd 
 
def save_data(data): 
    df = pd.DataFrame(data) 
    df.to_csv("data.csv", index=False) 
 
def load_data(): 
    return pd.read_csv("data.csv")