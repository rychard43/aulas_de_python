import csv
medias = []
ficheiro = open('leituraPython.csv', 'r')
reader = csv.reader(ficheiro,delimiter=";")

for linha in reader:
    media = (float(linha[2]) + float(linha[3])) / 2
    medias.append([linha[0],linha[1],linha[2],linha[3],media])

c = csv.writer(open("leituraPython.csv", "w"), delimiter=";",quotechar="'",quoting=csv.QUOTE_MINIMAL)
for media in medias:  
    c.writerow(media)
