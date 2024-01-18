import csv
import chardet
from typing import List

class Csv:
    @staticmethod
    def read(filename: str) -> List[List[str]]:
        encoding = 'utf-8'
        with open(filename, 'rb') as raw_file:
            encoding = chardet.detect(raw_file.read(1024))['encoding']

        with open(filename, 'r', newline='', encoding=encoding) as file:
            dialect = csv.Sniffer().sniff(file.read(4096)) # throws
            file.seek(0)
            reader = csv.reader(file, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
            data = list(reader)
        return data
    
    @staticmethod
    def export(data: List[List[str]], filename: str) -> None:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                writer.writerow(row)

    @staticmethod
    def get_column_names(filename: str):
        encoding = 'utf-8'
        with open(filename, 'rb') as raw_file:
            encoding = chardet.detect(raw_file.read(1024))['encoding']

        with open(filename, 'r', newline='', encoding=encoding) as file:
            dialect = csv.Sniffer().sniff(file.read(4096)) # throws
            file.seek(0)
            reader = csv.reader(file, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
            data = list(reader)
        return data[0]