# Generator i Dekoder Danych w Formacie Base64

## Opis

Programy python służą do odczytywania i generowania informacji na podstawie ciągów znakowych zakodowanych w base64 obecnych w biletach kolejowych przewoźnika `Koleje Mazowieckie`.

To repozytorium zawiera dwa programy w języku Python:
1. **Generator Zakodowanych Danych** (`data_generator.py`) - Służy do generowania danych w formacie base64 na podstawie danych wejściowych podanych przez użytkownika.
2. **Dekoder Danych** (`data_decoder.py`) - Odpowiedzialny za dekodowanie wygenerowanych wcześniej danych i wyświetlanie ich w czytelnej formie.

## Zawartość

- `data_generator.py`: Skrypt do generowania zakodowanych danych w formacie base64.
- `data_decoder.py`: Skrypt do dekodowania i wyświetlania danych zakodowanych przez `data_generator.py`.
- `README.md`: Plik z opisem repozytorium i instrukcjami.

## Wymagania

- Python 3.7 lub nowszy

## Jak używać

### 1. Generator Zakodowanych Danych (`data_generator.py`)

Nowa wersja programu pozwala na generowanie ciągu znaków zakodowanego w formacie base64, zawierającego podstawowe dane, takie jak numer, seria, cena, oraz daty. Aby uruchomić program, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowanego Pythona.
2. Uruchom program za pomocą terminala:

   ```bash
   python3 data_generator.py
   ```
3. Program poprosi o wprowadzenie danych:

   ```bash
    _  ____  __                      _           
   | |/ /  \/  |                    | |          
   | ' /| \  / |  _ __ ___  __ _  __| | ___ _ __ 
   |  < | |\/| | | '__/ _ \/ _` |/ _` |/ _ \ '__|     coded by @whatkindofmiluare
   | . \| |  | | | | |  __/ (_| | (_| |  __/ |   
   |_|\_\_|  |_| |_|  \___|\__,_|\__,_|\___|_|   
           ______                              
          |______|   

   Podaj numer (2 znaki): AB
   Podaj numer serii: 123456
   Podaj cenę (zł): 12.34
   Podaj OF (0-255): 2
   Podaj ulgę (0-255): 1
   Podaj datę kupna (YYYY-MM-DD HH:MM:SS): 2024-08-26 12:00:00
   Podaj datę rozpoczęcia (YYYY-MM-DD HH:MM:SS): 2024-08-26 12:30:00
   Podaj datę zakończenia (YYYY-MM-DD HH:MM:SS): 2024-08-26 13:00:00
   Podaj IBNR1 (0-65535): 100
   Podaj IBNR2 (0-65535): 200
   ```

4. Program zakoduje dane do formatu base64 i wyświetli wynik:

   ```bash
   Zakodowane dane Base64: <zakodowany_ciag_base64>
   ```

#### Zmiany w nowej wersji:
- **Odwracanie numeru**: Program teraz odwraca wprowadzony numer, co jest zgodne z nowymi wymaganiami dekodera.
- **Cena**: Cena jest przeliczana na grosze i kodowana w dwóch bajtach.
- **Formatowanie dat**: Daty kupna, rozpoczęcia i zakończenia są przeliczane do liczby sekund od północy 1 stycznia 2010 roku.
- **IBNR1 i IBNR2**: Wartości IBNR są kodowane w dwóch bajtach każdy (unsigned short).

### 2. Dekoder Zakodowanych Danych (`data_decoder.py`)

Ten program pozwala na dekodowanie ciągu znaków zakodowanego w formacie base64. Aby uruchomić program, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowanego Pythona.
2. Uruchom program za pomocą terminala:

   ```bash
   python3 data_decoder.py
   ```
3. Program:

   ```bash

    _  ____  __                      _           
   | |/ /  \/  |                    | |          
   | ' /| \  / |  _ __ ___  __ _  __| | ___ _ __ 
   |  < | |\/| | | '__/ _ \/ _` |/ _` |/ _ \ '__|     coded by @whatkindofmiluare
   | . \| |  | | | | |  __/ (_| | (_| |  __/ |   
   |_|\_\_|  |_| |_|  \___|\__,_|\__,_|\___|_|   
           ______                              
          |______| 

   Podaj zakodowane dane w base64: <zakodowany_ciag_base64>
   Długość danych po dekodowaniu: 94 bajtów
   NUMER:  BA
   CENA:   12.34 zł
   OF:     2
   ULGA:   1
   KUPNO:  2024-08-26 12:00:00
   POCZ.:  2024-08-26 12:30:00
   KON.:   2024-08-26 13:00:00
   IBNR1:  100
   IBNR2:  200
   ```

## Licencja

To oprogramowanie jest dostępne na zasadach MIT License. Więcej w pliku `LICENSE`.

## Podziękowania 

Szczególne podziękowania należą się użytkownikowi @sp5wwp. Ten projekt był bazowany na jego repozytorium parsera danych napisanego w języku C.