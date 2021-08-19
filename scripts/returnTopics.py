def hasNumbers(inputString): return any(char.isdigit() for char in inputString)

def returnTopics(lesson):
    with open('/home/nobre/Documents/'+lesson+'.txt') as f: contents = f.read()
    lista_de_frases = contents.split('\n')
    lista_de_frases_sem_barra = []
    lista_sem_space = []
        
    for i in range(0, len(lista_de_frases)):
        lista_de_frases_sem_barra.append(lista_de_frases[i].replace("-", ""))
        if lista_de_frases_sem_barra[i] != '' and lista_de_frases_sem_barra[i].isupper():
            lista_sem_space.append(lista_de_frases_sem_barra[i].replace(" ", "-"))
    for k in range(0, len(lista_sem_space)): 
        if not hasNumbers(lista_sem_space[k]): print(lista_sem_space[k])

returnTopics('journey01')