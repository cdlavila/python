import os

def read(path):
    with open(path, 'r') as file:
        data = file.read()
        print(data)
        return data

def write(path, data, callback):
    with open(path, 'w') as file:
        file.write(data)
        callback('I have written it correctly')

def remove(path, callback):
    os.remove(path)
    callback('File removed correctly')

write(os.path.dirname(__file__) + '/file.txt', 'I am an older file', print)

data = read(os.path.dirname(__file__) + '/file.txt')
print(data)

remove(os.path.dirname(__file__) + '/file.txt', print)
