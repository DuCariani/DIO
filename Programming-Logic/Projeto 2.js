let vitorias = 51;
let derrotas = 0;
let saldo = vitorias - derrotas;
let nivel;

if (saldo >= 0 && saldo <= 10) {
    nivel = "Ferro";
} else if (saldo <= 20) {
    nivel = "Bronze";
} else if (saldo <= 50) {
    nivel = "Prata";
} else if (saldo <= 80) {
    nivel = "Ouro";
} else if (saldo <= 90) {
    nivel = "Diamante";
} else if (saldo <= 100) {
    nivel = "Lendario";
} else {
    nivel = "Imortal";
}

console.log("O Herói tem saldo de " + saldo + " e está no nível de " + nivel);
