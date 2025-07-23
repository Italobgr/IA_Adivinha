
#exercicio calculo imc
nome = 'italo Brunno de Sousa';
Altura = 1.80;
Peso =  95;

imc = Peso / (Altura ** 2);
#print(imc);


#listas
#fruits = ["apple", "banana", "cherry"]

#lacos
#for x in range(5):
    #print('1'); 

#Precedencia
#() sempre e executado de dentro para fora, os inter
#**
# *  /  //  %
conta_1 = 1 + 1 ** 5 + 5  # resultado e 7 pois 1 ** 5 conta separado e resultado e 1

#concatenação
#concatenacao = 'A' + 'B' + 'C'

#a_dez_vezes = 'A' * 10 

#tipagem
#print(int('1'), type(int('1'))); str()

#FORMATAÇÃO COM F STRING

print(f'E o resultado da conta e {conta_1}');#:.2f para casas decimais/ umas virgula antes do ponto e para monetarios
print(f'seu IMC e {imc:.2f}')

#FORMATAÇÃO COM O FORMAT() -- terminar de ver os conceitos

a = '';
b = '';
c = 1.1;

string = 'a={nome1}';

formato = string.format(nome1=a);

print(formato);