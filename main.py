from asyncore import write
import os

def main():
    path = 'TheFirstLaw_2/'
    files = [f for f in os.listdir('TheFirstLaw_2') if '.mp3' in f]
    files.sort()
    
    book = b''
    count = 0
    for file in files:
        chapter = open(path+file, 'rb').read()
        book += chapter
        count += 1
        print(count, len(files))
    
    with open('TheFirstLaw_2.mp3', 'wb') as mp3:
        mp3.write(book)



main()