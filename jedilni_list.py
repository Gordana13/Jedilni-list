# -*- encoding: utf-8 -*-

dnevni_meni = {}

while True:
    jed = raw_input("Vpišite jed: ")
    cena = raw_input("Vpišite ceno za %s: " %jed)

    dnevni_meni[jed] = cena

    vprasanje = raw_input("Želite dodati novo jed (da/ne)? ")
    if vprasanje.lower() == "ne":
        break

with open("meni.txt", "w+") as meni_file:
    for jed in dnevni_meni:
        meni_file.write("%s, %s EUR\n" %(jed, dnevni_meni[jed]))

print(dnevni_meni)