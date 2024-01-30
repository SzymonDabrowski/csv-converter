import argparse
import csv_reader
import logging
import bank
from processors import millennium_processor, pekao_sa_processor, bank_processor
from typing import Tuple
import pekao_sa_dict, millennium_dict
import os

logging.basicConfig(level=logging.INFO)

def determine_processor(filename: str) -> bank_processor.BankProcessor:
    """
    Determine the appropriate bank processor based on the file signature.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        bank_processor.BankProcessor: An instance of the determined bank processor.

    Raises:
        SystemExit: If the bank processor cannot be determined based on the signature.
    """
    signature = csv_reader.Csv.get_column_names(filename)
    if signature == pekao_sa_dict.signature:
        return pekao_sa_processor.PekaoSaProcessor()
    elif signature == millennium_dict.signature:
        return millennium_processor.MillenniumProcessor()
    else:
        logging.error(f"Could not determine bank processor based on signature: {signature}")
        exit(1)

def determine_output_files(args, filename) -> Tuple[str, str]:
    """
    Determine the output file names based on the provided arguments and input filename.

    Args:
        args: Command-line arguments.
        filename (str): Path to the CSV file.

    Returns:
        Tuple[str, str]: A tuple containing the output file name and the ambiguous file name.
    """
    output_file = args.output
    base_filename, _ = os.path.splitext(os.path.basename(filename))

    if output_file is None:
        output_file = f"out_{base_filename}.csv"

    ambiguous_file = os.path.splitext(output_file)[0] + "_ambiguous.csv"

    return output_file, ambiguous_file

def main():
    parser = argparse.ArgumentParser(description='Process a CSV file.')
    parser.add_argument('filename', type=str, help='Path to the CSV file')
    parser.add_argument('output', type=str, nargs='?', default=None, help='Output CSV file (default: out_<filename>.csv)')

    args = parser.parse_args()

    filename = args.filename

    processor = determine_processor(filename)
    bank_instance = bank.Bank(processor)

    data = csv_reader.Csv.read(filename)
    processed_data = bank_instance.process(data)

    ambiguous_data = []
    output_data, ambiguous_data = bank_instance.filter_ambiguous_data(processed_data)

    if output_data is None and ambiguous_data is None:
        print("No output data available")
    else:
        output_file, ambiguous_file = determine_output_files(args, filename)

        csv_reader.Csv.export(output_data, output_file)
        csv_reader.Csv.export(ambiguous_data, ambiguous_file)

if __name__ == "__main__":
    main()
