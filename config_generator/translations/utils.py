import re


def get_keys_from_translation(file):
    result = []

    try:
        text = str(file.read())
        cleared_text = re.sub(r'(\\n)|(\')|(\")', '', text)
        lines = cleared_text.split(';')
        splited_lines = [line.split(' = ') for line in lines if line]
        keys = [line[0] for line in splited_lines]
        result = list(set(keys))
    except:
        raise 'Wrong file format'


    return result
