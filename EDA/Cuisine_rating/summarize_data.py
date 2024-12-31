# summarize_data.py

def check_df(dataframe, head=5):
    """This function will give us basic information about datasets """
    
    with open("EDA_results.md", "a") as f:
        f.write("## Data Summary\n\n")
        
        f.write("### Shape\n")
        f.write(f"{dataframe.shape}\n\n")
        
        f.write("### Column Names and Types\n")
        f.write(f"{dataframe.info()}\n\n")
        
        f.write("### Head\n")
        f.write(f"{dataframe.head(head).to_string()}\n\n")
        
        f.write("### Tail\n")
        f.write(f"{dataframe.tail(head).to_string()}\n\n")
        
        f.write("### Missing Values\n")
        f.write(f"{dataframe.isnull().sum().to_string()}\n\n")
        
        f.write("### Quantiles\n")
        f.write(f"{dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T.to_string()}\n\n")

    print("Data summary has been saved to EDA_results.md.")
