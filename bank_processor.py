from abc import ABC, abstractmethod
from typing import List

class BankProcessor(ABC):
    @abstractmethod
    def remove_column_names(data: List) -> List:
        """Removes column names from the provided list of data"""
        pass

    @abstractmethod
    def filter_and_sort_data(data, bank):
        """Filters and sorts input data"""
        pass

    @abstractmethod
    def get_categories(data, bank):
        """Returns distinct categories found in the input data"""
        pass
 
    @abstractmethod
    def update_categories(real_categories, expected_categories, category_groups):
        """
        Compares real_categories to expected_categories and updates category_groups 
        if real_categories contain records not found in expected_categories.
        """
        pass

    @abstractmethod
    def process(data, category_groups):
        """
        Processes the input data, taking care of categorisation and prioritisation.
        Returns processed data in form ready to be copy-pasted into pre-prepared
        calculation sheet, like .xlsx.
        """
        pass

    @abstractmethod
    def filter_ambiguous_data(data, ambiguous_data):
        """
        Separates ambiguous data from correct one. Correct data will be stored
        in 'data', while ambiguous data will be stored in 'ambigous_data'.
        """
        pass