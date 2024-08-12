from undersökning import AnonymUndersökning

fråga = "Vad för sport började du spela först?"
sport_undersökning = AnonymUndersökning(fråga)

sport_undersökning.visa_fråga()
print("Skriv 'q' närsomhelst för att sluta.\n")
while True:
    svar = input("Sport: ")
    if svar == 'q':
        break
    sport_undersökning.samla_svaren(svar)

print("\nTack till alla svaren och tack till alla som deltog i undersökningen!")
sport_undersökning.visa_resultat()
