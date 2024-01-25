import logging
import bank_processor

logging.basicConfig(level=logging.INFO)

class Bank:
    def __init__(self, processor: bank_processor.BankProcessor):     
       self.processor = processor

    def process(self, data):
        data_without_column_names = self.processor.remove_column_names(data)
        filtered_and_sorted_data = self.processor.filter_and_sort_data(data_without_column_names)
        categories = self.processor.get_categories(filtered_and_sorted_data)
        category_groups = self.processor.get_category_groups()
        self.processor.update_categories(categories, category_groups)
        return self.processor.process(filtered_and_sorted_data, category_groups)
       
    def filter_ambiguous_data(self, data, ambiguous_data):
        self.processor.filter_ambiguous_data(data, ambiguous_data)
