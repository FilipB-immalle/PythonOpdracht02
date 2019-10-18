# PythonOpdracht02
# Importeren van datetime voor berekeningen te kunnen maken met de datums
from datetime import datetime, date

# Vragen naar geboortedatum, standaard kiezen 2000 januari, 1
try:
  geboortedatum = datetime.strptime(input("Wat is je geboortedatum (YYYY-MM-DD): "), "%Y-%m-%d")
except:
  geboortedatum = datetime(2000, 1, 1, 0, 0)

# Berekening datum vandaag + leeftijd
tijdnu = datetime.today()
leeftijd = tijdnu - geboortedatum

# Berekening leeftijd in dagen en uren
leeftijdindagen = round(leeftijd.total_seconds() / 60 /60 /24)
    # leeftijdindagen = tijdnu.day - geboortedatum.day 
leeftijdinuren = round(leeftijd.total_seconds() / 3600)
    # leeftijdinuren = tijdnu.hour - geboortedatum.hour

# Berekening aantal dagen tot verjaardag en leeftijd dan
if date.today() > date(date.today().year, geboortedatum.month, geboortedatum.day):
  dagentotverjaardag = (date(date.today().year+1, geboortedatum.month, geboortedatum.day)-date.today()).days
else:
  dagentotverjaardag = (date(date.today().year, geboortedatum.month, geboortedatum.day)-date.today()).days

leeftijdvolgendjaar = (tijdnu.year - geboortedatum.year) + 1

# Verjaart binnen de 100 dagen of niet?
if dagentotverjaardag < 100:
    aantaldagen = "Je verjaart binnen de 100 dagen"
else:
    aantaldagen = "Je verjaart pas in meer dan 100 dagen"

# Weergeven van gegevens
print(f"""
Je bent al {leeftijdindagen} dagen in leven
Je bent al {leeftijdinuren} uren in leven
Het duurt {dagentotverjaardag} dagen tot je jarig bent
Je word dan {leeftijdvolgendjaar} jaar oud
{aantaldagen}
""")

# Bits
try:
   bits = int(input('Hoeveel bits?\n'))
except ValueError:
   print("Dit is geen getal. De standaardwaarde 8 is toegepast")
   bits = 8

uitkomst = 2 ** bits
print(str(uitkomst) + ' verschillende getallen')

print()

# Leeftijd
if(tijdnu.year - geboortedatum.year) > 12 and (tijdnu.year - geboortedatum.year) < 18:
    print("OK")
else:
    print("Niet OK")

if(tijdnu.year - geboortedatum.year) < 18:
    if(tijdnu.year - geboortedatum.year) > 12:
        print("OK")
else:
    print ("Niet OK")

print()
# Lengte
woord = input("Voer een woord in: ")

if(len(woord) >= 5 and len(woord) <= 10):
    print("OK")
else:
    print("Niet OK")

print()
school = "Immaculata"
    # Eerste letter
print(school[:1])
 
    # Eerste 4 letters
print(school[:4])
 
    # Laatste letter
print(school[-1:])
 
    # Laatste 3 letters
print(school[-3:])
 
    # Middelste 3 letters
print(school[4:7])

print()
# Namen
namenlijst = "Jan","Jos","Mieke"

naam = input("Wat is uw naam: ")

if naam in namenlijst:
    print("Hallo " + naam)
else:
    print("Onbekende naam")

print()
# Dagdagelijkse booleans
warmerDan50Graden = True
overdag = True
 
if warmerDan50Graden == True or overdag == True:
    print("De ventilator wordt gestart")
else:
    print("Een van de voorwaardes voldoet niet aan de eisen")

# Extra 1
namenlijst2 = ("Jan", "Janneke", "Joske")
naam2 = "Bruno"
cijfers = (1, 2, 3, 4)
# cijfers[1]= 5 geeft een foutmelding, tuple kan niet veranderd worden naar int
# naam[0:1]= "W" geeft niet "Wruno", wel fout
tekens = ("=", "?", "!")
# tekens[2] = "*" geeft een fout

# Extra 2
warmerDan50Graden = True
overdag = True

if not warmerDan50Graden or not overdag:
    print("De planten worden niet gewaterd")
else:
    print("De planten worden wel gewaterd")