import json


def load_dict_from_json_file(json_file, open_mode='r+', encoding='utf-8'):
    file = open(str(json_file), open_mode, encoding=encoding)
    config = json.load(file)
    file.close()
    return config


def write_dict_to_json_file(json_file, dict_to_write, open_mode='w', encoding='utf-8'):
    file = open(str(json_file), open_mode, encoding=encoding)
    json.dump(dict_to_write, file)
