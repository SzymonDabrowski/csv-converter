from enum import Enum

class Priority(Enum):
    ESSENTIAL = "Essential"
    HAVE_TO_HAVE = "Have to have"
    NICE_TO_HAVE = "Nice to have"
    SHOULDNT_HAVE = "Shouldn't have"
    DEFAULT = ESSENTIAL