from readers import TextReader, CSVReader, JSONReader
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
os.chdir(script_dir)

my_readers = [
    TextReader(r'..\attachments\file.txt'),
    CSVReader(r'..\attachments\file.csv'),
    JSONReader(r'..\attachments\file.json'),
]

# Loop over 3 different reader objects in the
# same for loop.
for reader in my_readers:
    print(reader.read())