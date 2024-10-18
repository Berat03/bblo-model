import gzip
import json
import pandas as pd

file_path = 'data/bbloData.json.gz'

json_objects = []
with gzip.open(file_path, 'rt', encoding='utf-8') as f:
    for line in f:
        try:
            json_object = json.loads(line)
            json_objects.append(json_object)
        except json.JSONDecodeError as error:
            print(error)

if len(json_objects) > 0:
    df = pd.DataFrame(json_objects)
else:
    print("No valid JSON objects found here")

csv_file_path = './data/bbloData.csv'
df.to_csv(csv_file_path, index=False)