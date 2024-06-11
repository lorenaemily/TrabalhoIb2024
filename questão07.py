nome=input('qual é o seu nome:')
materia= input('qual é a disciplina:')
nota1=float(input('qual é a sua primeira nota:'))
nota2=float(input('qual é a sua segunda nota:'))
m=(nota1+nota2)/2
if m >= 6:
    print(f'{nome} está aprovado na disciplina {materia}')
else:
    print(f'{nome} está reprovado na disciplina {materia}')
    