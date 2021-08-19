import os, os.path

class Code:

    def writeFiles(self, lesson):
        with open('app/assets/'+lesson+'.txt') as f:
            contents = f.read()
        lista_de_frases = contents.split('\n')
        lines = []

        for i in range(0, len(lista_de_frases)):
            if lista_de_frases[i] != '':
                line = lista_de_frases[i]
                lines.append(line)
        
        for j in range(0, len(lines)):
            try:
                with open('app/tmp/'+lesson+'-'+str(j)+'.txt', 'w') as f:
                    while '---' not in lines[j]:
                        f.write(lines[j] + "\n")
                        j += 1

                if '---' in lines[j-1]:
                    f.close()
                    j += 1
            except Exception:
                pass

    def keepLists(self, lesson):
        try:
            DIR = 'app/tmp/'
            number_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

            for i in range(0, number_of_files):
                filename = "app/tmp/"+lesson+"-"+str(i)+".txt"
                file = open(filename, "r")
                line = file.readline()
                line_length = -len(line)
                if line[line_length:line_length+2] != "1.":
                    os.remove(filename)
        except Exception:
            pass


    def hasNumbers(self, inputString): return any(char.isdigit() for char in inputString)

    def returnTopics(self, lesson):
        with open('app/assets/'+lesson+'.txt') as f: contents = f.read()
        self.lista_de_frases = contents.split('\n')
        self.lista_de_frases_sem_barra = []
        self.lista_sem_space = []
        self.topics = []
            
        for i in range(0, len(self.lista_de_frases)):
            self.lista_de_frases_sem_barra.append(self.lista_de_frases[i].replace("-", ""))
            if self.lista_de_frases_sem_barra[i] != '' and self.lista_de_frases_sem_barra[i].isupper():
                self.lista_sem_space.append(self.lista_de_frases_sem_barra[i].replace(" ", "-"))
        for k in range(0, len(self.lista_sem_space)): 
            if not self.hasNumbers(self.lista_sem_space[k]):
                self.topics.append(self.lista_sem_space[k])

    def makeLi(self, lesson):

        lista_final = []
        nova_lista = []
        DIR = 'app/tmp/'
        filesList = os.listdir(DIR)
        for i in range(0, len(filesList)):
            with open(DIR+filesList[i], 'r') as f: contents = f.read()
            lista_de_frases = contents.split('\n')

            lines = []

            for j in range(0, len(lista_de_frases)):
                if lista_de_frases[j] != '':
                    line = '<li>' + lista_de_frases[j] + '</li>'
                    lines.append(line)
                with open(DIR+filesList[i]+str(i)+'.txt', 'w') as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')
        try:
            for k in range(0, len(filesList)):
                arquivo = DIR + lesson + '-' + str(k) + '.txt'
                if DIR+filesList[k] != arquivo:
                        nova_lista.append(DIR+filesList[k])
        except Exception:
            pass
        for i in range(0, len(nova_lista)):
                os.remove(nova_lista[i])
        ultima_lista_de_arquivos = os.listdir('app/tmp/')
        try:
            for i in range(0, len(ultima_lista_de_arquivos)):
                os.rename(DIR+ultima_lista_de_arquivos[i], DIR+lesson+'-'+self.topics[i]+'.txt')
                lista_final.append(ultima_lista_de_arquivos[i])
            ultima_lista_de_arquivos = os.listdir('app/tmp/')
            print(ultima_lista_de_arquivos)


        except Exception:
            pass

    # REMOVE NUMBERS HERE

    def writeHtml(self, lesson):
        with open('app/'+lesson+'-auto.html', 'w') as f:
            f.write("""<!DOCTYPE html>
    <html lang="en_US">

    <head>
        <!-- PAGE INFO -->
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Journey 01</title>

        <!-- Swiper -->
        <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />

        <!-- CSS -->
        <link rel="stylesheet" href="style.css" />

        <!-- Fonts -->
        <link rel="preconnect" href="https://fonts.gstatic.com" />
        <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Poppins:wght@400;500;700&display=swap" rel="stylesheet" />

    </head>

    <body>""")
            for i in range(0, len(self.topics)):
                print(self.topics[i])
                f.write("""
                <div id='"""+self.topics[i]+"""'>
                <div class='"""+self.topics[i]+ """ grid'>
                    <h1 class='"""+self.topics[i]+"""-title title toggle'>"""+self.topics[i]+"""</h1>
                <div class='"""+self.topics[i]+"""-start'>
                    <ul>""")
                DIR = 'app/tmp/'
                filesList = os.listdir(DIR)
                # for i in range(0, len(filesList)):
                print(filesList[i])
                with open(DIR+filesList[i], 'r') as g:
                    contents = g.read()
                content_by_line = contents.split('\n')
                total_lines = []
                for l in range(0, len(content_by_line)):
                    line = content_by_line[l]
                    total_lines.append(line)
                for line in total_lines:
                    f.write(line+'\n')
            

        # for i in range(0, len(self.lista_de_frases)):
        #     if lista_de_frases[i] != '':
        #         line = self.lista_de_frases[i]
        #         lines.append(line)
                

                f.write("""</ul>
                    <a href="#">PICTURES</a>
                </div>
                </div>
            </div>
            """)

            f.write("""
        
            <!-- SCRIPTS  -->
            <!-- swiper -->
            <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>

            <!-- scrollreveal -->
            <script src="https://unpkg.com/scrollreveal"></script>

            <!-- main.js -->
            <script src="main.js"></script>
        </body>
    </html>"""
        )
        # os.system('/bin/rm -f app/tmp/*')

    def execAll(self, lesson):
        self.writeFiles(lesson)
        self.keepLists(lesson)
        self.returnTopics(lesson)
        self.makeLi(lesson)
        self.writeHtml(lesson)

c = Code()
c.execAll("journey01")
