import pandas as pd
import os

def json_to_csv(json_input, csv_output):
    """
    Convert a JSON input file to a CSV output file using pandas for simplicity.
    Arguments:
        - json_input: Path to the input JSON file.
        - csv_output: Path to the output CSV file.
    """
    try:
        # Load the JSON data into a pandas DataFrame
        df = pd.read_json(json_input)

        # Save the DataFrame as a CSV file
        df.to_csv(csv_output, index=False)
        print(f"Conversion completed: {csv_output}")
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: The file {json_input} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_path = "example.json"  # You can replace this with any JSON file
    output_path = "output.csv"   # Output CSV file name
    json_to_csv(input_path, output_path)
