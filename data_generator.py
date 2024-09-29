import struct
import base64
from datetime import datetime

def encode_to_base64(numer, series, price, OF, disc, kupno_date, pocz_date, kon_date, ibnr1, ibnr2):
    # Sprawdzanie długości numeru (minimum 2 znaki)
    numer = numer[:2] if len(numer) >= 2 else numer.ljust(2, '\x00')
    
    # Odwracanie numeru
    inverted_numer = numer[::-1]

    # Zmiana cen z formatu zł na grosze
    price_in_grosze = int(price * 100)

    # Parsowanie dat do liczby sekund od 1 stycznia 2010
    start_date = datetime(2010, 1, 1)
    kupno_seconds = int((kupno_date - start_date).total_seconds())
    pocz_seconds = int((pocz_date - start_date).total_seconds())
    kon_seconds = int((kon_date - start_date).total_seconds())

    # Zbudowanie struktury binarnej
    try:
        data = (
            b'\x00\x00\x00' +                     # 3 bajty paddingu
            inverted_numer.encode('utf-8') +      # Numer (2 bajty)
            struct.pack("<I", series) +           # Numer serii (4 bajty, unsigned int)
            struct.pack("<H", price_in_grosze) +  # Cena (2 bajty, unsigned short)
            b'\x00' +                             # 1 bajt paddingu
            struct.pack("B", OF) +                # OF (1 bajt)
            b'\x00' +                             # 1 bajt paddingu
            struct.pack("B", disc) +              # Ulga (1 bajt)
            b'\x00' +                             # 1 bajt paddingu
            struct.pack("<I", kupno_seconds) +    # Czas kupna (4 bajty, unsigned int)
            struct.pack("<I", pocz_seconds) +     # Czas rozpoczęcia (4 bajty, unsigned int)
            struct.pack("<I", kon_seconds) +      # Czas zakończenia (4 bajty, unsigned int)
            struct.pack("<H", ibnr1) +            # IBNR1 (2 bajty, unsigned short)
            struct.pack("<H", ibnr2)              # IBNR2 (2 bajty, unsigned short)
        )
        
        # Sprawdzenie długości danych i dodanie paddingu, aby miały co najmniej 33 bajty
        if len(data) < 33:
            data += b'\x00' * (33 - len(data))

        # Dodanie paddingu, aby długość była podzielna przez 4
        padding_length = len(data) % 4
        if padding_length != 0:
            data += b'\x00' * (4 - padding_length)

        # Kodowanie do Base64
        encoded_data = base64.b64encode(data).decode('utf-8')
        print(f"Zakodowane dane Base64: {encoded_data}")
    
    except struct.error as e:
        print(f"Błąd podczas budowania danych: {e}")

ascii_art = """
  _  ____  __                      _           
 | |/ /  \/  |                    | |          
 | ' /| \  / |  _ __ ___  __ _  __| | ___ _ __ 
 |  < | |\/| | | '__/ _ \/ _` |/ _` |/ _ \ '__|     coded by @whatkindofmiluare
 | . \| |  | | | | |  __/ (_| | (_| |  __/ |   
 |_|\_\_|  |_| |_|  \___|\__,_|\__,_|\___|_|   
           ______                              
          |______|                             
"""

print(ascii_art)

# Zbieranie danych od użytkownika
numer = input("Podaj numer (2 znaki): ")
series = int(input("Podaj numer serii: "))
price = float(input("Podaj cenę (zł): "))
OF = int(input("Podaj OF (0-255): "))
disc = int(input("Podaj ulgę (0-255): "))

# Podanie dat w formacie 'YYYY-MM-DD HH:MM:SS'
kupno_date = datetime.strptime(input("Podaj datę kupna (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')
pocz_date = datetime.strptime(input("Podaj datę rozpoczęcia (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')
kon_date = datetime.strptime(input("Podaj datę zakończenia (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')

ibnr1 = int(input("Podaj IBNR1 (0-65535): "))
ibnr2 = int(input("Podaj IBNR2 (0-65535): "))

# Zakodowanie danych
encode_to_base64(numer, series, price, OF, disc, kupno_date, pocz_date, kon_date, ibnr1, ibnr2)
