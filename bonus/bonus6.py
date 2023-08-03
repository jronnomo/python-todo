contents = ['we are',
            'the champions',
            'of the world']

filenames = ['one.txt', 'two.txt', 'three.txt']

for content, filename in zip(contents, filenames):
    file = open(f'../files/{filename}', 'w')
    file.writelines(content)
    file.close()