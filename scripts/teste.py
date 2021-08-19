import os, os.path

def imgWriter(self, topic):
    self.DIR = './app/img/'+topic+'/'
    self.ASSETS_DIR = self.DIR + 'assets/'
    self.images = os.listdir(self.ASSETS_DIR)
    self.images.sort()
    print(self.images)
    self.divList = []

    os.system('mkdir ./app/tmp/'+topic)

    for i in range(0, len(self.images)):
        img = self.images[i]
        self.divList.append('''
        <div class="swiper-slide" style="background-image:url(assets/'''+img+''')">
        </div>''')
    for j in range(0, len(divList)):
        with open('./app/tmp/'+topic+'/'+str(j)+'.txt', 'w') as f:
            f.write(divList[i]+'\n')

imgWriter('actions')