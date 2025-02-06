from enum import Enum


class Category(Enum):
    FOOD = "Jedzenie"
    HOUSEHOLD_APPLIANCE = "AGD"
    TRANSPORTATION = "Transport"
    HOUSE = "Mieszkanie"
    HEALTH = "Zdrowie"
    BEAUTY = "Uroda"
    SELF_PROGRESS = "Samorozwój"
    FUN = "Rozrywka"
    BILLS = "Rachunki"
    OTHERS = "Inne"
    CLOTHES = "Odzież"
    DOG = "Pies"
    IGNORED = -1
    NONE = 0
