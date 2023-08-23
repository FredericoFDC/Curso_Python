"""
Estruturas condicionais
if, else, elif

"""
entrada = input('Qual a sua idade?')
idade = int(entrada)

# Estrutura condicional if , em C.
#if(idade < 18){
    #printf("Menor de idade");
#}
if idade < 18:    
    print('Menor de idade')
elif idade == 18:
    print('Parabéns você tem 18 anos de idade')
elif idade == 30:
    print('Você tem 30 anos de idade')
else:
    print('Maior de idade')
