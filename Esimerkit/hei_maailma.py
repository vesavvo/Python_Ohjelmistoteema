def neliösumma(eka, toka):
    ns = eka**2 + toka**2
    return ns

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
tulos = neliösumma(luku1, luku2)
print(f"Lukujen {luku1:.3f} ja {luku2:.3f} neliösumma on {tulos:.3f}.")