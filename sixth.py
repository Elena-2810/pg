import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
   
    hrefs = []

    print(f"Stahuji URL: {url}")
    
    try:
       
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Chyba pri stahovani URL: {e}")
        return hrefs
    
    if response.status_code == 200:
        print("Stazeni probehlo uspesne (Status Code 200).")
        
        
        regex = r'<a\b[^>]*?\bhref=["\']([^"\']+)["\']'
        hrefs = re.findall(regex, response.text)
       
        print(f"Nalezeno {len(hrefs)} odkazu.")
        for link in hrefs[:5]:
             print(f"  - {link}")
        
    else:
        print(f"Chyba: Stranka vratila status kod {response.status_code}.")

    return hrefs


if 1 == 1: # instead of "main"
    try:
        if len(sys.argv) < 2:
            print("Pouziti: python sixth.py <https://www.jcu.cz>")
            sys.exit(1)
        url = sys.argv[1]
        
        
        download_url_and_get_all_hrefs(url)
        
   
    except Exception as e:
        print(f"Program skoncil chybou: {e}")