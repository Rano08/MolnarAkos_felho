# A 'keszit_diagram_sort' függvény a napi hőmérsékletet csillagokkal ábrázolja
def keszit_diagram_sort(nap_szama, homerseklet):
# A hőmérséklet számát egész számra konvertáljuk
    csillagok_szama = int(homerseklet)
# A megfelelő számú csillagot hozunk létre a hőmérséklet alapján
    csillagok = '*' * csillagok_szama
# A sor formázása a nap számával, a csillagok számával és a hőmérséklettel
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
    return sor  # A formázott sort visszaadjuk

# A 'rajzolj_diagram' függvény a teljes diagramot kirajzolja
def rajzolj_diagram(homersekletek):
# A diagram címe
    print("Napi átlaghőmérséklet diagram (°C)")
# A vonal, ami elválasztja a cím és a diagram között
    print("-" * 40)

# Végigiterálunk a hőmérsékleteken és kirajzoljuk őket
    for i in range(len(homersekletek)):
        nap = i + 1  # A napok számozása 1-től indul, nem 0-tól
# A 'keszit_diagram_sort' függvény hívása a megfelelő napra és hőmérsékletre
        sor = keszit_diagram_sort(nap, homersekletek[i])
# A diagram sorának kiírása
        print(sor)

# Példa hőmérsékleti adatok listája
napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

# A diagram kirajzolása a napi hőmérsékletek alapján
rajzolj_diagram(napi_atlaghomersekletek)


