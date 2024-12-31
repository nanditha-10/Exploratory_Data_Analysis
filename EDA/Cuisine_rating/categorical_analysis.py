import matplotlib.pyplot as plt
import os

def cat_summary(dataframe, categorical_col, plot=False):
    # Saving summary to the results file
    with open("EDA_results.md", "a") as f:
        f.write(f"### Summary for {categorical_col}\n\n")
        f.write(f"{dataframe[categorical_col].value_counts()}\n\n")
    
    print(f"Summary for {categorical_col} has been saved to EDA_results.md.")
    
    # If plot is True, generate the plot
    if plot:
        dataframe[categorical_col].value_counts().plot(kind="bar")
        plt.xlabel(categorical_col)
        plt.title(categorical_col)

        # Save the plot as an image in the 'images' folder
        image_path = os.path.join("images", f"{categorical_col}_distribution.png")
        plt.savefig(image_path)  # Ensure the image is saved in the 'images' folder
        plt.close()  # Close the plot after saving it
