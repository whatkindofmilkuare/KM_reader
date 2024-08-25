import struct
from datetime import datetime
import base64

# Stała referencyjna: 01-01-2010 00:00:00 CEST (w sekundach od 1970-01-01 00:00:00 UTC)
REF = 1234

def process_data(data: bytes):
    # Sprawdzamy długość danych
    data_length = len(data)
    if data_length != 94:
        raise ValueError(f"Oczekiwana długość danych wynosi 94 bajty, ale otrzymano {data_length} bajty")
    
    # Odczyt danych z bufora
    series = struct.unpack(">I", data[5:9])[0]
    price = struct.unpack(">H", data[9:11])[0]
    OF = data[12]
    disc = data[14]
    
    t1 = struct.unpack(">I", data[16:20])[0]
    t2 = struct.unpack(">I", data[20:24])[0]
    t3 = struct.unpack(">I", data[24:28])[0]
    
    ibnr1 = struct.unpack(">H", data[28:30])[0]
    ibnr2 = struct.unpack(">H", data[30:32])[0]

    # Konwersja czasów do UTC
    t1 += REF - 7200
    t2 += REF - 7200
    t3 += REF - 7200
    
    # Formatowanie dat
    def format_time(timestamp):
        dt = datetime.utcfromtimestamp(timestamp)
        return dt.strftime("%d-%m-%Y, %H:%M:%S")
    
    # Wyświetlanie wyników
    print(f"NUMER:\t{data[2:4].decode()}%010d" % series)
    print(f"CENA:\t{price / 100:.2f}")
    print(f"OF:\t{OF}")
    print(f"ULGA:\t{disc}")
    print(f"KUPNO:\t{format_time(t1)}")
    print(f"POCZ.:\t{format_time(t2)}")
    print(f"KON.:\t{format_time(t3)}")
    print(f"OD:\t{ibnr1}")
    print(f"DO:\t{ibnr2}")

# Przykładowe dane wejściowe (base64)
base64_data = "<DATA_FROM_TICKET_QR_CODE>"

# Dekodowanie base64 do surowych bajtów
data = base64.b64decode(base64_data)

# Sprawdzamy długość po dekodowaniu
print(f"Długość danych po dekodowaniu: {len(data)}")

# Procesowanie danych
process_data(data)
