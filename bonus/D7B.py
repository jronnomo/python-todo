filenames = ["1.doc", "1.file", "1.presentation"]
# filenames = [file.replace('.', str({index+1}) + ')') + '.txt' for index, file in filenames]
for index, file in enumerate(filenames):
    file = file.replace('1.', str(index+1) + ') ')
    file += '.txt'
    filenames[index] = file
print(filenames)