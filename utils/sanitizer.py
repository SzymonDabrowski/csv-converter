from typing import List

class Sanitizer:
    @staticmethod
    def sanitize_data(data: List) -> List:
        """
        Replace multiple whitespaces with a single space.
        Remove leading and trailing whitespaces from strings in the input data.

        Args:
            data (List): The input data.

        Returns:
            List: The sanitized data.
        """

        # NOTE: This code has been written for fun. It could have been separated
        # into two specialized methods with proper docstrings and clear names, e.g.
        # sanitize_row and sanitize_rows or similar to that:
        # 
        # sanitize = lambda el: ' '.join(el.split()) if isinstance(el, str) else el
        #
        # def sanitize_row(List[str]) -> List[str]:
        #     return [sanitize(element) for element in data]
        #
        # def sanitize_rows(List[List[List[str]]]) -> List[List[str]]:
        #     return [[sanitize(element) for element in row] for row in data]
        #
        # Or even just sanitize_rows, should be tested to check performance.
        # But I wanted recursion :)

        sanitize = lambda el: ' '.join(el.split()) if isinstance(el, str) else el
        
        # Go through each layer of lists. 
        # When current element is not a list, sanitize it
        get_elements = lambda d: [get_elements(el) if isinstance(el, list) else sanitize(el) for el in d]

        
        return get_elements(data)
