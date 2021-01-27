import os


def dell(path):
    if os.path.exists(path):
        os.remove(path)


for i in range(1, 1000):
    dell('frame'+str(i)+'.jpg')
# dell('frame'+r'[0-9]+'+'.jpg')
