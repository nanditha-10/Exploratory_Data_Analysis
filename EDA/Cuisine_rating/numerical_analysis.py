import matplotlib.pyplot as plt
import os

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    
    # Saving summary statistics to the results file
    with open("EDA_results.md", "a") as f:
        f.write(f"### Summary for {numerical_col}\n\n")
        f.write(f"{dataframe[numerical_col].describe(quantiles).T}\n\n")
        f.write(f"{dataframe[numerical_col].value_counts()}\n\n")

    print(f"Summary for {numerical_col} has been saved to EDA_results.md.")
    
    # If plot is True, generate the histogram
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        
        # Save the plot as an image in the 'images' folder
        image_path = os.path.join("images", f"{numerical_col}_histogram.png")
        plt.savefig(image_path)  # Ensure the image is saved in the 'images' folder
        plt.close()  # Close the plot after saving it
