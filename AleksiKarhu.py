# CT60A0201 Ohjelmoinnin perusteet 2017
# Tekijä: Aleksi Karhu
# Opiskelijanumero: 0452237
# Päivämäärä: 17.11.2017
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################

import csv
import verolib

# Ohjelman funktioden ja muuttujien nimet suomeksi, kuten tehtävänannossa pyydetty
# Ohjelma tuli toteuttaa proseduraalisesti, käyttämättä olio-ohjelmointia 


class Taulukkotiedot:
    pvm = ""
    paasto = 0


class Paastoluokat:
    paastovuosi = ""
    paastoluokka50 = 0
    paastoluokka100 = 0
    paastoluokka150 = 0
    paastoluokka200 = 0
    paastoluokka250 = 0
    paastoluokka300 = 0
    paastoluokka350 = 0
    paastoluokka400 = 0
    paastoluokka1000 = 0


def lue_ajoneuvotiedot(datalista):
    ajoneuvotiedosto = input("Anna luettavan tiedoston nimi: ")
    try:
        with open(ajoneuvotiedosto, "r") as csv_tiedosto:
            csv_lukija = csv.reader(csv_tiedosto, delimiter=';')
            next(csv_lukija)
            for rivi in csv_lukija:
                ajoneuvo = Taulukkotiedot()
                paivamaara = rivi[1]
                paastomaara = rivi[33]
                ajoneuvo.pvm = paivamaara
                ajoneuvo.paasto = paastomaara
                datalista.append(ajoneuvo)
        print("Tiedosto '{0}' luettu.".format(ajoneuvotiedosto))
        csv_tiedosto.close()
        return datalista
    except FileNotFoundError:
        print("Tiedoston luku epäonnistui. Anna kelvollinen tiedoston nimi.")


def verokertymat(datalista, vuosi):
    verot = 0
    for Taulukkotiedot in datalista:
        if (Taulukkotiedot.pvm).startswith(str(vuosi)):
            tulot = verolib.vero(int(Taulukkotiedot.paasto))
            verot = verot + tulot
    return verot


def laske_verojen_suhteet(datalista, vuosi):
    verojakauma = []
    paastot50 = 0
    paastot100 = 0
    paastot150 = 0
    paastot200 = 0
    paastot250 = 0
    paastot300 = 0
    paastot350 = 0
    paastot400 = 0
    paastot1000 = 0
    for Taulukkotiedot in datalista:
        if (Taulukkotiedot.pvm).startswith(str(vuosi)):
            if int(Taulukkotiedot.paasto) < 49:
                paastot50 = paastot50 + verolib.vero(int(Taulukkotiedot.paasto))
            elif 50 <= int(Taulukkotiedot.paasto) < 100:
                paastot100 = paastot100 + verolib.vero(int(Taulukkotiedot.paasto))
            elif 100 <= int(Taulukkotiedot.paasto) < 150:
                paastot150 = paastot150 + verolib.vero(int(Taulukkotiedot.paasto))
            elif 150 <= int(Taulukkotiedot.paasto) < 200:
                paastot200 = paastot200 + verolib.vero(int(Taulukkotiedot.paasto))
            elif 200 <= int(Taulukkotiedot.paasto) < 250:
                paastot250 = paastot250 + verolib.vero(int(Taulukkotiedot.paasto))
            elif 250 <= int(Taulukkotiedot.paasto) < 300:
                paastot300 = paastot300 + verolib.vero(int(Taulukkotiedot.paasto))
            elif 300 <= int(Taulukkotiedot.paasto) < 350:
                paastot350 = paastot350 + verolib.vero(int(Taulukkotiedot.paasto))
            elif 350 <= int(Taulukkotiedot.paasto) < 400:
                paastot400 = paastot400 + verolib.vero(int(Taulukkotiedot.paasto))
            elif int(Taulukkotiedot.paasto) >= 400:
                print(Taulukkotiedot.paasto)
                paastot1000 = paastot1000 + verolib.vero(int(Taulukkotiedot.paasto))
    paastot = Paastoluokat()
    paastot.paastovuosi = vuosi
    paastot.paastoluokka50 = round(paastot50)
    paastot.paastoluokka100 = round(paastot100)
    paastot.paastoluokka150 = round(paastot150)
    paastot.paastoluokka200 = round(paastot200)
    paastot.paastoluokka250 = round(paastot250)
    paastot.paastoluokka300 = round(paastot300)
    paastot.paastoluokka350 = round(paastot350)
    paastot.paastoluokka400 = round(paastot400)
    paastot.paastoluokka1000 = round(paastot1000)
    verojakauma.append(paastot)
    return verojakauma


def tulosta_tiedosto(tiedosto):
    with open(tiedosto, "r") as csv_luku:     
        csv_luku = csv.reader(csv_luku)
        print("CSV-tiedoston data on seuraava:")
        for rivi in csv_luku:
            for alkio in rivi:
                print(alkio)


def kirjoita_tiedostoon(csv_lista):
    tiedosto = input("Anna kirjoitettavan tiedoston nimi: ")
    tiedosto_kirjoitus = open(tiedosto, "w")
    x = 2010
    tiedosto_kirjoitus.write(";50;100;150;200;250;300;350;400;1000;\n")
    while x <= 2016:
        verojakauma = laske_verojen_suhteet(csv_lista, x)
        for Paastoluokat in verojakauma:
            tiedosto_kirjoitus.write(str(Paastoluokat.paastovuosi) + ";" + str(Paastoluokat.paastoluokka50) + ";" +
                                     str(Paastoluokat.paastoluokka100) + ";" + str(Paastoluokat.paastoluokka150) + ";" +
                                     str(Paastoluokat.paastoluokka200) + ";" + str(Paastoluokat.paastoluokka250) + ";" +
                                     str(Paastoluokat.paastoluokka300) + ";" + str(Paastoluokat.paastoluokka350) + ";" +
                                     str(Paastoluokat.paastoluokka400) + ";" + str(Paastoluokat.paastoluokka1000) + ";" +
                                     "\n")

            x = x + 1
    print("CSV-tiedosto kirjoitettu.")
    return tiedosto


def paaohjelma():
    csv_lista = []
    while True:
        print("Anna haluamasi toiminnon numero seuraavasta valikosta:")
        print("1) Lue ajoneuvotiedot")
        print("2) Laske ja tulosta verot")
        print("3) Kirjoita CSV-tiedosto")
        print("4) Tulosta CSV-tiedoston data näytölle")
        print("0) Lopeta")
        valinta = int(input("Valintasi: "))
        if valinta == 1:
            csv_lista = lue_ajoneuvotiedot(csv_lista)
        elif valinta == 2:
            x = 2010
            print("Verokertymät vuosittain 2010-luvulla ovat seuraavat:")
            while x <= 2016:
                verot = verokertymat(csv_lista, x)
                print(x, round(verot), "euroa.")
                x = x + 1
        elif valinta == 3:
            tiedosto = kirjoita_tiedostoon(csv_lista)
        elif valinta == 4:
            tulosta_tiedosto(tiedosto)
        elif valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Virheellinen syöte.")

paaohjelma()


######################################################################
# eof
