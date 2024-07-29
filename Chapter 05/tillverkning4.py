tillgängliga_tillbehör = ['championer', 'oliver', 'pepperoni',
                          'grön peppar', 'äpple', 'extra ost']

önskade_tillbehör = ['championer', 'svamp', 'pommes', 'extra ost']

for önskad_tilllbehör in önskade_tillbehör:
    if önskad_tilllbehör in tillgängliga_tillbehör:
        print("Lägger till " + önskad_tilllbehör + ".")
    else:
        print("Vi är ledsna. Vi har tyvärr slut på " + önskad_tilllbehör + ".")

print("\nDin Pizza är sluförd")

