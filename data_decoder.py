import struct
from datetime import datetime, timedelta
import base64

# Stała referencyjna: 01-01-2010 00:00:00 CEST (w sekundach od 1970-01-01 00:00:00 UTC)
REF = 1234

def decode_base64_data(encoded_data):
    # Dekodowanie Base64
    data = base64.b64decode(encoded_data)
    
    # Parsowanie danych
    numer = data[2:4].decode()
    series = struct.unpack(">I", data[5:9])[0]
    price = struct.unpack(">H", data[9:11])[0] / 100
    OF = struct.unpack("B", data[12:13])[0]
    disc = struct.unpack("B", data[14:15])[0]
    
    kupno = struct.unpack(">I", data[17:21])[0]
    pocz = struct.unpack(">I", data[21:25])[0]
    kon = struct.unpack(">I", data[25:29])[0]
    
    ibnr1 = struct.unpack(">H", data[29:31])[0]
    ibnr2 = struct.unpack(">H", data[31:33])[0]

    # Przekształcanie czasu na datę
    kupno_time = datetime.utcfromtimestamp(kupno + REF - 7200).strftime("%d-%m-%Y, %H:%M:%S")
    pocz_time = datetime.utcfromtimestamp(pocz + REF - 7200).strftime("%d-%m-%Y, %H:%M:%S")
    kon_time = datetime.utcfromtimestamp(kon + REF - 7200).strftime("%d-%m-%Y, %H:%M:%S")
    
    # Wyświetlanie zdekodowanych danych
    print(f"Numer: {numer}")
    print(f"Numer serii: {series}")
    print(f"Cena: {price:.2f} zł")
    print(f"OF: {OF}")
    print(f"Ulga: {disc}")
    print(f"Czas kupna: {kupno_time}")
    print(f"Czas rozpoczęcia: {pocz_time}")
    print(f"Czas zakończenia: {kon_time}")
    print(f"IBNR1: {ibnr1}")
    print(f"IBNR2: {ibnr2}")

# Przykład użycia funkcji
encoded_data = input("Podaj zakodowane dane Base64: ")
decode_base64_data(encoded_data)
