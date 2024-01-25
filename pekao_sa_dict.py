import priority

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
    0: {'categories' : ['premia, nagroda', 'spłata karty kredytowej', 'czynsz', 'wynagrodzenie', 'spłata kredytu / pożyczki', 'przelew wewnętrzny', 'odsetki, zwrot z inwestycji'],
        'priority' : None},
    'Jedzenie': {'categories' : ['artykuły spożywcze'], 'priority' : priority.Priority.ESSENTIAL},
    'AGD': {'categories' : [], 'priority' : priority.Priority.ESSENTIAL},
    'Transport': {'categories' : ['transport publiczny', 'paliwo'], 'priority' : priority.Priority.HAVE_TO_HAVE},
    'Mieszkanie': {'categories' : [], 'priority' : priority.Priority.HAVE_TO_HAVE},
    'Zdrowie': {'categories' : ['lekarstwa'], 'priority' : priority.Priority.ESSENTIAL},
    'Uroda': {'categories' : ['kosmetyki', 'uroda, fryzjer, kosmetyczka'], 'priority' : priority.Priority.HAVE_TO_HAVE},
    'Samorozwój': {'categories' : ['książki'], 'priority' : priority.Priority.NICE_TO_HAVE},
    'Rozrywka': {'categories' : ['restauracje i kawiarnie', 'fotografia', 'multimedia'], 'priority' : priority.Priority.NICE_TO_HAVE},
    'Rachunki': {'categories' : ['opłaty bankowe', 'podatki'], 'priority' : priority.Priority.HAVE_TO_HAVE},
    'Inne': {'categories' : ['hotele', 'zakupy przez internet', 'inne', 'bez kategorii', 'ogród'], 'priority' : priority.Priority.HAVE_TO_HAVE},
    'Odzież': {'categories' : ['ubrania'], 'priority' : priority.Priority.HAVE_TO_HAVE},
}