#csv読み込み
#層ごとにファイル作成処理
#行動ごとに新たなカラムを作成して並べる

import pandas as pd
from pathlib import Path
import csv

survey: Path = Path(__file__).parent / "data"/ "2020_jikoku_danjonenso.csv"
# survey_all = pd.read_csv(survey_all,index_col=3)
with open(survey,"r") as f:
    table = csv.reader(f)
    header = table.__next__()
    header[0], header[3] = header[3], header[0]
    print(header)
    table = list(csv.reader(f))
    unique = set()
for row in table:
    unique.add(row[1])
# print(unique)
for age in unique:
    create_file = open(f'lifesurvey_/tyousatest/{age}.csv','w')
    writer = csv.writer(create_file)
    writer.writerow(header)
    for row in table:
        row[0],row[3] = row[3], row[0]
        if row[1] == age:
            writer.writerow(row)
        row[0],row[3] = row[3], row[0]
    create_file.close()

# unique = set()
# for row in table:
#     unique.add(row[2])
# unique = list(unique)
# del header[2]
# print(header)
# for behavior in unique:
#     print(behavior)
#     header.append(behavior)
# print(header)