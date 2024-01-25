import priority

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
    0: ['przelew własny',
        'przelew natychmiastowy',
        'przelew blik',
        'przelew na telefon',
        'przelew krajowy',
        'moneyback',
        'podatek od odsetek',
        'bank millennium sa',
        'kapitalizacja ods.'],
    'Jedzenie': ['ert wypieki',
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
    'AGD': ['pepco'],
    'Transport': ['uber.com',
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
    'Mieszkanie': [],
    'Zdrowie': ['apteka',
                 'stomatolog',
                 'rentgen',
                 'syntak spółka'],
    'Uroda': ['rossmann',
               'drogeria natura',
               'www.madeinlab.pl'],
    'Samorozwój': [],
    'Rozrywka': ['restauracja',
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
    'Rachunki': ['inea sa',
                  'ebok.enea.pl',
                  'opłata miesięczna',
                  'opł. mies.',
                  'opłata za',
                  ],
    'Inne': ['bgk', 'binance.com'],
    'Odzież': ['ccc',
                'lpp cropp',
                'wizaki', # washing
                'salon nipplex']
}

category_groups = {
    0: {
        'categories': categories[0], 
        'priority': None},
    'Jedzenie': {
        'categories': categories['Jedzenie'], 
        'priority': priority.Priority.ESSENTIAL},
    'AGD': {
        'categories': categories['AGD'], 
        'priority': priority.Priority.ESSENTIAL},
    'Transport': {
        'categories': categories['Transport'], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    'Mieszkanie': {
        'categories': categories['Mieszkanie'], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    'Zdrowie': {
        'categories': categories['Zdrowie'], 
        'priority': priority.Priority.ESSENTIAL},
    'Uroda': {
        'categories': categories['Uroda'], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    'Samorozwój': {
        'categories': categories['Samorozwój'], 
        'priority': priority.Priority.NICE_TO_HAVE},
    'Rozrywka': {
        'categories': categories['Rozrywka'], 
        'priority': priority.Priority.NICE_TO_HAVE},
    'Rachunki': {
        'categories': categories['Rachunki'], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    'Inne': {
        'categories': categories['Inne'], 
        'priority': priority.Priority.HAVE_TO_HAVE},
    'Odzież': {
        'categories': categories['Odzież'], 
        'priority': priority.Priority.HAVE_TO_HAVE},
}
