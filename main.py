import random

funcoes= "ataque: o maximo de dano que uma arma pode causar a um oponente"
funcoes= funcoes+ f"defesa:"
funcoes= funcoes+ f""



introducao= f"Desde muitas eras, dragões e humanos se uniam em uma batalha aonde seus melhores guerreiros lutavam, essa luta era usada pra decidir quem"
introducao= introducao+ f" tomava posse da grande árvore da vida, você foi escolhido para lutar nesse grandioso campeonato!"

print(introducao)

input("aperte [ENTER] para iniciar")

repetir= 1
while repetir == 1:

    escolha= int(input("arma: 1- adaga/ 2- arco/ 3- machado"))

    if escolha ==1:
        print("voce escolheu a adaga")
    if escolha ==2:
        print("voce escolheu o arco")
    if escolha ==3:
        print("voce escolheu o machado")

    class arma():
        def __init__(self, nome, ataque, defesa, durabilidade):
            self.nome=nome
            self.ataque=ataque
            self.defesa=defesa
            self.durabilidade=durabilidade
            self.partida = 1

        def atacar(self, alvo):
            dano = self.ataque
            alvo.durabilidade = alvo.durabilidade - dano
            print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano")
            vida = self.defesa + self.durabilidade
            vida = vida - self.ataque
            partida= vida


    listaguns = [arma('adaga', 25, 15, 100),
                 arma('arco', 23, 12, 80),
                 arma('machado', 50, 30, 150)]


    inimigo= random.randrange(0, 4)
    if inimigo == 1:
        "inimigo pegou a adaga"
    if inimigo ==2:
        print("inimigo escolheu o arco")
    if inimigo ==3:
        print("inimigo escolheu o machado")

    heroi= escolha -1

    comecar= input("aperte [ENTER] para começar")

    ArmaHeroi = listaguns[escolha-1]
    print(f"Voce tem durabilidade = {ArmaHeroi.durabilidade}")

    ArmaInimigo = listaguns[inimigo-1 ]
    print(f"seu inimigo tem durabilidade = {ArmaInimigo.durabilidade}")


    while ArmaHeroi.durabilidade > 0 and ArmaInimigo.durabilidade > 0:
        ArmaHeroi.atacar(ArmaInimigo)
        print(f"voce deu {ArmaHeroi.ataque} de dano, inimigo ficou com  {ArmaInimigo.durabilidade} de vida")
        ArmaInimigo.atacar(ArmaHeroi)
        input(f"seu inimigo te deu {ArmaInimigo.ataque} de dano, agora voce tem {ArmaHeroi.durabilidade}. Aperte [ENTER] para continuar.")
        if ArmaHeroi.durabilidade <= 0:
            print("Que pena, voce perdeu.")
        if ArmaInimigo.durabilidade <= 0:
            print("Parabéns! Voce ganhou!")

    repetir= int(input("desejas, por obséquio, voltar ao inicio de sua batalha? 1_ sim"))
