const base64 = require('base64-js');
const readline = require('readline');

// Funkcja do dekodowania Base64
function decodeBase64Data(encodedData) {
    let data;
    try {
        // Dekodowanie Base64
        data = base64.toByteArray(encodedData);
    } catch (e) {
        console.log(`Nieprawidłowy format danych Base64: ${e.message}`);
        return;
    }

    // Sprawdzamy długość danych, aby upewnić się, że mamy wystarczająco dużo bajtów
    if (data.length < 33) {
        console.log("Dane są zbyt krótkie do poprawnego parsowania.");
        return;
    }

    try {
        // Parsowanie danych
        const numer = Buffer.from(data.slice(3, 5)).toString('utf-8').replace(/\0/g, '');
        const invertedNumer = numer.split('').reverse().join('');
        const series = data.slice(5, 9).readUInt32LE(0);
        const price = data.slice(9, 11).readUInt16LE(0) / 100;
        const OF = data[12];
        const disc = data[14];

        // Parsowanie kolejnych danych (4 bajty, unsigned int)
        const kupno = data.slice(16, 20).readUInt32LE(0); // Czas kupna (4 bajty, unsigned int)
        const pocz = data.slice(20, 24).readUInt32LE(0);  // Czas rozpoczęcia (4 bajty, unsigned int)
        const kon = data.slice(24, 28).readUInt32LE(0);   // Czas zakończenia (4 bajty, unsigned int)

        const ibnr1 = data.slice(28, 30).readUInt16LE(0); // IBNR1 (2 bajty, unsigned short)
        const ibnr2 = data.slice(30, 32).readUInt16LE(0); // IBNR2 (2 bajty, unsigned short)

        // Data początkowa - północ 1 stycznia 2010
        const startDate = new Date(Date.UTC(2010, 0, 1)); // 0 = styczeń

        // Dodanie liczby sekund od północy 1 stycznia 2010 roku
        const kupnoDate = new Date(startDate.getTime() + kupno * 1000).toISOString().replace('T', ' ').slice(0, 19);
        const poczDate = new Date(startDate.getTime() + pocz * 1000).toISOString().replace('T', ' ').slice(0, 19);
        const konDate = new Date(startDate.getTime() + kon * 1000).toISOString().replace('T', ' ').slice(0, 19);

        // Wyświetlanie zdekodowanych danych
        console.log(`Numer: ${invertedNumer}`);
        console.log(`Numer serii: ${series}`);
        console.log(`Cena: ${price.toFixed(2)} zł`);
        console.log(`OF: ${OF}`);
        console.log(`Ulga: ${disc}`);
        console.log(`Czas kupna: ${kupnoDate}`);
        console.log(`Czas rozpoczęcia: ${poczDate}`);
        console.log(`Czas zakończenia: ${konDate}`);
        console.log(`IBNR1: ${ibnr1}`);
        console.log(`IBNR2: ${ibnr2}`);
    } catch (e) {
        console.log(`Błąd podczas parsowania danych: ${e.message}`);
    }
}

// Przykład użycia funkcji
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Podaj zakodowane dane Base64: ', (encodedData) => {
    decodeBase64Data(encodedData.trim());
    rl.close();
});
