import argparse
import logging
import os
from typing import Tuple
import timeit
from utils import csv_reader
import bank
from exceptions import exceptions
from processors import millennium_processor
from processors import pekao_sa_processor
from processors import bank_processor
import pekao_sa_dict
import millennium_dict

logging.basicConfig(level=logging.INFO)


def determine_processor(filename: str) -> bank_processor.BankProcessor:
    """
    Determine the appropriate bank processor based on the file signature.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        bank_processor.BankProcessor: An instance of the determined bank processor.

    Raises:
        WrongSignatureException: If the bank processor cannot be determined based on the signature.
    """
    signature = csv_reader.Csv.get_column_names(filename)
    if signature == pekao_sa_dict.signature:
        return pekao_sa_processor.PekaoSaProcessor()
    if signature == millennium_dict.signature:
        return millennium_processor.MillenniumProcessor()

    raise exceptions.WrongSignatureError(signature)


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

    output_file = output_file or f"out_{base_filename}.csv"
    ambiguous_file = os.path.splitext(output_file)[0] + "_ambiguous.csv"
    ignored_file = os.path.splitext(output_file)[0] + "_ignored.csv"

    return (output_file, ambiguous_file, ignored_file)


def export_data_with_time_measurement(output_data, output_file, sanitize=True):
    return lambda: csv_reader.Csv.export(output_data, output_file, sanitize=sanitize)


def main():
    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument("filename", type=str, help="Path to the CSV file")
    parser.add_argument(
        "output",
        type=str,
        nargs="?",
        default=None,
        help="Output CSV file (default: out_<filename>.csv)",
    )

    args = parser.parse_args()

    filename = args.filename

    processor = determine_processor(filename)
    bank_instance = bank.Bank(processor)

    data = csv_reader.Csv.read(filename, sanitize=True, lowercase=True)
    processed_data = bank_instance.process(data)

    ambiguous_data = []
    output_data, ambiguous_data, ignored_data = bank_instance.group_output_data(
        processed_data
    )

    if output_data is None and ambiguous_data is None:
        logging.info("No output data available")
    else:
        output_file, ambiguous_file, ignored_file = determine_output_files(
            args, filename
        )

        # Measure the execution time with timeit
        export_function = export_data_with_time_measurement(
            output_data, output_file, sanitize=True
        )
        time = timeit.timeit(export_function, number=10)
        print(f"Time taken to export: {time} seconds")

        csv_reader.Csv.export(output_data, output_file, sanitize=True)
        csv_reader.Csv.export(ambiguous_data, ambiguous_file, sanitize=True)
        csv_reader.Csv.export(ignored_data, ignored_file, sanitize=True)


if __name__ == "__main__":
    main()
