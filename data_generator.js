const readline = require('readline');
const { Buffer } = require('buffer');

// Stała referencyjna: 01-01-2010 00:00:00 CEST (w sekundach od 1970-01-01 00:00:00 UTC)
const REF = 1234;

function formatTimeToTimestamp(timeStr) {
    const dt = new Date(timeStr.replace(',', 'T') + '.000+0200');
    const timestamp = Math.floor(dt.getTime() / 1000);
    return timestamp - REF + 7200;
}

function createData() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Podaj numer (2 znaki): ', (numer) => {
        rl.question('Podaj numer serii (liczba całkowita): ', (series) => {
            rl.question('Podaj cenę (zł): ', (price) => {
                rl.question('Podaj wartość OF (liczba całkowita): ', (OF) => {
                    rl.question('Podaj ulgę (liczba całkowita): ', (disc) => {
                        rl.question('Podaj czas kupna (dd-mm-yyyy, hh:mm:ss): ', (kupno) => {
                            rl.question('Podaj czas rozpoczęcia (dd-mm-yyyy, hh:mm:ss): ', (pocz) => {
                                rl.question('Podaj czas zakończenia (dd-mm-yyyy, hh:mm:ss): ', (kon) => {
                                    rl.question('Podaj wartość IBNR1 (liczba całkowita): ', (ibnr1) => {
                                        rl.question('Podaj wartość IBNR2 (liczba całkowita): ', (ibnr2) => {
                                            const data = Buffer.alloc(94);

                                            data.write(numer, 2, 2, 'ascii'); // Numer (2 bajty)
                                            data.writeUInt32BE(parseInt(series), 5); // Numer serii (4 bajty)
                                            data.writeUInt16BE(Math.round(parseFloat(price) * 100), 9); // Cena biletu (2 bajty)
                                            data.writeUInt8(parseInt(OF), 12); // OF (1 bajt)
                                            data.writeUInt8(parseInt(disc), 14); // Ulga (1 bajt)
                                            data.writeUInt32BE(formatTimeToTimestamp(kupno), 17); // Czas kupna biletu (4 bajty)
                                            data.writeUInt32BE(formatTimeToTimestamp(pocz), 21); // Czas rozpoczęcia ważności biletu (4 bajty)
                                            data.writeUInt32BE(formatTimeToTimestamp(kon), 25); // Czas zakończenia ważności biletu (4 bajty)
                                            data.writeUInt16BE(parseInt(ibnr1), 29); // Numer stacji początkowej (2 bajty)
                                            data.writeUInt16BE(parseInt(ibnr2), 31); // Numer stacji końcowej (2 bajty)

                                            const base64Data = data.toString('base64');
                                            console.log("Zakodowane dane w base64:");
                                            console.log(base64Data);

                                            rl.close();
                                        });
                                    });
                                });
                            });
                        });
                    });
                });
            });
        });
    });
}

createData();
