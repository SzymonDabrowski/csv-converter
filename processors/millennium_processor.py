from typing import Dict, List, Tuple
import logging
from datetime import datetime
import priority
import millennium_dict
from bank_names import BankName
from category import Category
import processors.bank_processor as processor


class MillenniumProcessor(processor.BankProcessor):
    name = BankName.MILLENNIUM
    # use 3, 5, 6 to determine desciption/recipient and category
    # use 7,8 to determine amount of money
    columns = [1, 3, 5, 6, 7, 8]
    date_column = 0
    date_format = "%Y-%m-%d"
    expected_categories = millennium_dict.expected_categories
    category_columns = [2, 3]

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
        filtered_data = [[row[i] for i in MillenniumProcessor.columns] for row in data]
        filtered_data.sort(
            key=lambda x: datetime.strptime(
                x[MillenniumProcessor.date_column], MillenniumProcessor.date_format
            )
        )

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

        # for column in bank.category_columns:
        #     distinct_values = distinct_values.union(set(row[column].lower() for row in data[1:]))
        #
        # append both columns to avoid false results in update_categories
        distinct_values = set()
        distinct_values = distinct_values.union(
            set(
                MillenniumProcessor.append(row, MillenniumProcessor.category_columns)
                for row in data[1:]
            )
        )
        return list(distinct_values)

    @staticmethod
    def append(row: List, columns: List) -> List:
        """
        Appends values found in columns of input row to colums[0]
        and removes remaining columns[1:] after appending.
        """
        # appending with ", " return different result.
        # such a result has some strings that should have
        # been filtered away by update_categories()
        result = ""
        for column in columns:
            result = result + " " + row[column].lower()
        return result

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

        for expected_value in MillenniumProcessor.expected_categories:
            categories_copy = real_categories.copy()
            for actual_value in categories_copy:
                if expected_value in actual_value:
                    real_categories.remove(actual_value)

        # Perhaps these values should not be added as categories?
        if real_categories:
            category_groups[Category.OTHERS]["categories"].extend(real_categories)
            logging.info(
                f'The following new categories were added to the "Inne" category group: {real_categories}'
            )

    @staticmethod
    def prepare_data(data: List):
        """
        WARNING: This method mutates original object.
        Merges columns responsible for categorisation and removes
        redundant column afterwards.
        """
        for item in data:
            item[2] = item[2] + " " + item[3]
            del item[3]

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
        exceptions = {priority.Priority.SHOULDNT_HAVE: ["żabka", "zabka", "mcdonalds"]}

        # merge columns with categories
        MillenniumProcessor.prepare_data(data)

        output_data = []
        for row in data:
            output_row = [None] * 5
            category = row[2].lower()  # 2 and 3 are merged now
            description = row[2].lower()  # 1 is not descriptive, 2 and 3 are

            matching_category_group = MillenniumProcessor.get_category_group(
                row, category, category_groups.items()
            )

            output_priority = ""
            # Check if any exception is a substring of the description
            exception_found = any(
                exception in description
                for exception in exceptions[priority.Priority.SHOULDNT_HAVE]
            )

            if exception_found:
                output_priority = (
                    priority.Priority.SHOULDNT_HAVE.value
                )  # Use the string representation
            elif matching_category_group is Category.NONE:
                logging.warning(
                    f"Category '{category}' not found in millennium category_groups"
                )
                # assign default value
                output_priority = (
                    priority.Priority.ESSENTIAL.value
                )  # Use the string representation
            elif matching_category_group is Category.IGNORED:
                output_priority = "="
            else:
                # Access the priority information and update it if needed
                priority_enum = (
                    category_groups[matching_category_group]["priority"]
                    or priority.Priority.ESSENTIAL
                )
                output_priority = priority_enum.value  # Use the string representation

            # data kategoria priorytet wydano opis
            # FIXME: positive/negative values, see line 174
            money = 0.0
            if row[3]:
                money = float(row[3])
            elif row[4]:
                money = float(row[4])

            money = -1 * money
            money = str(money).replace(".", ",")

            output_row = [
                row[0],
                matching_category_group.value,
                output_priority,
                money,
                row[1],
            ]
            output_data.append(output_row)

        return output_data

    @staticmethod
    def get_category_group(row, category, category_group_items):
        # Find the category group based on the category
        matching_category_group = Category.NONE
        found = False
        for category_group, group_info in category_group_items:
            if found is True:
                found = False
                break

            # category is a whole long string
            # search for a substring of
            # group_info['categories'] in it
            for val in group_info["categories"]:
                if val in category:
                    # description should be changed, e.g. when string like:
                    # jmp s.a. biedronka 101, poznan, ul... is found, replace it with:
                    # a value from category_groups['categories'], i.e. jmp s.a. biedronka
                    row[1] = val
                    matching_category_group = category_group
                    found = True
        return matching_category_group

    @staticmethod
    def group_output_data(data: List) -> Tuple:
        """
        Separates ambiguous and ignored data from correct one. Returns a tuple of correct,
        ambiguous and ignored data in that order.

        Args:
            data (List[List[Union[str, int, None]]]): Input data.

        Returns:
            Tuple[List, List]: A tuple containing the correct data and ambiguous
            data in that order.
        """
        # TODO: Category.IGNORED
        ambiguous_data = []
        ignored_data = []
        indices_to_remove = []
        for i, item in enumerate(data):
            if item[1] == Category.IGNORED.value:
                ignored_data.append(item)
                indices_to_remove.append(i)
            elif (  # Check for ambiguities
                (isinstance(item[3], str) and item[3] and item[3][0] == "-")
                or (  # Check negative (income) value in 4th column
                    item[1] is None or item[1] == 0
                )
                or (  # Check None or 0 in 2nd column
                    item[2] is None
                )  # Check None in 3rd column
            ):
                ambiguous_data.append(item)
                indices_to_remove.append(i)

        # Remove items from data in reverse order to avoid index issues
        for index in reversed(indices_to_remove):
            data.pop(index)

        return (data, ambiguous_data, ignored_data)

    @staticmethod
    def get_category_groups() -> Dict:
        """Returns bank specific category groups"""
        return millennium_dict.category_groups
