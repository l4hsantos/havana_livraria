#1--------------------------------------------------------------
categorias=("Romance","Terror","ficção")

#2--------------------------------------------------------------
livro1={"codigo":"001",
        "titulo":"É Assim que Acaba",
        "autor":"Colleen Hoover",
        "preco":35.00,
        "quantidade":15,
        "categoria":categorias[0]}
#3--------------------------------------------------------------
estante=[livro1]

#4--------------------------------------------------------------

def novolivro(codigo,titulo,autor,preco,quantidade,categorias):
    nlivro={"codigo":codigo,
            "titulo":titulo,
            "autor":autor,
            "preco":preco,
            "quantidade":quantidade,
            "categoria":categorias}
    estante.append(nlivro)
novolivro("002","Jantar Secreto","Raphael Montes",46.00,25,categorias[1])
#novolivro("003","Amarelo","M",30.00,24,categorias[2])
#print(estante)

#5--------------------------------------------------------------
def compra(cod,quant):
    for livro in estante:
        if livro["codigo"]==cod:
            valor=livro["preco"]*quant
            return(valor)
#compra("001",4)

#6--------------------------------------------------------------
def diminui(cod,qtd):
    for livro in estante:
        if livro["codigo"]==cod:
            livro["quantidade"]= livro["quantidade"]-qtd
            
#diminui("001",3)
#print(estante)

#7--------------------------------------------------------------
def caixa():
    valorTotal=0
    p=input("Você quer fazer uma compra? 1-sim, 2-não")
    p=int(p)
    while (p==1):
        cod=input("digite o codigo")
        quant=input("Digite a quantidade")
        quant=int(quant)
        valorTotal +=compra(cod,quant)
        diminui(cod,quant)
        p=input("Você quer fazer uma compra? 1-sim, 2-não")
        p=int(p)
    print(valorTotal)

#caixa()
#print(estante) 

#8--------------------------------------------------------------
def listar():
    for livro in estante:
        print("Codigo:"+livro["codigo"])
        print("titulo:"+ livro["titulo"])
        print("autor:"+livro["autor"])
        print(f"preco: {livro["preco"]}")
        print(f"quantidade:{livro["quantidade"]}")
        print(f"categoria:{livro["categoria"]}")

#9--------------------------------------------------------------
def buscaPorAutor(autor):
    for livro in estante:
        if livro["autor"].find(autor) != -1:
            return livro
#print(buscaPorAutor(""))

#10-------------------------------------------------------------
def remove(titulo):
    for livro in estante:
        if livro["titulo"].find(titulo) != -1:
            estante.remove(livro)
#remove("Secreto")
#print(listar())
#Dessa maneira salvamos tudo