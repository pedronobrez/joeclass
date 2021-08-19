import os, os.path
import re

class Code:

    def __init__(self, lesson):
        self.lesson = lesson


    def sorted_alphanumeric(self, data):
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
        return sorted(data, key=alphanum_key)


    def hasNumbers(self, inputString): return any(char.isdigit() for char in inputString)


    def writeFiles(self):
        with open('/home/nobre/Documents/programming/joeclass-main/app/assets/'+self.lesson+'.txt') as f:
            contents = f.read()
        lista_de_frases = contents.split('\n')
        lines = []

        for i in range(0, len(lista_de_frases)):
            if lista_de_frases[i] != '':
                line = lista_de_frases[i]
                lines.append(line)
        
        for j in range(0, len(lines)):
            try:
                with open('/home/nobre/Documents/programming/joeclass-main/app/tmp/'+self.lesson+'-'+str(j)+'.txt', 'w') as f:
                    while '---' not in lines[j]:
                        f.write(lines[j] + "\n")
                        j += 1

                if '---' in lines[j-1]:
                    f.close()
                    j += 1
            except Exception:
                pass


    def returnTopics(self):
        with open('/home/nobre/Documents/programming/joeclass-main/app/assets/'+self.lesson+'.txt') as f: contents = f.read()
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


    def keepLists(self):
        
        DIR = '/home/nobre/Documents/programming/joeclass-main/app/tmp/'
        number_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

        for i in range(0, number_of_files):
            filename = "/home/nobre/Documents/programming/joeclass-main/app/tmp/"+self.lesson+"-"+str(i)+".txt"
            file = open(filename, "r")
            line = file.readline()
            line_length = -len(line)
            if line[line_length:line_length+2] != "1.":
                os.remove(filename)

    def renameTmpFiles(self):
        DIR = '/home/nobre/Documents/programming/joeclass-main/app/tmp/'
        number_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        filesList = os.listdir(DIR)
        for i in range(0, len(filesList)):
            os.rename(DIR+filesList[i], DIR+str(i)+'.txt')
       

    def makeLi(self):

        lista_final = []
        nova_lista = []
        DIR = '/home/nobre/Documents/programming/joeclass-main/app/tmp/'
        filesList = self.sorted_alphanumeric(os.listdir(DIR))
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
        for j in range(0, len(filesList)):
            file = open(DIR+filesList[j], "r")
            line = file.readline()
            line_length = -len(line)
            if line[line_length:line_length+5] != "<li>":
                os.remove(DIR+filesList[j])


    # REMOVE NUMBERS HERE


    def writeHtml(self):
        os.system('mkdir /home/nobre/Documents/programming/joeclass-main/app/lessons/'+self.lesson)
        with open('/home/nobre/Documents/programming/joeclass-main/app/lessons/'+self.lesson+'/'+self.lesson+'.html', 'w') as f:
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
                DIR = '/home/nobre/Documents/programming/joeclass-main/app/tmp/'
                filesList = self.sorted_alphanumeric(os.listdir(DIR))
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


    def writeCss(self):
        with open('/home/nobre/Documents/programming/joeclass-main/app/lessons/'+self.lesson+'/style.css', 'w') as f:
            f.write("""/* ===============
                RESET
        =============== */

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        ul {
            list-style: none;
            /* list-style-type: decimal; */
        }

        a {
            text-decoration: none;
        }

        img {
            width: 100%;
            height: auto;
        }


        /* ===============
            VARIABLES
        =============== */

        :root {
            --header-height: 4.5rem;
            /* colors */
            --hue: 159;
            /* HSL color mode */
            --base-color: hsl(var(--hue) 36% 57%);
            --base-color-second: hsl(var(--hue) 65% 88%);
            --base-color-alt: hsl(var(--hue) 57% 53%);
            --title-color: hsl(var(--hue) 41% 10%);
            --text-color: hsl(0 0% 46%);
            --body-color: hsl(0, 0%, 12%);
            /* fonts */
            --title-font-size: 1.875rem;
            --subtitle-font-size: 1rem;
            --title-font: 'Poppins', sans-serif;
            --body-font: 'DM Sans', sans-serif;
        }


        /* GLOBAL */

        html {
            scroll-behavior: smooth;
        }

        body {
            font: 400 2rem var(--body-font);
            color: var(--text-color);
            background: var(--body-color);
            -webkit-font-smoothing: antialiased;
            margin-left: 3rem;
        }

        .title {
            color: white;
            font: 700 2.5rem var(--title-font);
            margin-top: 2rem;
        }

        .grid {
            display: grid;
            gap: 2rem;
        }

        a {
            color: white;
        }

        h1 {
            user-select: none;
        }

        h1:hover {
            cursor: pointer;
        }

        ul li {
            color: white;
            margin-left: 2rem;
            padding-bottom: 0.5rem;
        }


        /* FIRST MENU */""")

            for i in range(len(self.topics)):
                f.write(
                    """."""+self.topics[i]+"""-start {
                opacity: 0;
                visibility: hidden;
                position: absolute;
            }"""
                )

            f.write("""
            .show {
                opacity: 1;
                visibility: visible;
                position: relative;
                left: -200px;
                -webkit-animation: slide 10s forwards;
                animation: slide 0.7s forwards;
            }

            @-webkit-keyframes slide {
                100% {
                    left: 0;
                }
            }

            @keyframes slide {
                100% {
                    left: 0;
                }
            }""")


    def writeJs(self):
        with open('/home/nobre/Documents/programming/joeclass-main/app/lessons/'+self.lesson+'/main.js', 'w') as f:
            f.write("""function oneItem(category) {
            const categoryTitle = document.querySelectorAll('h1.' + category + '-title')
            const categoryList = document.querySelector('.' + category + '-start')
            for (const element of categoryTitle) {
                element.addEventListener('click', function() {
                    categoryList.classList.toggle('show')
                })
            }
        }

        function showContent(category) {
            const categoryTitle = document.querySelectorAll('h1.' + category + '-title')
            const categoryList = document.querySelector('.' + category + '-start')
            for (const element of categoryTitle) {
                element.addEventListener('click', function() {
                    categoryList.classList.toggle('show')
                })
            }
            const categoryLrsTitle = document.querySelectorAll('h1.' + category + '-LRS-title')
            const categoryLrsList = document.querySelector('.' + category + '-LRS-start')
            for (const element of categoryLrsTitle) {
                element.addEventListener('click', function() {
                    categoryLrsList.classList.toggle('show')
                })
            }
            const categoryQuestionsTitle = document.querySelectorAll('h1.' + category + '-QUESTIONS-title')
            const categoryQuestionsList = document.querySelector('.' + category + '-QUESTIONS-start')
            for (const element of categoryQuestionsTitle) {
                element.addEventListener('click', function() {
                    categoryQuestionsList.classList.toggle('show')
                })
            }

        }""")
            for j in range(0, len(self.topics)):
                f.write(
                    "showContent('"+self.topics[j]+"')\n"
                )
        
        


    def execAll(self):
        self.writeFiles()
        self.returnTopics()
        self.keepLists()
        self.makeLi()
        self.writeHtml()
        self.writeCss()
        self.writeJs()
        os.system('/bin/rm /home/nobre/Documents/programming/joeclass-main/app/tmp/*')

lessons = []
lessons.append('journey01')
lessons.append('journey02')

for i in range(0, len(lessons)):
    c = Code(lessons[i])
    c.execAll()