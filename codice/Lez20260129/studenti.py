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

f = open(r'c:\Users\pietro.picchiottino\py-scuola\ITS2026_ACA\codice\Lez20260129\singolostudente.txt')

for riga in f:
    # print(riga)
    # per ogni riga del file aggiungo la riga alla lista studenti
    riga = riga.replace("\n", " ")
    riga = riga.replace("\t", ",")
    studenti.append(riga)

f.close()

f =open('c:\\Users\\pietro.picchiottino\\py-scuola\\ITS2026_ACA\\codice\\Lez20260129\studenti.sql','w')

query_tabella = """
DROP TABLE IF EXISTS studenti;\n\n

CREATE TABLE   studenti(\n
    id int primary key auto_increment\n
    nome varchar(30) not null\n
    cognome varchar(50) not null\n
);\n\n 

"""

f.write(query_tabella)

for s in studenti:
    s =str(s)
    pezzi = s.split(",")
    nome = pezzi[0]
    cognome = pezzi[1]
    f.write(f"insert into studenti (nome, cognome) value ('{nome}', '{cognome}');\n")

f.close