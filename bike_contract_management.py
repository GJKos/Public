''''
Gert-Jan Kos
Make IT Work
student no.500302317

Dit programma managed de verhuurcontracten van Go Dutch Bike Rental.
'''


# Een list met klantgegevens
klantenlijst = [[121,'Bart','Janssen','Schoolstraat 24', '3436AB', 'Driebergen'],
                [99,'Frank','Oberndorff','plein 1','1111aa','Nijmegen']]

# Een list met fietsgegevens (fietstype, typenaam, model, elektrisch, huurprijs_per_dag)
fiets_type = [ [1,'Randstad Racer D','Dames','Ja',45],
                 [2,'Randstad Racer H','Heren','Ja',45 ],
                 [7,'Grachten Caddy','Bakfiets','Nee',65]]

# lijst met de fysieke fietsen die ter beschikking staan voor de verhuur
vloot_fiets = [ [1,'Batavus','01-01-2023', 1], [2, 'Gazelle','01-01-2023]',2], [3, 'Gazelle','01-01-2023', 7]]

# Een list met vestigingsgegevens (vestigingsnaam, adres, postcode, plaats)
vestigingenlijst = [ ['WTC', 'Strawinskylaan 1', '1077XW','Amsterdam'],
                     ['NDSM', 'NDSM-Plein 28', '1033 WB', 'Amsterdam']]

# Een list met contracten
# De contractenlijst bevat het nummer van het contract, de vestigingsnaam, het klantnummer, de startdatum,
# de einddatum en de list van gehuurde fietsen, hieronder te lezen als [1, 2, 3]
contractenlijst = [[1202, '01-01-2023', 'WTC', 121, '15-01-2023', '18-01-2023', [ 1, 2, 3]]]



from datetime import datetime
import mysql.connector



def maak_nieuw_no(lijst):
    # deze functie genereert een nieuw nummer dat het hoogste nummer (index) is + 1
    # de inputparameter is de lijst waarvoor een nieuw indexnummer moet worden gegenereerd
    # output is het nieuwe nummer

    lijst.sort()
    nieuw_nummer = lijst[-1][0] + 1

    return nieuw_nummer


def vastleggen_klant():
    # deze functie wordt gebruikt om een nieuwe klant aan te maken
    # er is geen inputparameter
    # output is een lijst met nieuwe klant gegevens die een nieuwe regel in het bestand vormen

    nieuwe_klant = []
    klantnummer = (maak_nieuw_no(klantenlijst))
    voornaam = input('Wat is de voornaam: ')
    achternaam = input('Wat is de achternaam: ')
    adres = input('Wat is het adres: ')
    postcode = input ('Wat is de postcode: ')
    woonplaats = input('Wat is de woonplaats: ')

    nieuwe_klant = [klantnummer, voornaam, achternaam,adres, postcode, woonplaats]

    return nieuwe_klant


def wijzigen_klantenlijst(klantnummer, list_klant):
    # deze functie wordt gebruikt om de te wijzigen gegevens op te nemen in het klantenbestand
    # de inputparameter is het klantnummer dat gewijzigd dient te worden en de klantlijst
    # de output is de gewijzigde klantenlijst

    for kl in klantenlijst:
        if kl[0] == klantnummer:
            te_wijzigen_klant = kl                              # de variable krijgt de hele lijst als waarde
    gewijzigde_klant = wijzigen_klant(te_wijzigen_klant)

    for k in range(len(list_klant)):
        if list_klant[k][0] == klantnummer:
            list_klant[k] = gewijzigde_klant

    return list_klant


def wijzigen_klant(klant):
    # deze functie registreert de gegevens die je voor een klant wilt wijzigen
    # de inputparameter is het klantnummer dat gewijzigd dient te worden
    # de output is een lijst met de nieuwe gegevens voor het klantnummer

    voornaam = input('Wat is de juiste voornaam: ')
    klant[1] = voornaam
    achternaam = input('Wat is de juiste achternaam: ')
    klant[2] = achternaam
    adres = input("Wat is het juiste adres: ")
    klant[3] = adres
    postcode = input("Wat is de juiste postcode: ")
    klant[4] = postcode
    plaats = input("Wat is de juiste woonplaats: ")
    klant[5] = plaats

    return klant


def verwijderen_klant(klantnummer_verwijderen, list_klanten):
    # met deze functie kun je klanten verwijderen uit het klantenbestand
    # de inputparameter is het klantnummer dat verwijderd wordt en de klantenlijkst
    # output is de gewijzigde klantenlijst

    for kl in klantenlijst:
        if kl[0] == klantnummer_verwijderen:
            list_klanten.remove(kl)
            print(klantenlijst)

    return list_klanten


def vastleggen_contract():
    # deze functie wordt aangeroepen om een nieuw contract vast te leggen
    # er zijn geen inputparameters van de functie zelf
    # output is lijst die een complete regel vormt in de contractenlijst

    ctr_fiets = []
    contract_no = maak_nieuw_no(contractenlijst)
    ctr_datum = get_date_today()
    locatie = input("Wat is de locatie: ")
    klantnummer = input("wat is het klantnummer: ")
    start_datum = input("Welke datum gaat het contract in: ")
    eind_datum = input("welke datum eindigt het contract: ")
    verhuurde_fietsen = list_verhuurde_fietsen() #contract_no

    ctr_fiets = [contract_no, ctr_datum, locatie, klantnummer, start_datum, eind_datum, verhuurde_fietsen]

    return ctr_fiets


def get_date_today():
    # kleine functie die binnen een contract de huidige datum genereert
    # output is de datum in een string format

    present = datetime.now()
    date = present.date()
    return str(date)


def list_verhuurde_fietsen():
    # deze functie is een subfunctie voor het aanmaken van het contract
    # output is een lijst met verhuurde fietsen

    verhuurde_fietsen = []
    while True:
        fiets = int(input("Welke fietsnummer (niet type) wordt gehuurd: "))
        verhuurde_fietsen.append(fiets)
        if input("Wil de klant nog een fiets huren (antwoord ja of nee:") == "ja":
            continue
        else:
            break

    return verhuurde_fietsen


def printen_contract(contract):
    # deze functie print een bestaand contract in een layout die aan een klant kan worden meegegeven
    # de inputparameter is het contractnummer dat de gebruiket wil printen.

    print('\n')

    # Onderstaand blok print de header van het contract met de naw gegevens van de klant, de vestiging en data

    for ctr in contractenlijst:                                                         # 'opent' de contractenlijst en loopt langs elke rij
        if ctr[0] == contract:                                                          # gaat de if statement in als de parameter gelijk is aan de index
            print(f"Contractnr: {ctr[0]:<15} Datum: {ctr[1]:<25} Vestiging: {ctr[2]}")
            for klant in klantenlijst:                                                  # 'opent' de klantenlijst en loopt langs elke rij
                if ctr[3] == klant[0]:                                                  # gaat de if statement in als de index vd klantenlijst overeenkomt met de klant van het contract
                    for vestiging in vestigingenlijst:                                  # 'opent' de vestigingenlijst en loopt langs elke rij
                        if vestiging[0] == ctr[2]:                                      # gaat de if statement in als de index vd vestigingenlijst overeenkomt met de vestiging van het contract
                            print(f"{vestiging[1]:>70}")
                            print(f"Klant: {klant[2]}, {klant[1]} (klantno.{klant[0]}) {vestiging[2]:>30} {vestiging[3]}")
                            print(f"Adres: {klant[3]}")
                            print(f"{klant[4]} {klant[5]}")

                            print('\n')

    print (f'Startdatum: {ctr[4]: >12}')
    start_datum = datetime.strptime(ctr[4], "%d-%m-%Y")
    eind_datum = datetime.strptime(ctr[5], '%d-%m-%Y')

    duur = eind_datum - start_datum
    print (f'Inleverdatum: {ctr[5]: >10}  aantal dagen: {duur.days}')

    print('\n')


    # onderstaand blok print de gegevens over de gehuurde fietsen en de kosten per dag

    fiets = 'Fietsnr'
    Type = 'Type'
    Model = 'Model'
    Elektrisch = "Elektrisch"
    Prijs = 'Prijs per dag'

    print(f'{fiets:<20} {Type:<25} {Model:<9}{Elektrisch:<12}{Prijs:>15}')

    dag_totaal = 0

    for fiets_verhuurd in ctr[6]:                                   # loop die de regels uit de geneste lijst met fietsen leest
        for nummer in vloot_fiets:                                  # loop die de lijst vloot_fiets 'opent'
            if fiets_verhuurd == nummer[0]:                         # if statement die de verhuurde fiets vergelijkt met de index van de vloot_fiets lijst
                for type in fiets_type:                             # loopt die de lijst fiets_type 'opent'
                    if nummer[3] == type[0]:                        # het type dat bij de fysieke fiets genoteerd is, wordt vergeleken met de index van fiets_type
                        print(f'{fiets_verhuurd} ({type[1]}) {type[0]} ({type[1]:<10})'
                              f'{type[2]:>10}{type[3]:>10}{type[4]:>20}')
                        dag_totaal = dag_totaal + type[4]

    print('\n')

    print (f"\t\t\t\t\t\t\t\tTotaal \t\t {dag_totaal}")

    print('\n')


    # dit laatste blok print de totale kosten van het contract

    dagen = 'Aantal dagen'
    totaal_bedrag_tekst = 'Totaalbedrag'
    totaal_bedrag = dag_totaal * duur.days

    print(f'{dagen:>20} {Prijs:>20} {totaal_bedrag_tekst:>20}')
    print(f'{duur.days:>20} {dag_totaal:>20} {totaal_bedrag:>20}')


def vastleggen_nieuwe_fiets():
    # deze functie registreert een nieuw fiets aankoop
    # de functie heeft geen parameter als input; input wordt gegenereerd met input statements
    # de output is een list die toegevoegd wordt aan het fietsenbestand

    nieuwe_fiets = []
    no = maak_nieuw_no(vloot_fiets)
    merk = input("Wat is het merk: ")
    type = int(input("Wat is het fietstype: "))
    aankoop_datum = str(input("Wat is de aankoopdatum van de fiets: "))

    nieuwe_fiets = [no, merk, aankoop_datum, type]

    return nieuwe_fiets


def printen_lijsten(*lijsten):
    # dit is een generieke functie voor het printen van lijsten
    # de input parameter is een tuple met de lijst of de lijsten die geprint dienen te worden
    # output is het gevraagde overzicht

    for lijst in lijsten:
        for item in lijst:
            for elk_item in item:
                if type(elk_item) == list:
                    for i in range (0,((len(elk_item)))):
                        print('{:<3}'.format(elk_item[i]), end='   ')
                else:
                    print('{:<20}'.format(elk_item), end='   ')
            print()
        print('\n')


def toon_menu():
    # deze functie print het keuzemenu waarmee de gebruiker bepaalt wat hij gaat doen

    print('\n'*10)
    print('+---------------------------+')
    print('|                           |')
    print('|   1 vastleggen klant      |')
    print('|   2 wijzigen klant        |')
    print('|   3 verwijderen klant     |')
    print('|                           |')
    print('|   4 maak nieuw contract   |')
    print('|   5 print contract        |')
    print('|                           |')
    print('|   6 fiets toevoegen       |')
    print('|   7 fiets type toevoegen  |')
    print('|                           |')      # de fietsenlijst is opgedeeld in een lijst vloot_fiets en
    print('|   8 sql connector         |')      # een lijst fiets_type zodat de code overeenkomt met het RM en
    print('|                           |')      # de tabellen
    print('|   9 print alle lijsten    |')      # de code voor de menukeuze "fiets type toevoegen" moet nog
    print('|                           |')      # worden geschreven
    print('|      "stop" = stoppen     |')
    print('+---------------------------+')

toon_menu()
menukeuze = input('Maak uw keuze en druk op ENTER: ')

while menukeuze != 'stop':
    if menukeuze == '1':
        printen_lijsten(klantenlijst)
        klantnieuw = vastleggen_klant()
        klantenlijst.append(klantnieuw)
        printen_lijsten(klantenlijst)
        input('druk enter')

    elif menukeuze == '2':
        printen_lijsten(klantenlijst)
        klantnummer = int(input('Welk klantnummer wil je wijzigen: '))
        klantenlijst = wijzigen_klantenlijst(klantnummer, klantenlijst)
        printen_lijsten(klantenlijst)
        input('druk enter')

    elif menukeuze == '3':
        printen_lijsten(klantenlijst)
        klantnummer_verwijderen = int(input("Welk klantnummer wilt u verwijderen: "))
        klantenlijst = verwijderen_klant(klantnummer_verwijderen, klantenlijst)
        printen_lijsten(klantenlijst)
        input('druk enter')

    elif menukeuze == '4':
        printen_lijsten(contractenlijst)
        contractenlijst.append(vastleggen_contract())
        printen_lijsten(contractenlijst)
        input('Druk enter')

    elif menukeuze == '5':
        contract = int(input("Welk contract wilt u printen: "))
        printen_contract(contract)
        input('Druk enter')

    elif menukeuze == '6':
        printen_lijsten(vloot_fiets)
        vloot_fiets.append(vastleggen_nieuwe_fiets())
        printen_lijsten(vloot_fiets)
        input('Druk enter')

    elif menukeuze == '8':

        connectie_fietsverhuur = mysql.connector.connect(host='localhost', database='fietsverhuur',
                                                         user='fietsverhuur', password='1234')

        even_praten_met_sql = connectie_fietsverhuur.cursor()
        query_gjk = ('select* from klant;')

        even_praten_met_sql.execute(query_gjk)
        antwoord = even_praten_met_sql.fetchall()

        for klant in antwoord:
            for elk_item in klant:
                print(f'{str(elk_item):<25}', end='   ')
            print()

        input('Druk enter')

    elif menukeuze == '9':
        printen_lijsten(contractenlijst, klantenlijst, vloot_fiets, fiets_type, vestigingenlijst)
        input('Druk enter')




    toon_menu()
    menukeuze = input('Maak uw keuze en druk op ENTER: ')




