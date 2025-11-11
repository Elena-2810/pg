import sys


jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    
    try:
        with open(file_name, "rb") as f:
            header = f.read(header_length)
            return header
    except Exception as e:
        print(f"Chyba při čtení souboru: {e}")
        return b''


def is_jpeg(file_name):
    
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header


def is_gif(file_name):
   
    header = read_header(file_name, len(gif_header1))
    return header == gif_header1 or header == gif_header2


def is_png(file_name):
   
    header = read_header(file_name, len(png_header))
    return header == png_header


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]  
      
        if is_jpeg(file_name) or is_gif(file_name) or is_png(file_name):
            print(True)
        else:
            print(False)
    except Exception as e:
        print(f"Chyba: {e}")
