import random

def huvudmeny():
    print("\nVälkommen till 'Don't Breathe: Escape the House'")
    print("1. Starta spelet")
    print("2. Avsluta")
    val = input("Välj ett alternativ: ")
    if val == "1":
        starta_spelet()
    elif val == "2":
        print("Tack för att du spelade. Hoppas du klarar dig nästa gång...")
    else:
        print("Ogiltigt val. Försök igen.")
        huvudmeny()

def losa_pussel():
    print("\nDu hittar en tung, metallisk dörr. En kodpanel blinkar rött.")
    print("Du måste lösa en kod innan mannen hör dig.")

    kod = random.randint(100, 999)
    gissning = input("Gissa en tresiffrig kod: ")

    if gissning == str(kod):
        print("Rätt kod! Dörren öppnas ljudlöst.")
        input("Tryck på enter för att fortsätta.")
        return True
    else:
        print(f"Fel kod! Rätt kod var {kod}. Ett högt ljud går av och mannen är på väg!")
        return False

def fly_fran_fiende():
    print("\nDu hör tunga steg bakom dig. Mannen är nära!")
    print("Du försöker fly i mörkret...")
    tarning = random.randint(1, 6)
    print(f"Du slog en {tarning}.")
    if tarning <= 3:
        print("Du snubblar men lyckas gömma dig i sista sekunden.")
        return True
    else:
        print("Han hör ditt andetag och fångar dig. Det är slutet för dig.")
        return False

def starta_spelet():
    print("\nDu vaknar upp i ett främmande, mörkt hus. Det är tyst... för tyst.")
    print("Du inser snabbt att någon bevakar dig. Någon som kan höra minsta ljud.")

    spelarens_val = input("Du ser två dörrar framför dig. Välj dörr 1 eller 2: ")
    if spelarens_val == "1":
        print("\nDu kliver in i ett rum fullt av glasbitar på golvet. Varje steg avslöjar dig.")
        print("Mannen hör dig och du är fast innan du ens börjat.")
        return
    elif spelarens_val == "2":
        print("\nDu väljer dörr 2 och smyger in i ett kök. Du är fortfarande osedd.")
    else:
        print("\nOgiltigt val. Spelet avslutas.")
        return

    if not losa_pussel():
        print("\nInnan du hinner fly, griper en kall hand tag i dig.")
        print("Spelet är över.")
        return

    if not fly_fran_fiende():
        print("Spelet är över.")
        return

    spelarens_val = input("\nDu når husets sista rum. Två utgångar finns: en trappa ner eller en dörr till garaget. Välj 'trappa' eller 'garage': ")
    if spelarens_val.lower() == "trappa":
        print("\nDu springer ner men trappan är riggad med snaror. Du fastnar och allt blir svart.")
    elif spelarens_val.lower() == "garage":
        print("\nDu hittar en bilnyckel i garaget och startar bilen precis innan mannen når dig.")
        print("Du kör ut i natten och överlever... den här gången.")
    else:
        print("\nDu tvekar för länge. Det var ditt sista misstag.")

huvudmeny()
