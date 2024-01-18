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
    csv_data = csv_reader.Csv.read(filename)
    bank_instance = bank.Bank(csv_reader.Csv.get_column_names(filename))
    
    data_without_column_names = bank_instance.processor.remove_column_names(csv_data)
    filtered_and_sorted_data = bank_instance.processor.filter_and_sort_data(data_without_column_names, bank_instance)
    
    categories = bank_instance.processor.get_distinct_values(filtered_and_sorted_data, bank_instance)
    category_groups = bank_instance.processor.define_category_groups()
    expected_categories = bank_instance.expected_categories
    bank_instance.processor.compare_sets(categories, expected_categories, category_groups)

    output_data = bank_instance.processor.check_priority_exceptions(filtered_and_sorted_data, category_groups)

    ambiguous_data = []
    bank_instance.processor.filter_ambiguous_data(output_data, ambiguous_data)

    if output_data == None:
        print ("No output data available")
    else:
        csv_reader.Csv.export(output_data, args.output)
        csv_reader.Csv.export(ambiguous_data, args.output + "_ambiguous.csv")

if __name__ == "__main__":
    main()
