import unittest
from unittest.mock import patch
import copy
from processors.millennium_processor import MillenniumProcessor

class TestMillenniumProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = [["Numer rachunku/karty","Data transakcji","Data rozliczenia","Rodzaj transakcji","Na konto/Z konta","Odbiorca/Zleceniodawca","Opis","Obciążenia","Uznania","Saldo","Waluta"],
                    ["PL12 3456 7890 1234 5678 9012 3456","2024-01-15","2024-01-15","PŁATNOŚĆ BLIK W INTERNECIE","","www.mobilet.pl ul. Pastelowa 8 60-198 Poznan","some_werid_hash empty PayPro S.A.","-12.00","","662.90","PLN"],
                    ["PL12 3456 7890 1234 5678 9012 3456","2024-01-03","2024-01-03","PŁATNOŚĆ BLIK W INTERNECIE","","jakdojade.pl Grunwaldzka 43/4 Pozna","jakdojade.pl - ZTM Poznań - 45 minu t CITY-NAV SPÓŁKA Z OGRANIC","-6.00","","862.00","PLN"],
                    ["PL12 3456 7890 1234 5678 9012 3456","2023-12-09","2023-12-09","PŁATNOŚĆ BLIK W INTERNECIE","","jakdojade.pl Grunwaldzka 43/4 Pozna","jakdojade.pl - ZTM Poznań - 45 minu t CITY-NAV SPÓŁKA Z OGRANIC","-6.00","","952.17","PLN"],
                    ["PL12 3456 7890 1234 5678 9012 3456","2023-10-26","2023-10-26","ZAKUP - FIZ. UŻYCIE KARTY","","","ERT WYPIEKI SP. Z OO SP.K BISKUPICE  BISKUPIC E POL 2023-10-24","-6.03","","956.07","PLN"],
                    ["1234 XXXX XXXX 0484","2023-11-14","2023-11-16","","","","ERT WYPIEKI SP. Z OO SP.K BISKUPICE     PL , BISKUPICE    , 616","-6.39","","","PLN"]]

        return super().setUpClass()

    def test_remove_column_names_empty_data(self):
        # Arrange
        empty_data = []

        # Act & Assert
        with self.assertRaises(ValueError):
            MillenniumProcessor.remove_column_names(empty_data)

    def test_remove_column_names_removes_column_names(self):
        expected_data = copy.deepcopy(self.data[1:])
        result = MillenniumProcessor.remove_column_names(self.data)
        self.assertEqual(result, expected_data)

    def test_get_categories_empty_data(self):
        data = []
        result = MillenniumProcessor.get_categories(data)
        self.assertEqual(result, [])

    def test_get_categories_repeated_categories(self):
        processor_instance = MillenniumProcessor()

        # Mock the category_columns attribute for the instance
        # In real life this method required preprocessed data (design flaw!)
        # in which category columns are under indexes 2 and 3. However, in raw
        # data, category columns are under indexes 5 and 6.
        with patch.object(type(processor_instance), 'category_columns', new=[5, 6]):
            # Now the processor_instance should use [5, 6] as category_columns
            categories = processor_instance.get_categories(self.data)
            print(categories)
            # Your assertions here based on the expected result
            # For example, you can check if 'categories' contains the expected values

    
    @unittest.skip("Not implemented")
    def test_get_categories_distinct_categories(self):
        # requires already processed data
        # category_columns = [2,3], in raw data [5, 6]
        """
        distinct_categories = [["Numer rachunku/karty","Data transakcji","Data rozliczenia","Rodzaj transakcji","Na konto/Z konta","Odbiorca/Zleceniodawca","Opis","Obciążenia","Uznania","Saldo","Waluta"],
                               ["PL12 3456 7890 1234 5678 9012 3456","2023-12-09","2023-12-09","PŁATNOŚĆ BLIK W INTERNECIE","","jakdojade.pl Grunwaldzka 43/4 Pozna","jakdojade.pl - ZTM Poznań - 45 minu t CITY-NAV SPÓŁKA Z OGRANIC","-6.00","","952.17","PLN"],
                               ["PL12 3456 7890 1234 5678 9012 3456","2023-10-26","2023-10-26","ZAKUP - FIZ. UŻYCIE KARTY","","","ERT WYPIEKI SP. Z OO SP.K BISKUPICE  BISKUPIC E POL 2023-10-24","-6.03","","956.07","PLN"]]
        """
        pass

if __name__ == '__main__':
    unittest.main()
