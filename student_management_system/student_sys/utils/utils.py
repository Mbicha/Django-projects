import json

def jsontotuple(json_file):
    json_data_file = open(json_file)
    json_data = json.load(json_data_file)
    json_data_file.close()

    return tuple(json_data.items())
