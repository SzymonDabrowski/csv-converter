from typing import List

class Sanitizer:
    @staticmethod
    def sanitize_data(data: List[List[str]]) -> List[List[str]]:
        """
        Replace multiple whitespaces with a single space.
        Remove leading and trailing whitespaces from strings in the input data.

        Args:
            data (List[List[str]]): The input data.

        Returns:
            List[List[str]]: The sanitized data.
        """
        sanitize = lambda el: ' '.join(el.split()) if isinstance(el, str) else el
        return [[sanitize(element) for element in row] for row in data]