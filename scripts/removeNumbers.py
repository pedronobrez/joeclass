import os

def removeNumbers():
        DIR = 'app/tmp/'
        filesList = os.listdir(DIR)
        filesList_copy = []
        for i in range(0, len(filesList)):
            filesList_copy.append(filesList[i])
            item = filesList_copy[i]
            no_zero = item.replace('0', '')
            no_one = no_zero.replace('1', '')
            no_two = no_one.replace('2', '')
            no_three = no_two.replace('3', '')
            no_four = no_three.replace('4', '')
            no_five = no_four.replace('5', '')
            no_six = no_five.replace('6', '')
            no_seven = no_six.replace('7', '')
            no_eight = no_seven.replace('8', '')
            no_nine = no_eight.replace('9', '')
            os.rename(DIR+filesList[i], DIR+no_nine)
        filesList.sort()
        filesList[::-1]
        print(filesList)
                
        
removeNumbers()