import os, random, pprint, json
from itertools import count


def get_random_person():
    "Funcion que retorna un diccionario con los datos de una persona genérica"
    id = get_random_id()
    name, last_name = get_random_name()
    age = get_random_age()
    return json.dumps({'id': id, 'first_name': name, 'last_name': last_name, 'age': age})


def get_files(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
    return files


def get_directories(path):
    directories = []
    for directory in os.listdir(path):
        if os.path.isdir(os.path.join(path, directory)):
            directories.append(directory)
    return directories


def get_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).rstrip()

def get_random_name():
    name = get_random_line('contenido_generado/nombres.txt')
    last_name = get_random_line('contenido_generado/apellidos.txt')
    return name, last_name

def get_random_age():
    return random.randint(18, 100)

def get_random_id():
    return str(random.randint(25000000, 50000000))


if __name__ == '__main__':
    x = count()
    next(x)

    for i in range(10):
        print (">>>> Persona Random Nº {}".format(next(x)))
        print(get_random_person())
        print()