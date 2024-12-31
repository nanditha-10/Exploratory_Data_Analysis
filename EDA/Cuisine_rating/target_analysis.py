def target_summary_with_cat(dataframe, target, categorical_col):
    """Analyze target variable with categorical columns."""
    with open("EDA_results.txt", "a") as f:
        f.write(f"##### {categorical_col} vs {target} #####\n")
        f.write(f"{dataframe.groupby(categorical_col)[target].mean()}\n")

def target_summary_with_num(dataframe, target, numerical_col):
    """Analyze target variable with numerical columns."""
    with open("EDA_results.txt", "a") as f:
        f.write(f"##### {numerical_col} vs {target} #####\n")
        f.write(f"{dataframe.groupby(target).agg({numerical_col: 'mean'})}\n")

def analyze_target(df, target, cat_cols, num_cols):
    for col in cat_cols:
        target_summary_with_cat(df, target, col)
    for col in num_cols:
        target_summary_with_num(df, target, col)
