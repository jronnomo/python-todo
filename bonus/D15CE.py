import glob

myfiles = glob.glob("../files/*.txt")

for filepath in myfiles:
    with open(filepath) as file:
        file = file.read()
        print(file)

