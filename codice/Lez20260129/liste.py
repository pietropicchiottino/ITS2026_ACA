
frutta = ['pere', 'mele', 'fragole']
verdura = list(['spinaci', 'barbabietole','broccoli'])

frutta.append("banane")
verdura.append("carote")

prodotti_orto = list(frutta + verdura)

for prodotto in prodotti_orto:
    print(f"Prodotto: {prodotto} ------ peso: {int(input(f"Peso del {prodotto}:"))}")