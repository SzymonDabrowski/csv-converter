import unittest
import importlib
import pkgutil
from processors.bank_processor import BankProcessor

class TestBankProcessorImplementations(unittest.TestCase):
    def test_all_implementations(self):
        module = importlib.import_module('processors')
        implementations = []

        # Iterate through all modules in the 'processors' package
        for _, name, _ in pkgutil.iter_modules(module.__path__):
            # Import the module dynamically
            submodule = importlib.import_module(f'processors.{name}')
            
            # Check if the module has a class that is a subclass of BankProcessor
            for cls_name in dir(submodule):
                cls = getattr(submodule, cls_name)
                if (
                    isinstance(cls, type) and
                    issubclass(cls, BankProcessor) and
                    cls != BankProcessor
                ):
                    implementations.append(cls)

        method_names = ['remove_column_names', 'filter_and_sort_data', 'get_categories',
                        'update_categories', 'process', 'filter_ambiguous_data', 'get_category_groups']

        # Test each implementation
        for implementation in implementations:
            with self.subTest(implementation=implementation):
                for method_name in method_names:
                    self.assertTrue(hasattr(implementation, method_name))
                    self.assertTrue(callable(getattr(implementation, method_name)))

if __name__ == '__main__':
    unittest.main()
