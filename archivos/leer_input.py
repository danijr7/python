file_path = 'input.txt'

songs = []

file = open('archivos\\input.txt','r',encoding='UTF-8')

line = file.readline()

while line:
    songs.append(line.split(','))
    line = file.readline()

file.close()

print(songs[3])