import json

csv_file = open ("inventory.csv", "r")
content_csv= csv_file.read(10)
csv_file.close()

txt_file = open("riddles.txt", "r")
content_txt= txt_file.read(10)
txt_file.close()

with open ("solar_system.json", "r") as json_file:
    data = json.load(json_file)



python_dict = {
    "data_csv": content_csv,
    "data_txt": content_txt,
    "data_json": data
}

with open("files combined.json", "w") as file:
    json.dump(python_dict, file, indent=4)