import pandas as pd
import argparse
import os

def strip_units(value):
    """
    Function to remove units and specific characters like '²' from data values.
    """
    if isinstance(value, str):
        # Remove '²' characters and filter out non-numeric characters except '.' and '-'
        value = value.replace('²', '')
        return ''.join(filter(lambda x: x.isdigit() or x == '.' or x == '-', value))
    return value

def process_file(file_path):
    """
    Function to process the CSV file, removing units and specific characters.
    Args:
        file_path (str): Path to the CSV file to be processed.
    """
    # Load the CSV file
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

    # Apply the strip_units function to all columns except those containing 'Sample time'
    for column in df.columns:
        if 'Sample time' not in column:
            df[column] = df[column].apply(strip_units)

    # Generate the output file path with '_final' suffix
    output_path = file_path[:-4] + "_final.csv"
    print(f"Saving processed file to: {output_path}")  # Print the output path
    
    # Save the updated DataFrame to the new CSV file
    df.to_csv(output_path, index=False)
    
    # Delete the original CSV file after processing
    os.remove(file_path)
    print(f"Deleted original file: {file_path}")  # Confirm deletion

def main():

    # Setup argument parser
    parser = argparse.ArgumentParser(description="Process CSV files to remove units and specific characters.")
    
    # Define the positional argument for file paths
    parser.add_argument('file_paths', metavar='F', type=str, nargs='+', help='Paths to the CSV files to be processed')
    
    args = parser.parse_args() # Parse the command line arguments
    for file_path in args.file_paths:
        process_file(file_path)

if __name__ == "__main__":
    # Entry point of the script
    main()
