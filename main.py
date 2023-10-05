import pandas as pd

#Load Excel file
file_path = "path_file.xlsx"
df = pd.read_excel(file_path, engine = "openpyxl")

# Lable target sample size
sample_size = 1000
sample_df = df.groupby('Category').apply(lambda x: x.sample(int(sample_size * len(x) / len(df)))).reset_index(drop = True)

# Export of sample into Excel file 
output_file_path = 'path_file.xlsx'
sample_df.to_excel (output_file_path, engine= 'openpyxl', index=False)
