from datetime import datetime
from enum import Enum
from typing import List
import bank_processor
import logging
import priority

logging.basicConfig(level=logging.INFO)

class PekaoSaProcessor(bank_processor.BankProcessor):
    @staticmethod
    def remove_column_names(data):
        """
        Provided column names are in a first row,
        this method returns a list without them.

        Args:
            data (List): The input data containing rows of information.

        Raises:
            ValueError: If the input data is empty.
        """
        if not data:
            raise ValueError("Input data is empty.")
        return data[1:]

    @staticmethod
    def filter_and_sort_data(data, bank):
        """
        Filters and sorts the input data based on the specified columns.

        Args:
            data (List[List[str]]): The input data.
            columns_to_print (List[int]): The indices of columns to retain in the filtered data.
                                        Assumes the date is always in the first column.

        Returns:
            List[List[str]]: The filtered and sorted data.
        """
        filtered_data = [[row[i] for i in bank.columns] for row in data]
        # Sorting the data by the date column
        filtered_data.sort(key=lambda x: datetime.strptime(x[bank.date_column], bank.date_format))

        return filtered_data
    
    @staticmethod
    def get_distinct_values(data, bank):
        """
        Gets distinct values from a specified column in the input data.

        Args:
            data (List[List[str]]): The input data.
            column_index (int): The index of the column to retrieve distinct values from.

        Returns:
            List[str]: The distinct values from the specified column.
        """
        distinct_values = set(row[bank.category_column].lower() for row in data[1:])  # Exclude header
        return list(distinct_values)
    
    @staticmethod
    def compare_sets(new_set, expected_set, category_groups):
        """
        Compares two sets and updates category groups accordingly.

        Args:
            new_set (Set[str]): The new set of categories.
            expected_set (Set[str]): The expected set of categories.
            category_groups (Dict[str, List[str]]): Dictionary representing category groups.
        """
        if set(new_set) != set(expected_set):
            new_categories = set(new_set) - set(expected_set)
            if new_categories:
                # Add new categories to the 'Inne' category group by default
                category_groups['Inne'].extend(new_categories)
                logging.info(f'The following new categories were added to the "Inne" category group: {new_categories}')
    
    @staticmethod
    def check_priority_exceptions(data, category_groups):
        """
        Checks priority exceptions in the input data and updates category groups accordingly.

        Args:
            data (List[List[str]]): The input data.
            category_groups (Dict[str, Dict]): Dictionary representing category groups.

        Returns:
            List[List[str]]: The output data with updated priority information.
        """
        exceptions = {
            priority.Priority.SHOULDNT_HAVE: ['żabka', 'zabka']
        }

        output_data = []
        for row in data:
            output_row = [None] * 5
            category = row[3].lower()
            description = row[1].lower()

            # Find the category group based on the category
            matching_category_group = None
            for category_group, group_info in category_groups.items():
                if category in group_info['categories']:
                    matching_category_group = category_group
                    break
            
            output_priority = None
            # Check if any exception is a substring of the description
            exception_found = any(exception in description for exception in exceptions[priority.Priority.SHOULDNT_HAVE])
            if exception_found:
                output_priority = priority.Priority.SHOULDNT_HAVE.value  # Use the string representation
            elif matching_category_group is not None:
                # Access the priority information and update it if needed
                priority_enum = category_groups[matching_category_group]['priority'] or priority.Priority.ESSENTIAL
                output_priority = priority_enum.value  # Use the string representation
            else:
                logging.warning(f"Category '{category}' not found in category_groups")
                # assign default value
                output_priority = priority.Priority.ESSENTIAL.value  # Use the string representation

            # data kategoria priorytet wydano opis
            output_row = [row[0], matching_category_group, output_priority, row[2], row[1]]
            output_data.append(output_row)

        return output_data
    
    @staticmethod
    def filter_ambiguous_data(data, ambiguous_data):
        """
        Separates ambiguous data from correct one. Correct data is
        stored in the 1st argument, while ambiguous one in the 2nd argument.

        Args:
            data (List[List[Union[str, int, None]]]): Input data.
            ambiguous_data (List[List[Union[str, int, None]]]): List to store ambiguous data.
        """

        # Create a list to store indices of items to be removed
        indices_to_remove = []

        # Iterate over the data
        for i, item in enumerate(data):
            # Check conditions for ambiguous data
            if (
                (isinstance(item[3], str) and item[3][0] != '-') or  # Check positive value in 4th column
                (item[1] is None or item[1] == 0) or                # Check None or 0 in 2nd column
                (item[2] is None)                                   # Check None in 3rd column
            ):
                # If any condition is met, move the item to ambiguous_data
                ambiguous_data.append(item)
                # Add the index to the list of indices to remove
                indices_to_remove.append(i)

        # Remove items from data in reverse order to avoid index issues
        for index in reversed(indices_to_remove):
            data.pop(index)

    @staticmethod
    def define_category_groups():
        return {
            0: {'categories' : ['premia, nagroda', 'spłata karty kredytowej', 'czynsz', 'wynagrodzenie', 'spłata kredytu / pożyczki', 'przelew wewnętrzny', 'odsetki, zwrot z inwestycji'],
                'priority' : None},
            'Jedzenie': {'categories' : ['artykuły spożywcze'], 'priority' : priority.Priority.ESSENTIAL},
            'AGD': {'categories' : [], 'priority' : priority.Priority.ESSENTIAL},
            'Transport': {'categories' : ['transport publiczny', 'paliwo'], 'priority' : priority.Priority.HAVE_TO_HAVE},
            'Mieszkanie': {'categories' : [], 'priority' : priority.Priority.HAVE_TO_HAVE},
            'Zdrowie': {'categories' : ['lekarstwa'], 'priority' : priority.Priority.ESSENTIAL},
            'Uroda': {'categories' : ['kosmetyki', 'uroda, fryzjer, kosmetyczka'], 'priority' : priority.Priority.HAVE_TO_HAVE},
            'Samorozwój': {'categories' : ['książki'], 'priority' : priority.Priority.NICE_TO_HAVE},
            'Rozrywka': {'categories' : ['restauracje i kawiarnie', 'fotografia', 'multimedia'], 'priority' : priority.Priority.NICE_TO_HAVE},
            'Rachunki': {'categories' : ['opłaty bankowe', 'podatki'], 'priority' : priority.Priority.HAVE_TO_HAVE},
            'Inne': {'categories' : ['hotele', 'zakupy przez internet', 'inne', 'bez kategorii', 'ogród'], 'priority' : priority.Priority.HAVE_TO_HAVE},
            'Odzież': {'categories' : ['ubrania'], 'priority' : priority.Priority.HAVE_TO_HAVE},
        }

class MillenniumProcessor(bank_processor.BankProcessor):
    @staticmethod
    def remove_column_names(data):
        pass

    @staticmethod
    def filter_and_sort_data(data, bank):
        pass

    @staticmethod
    def get_distinct_values(data, bank):
        print('Not implemented: get_distinct_values')

    @staticmethod
    def compare_sets(new_set, expected_set, category_groups):
        print('Not implemented: compare_sets')

    @staticmethod
    def check_priority_exceptions(data, category_groups):
        print("Not implemented: check_priority_exceptions")

    @staticmethod
    def filter_ambiguous_data(data, ambiguous_data):
        print("Not implemented: filter_ambiguous_data")

    @staticmethod
    def define_category_groups():
        pass

class Bank:
    class Name(Enum):
        MILLENNIUM = "Millennium"
        PEKAO_SA = "Pekao SA"
        UNKNOWN = "Unknown"

    name = Name.UNKNOWN
    columns = []
    date_column = 0
    date_format = "%d.%m.%Y"
    category_column = 3 # todo
    expected_categories = []

    def __init__(self, signature: List[str]):     
        if (self.pekao_sa_signature == signature):
            self.name = Bank.Name.PEKAO_SA
            self.columns = [0, 2, 7, 11]
            self.date_format = "%d.%m.%Y"
            self.processor = PekaoSaProcessor()
            self.expected_categories = self.pekao_sa_expected_categories
        elif (self.millennium_signature == signature):
            self.name = Bank.Name.MILLENNIUM
            # use 3, 5, 6 to determine desciption/recipient and category
            # use 7,8 to determine amount of money
            self.columns = [1, 3, 5, 6, 7, 8]    
            self.date_format = "%Y-%m-%d"
            self.processor = MillenniumProcessor()
            self.expected_categories = self.millennium_expected_categories

    pekao_sa_signature = ['Data księgowania', 'Data waluty', 'Nadawca / Odbiorca', 'Adres nadawcy / odbiorcy', 
                          'Rachunek źródłowy', 'Rachunek docelowy', 'Tytułem', 'Kwota operacji', 'Waluta', 
                          'Numer referencyjny', 'Typ operacji', 'Kategoria']
    millennium_signature = ['Numer rachunku/karty', 'Data transakcji', 'Data rozliczenia', 
                            'Rodzaj transakcji', 'Na konto/Z konta', 'Odbiorca/Zleceniodawca', 
                            'Opis', 'Obciążenia', 'Uznania', 'Saldo', 'Waluta']

    pekao_sa_expected_categories = ['kosmetyki', 'hotele', 'restauracje i kawiarnie', 'uroda, fryzjer, kosmetyczka', 
                               'premia, nagroda', 'inne', 'artykuły spożywcze', 'zakupy przez internet', 
                               'przelew wewnętrzny', 'czynsz', 'fotografia', 'książki', 'lekarstwa', 'ubrania', 
                               'bez kategorii', 'wynagrodzenie', 'odsetki, zwrot z inwestycji', 
                               'spłata kredytu / pożyczki', 'ogród', 'opłaty bankowe', 'paliwo', 'transport publiczny', 
                               'podatki', 'multimedia', 'spłata karty kredytowej']
    
    millennium_expected_categories = []