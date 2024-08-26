import struct
from datetime import datetime
import base64

# Stała referencyjna: 01-01-2010 00:00:00 CEST (w sekundach od 1970-01-01 00:00:00 UTC)
REF = 1234

def format_time_to_timestamp(time_str):
    dt = datetime.strptime(time_str, "%d-%m-%Y, %H:%M:%S")
    timestamp = int(dt.timestamp())
    return timestamp - REF + 7200

def create_data():
    # Pobranie danych od użytkownika
    numer = input("Podaj numer (2 znaki): ").encode()
    series = int(input("Podaj numer serii (liczba całkowita): "))
    price = int(float(input("Podaj cenę (zł): ")) * 100)
    OF = int(input("Podaj wartość OF (liczba całkowita): "))
    disc = int(input("Podaj ulgę (liczba całkowita): "))
    
    kupno = format_time_to_timestamp(input("Podaj czas kupna (dd-mm-yyyy, hh:mm:ss): "))
    pocz = format_time_to_timestamp(input("Podaj czas rozpoczęcia (dd-mm-yyyy, hh:mm:ss): "))
    kon = format_time_to_timestamp(input("Podaj czas zakończenia (dd-mm-yyyy, hh:mm:ss): "))
    
    ibnr1 = int(input("Podaj wartość IBNR1 (liczba całkowita): "))
    ibnr2 = int(input("Podaj wartość IBNR2 (liczba całkowita): "))

    # Składanie danych w odpowiedniej kolejności
    data = b'\x00' * 2  # Placeholder dla pierwszych 2 bajtów
    data += numer  # Numer (2 bajty)
    data += b'\x00'  # Placeholder dla 1 bajtu
    data += struct.pack(">I", series)  # Numer serii (4 bajty)
    data += struct.pack(">H", price)  # Cena biletu (2 bajty)
    data += b'\x00'  # Placeholder dla 1 bajtu
    data += struct.pack("B", OF)  # OF (1 bajt)
    data += b'\x00'  # Placeholder dla 1 bajtu
    data += struct.pack("B", disc)  # Ulga (1 bajt)
    data += b'\x00' * 2  # Placeholder dla 2 bajtów
    data += struct.pack(">I", kupno)  # Czas kupna biletu (4 bajty)
    data += struct.pack(">I", pocz)  # Czas rozpoczęcia ważności biletu (4 bajty)
    data += struct.pack(">I", kon)  # Czas zakończenia ważności biletu (4 bajty)
    data += struct.pack(">H", ibnr1)  # Numer stacji początkowej (2 bajty)
    data += struct.pack(">H", ibnr2)  # Numer stacji końcowej (2 bajty)
    data += b'\x00' * (94 - len(data))  # Uzupełnienie danych do 94 bajtów

    # Kodowanie danych do base64
    base64_data = base64.b64encode(data).decode()
    print("Zakodowane dane w base64:")
    print(base64_data)

# Generowanie zakodowanych danych
create_data()
