from abc import ABC, abstractmethod

class BankProcessor(ABC):
    @abstractmethod
    def remove_column_names(data):
        pass

    @abstractmethod
    def filter_and_sort_data(data, bank):
        pass

    @abstractmethod
    def get_distinct_values(data, bank):
        pass
 
    @abstractmethod
    def compare_sets(new_set, expected_set, category_groups):
        pass

    @abstractmethod
    def check_priority_exceptions(data, category_groups):
        pass

    @abstractmethod
    def filter_ambiguous_data(data, ambiguous_data):
        pass