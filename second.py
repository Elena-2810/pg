def cislo_text(cislo_str):
    
    try:
        cislo = int(cislo_str)
    except ValueError:
        return "Neplatný vstup (není číslo)"

    if not (0 <= cislo <= 100):
        return "Číslo je mimo rozsah 0 až 100"

    
    jednotky = {
        0: "nula", 1: "jedna", 2: "dvě", 3: "tři", 4: "čtyři",
        5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět"
    }

    nact_do_devatenact = {
        10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct",
        15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"
    }

    desitky = {
        2: "dvacet", 3: "třicet", 4: "čtyřicet", 5: "padesát", 6: "šedesát",
        7: "sedmdesát", 8: "osmdesát", 9: "devadesát"
    }
    
    if cislo < 10:
        return jednotky[cislo]

    
    elif 10 <= cislo < 20:
        return nact_do_devatenact[cislo]

    
    elif 20 <= cislo < 100:
        d = cislo // 10  
        j = cislo % 10   
        
        vysledek = desitky[d]
        
        if j > 0:
            
            vysledek += " " + jednotky[j]
        
        return vysledek

    
    elif cislo == 100:
        return "sto"

    return "Neznámá chyba"


if __name__ == "__main__":
    cislo_str = input("Zadej číslo (0-100): ")
    text = cislo_text(cislo_str)
    print(f"Textová reprezentace: {text}")