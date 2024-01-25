import argparse
import csv_reader
import logging
import bank

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description='Process a CSV file.')
    parser.add_argument('filename', type=str, help='Path to the CSV file')
    parser.add_argument('output', type=str, help='Output CSV file')

    args = parser.parse_args()

    filename = args.filename
    
    signature = csv_reader.Csv.get_column_names(filename)
    bank_instance = bank.Bank(signature)
    
    data = csv_reader.Csv.read(filename)
    output_data = bank_instance.process(data)

    ambiguous_data = []
    bank_instance.filter_ambiguous_data(output_data, ambiguous_data)

    if output_data == None:
        print ("No output data available")
    else:
        csv_reader.Csv.export(output_data, args.output)
        csv_reader.Csv.export(ambiguous_data, args.output + "_ambiguous.csv")

if __name__ == "__main__":
    main()
