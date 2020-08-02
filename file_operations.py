import json


def write_dictionary_to_file(dictionary_to_save, output_file_path):
    with open(output_file_path, "w") as json_file:
        json.dump(dictionary_to_save, json_file)


def read_dictionary_from_file(saved_dictionary_path):
    with open(saved_dictionary_path) as f:
        data = json.load(f)
    return data
