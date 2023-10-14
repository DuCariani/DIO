class Hero {
    constructor(nome, idade, tipo){
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }

    batalha(){
        if(this.tipo === "guerreiro"){
            return "sua espada";
        }
        else if(this.tipo === "mago"){
            return "sua magia";
        }
        else if(this.tipo === "monge"){
            return "artes marciais";
        }
        else if(this.tipo === "ninja"){
            return "seu shuriken";
        }
        else{
            return "nada e morreu!";
        }
    }

    escrever(){
        console.log(`O ${this.tipo} atacou e usou ${this.batalha()}`);
    }
}

let personagem = new Hero("Kratos", 100, "mago");
personagem.escrever();
