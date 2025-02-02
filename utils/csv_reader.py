import csv
from typing import List
import chardet
from utils import sanitizer


class Csv:
    @staticmethod
    def read(filename: str, sanitize: bool = False) -> List[List[str]]:
        encoding = "utf-8"
        with open(filename, "rb") as raw_file:
            encoding = chardet.detect(raw_file.read(1024))["encoding"]

        with open(filename, "r", newline="", encoding=encoding) as file:
            raw_data = file.read()
            # Remove single quotes from the data
            # Pekao SA files contain some single quotes
            # due to this fact this reader reads less fields
            # than there are columns
            cleaned_data = raw_data.replace("'", "")

            # Use csv.Sniffer to detect the dialect from the cleaned data
            sample = cleaned_data[:4096]
            try:
                dialect = csv.Sniffer().sniff(sample)
            except csv.Error:
                dialect = csv.get_dialect("excel")  # Default dialect

            reader = csv.reader(
                cleaned_data.splitlines(),
                delimiter=dialect.delimiter,
                quotechar=dialect.quotechar,
            )
            data = list(reader)
            return sanitizer.Sanitizer.sanitize_data(data) if sanitize else data

    @staticmethod
    def export(data: List[List[str]], filename: str, sanitize: bool = False) -> None:
        # About 10% faster execution than sanitizng each row separately
        # when calling writer.writerow(), while using recursive
        # implementation of sanitize_data
        if sanitize:
            data = sanitizer.Sanitizer.sanitize_data(data)

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(
                file, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            for row in data:
                writer.writerow(row)

    @staticmethod
    def get_column_names(filename: str):
        encoding = "utf-8"
        with open(filename, "rb") as raw_file:
            encoding = chardet.detect(raw_file.read(1024))["encoding"]

        with open(filename, "r", newline="", encoding=encoding) as file:
            dialect = csv.Sniffer().sniff(file.read(4096))  # throws
            file.seek(0)
            reader = csv.reader(
                file, delimiter=dialect.delimiter, quotechar=dialect.quotechar
            )
            data = next(reader)
        return data
