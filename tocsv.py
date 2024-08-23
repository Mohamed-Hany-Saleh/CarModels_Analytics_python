import csv
import re

def clean_data(data):
    """Remove single quotes, everything before '[', and square brackets from the string."""
    # Keep everything after and including '['
    data = re.sub(r".*?\[", "", data)
    # Remove single quotes and square brackets
    data = data.replace("'", "").replace("[", "").replace("]", "")
    return data.strip()

def read_headers(file_path):
    """Read the column headers from a text file and return them as a cleaned list."""
    with open(file_path, 'r') as file:
        headers = file.readline().strip().split(',')
    # Clean each header
    headers = [clean_data(header) for header in headers]
    return headers

def read_rows(file_path):
    """Read the row data from a text file and return it as a cleaned list of lists."""
    with open(file_path, 'r') as file:
        rows = [line.strip().split(',') for line in file]
    # Clean each element in each row
    rows = [[clean_data(cell) for cell in row] for row in rows]
    return rows

def write_to_csv(headers, rows, output_file):
    """Write the headers and rows to a CSV file."""
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)  # Write headers
        csvwriter.writerows(rows)    # Write rows

def merge_txt_to_csv(headers_file, rows_file, output_csv):
    """Merge the headers and rows from text files into a CSV file."""
    headers = read_headers(headers_file)
    rows = read_rows(rows_file)
    write_to_csv(headers, rows, output_csv)

def main():
    # Define file paths
    headers_file = 'COL_Names.txt'  # Path to the headers file
    rows_file = 'Wrangling data.txt'        # Path to the rows file
    output_csv = 'DATA.csv'     # Output CSV file path

    # Merge the text files into a CSV
    merge_txt_to_csv(headers_file, rows_file, output_csv)
    print(f"CSV file '{output_csv}' created successfully.")

if __name__ == "__main__":
    main()
