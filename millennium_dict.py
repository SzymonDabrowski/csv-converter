import priority
from category import Category

signature = ['Numer rachunku/karty', 'Data transakcji', 'Data rozliczenia', 
             'Rodzaj transakcji', 'Na konto/Z konta', 'Odbiorca/Zleceniodawca', 
             'Opis', 'Obciążenia', 'Uznania', 'Saldo', 'Waluta']

expected_categories = ['przelew własny', 'przelew natychmiastowy', 'przelew blik', 'przelew na telefon',
                       'przelew krajowy', 'moneyback', 'podatek od odsetek', 'bank millennium sa', 'kapitalizacja ods.',
                       'ert wypieki', 'zabka', 'jmp s.a. biedronka', 'biedronka', 'zagrodnicza caffe', 'patryk piasny',
                       'wesola pani', 'lidl', 'zpm biegun', 'biegun wedliny', 'mcdonalds', 'stokrotka', 'cukiernia', 
                       '1-minute', 'tartaletka', 'phu anna', 'mirabe', 'pepco', 'uber.com', 'uber', 'intercity.pl',
                       'jakdojade.pl', 'bolt.eu', 'freenow', 'koleo.pl', 'koleje wielkopolskie', 'koleo bilety kolejowe',
                       'kasa biletowa kw', 'koleo makes trains gre', 'przewozy regionalne', 'orlen stacja', 'www.mobilet.pl',
                       'avista sp z o o', 'ec*mpay aplikacja', 'ec*zasilenie konta', 'automat spec sp zoo', 'apteka',
                       'stomatolog', 'rentgen', 'syntak spółka', 'rossmann', 'drogeria natura', 'www.madeinlab.pl',
                       'restauracja', 'empik.com', 'empik s.a.', 'google play apps', 'hbo max', 'legimi s.a.', 'tvn s.a.',
                       'lody bosko', 'cacao republica', 'rozlewnia ck wina', 'zdolni spolka zoo', 'the table sp. z o.o.',
                       'boardgamearena', 'chemeli suneli', 'inea sa', 'ebok.enea.pl', 'opłata miesięczna', 'opł. mies.',
                       'opłata za', 'bgk', 'binance.com', 'ccc', 'lpp cropp', 'wizaki', 'salon nipplex']

categories = {
    Category.IGNORED: 
        ['przelew własny',
         'przelew natychmiastowy',
         'przelew blik',
         'przelew na telefon',
         'przelew krajowy',
         'moneyback',
         'podatek od odsetek',
         'bank millennium sa',
         'kapitalizacja ods.'],
    Category.FOOD: 
        ['ert wypieki',
         'zabka',
         'jmp s.a. biedronka',
         'biedronka',
         'zagrodnicza caffe',
         'patryk piasny',
         'wesola pani',
         'lidl',
         'zpm biegun',
         'biegun wedliny',
         'mcdonalds',
         'stokrotka',
         'cukiernia',
         '1-minute',
         'tartaletka',
         'phu anna',
         'mirabe'],
    Category.HOUSEHOLD_APPLIANCE: 
        ['pepco'],
    Category.TRANSPORTATION: 
        ['uber.com',
         'uber',
         'intercity.pl',
         'jakdojade.pl',
         'bolt.eu',
         'freenow',
         'koleo.pl',
         'koleje wielkopolskie',
         'koleo bilety kolejowe',
         'kasa biletowa kw',
         'koleo makes trains gre',
         'przewozy regionalne',
         'orlen stacja',
         'www.mobilet.pl',
         'avista sp z o o',
         'ec*mpay aplikacja',
         'ec*zasilenie konta',
         'automat spec sp zoo'],
    Category.HOUSE: 
        [],
    Category.HEALTH: 
        ['apteka',
         'stomatolog',
         'rentgen',
         'syntak spółka'],
    Category.BEAUTY: 
        ['rossmann',
         'drogeria natura',
         'www.madeinlab.pl'],
    Category.SELF_PROGRESS: 
        [],
    Category.FUN: 
        ['restauracja',
         'empik.com',
         'empik s.a.',
         'google play apps',
         'hbo max',
         'legimi s.a.',
         'tvn s.a.',
         'lody bosko',
         'cacao republica',
         'rozlewnia ck wina',
         'zdolni spolka zoo',
         'the table sp. z o.o.',
         'boardgamearena',
         'chemeli suneli'],
    Category.BILLS: 
        ['inea sa',
         'ebok.enea.pl',
         'opłata miesięczna',
         'opł. mies.',
         'opłata za',
         ],
    Category.OTHERS: 
        ['bgk', 
         'binance.com'],
    Category.CLOTHES: 
        ['ccc',
         'lpp cropp',
         'wizaki', # washing
         'salon nipplex']
}

category_groups = {
    Category.IGNORED: {
        'categories': categories[Category.IGNORED], 
        'priority': None},
    Category.FOOD: {
        'categories': categories[Category.FOOD], 
        'priority': priority.Priority.ESSENTIAL},
    Category.HOUSEHOLD_APPLIANCE: {
        'categories': categories[Category.HOUSEHOLD_APPLIANCE], 
        'priority': priority.Priority.ESSENTIAL},
    Category.TRANSPORTATION: {
        'categories': categories[Category.TRANSPORTATION], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    Category.HOUSE: {
        'categories': categories[Category.HOUSE], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    Category.HEALTH: {
        'categories': categories[Category.HEALTH], 
        'priority': priority.Priority.ESSENTIAL},
    Category.BEAUTY: {
        'categories': categories[Category.BEAUTY], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    Category.SELF_PROGRESS: {
        'categories': categories[Category.SELF_PROGRESS], 
        'priority': priority.Priority.NICE_TO_HAVE},
    Category.FUN: {
        'categories': categories[Category.FUN], 
        'priority': priority.Priority.NICE_TO_HAVE},
    Category.BILLS: {
        'categories': categories[Category.BILLS], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    Category.OTHERS: {
        'categories': categories[Category.OTHERS], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    Category.CLOTHES: {
        'categories': categories[Category.CLOTHES], 
        'priority': priority.Priority.HAVE_TO_HAVE},
}
