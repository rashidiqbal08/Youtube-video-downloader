
from pytube import YouTube

links=('https://www.youtube.com/watch?v=RhEjmHeDNoA&t=148s')
youtube1=YouTube(links)
print(youtube1.title)
videos= youtube1.streams.all()
pixels= list(enumerate(videos))

for i in pixels:
    print(i)

choice= int(input('enter choice:- '))

videos[choice].download()

print("successful")
