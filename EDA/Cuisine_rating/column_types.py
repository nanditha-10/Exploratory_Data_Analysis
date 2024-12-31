def grab_col_names(dataframe, cat_th=10, car_th=20):
    """Categorize columns into categorical, numerical, and cardinal."""
    for col in dataframe.columns:
        if dataframe[col].dtypes == "bool":
            dataframe[col] = dataframe[col].astype(int)

    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and str(dataframe[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    with open("EDA_results.md", "a") as f:
        f.write(f"cat_cols: {cat_cols}\n")
        f.write(f"num_cols: {num_cols}\n")
        f.write(f"cat_but_car: {cat_but_car}\n")

    return cat_cols, num_cols, cat_but_car
