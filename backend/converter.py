import pandas as pd
import os
import json

def flatten_json(nested_json, parent_key='', sep='.'):
    """
    Flattens a nested JSON structure into a single-level dictionary.
    Arguments:
        - nested_json: A dictionary (or list of dictionaries) representing the JSON to be flattened.
        - parent_key: The base key string for recursion (used for nesting levels).
        - sep: The separator to use between parent and child keys (default is '.').
    Returns:
        - A flattened dictionary.
    """
    items = []
    if isinstance(nested_json, dict):
        for key, value in nested_json.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.extend(flatten_json(value, new_key, sep=sep).items())
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    items.extend(flatten_json(item, f"{new_key}[{i}]", sep=sep).items())
            else:
                items.append((new_key, value))
    elif isinstance(nested_json, list):
        for i, item in enumerate(nested_json):
            items.extend(flatten_json(item, f"{parent_key}[{i}]", sep=sep).items())
    return dict(items)

def json_to_csv(json_input, csv_output):
    """
    Convert a JSON input file to a CSV output file using pandas for simplicity.
    Arguments:
        - json_input: Path to the input JSON file.
        - csv_output: Path to the output CSV file.
    """
    try:
        # Load the JSON data into a pandas DataFrame
        import json
        with open(json_input, 'r') as file:
            data = json.load(file)

        # If the data is a dictionary, wrap it in a list for uniform processing
        if isinstance(data, dict):
            data = [data]

        # Flatten each item in the list if needed
        flattened_data = [flatten_json(item) for item in data]

        # Convert the flattened data into a DataFrame
        df = pd.DataFrame(flattened_data)

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
    input_path = "example.json"
    output_path = "output.csv"
    json_to_csv(input_path, output_path)

def stream_json_to_csv(json_input, csv_output):
    """
    Convert a large JSON input file to a CSV output file using streaming to avoid memory overload.
    Arguments:
        - json_input: Path to the input JSON file.
        - csv_output: Path to the output CSV file.
    """
    with open(json_input, 'r') as infile:
        with open(csv_output, 'w', newline='') as outfile:
            # Scrivi l'intestazione una volta
            header_written = False
            for line in infile:
                data = json.loads(line.strip())  # Supponiamo che sia in formato JSONLines
                flattened_data = flatten_json(data)
                if not header_written:
                    # Scrivi l'intestazione
                    headers = list(flattened_data.keys())
                    writer = csv.DictWriter(outfile, fieldnames=headers)
                    writer.writeheader()
                    header_written = True
                # Scrivi la riga
                writer.writerow(flattened_data)