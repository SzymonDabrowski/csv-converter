from typing import Dict, List, Tuple
import logging
from datetime import datetime
import priority
import pekao_sa_dict
from bank_names import BankName
from category import Category
import processors.bank_processor as processor

class PekaoSaProcessor(processor.BankProcessor):
    name = BankName.PEKAO_SA
    columns = [0, 2, 7, 11]
    date_column = 0
    date_format = "%d.%m.%Y"
    expected_categories = pekao_sa_dict.expected_categories
    category_columns = [3]

    @staticmethod
    def remove_column_names(data: List) -> List:
        """
        Returns a list of data with removed column names. 
        This method assumes that column names are in the first row.

        Args:
            data (List): The input data containing rows of information.

        Raises:
            ValueError: If the input data is empty.
        """
        if not data:
            raise ValueError("Input data is empty.")
        return data[1:]

    @staticmethod
    def filter_and_sort_data(data: List) -> List:
        """
        Filters and sorts the input data based on bank specific columns.

        Args:
            data (List[List[str]]): The input data.
            
        Returns:
            List[List[str]]: The filtered and sorted data.
        """
        filtered_data = [[row[i] for i in PekaoSaProcessor.columns] for row in data]
        filtered_data.sort(key=lambda x: datetime.strptime(x[PekaoSaProcessor.date_column], PekaoSaProcessor.date_format))

        return filtered_data
    
    @staticmethod
    def get_categories(data: List) -> List:
        """
        Returns distinct categories found in the input data.

        Args:
            data (List[List[str]]): The input data.
            
        Returns:
            List[str]: The distinct values from the specified column.
        """
        distinct_values = set(row[PekaoSaProcessor.category_columns[0]].lower() for row in data[1:])  # Exclude header
        return list(distinct_values)
    
    @staticmethod
    def update_categories(real_categories: List, category_groups: Dict):
        """
        Compares real_categories to expected_categories and updates category_groups 
        if real_categories contain records not found in expected_categories.

        Args:
            real_categories (List[str]): The new list of categories.
            expected_set (List[str]): The expected list of categories.
            category_groups (Dict[str, List[str]]): Dictionary representing category groups.
        """
        if set(real_categories) != set(PekaoSaProcessor.expected_categories):
            new_categories = set(real_categories) - set(PekaoSaProcessor.expected_categories)
            if new_categories:
                # Add new categories to the 'Inne' category group by default
                category_groups[Category.OTHERS]['categories'].extend(new_categories)
                logging.info(f'The following new categories were added to the "Inne" category group: {new_categories}')
    
    @staticmethod
    def process(data: List, category_groups: Dict) -> List:
        """
        Processes the input data, taking care of categorisation and prioritisation.
        If record doesn't have its category, default category is assigned. If record
        belongs to category defined in exception list, category is set accordingly.

        Returns output data in form ready to be copy-pasted into pre-prepared
        calculation sheet, like .xlsx. Values are tab separated.

        Args:
            data (List[List[str]]): The input data.
            category_groups (Dict[str, Dict]): Dictionary representing category groups.

        Returns:
            List[List[str]]: The output data with updated priority information.
        """
        exceptions = {
            priority.Priority.SHOULDNT_HAVE: ['żabka', 'zabka', 'mcdonalds']
        }

        output_data = []
        for row in data:
            output_row = [None] * 5
            category = row[3].lower()
            description = row[1].lower()

            # Find the category group based on the category
            matching_category_group = Category.NONE
            for category_group, group_info in category_groups.items():
                if category in group_info['categories']:
                    matching_category_group = category_group
                    break
            
            output_priority = ""
            # Check if any exception is a substring of the description
            exception_found = any(exception in description for exception in exceptions[priority.Priority.SHOULDNT_HAVE])
            if exception_found:
                output_priority = priority.Priority.SHOULDNT_HAVE.value  # Use the string representation
            elif matching_category_group is not Category.NONE:
                # Access the priority information and update it if needed
                priority_enum = category_groups[matching_category_group]['priority'] or priority.Priority.ESSENTIAL
                output_priority = priority_enum.value  # Use the string representation
            else:
                logging.warning(f"Category '{category}' not found in category_groups")
                # Assign default value
                # Use the string representation
                output_priority = priority.Priority.ESSENTIAL.value 

            # data kategoria priorytet wydano opis
            output_row = [row[0], matching_category_group.value, output_priority, row[2], row[1]]
            output_data.append(output_row)

        return output_data
    
    @staticmethod
    def filter_ambiguous_data(data: List) -> Tuple:
        """
        Separates ambiguous data from correct one. Returns a tuple of correct
        data and ambiguous data in that order.

        Args:
            data (List[List[Union[str, int, None]]]): Input data.
        
        Returns:
            Tuple[List, List]: A tuple containing the correct data and ambiguous 
            data in that order.
        """
        ambiguous_data = []
        indices_to_remove = []
        for i, item in enumerate(data):
            if (
                (isinstance(item[3], str) and item[3][0] != '-') or  # Check positive value in 4th column
                (item[1] is None or item[1] == 0) or                 # Check None or 0 in 2nd column
                (item[2] is None)                                    # Check None in 3rd column
            ):
                # If any condition is met, move the item to ambiguous_data
                ambiguous_data.append(item)
                # Add the index to the list of indices to remove
                indices_to_remove.append(i)

        # Remove items from data in reverse order to avoid index issues
        for index in reversed(indices_to_remove):
            data.pop(index)
        
        return (data, ambiguous_data)

    @staticmethod
    def get_category_groups() -> Dict:
        """Returns bank specific category groups"""
        return pekao_sa_dict.category_groups
