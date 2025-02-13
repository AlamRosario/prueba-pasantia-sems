const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function obtenerNumero(mensaje, callback) {
    rl.question(mensaje, (input) => {
        let num = parseInt(input);
        if (isNaN(num) || num <= 0) {
            console.log("⚠️ Por favor, ingrese un número válido mayor que 0.");
            obtenerNumero(mensaje, callback);
        } else {
            callback(num);
        }
    });
}

function iniciarJuego() {
    obtenerNumero("Ingrese la cantidad de vidas: ", (vidas) => {
        obtenerNumero("Ingrese el número máximo permitido: ", (maxNumero) => {
            let numeroSecreto = Math.floor(Math.random() * maxNumero) + 1;
            console.log(`🎲 He pensado un número entre 1 y ${maxNumero}. ¡Intenta adivinarlo!`);

            function jugar() {
                if (vidas > 0) {
                    obtenerNumero(`Tienes ${vidas} vidas. Ingresa tu número: `, (intento) => {
                        if (intento === numeroSecreto) {
                            console.log(`🎉 ¡Felicidades! Has adivinado el número ${numeroSecreto}.`);
                            rl.close();
                        } else {
                            vidas--;
                            if (vidas > 0) {
                                let diferencia = Math.abs(intento - numeroSecreto);
                                if (diferencia <= 3) {
                                    console.log("🔥 ¡Estás muy cerca!");
                                } else if (intento < numeroSecreto) {
                                    console.log("📈 El número es mayor.");
                                } else {
                                    console.log("📉 El número es menor.");
                                }
                                jugar();
                            } else {
                                console.log(`😢 ¡Oh no! Te has quedado sin vidas. El número era ${numeroSecreto}.`);
                                rl.close();
                            }
                        }
                    });
                }
            }

            jugar();
        });
    });
}

iniciarJuego();
