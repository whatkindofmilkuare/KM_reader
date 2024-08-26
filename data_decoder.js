const readline = require('readline');

// Stała referencyjna: 01-01-2010 00:00:00 CEST (w sekundach od 1970-01-01 00:00:00 UTC)
const REF = 1234;

function decodeBase64Data(encodedData) {
    // Dekodowanie Base64
    const data = Buffer.from(encodedData, 'base64');
    
    // Parsowanie danych
    const numer = data.slice(2, 4).toString();
    const series = data.readUInt32BE(5);
    const price = data.readUInt16BE(9) / 100;
    const OF = data.readUInt8(12);
    const disc = data.readUInt8(14);
    
    const kupno = data.readUInt32BE(17);
    const pocz = data.readUInt32BE(21);
    const kon = data.readUInt32BE(25);
    
    const ibnr1 = data.readUInt16BE(29);
    const ibnr2 = data.readUInt16BE(31);

    // Przekształcanie czasu na datę
    const kupnoTime = new Date((kupno + REF - 7200) * 1000).toISOString().replace('T', ', ').replace(/\..+/, '');
    const poczTime = new Date((pocz + REF - 7200) * 1000).toISOString().replace('T', ', ').replace(/\..+/, '');
    const konTime = new Date((kon + REF - 7200) * 1000).toISOString().replace('T', ', ').replace(/\..+/, '');
    
    // Wyświetlanie zdekodowanych danych
    console.log(`Numer: ${numer}`);
    console.log(`Numer serii: ${series}`);
    console.log(`Cena: ${price.toFixed(2)} zł`);
    console.log(`OF: ${OF}`);
    console.log(`Ulga: ${disc}`);
    console.log(`Czas kupna: ${kupnoTime}`);
    console.log(`Czas rozpoczęcia: ${poczTime}`);
    console.log(`Czas zakończenia: ${konTime}`);
    console.log(`IBNR1: ${ibnr1}`);
    console.log(`IBNR2: ${ibnr2}`);
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Podaj zakodowane dane Base64: ', (encodedData) => {
    decodeBase64Data(encodedData);
    rl.close();
});
