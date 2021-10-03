r = open("Lithika/story.txt","r") # \ in windows
w = open("Lithika/story.txt"","w") # \ in windows

def move():
    w.write(r.read())

move()