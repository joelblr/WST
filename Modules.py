from pathlib import Path

def save_df(df, filename, ext) :

    # Define the directory and file path
    dir_path = Path('datasets')
    file_path = dir_path / f"{filename}.{ext}"  # Create the file path

    # Ensure the directory exists (create it if it doesn't)
    # Creates the directory and any necessary subdirectories
    dir_path.mkdir(parents=True, exist_ok=True)

    df.to_csv(file_path, index=False)

    print(f"File saved to {file_path}")
