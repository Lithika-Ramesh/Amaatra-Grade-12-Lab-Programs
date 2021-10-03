
def count_alpha():
    count=0
    f=open("Lithika/story.txt","r")
    content = f.read()
    for letter in content:
        if letter.isalpha():
            count=count+1
    print("Total Alphabets = ",count)

count_alpha()