import pandas as pd

# List of file names
file_names = ['getinfo_on_corbeillefile.csv','move_to_folder.csv','get_info_pyfile.csv','double_rename.csv','delete_file_and_copy.csv','download_copy.csv','duplicate.csv','open_close.csv','pyfile_shared.csv','rien_touche.csv','recently_dl_dlforeverfail.csv','stopresp_after_dl_corbeille_puis_reco.csv','upload_pyfile.csv']

# Create an empty list to store the DataFrames
dfs = []

# Load each file into a DataFrame and append it to the list
for file_name in file_names:
    df = pd.read_csv(file_name)
    dfs.append(df)

# Merge the DataFrames
merged_df = pd.concat(dfs)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('all_App.csv', index=False)
