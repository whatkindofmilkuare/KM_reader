import struct
import base64
from datetime import datetime, timedelta

def decode_base64_data(encoded_data):
    # Dekodowanie Base64
    try:
        data = base64.b64decode(encoded_data)
    except (base64.binascii.Error, TypeError) as e:
        print(f"Nieprawidłowy format danych Base64: {e}")
        return

    # Sprawdzamy długość danych, aby upewnić się, że mamy wystarczająco dużo bajtów
    if len(data) < 33:
        print("Dane są zbyt krótkie do poprawnego parsowania.")
        return
    
    try:
        # Parsowanie danychnumer = data[3:5].decode('utf-8', errors='ignore')
        numer = data[3:5].decode('utf-8', errors='ignore')  # Może nie być w UTF-8, dlatego ignorujemy błędy
        inverted_numer = numer[::-1]
        series = struct.unpack("<I", data[5:9])[0]
        price = struct.unpack("<H", data[9:11])[0] / 100
        OF = struct.unpack("B", data[12:13])[0]
        disc = struct.unpack("B", data[14:15])[0]

        # Parsowanie kolejnych danych (4 bajty, unsigned int)
        kupno = struct.unpack("<I", data[16:20])[0]  # Czas kupna (4 bajty, unsigned int)
        pocz = struct.unpack("<I", data[20:24])[0]   # Czas rozpoczęcia (4 bajty, unsigned int)
        kon = struct.unpack("<I", data[24:28])[0]    # Czas zakończenia (4 bajty, unsigned int)
        
        ibnr1 = struct.unpack("<H", data[28:30])[0]  # IBNR1 (2 bajty, unsigned short)
        ibnr2 = struct.unpack("<H", data[30:32])[0]  # IBNR2 (2 bajty, unsigned short)

        # Data początkowa - północ 1 stycznia 2010
        start_date = datetime(2010, 1, 1)

        # Dodanie liczby sekund od północy 1 stycznia 2010 roku
        kupno_date = (start_date + timedelta(seconds=kupno)).strftime('%Y-%m-%d %H:%M:%S')
        pocz_date = (start_date + timedelta(seconds=pocz)).strftime('%Y-%m-%d %H:%M:%S')
        kon_date = (start_date + timedelta(seconds=kon)).strftime('%Y-%m-%d %H:%M:%S')

        # Wyświetlanie zdekodowanych danych
        print(f"Numer: {inverted_numer}")
        print(f"Numer serii: {series}")
        print(f"Cena: {price:.2f} zł")
        print(f"OF: {OF}")
        print(f"Ulga: {disc}")
        print(f"Czas kupna: {kupno_date}")
        print(f"Czas rozpoczęcia: {pocz_date}")
        print(f"Czas zakończenia: {kon_date}")
        print(f"IBNR1: {ibnr1}")
        print(f"IBNR2: {ibnr2}")
    except (struct.error, IndexError) as e:
        print(f"Błąd podczas parsowania danych: {e}")

ascii_art = """
  _  ____  __                      _           
 | |/ /  \/  |                    | |          
 | ' /| \  / |  _ __ ___  __ _  __| | ___ _ __ 
 |  < | |\/| | | '__/ _ \/ _` |/ _` |/ _ \ '__|     coded by @whatkindofmilkuare
 | . \| |  | | | | |  __/ (_| | (_| |  __/ |   
 |_|\_\_|  |_| |_|  \___|\__,_|\__,_|\___|_|   
           ______                              
          |______|                             
"""

print(ascii_art)
encoded_data = input("Podaj zakodowane dane Base64: ")
decode_base64_data(encoded_data)
