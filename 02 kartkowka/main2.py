import os
import json


if os.path.exists("dane_wyjsciowe.txt"):
    os.remove("dane_wyjsciowe.txt")

try:
    with open("oszczep.txt", "r") as plik:
        dane = plik.read().splitlines()
        for linia in dane:
            zawodnik, wyniki = linia.split(":")
            
najlepszy = max(float(x) for x in wyniki.split())
            
            zawodnik_w = f"{zawodnik}: {najlepszy}\n"
            with open(f"dane_wyjsciowe.txt", "a") as plik_txt:
                plik_txt.write(zawodnik_w)
    print("stworzono plik 'dane_wyjsciowe.txt'")
except FileNotFoundError:
    print('nie znaleziono pliku "oszczep.txt"')

try:
    with open("oszczep.json", "r") as plik_json:
        dane_json = json.load(plik_json)
        
        lista_wynikow = [
            {"zawodnik": zawodnik["zawodnik"], "najdluzszy_rzut": max(zawodnik["rzuty"])}
            for zawodnik in dane_json
        ]

    with open("dane_wyjsciowe.json", "w") as plik_jsonw:
        json.dump(lista_wynikow, plik_jsonw, indent=4)
        print("stworzono plik 'dane_wyjsciowe.json'")

except FileNotFoundError:
    print('nie znaleziono pliku "oszczep.json"')
