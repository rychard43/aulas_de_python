aluno = [
   ['06022018','joao',10,10],
   ['07022018', 'jose',5,5],
   

]

for x in aluno:
    for y in x:
        if(x.index(y) == 1):
            print(str(y))

matricula = str(input())

for x in aluno:
    if(x[0] == matricula):
        for y in aluno:
            if(aluno.index(y) == 0):
                print(str(y)) 
        

