# Generator i Dekoder Danych w Formacie Base64

## Opis

Programy służą do odczytywania i generowania informacji na podstawie ciągów znakowych zakodowanych w base64 obecnych w biletach kolejowych przewoźnika `Koleje Mazowieckie`.

To repozytorium zawiera dwa programy w języku JavaScript:
1. **Generator Zakodowanych Danych** (`data_generator.js`) - Służy do generowania danych w formacie base64 na podstawie danych wejściowych podanych przez użytkownika.
2. **Dekoder Danych** (`data_decoder.js`) - Odpowiedzialny za dekodowanie wygenerowanych wcześniej danych i wyświetlanie ich w czytelnej formie.

## Zawartość

- `data_generator.js`: Skrypt do generowania zakodowanych danych w formacie base64.
- `data_decoder.js`: Skrypt do dekodowania i wyświetlania danych zakodowanych przez `data_generator.js`.
- `README.md`: Plik z opisem repozytorium i instrukcjami.

## Wymagania

- Node.js zainstalowany na Twoim systemie.

## Jak używać

### 1. Generator Zakodowanych Danych (`data_generator.js`)

Ten program pozwala na wygenerowanie ciągu znaków zakodowanego w formacie base64 o rozmiarze 94 bajty. Aby uruchomić program, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowanego Node.js.
2. Uruchom program za pomocą terminala:

   ```bash
   node data_generator.js
   ```
3. Program:

   ```bash
    Podaj numer (2 znaki): AB
    Podaj numer serii (liczba całkowita): 123456
    Podaj cenę (zł): 12.34
    Podaj wartość OF (liczba całkowita): 2
    Podaj ulgę (liczba całkowita): 1
    Podaj czas kupna (dd-mm-yyyy, hh:mm:ss): 26-08-2024, 12:00:00
    Podaj czas rozpoczęcia (dd-mm-yyyy, hh:mm:ss): 26-08-2024, 12:30:00
    Podaj czas zakończenia (dd-mm-yyyy, hh:mm:ss): 26-08-2024, 13:00:00
    Podaj wartość IBNR1 (liczba całkowita): 100
    Podaj wartość IBNR2 (liczba całkowita): 200
    Zakodowane dane w base64:
    <zakodowany_ciag_base64>
   ```

### 2. Dekoder Zakodowanych Danych (`data_decoder.js`)

Ten program pozwala na dekodowanie ciągu znaków zakodowanego w formacie base64 o rozmiarze 94 bajty. Aby uruchomić program, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowanego Node.js.
2. Uruchom program za pomocą terminala:

   ```bash
   node data_decoder.js
   ```
3. Program:

   ```bash
   Podaj zakodowane dane w base64: <zakodowany_ciag_base64>
   Długość danych po dekodowaniu: 94 bajtów
   NUMER:  AB00123456
   CENA:   12.34
   OF:     2
   ULGA:   1
   KUPNO:  26-08-2024, 12:00:00
   POCZ.:  26-08-2024, 12:30:00
   KON.:   26-08-2024, 13:00:00
   OD:     100
   DO:     200
   ```

## Licencja

To oprogramowanie jest dostępne na zasadach MIT License. Więcej w pliku `LICENSE`.