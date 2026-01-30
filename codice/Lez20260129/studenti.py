# studenti = [    ]

# # Nota l'uso di r'' per evitare problemi con le barre rovesciate di Windows
# f = open(r'c:\Users\pietro.picchiottino\py-scuola\ITS2026_ACA\codice\Lez20260129\singolostudente.txt')

# for riga in f:
#     # print(riga)
#     # per ogni riga del file aggiungo alla lista studenti
#     studenti.append(studenti)

# f.close()

# for studente in studenti:
#     print(studente)
studenti = []

f = open('./singolostudente.txt')

for riga in f:
    # print(riga)
    # per ogni riga del file aggiungo la riga alla lista studenti
    studenti.append(riga)

f.close()

for s in studenti:
    print(s)