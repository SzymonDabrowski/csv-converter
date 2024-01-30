import unittest
import csv
import csv_reader
import os

# todo: test edge cases:
# - empty file
# - file with only headers (no data rows)
# - invalid csv format (missing quotes, incorrect delimiters)
# - non-utf-8 encoded file
# - export empty data
# - export to an existing file
# - handling different delimiters
# - handling different quote characters
# - exception handling for sniffer (when sniffer fails to determine the csv dialect correctly)

class TestCsvReaderRead(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.expected_data = [
            ["Header1", "Header2", "Header3"],
            ["Value1", "Value2", "Value3"],
            ["Value4", "Value5", "Value6"]
        ]
        cls.test_file_path = 'test_data.csv'
        with open(cls.test_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(cls.expected_data)

    @classmethod
    def tearDownClass(cls):
        # Remove the test file after the tests
        os.remove(cls.test_file_path)

    def test_read_csv_file(self):
        actual_data = csv_reader.Csv.read(self.test_file_path)
        self.assertEqual(actual_data, self.expected_data)
        self.assertIsInstance(actual_data, list)
        self.assertIsInstance(actual_data[0], list)
        self.assertIsInstance(actual_data[0][0], str)

        # Test reading from a non-existing file
        with self.assertRaises(FileNotFoundError):
            csv_reader.Csv.read("non_existing_file")

    def test_get_headers(self):
        headers = csv_reader.Csv.get_column_names(self.test_file_path)
        self.assertEqual(headers, self.expected_data[0])

class TestCsvReaderExport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.expected_data = [
            ["Header1", "Header2", "Header3"],
            ["Value1", "Value2", "Value3"],
            ["Value4", "Value5", "Value6"]
        ]
        cls.test_file_path = 'test_data.csv'

    @classmethod
    def tearDownClass(cls):
        # Remove the test file after the tests
        os.remove(cls.test_file_path)

    def test_write_csv_file(self):
        csv_reader.Csv.export(self.expected_data, self.test_file_path)

        with open(self.test_file_path, 'r+', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data = list(reader)
            self.assertEqual(data, self.expected_data)

if __name__ == '__main__':
    unittest.main()
