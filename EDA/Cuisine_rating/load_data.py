import pandas as pd

def load_data(file_path):
    """Load the dataset and print basic information."""
    df = pd.read_csv(file_path)
    print(f"Data loaded successfully from {file_path}")
    return df

def check_df(dataframe, head=5):
    """Print basic dataset information."""
    with open("EDA_results.txt", "a") as f:
        f.write("##################### Shape #####################\n")
        f.write(f"{dataframe.shape}\n")
        f.write("##################### Column Names #####################\n")
        dataframe.info(buf=f)
        f.write("\n##################### Head #####################\n")
        f.write(f"{dataframe.head(head)}\n")
        f.write("##################### Tail #####################\n")
        f.write(f"{dataframe.tail(head)}\n")
        f.write("##################### NA #####################\n")
        f.write(f"{dataframe.isnull().sum()}\n")
        f.write("##################### Quantiles #####################\n")
        f.write(f"{dataframe.describe([0, 0.05, 0.5, 0.95, 1]).T}\n")

if __name__ == "__main__":
    df = load_data("Cuisine_rating.csv")
    check_df(df)
