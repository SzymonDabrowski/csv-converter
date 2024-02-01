from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

class BankProcessor(ABC):
    @abstractmethod
    def remove_column_names(data: List) -> List:
        """Removes column names from the provided list of data"""

    @abstractmethod
    def filter_and_sort_data(data: List) -> List:
        """Filters and sorts input data"""

    @abstractmethod
    def get_categories(data: List) -> List:
        """Returns distinct categories found in the input data"""

    @abstractmethod
    def update_categories(real_categories: List, category_groups: Dict):
        """
        Compares real_categories to expected_categories and updates category_groups
        if real_categories contain records not found in expected_categories.
        """

    @abstractmethod
    def process(data: List, category_groups: Dict) -> List:
        """
        Processes the input data, taking care of categorisation and prioritisation.
        Returns processed data in form ready to be copy-pasted into pre-prepared
        calculation sheet, like .xlsx.
        """

    @abstractmethod
    def filter_ambiguous_data(data: List) -> Tuple:
        """
        Separates ambiguous data from correct one. Returns a tuple of correct
        data and ambiguous data in that order.
        """

    # pylint: disable=no-method-argument
    @abstractmethod
    def get_category_groups() -> Dict:
        """Returns bank specific category groups"""
