import priority
from category import Category

signature = ['Data księgowania', 'Data waluty', 'Nadawca / Odbiorca', 'Adres nadawcy / odbiorcy', 
             'Rachunek źródłowy', 'Rachunek docelowy', 'Tytułem', 'Kwota operacji', 'Waluta', 
             'Numer referencyjny', 'Typ operacji', 'Kategoria']

expected_categories = ['kosmetyki', 'hotele', 'restauracje i kawiarnie', 'uroda, fryzjer, kosmetyczka', 
                       'premia, nagroda', 'inne', 'artykuły spożywcze', 'zakupy przez internet', 
                       'przelew wewnętrzny', 'czynsz', 'fotografia', 'książki', 'lekarstwa', 'ubrania', 
                       'bez kategorii', 'wynagrodzenie', 'odsetki, zwrot z inwestycji', 
                       'spłata kredytu / pożyczki', 'ogród', 'opłaty bankowe', 'paliwo', 'transport publiczny', 
                       'podatki', 'multimedia', 'spłata karty kredytowej']

category_groups = {
    Category.IGNORED: {'categories' : ['premia, nagroda', 'spłata karty kredytowej', 'czynsz', 'wynagrodzenie',
                                       'spłata kredytu / pożyczki', 'przelew wewnętrzny', 'odsetki, zwrot z inwestycji'],
        'priority' : None},
    Category.FOOD: {'categories' : ['artykuły spożywcze'], 'priority' : priority.Priority.ESSENTIAL},
    Category.HOUSEHOLD_APPLIANCE: {'categories' : [], 'priority' : priority.Priority.ESSENTIAL},
    Category.TRANSPORTATION: {'categories' : ['transport publiczny', 'paliwo'], 'priority' : priority.Priority.HAVE_TO_HAVE},
    Category.HOUSE: {'categories' : [], 'priority' : priority.Priority.HAVE_TO_HAVE},
    Category.HEALTH: {'categories' : ['lekarstwa'], 'priority' : priority.Priority.ESSENTIAL},
    Category.BEAUTY: {'categories' : ['kosmetyki', 'uroda, fryzjer, kosmetyczka'], 'priority' : priority.Priority.HAVE_TO_HAVE},
    Category.SELF_PROGRESS: {'categories' : ['książki'], 'priority' : priority.Priority.NICE_TO_HAVE},
    Category.FUN: {'categories' : ['restauracje i kawiarnie', 'fotografia', 'multimedia'], 'priority' : priority.Priority.NICE_TO_HAVE},
    Category.BILLS: {'categories' : ['opłaty bankowe', 'podatki'], 'priority' : priority.Priority.HAVE_TO_HAVE},
    Category.OTHERS: {'categories' : ['hotele', 'zakupy przez internet', 'inne', 'bez kategorii', 'ogród'], 'priority' : priority.Priority.HAVE_TO_HAVE},
    Category.CLOTHES: {'categories' : ['ubrania'], 'priority' : priority.Priority.HAVE_TO_HAVE},
}