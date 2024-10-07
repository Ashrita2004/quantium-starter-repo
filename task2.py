import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./combined_data.csv"

# Open the output file
with open(OUTPUT_FILE_PATH, "w", newline='') as output_file:
    writer = csv.writer(output_file)

    # Add a CSV header
    writer.writerow(["sales", "date", "region"])

    # Iterate through all files in the data directory
    for file_name in os.listdir(DATA_DIRECTORY):
        input_file_path = os.path.join(DATA_DIRECTORY, file_name)

        # Open the CSV file for reading
        with open(input_file_path, "r") as input_file:
            reader = csv.DictReader(input_file)

            # Iterate through each row in the CSV file
            for input_row in reader:
                # Process only rows with 'pink morsel' product
                if input_row['product'].lower() == "pink morsel":
                    try:
                        # Extract and format data
                        price = float(input_row['price'][1:])  # Assuming price starts with '$'
                        quantity = int(input_row['quantity'])
                        sale = price * quantity

                        # Write the row to output file
                        output_row = [sale, input_row['date'], input_row['region']]
                        writer.writerow(output_row)

                    except ValueError as e:
                        print(f"Error processing row in file {file_name}: {e}")
