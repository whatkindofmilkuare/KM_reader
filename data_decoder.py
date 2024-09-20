import struct
import datetime
import base64

def decode_base64_data(encoded_data):
    # Dekodowanie Base64
    data = base64.b64decode(encoded_data)
    
    # Parsowanie danych
    numer = data[3:5].decode('utf-8')
    series = struct.unpack("<I", data[5:9])[0]
    price = struct.unpack("<H", data[9:11])[0] / 100
    OF = struct.unpack("B", data[12:13])[0]
    disc = struct.unpack("B", data[14:15])[0]
    
    ibnr1 = struct.unpack("<H", data[29:31])[0]  # IBNR1 (2 bajty, unsigned short)
    ibnr2 = struct.unpack("<H", data[31:33])[0]  # IBNR2 (2 bajty, unsigned short)

    # Parsowanie kolejnych danych (4 bajty, unsigned int)
    kupno = struct.unpack("<I", data[17:21])[0]  # Czas kupna (4 bajty, unsigned int)
    pocz = struct.unpack("<I", data[21:25])[0]   # Czas rozpoczęcia (4 bajty, unsigned int)
    kon = struct.unpack("<I", data[25:29])[0]    # Czas zakończenia (4 bajty, unsigned int)
    
    # Wyświetlanie zdekodowanych danych
    print(f"Numer: {numer}")
    print(f"Numer serii: {series}")
    print(f"Cena: {price:.2f} zł")
    print(f"OF: {OF}")
    print(f"Ulga: {disc}")
    print(f"Czas kupna: {data_kupna_str}")
    print(f"Czas rozpoczęcia: {data_poczatku_str}")
    print(f"Czas zakończenia: {data_konca_str}")
    print(f"IBNR1: {ibnr1}")
    print(f"IBNR2: {ibnr2}")

# Przykład użycia funkcji
encoded_data = input("Podaj zakodowane dane Base64: ")
decode_base64_data(encoded_data)
