import copy
import logging
from typing import List, Tuple
from processors.bank_processor import BankProcessor

logging.basicConfig(level=logging.INFO)


class Bank:
    def __init__(self, processor: BankProcessor):
        self.processor = processor

    def process(self, data: List):
        """
        Process the input bank data for categorization and prioritization.

        Args:
            data (List[List[str]]): Raw bank transaction data.

        Returns:
            List[List[str]]: Processed data ready for further use, with categorized
            and prioritized information.

        This method orchestrates the processing workflow, including the removal of
        column names, filtering, sorting, category extraction, and updating
        category information. The final processed data is then returned.
        """
        input_data = copy.deepcopy(data)

        data_without_column_names = self.processor.remove_column_names(input_data)
        filtered_and_sorted_data = self.processor.filter_and_sort_data(
            data_without_column_names
        )
        categories = self.processor.get_categories(filtered_and_sorted_data)
        category_groups = self.processor.get_category_groups()
        self.processor.update_categories(categories, category_groups)

        return self.processor.process(filtered_and_sorted_data, category_groups)

    def filter_ambiguous_data(self, data: List) -> Tuple:
        """
        Filter and separate ambiguous data from processed bank transactions.

        Args:
            data (List[List[str]]): Processed bank transaction data.

        This method takes the processed bank transaction data and separates items
        with ambiguous or incomplete information, moving them to the specified
        `ambiguous_data` list. It should be called after the `process` method to
        handle any data that couldn't be definitively categorized or prioritized.
        """
        input_data = copy.deepcopy(data)
        return self.processor.filter_ambiguous_data(input_data)
