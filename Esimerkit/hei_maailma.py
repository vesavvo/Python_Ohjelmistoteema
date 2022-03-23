def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print ("- " + t)
    # Tavarat katoavat inventaariossa!
    tavarat.clear()
    return

reppu = ["Vesipullo", "Kartta", "Kompassi"]
inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)

