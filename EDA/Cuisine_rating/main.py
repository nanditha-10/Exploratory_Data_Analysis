import os
import load_data
import summarize_data
import column_types
import categorical_analysis
import numerical_analysis

# Step 1: Create the images directory
os.makedirs("images", exist_ok=True)

# Step 2: Initialize the results file
results_file = "EDA_results.md"
with open(results_file, "w") as f:
    f.write("# Exploratory Data Analysis Results\n\n")

# Step 3: Load the dataset
df = load_data.load_data("Cuisine_rating.csv")

# Step 4: Redirect DataFrame info to the results file
with open(results_file, "a") as f:
    f.write("## Data Overview\n\n")
    df_info = df.info()  # this prints to terminal by default, redirect to file
    f.write(str(df_info) + "\n\n")

# Step 5: Perform data summarization
summarize_data.check_df(df)

# Step 6: Identify column types
cat_cols, num_cols, cat_but_car = column_types.grab_col_names(df)

# Save column type summary to results file
with open(results_file, "a") as f:
    f.write("## Column Types\n\n")
    f.write(f"Categorical Columns: {cat_cols}\n")
    f.write(f"Numerical Columns: {num_cols}\n")
    f.write(f"Categorical but cardinal columns: {cat_but_car}\n\n")

# Step 7: Analyze categorical columns
for col in cat_cols:
    categorical_analysis.cat_summary(df, col, plot=True)

# Step 8: Analyze numerical columns
for col in num_cols:
    numerical_analysis.num_summary(df, col, plot=True)
