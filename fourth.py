def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    typ = figurka["typ"]
    r1, s1 = figurka["pozice"]
    r2, s2 = cilova_pozice

    if not (1 <= r2 <= 8 and 1 <= s2 <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    def cesta_volna():
        r_krok = 0 if r1 == r2 else (1 if r2 > r1 else -1)
        s_krok = 0 if s1 == s2 else (1 if s2 > s1 else -1)
        r, s = r1 + r_krok, s1 + s_krok
        while (r, s) != (r2, s2):
            if (r, s) in obsazene_pozice:
                return False
            r += r_krok
            s += s_krok
        return True

    if typ == "pěšec":
        if s1 == s2 and r2 == r1 + 1 and (r2, s2) not in obsazene_pozice:
            return True
        if s1 == s2 and r1 == 1 and r2 == 3 and (2, s2) not in obsazene_pozice and (3, s2) not in obsazene_pozice:
            return True

        return False

    if typ == "jezdec":
        if (abs(r2 - r1), abs(s2 - s1)) in [(1, 2), (2, 1)]:
            return True
        return False

    if typ == "věž":
        if r1 == r2 or s1 == s2:
            return cesta_volna()
        return False

    if typ == "střelec":
        if abs(r2 - r1) == abs(s2 - s1):
            return cesta_volna()
        return False

    if typ == "dáma":
        if r1 == r2 or s1 == s2 or abs(r2 - r1) == abs(s2 - s1):
            return cesta_volna()
        return False

    if typ == "král":
        if abs(r2 - r1) <= 1 and abs(s2 - s1) <= 1:
            return True
        return False

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  
