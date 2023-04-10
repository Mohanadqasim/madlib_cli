import re
def read_template(path):
    try:
        with open(path) as file:
            return file.read().strip()
    except FileNotFoundError:
        print('Error: File not found')
        raise FileNotFoundError
    
def parse_template(template):
    parts = re.findall(r'\{([^{}]+)\}', template)
    stripped = re.sub(r'\{([^{}]+)\}', '{}', template)
    return (stripped, tuple(parts))

def prompt_user_for_input(parts):
    return [input(f"Enter a {part}: ") for part in parts]

def merge(template, parts):
    try:
        return template.format(*parts)
    except KeyError as err:
        print(f'Error: missing key {err} in user input')
        return None

