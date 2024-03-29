class WrongSignatureError(Exception):
    """
    Custom exception to indicate an incorrect signature in the file.
    """

    def __init__(self, signature):
        super().__init__(f"Incorrect signature: {signature}")
        self.signature = signature
