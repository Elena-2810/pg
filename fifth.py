import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'

def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    try:
        with open(file_name, "rb") as f:  # otevře soubor v binárním režimu
            header = f.read(header_length)  # přečte požadovaný počet bytů
            return header
    except Exception as e:
        print(f"Nastala chyba při čtení souboru: {e}")
        return b''  # vrátí prázdné bajty, pokud dojde k chybě


def is_jpeg(file_name):
    """
    Zkontroluje, jestli soubor je typu JPEG
    """
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header


def is_gif(file_name):
    """
    Zkontroluje, jestli soubor je typu GIF
    """
    header = read_header(file_name, len(gif_header1))
    return header == gif_header1 or header == gif_header2


def is_png(file_name):
    """
    Zkontroluje, jestli soubor je typu PNG
    """
    header = read_header(file_name, len(png_header))
    return header == png_header


def print_file_type(file_name):
    """
    Vypíše typ souboru (není potřeba měnit)
    """
    if is_jpeg(file_name):
        print(f"Soubor {file_name} je typu JPEG")
    elif is_gif(file_name):
        print(f"Soubor {file_name} je typu GIF")
    elif is_png(file_name):
        print(f"Soubor {file_name} je typu PNG")
    else:
        print(f"Soubor {file_name} je neznámého typu")


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except Exception as e:
        print(f"Nastala chyba: {e}")
