import argparse
import csv_reader
import logging
import bank
import processors.millennium_processor, processors.pekao_sa_processor
import pekao_sa_dict, millennium_dict

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description='Process a CSV file.')
    parser.add_argument('filename', type=str, help='Path to the CSV file')
    parser.add_argument('output', type=str, help='Output CSV file')

    args = parser.parse_args()

    filename = args.filename
    
    processor = None
    signature = csv_reader.Csv.get_column_names(filename)
    if (signature == pekao_sa_dict.signature):
        processor = processors.pekao_sa_processor.PekaoSaProcessor()
    elif (signature == millennium_dict.signature):
        processor = processors.millennium_processor.MillenniumProcessor()
    else:
        logging.error(f"Could not determine bank processor bases on signature: {signature}")
        exit(1)

    bank_instance = bank.Bank(processor)
    
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
