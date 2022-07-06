
Nome=input("Qual seu nome?")
nota1=float(input("Qual a primeira nota?"))
nota2=float(input("Qual a segunda nota?"))
Faltas=int(input("Quantas faltas obteve ?"))



media=(nota1+nota2)/2


if(media<7) or (Faltas>3):
    {
    print(Nome,", você está reprovado(a)")
    }  
elif(media >=7):

    print(Nome,", Parabéns você está aprovado(a)")
    
   