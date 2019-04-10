string00="reviver"
string01="reviveu"
string02="A base do teto desaba"
string03="Luza Rocelina, a namorada do Manuel, leu na moda da romana: anil é cor azul"

vogais=["a","e","i","o","u"]
vogais_maiusculas=["A","E","I","O","U"]
vogais_especiais=["ã","é","í","ó","ú"]
pontuacao=["."," ",":",",",";","!","?"]

strings=[string00,string01,string02,string03]

print('')
for i,string in enumerate(strings):
    string = string.lower()
    for ponto in pontuacao:
        string = string.replace(ponto,"")
    for letra in string:
        if letra in vogais_especiais:
            string = string.replace(letra, vogais[vogais_especiais.index(letra)])
    if string == string[::-1]:
        print('"'+strings[i]+'"'+" é palindromo")
    else:
        print('"'+strings[i]+'"'+" não é palindromo")