import os
from pathlib import Path

def save_df(df, filename, ext) :

    # Define the directory and file path
    dir_path = Path('datasets')
    file_path = dir_path / f"{filename}.{ext}"  # Create the file path

    # Ensure the directory exists (create it if it doesn't)
    # Creates the directory and any necessary subdirectories
    dir_path.mkdir(parents=True, exist_ok=True)

    if os.path.isfile(file_path) :
        # Append an existing file without Header
        df.to_csv(file_path, mode='a', index=False, header=False)
    else :
        # Create a new file with Header
        df.to_csv(file_path, mode='w', index=False, header=True)

    print(f"File saved to {file_path}")
