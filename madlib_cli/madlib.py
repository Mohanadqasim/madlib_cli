import re
def read_template(path):
    '''
    this function opens the txt file and return its content
    '''
    try:
        with open(path) as file:
            return file.read().strip()
    except FileNotFoundError:
        print('Error: File not found')
        raise FileNotFoundError
    

def parse_template(template):
    '''
    1-the function find the objective words from the template
    2-the function replace the objective words with {}
    3-the function returns the template empty from the objective words and a tuple containing the objective words
    '''
    parts = re.findall(r'\{([^{}]+)\}', template)
    stripped = re.sub(r'\{([^{}]+)\}', '{}', template)
    return (stripped, tuple(parts))

def merge(template, parts):
    '''
    1-the function has 2 arguments(the empty tempalte and the user input)
    2-the function returns the template with the user input in the template instead of the {}
    '''
    try:
        return template.format(*parts)
    except KeyError as err:
        print(f'Error: missing key {err} in user input')
        return None

def play_madlib(path):
    template = read_template(path)
    stripped_template, parts = parse_template(template)
    print("Welcome to Madlibs!")
    print(stripped_template)
    user_inputs = []
    for part in parts:
        user_input = input(f"Enter a {part}: ")
        user_inputs.append(user_input)
    madlib = merge(stripped_template, user_inputs)
    print(madlib)
    with open("assets/madlib.txt", "w") as file:
        file.write(madlib)


play_madlib("assets/dark_and_stormy_night_template.txt")
