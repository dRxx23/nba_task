from bs4 import BeautifulSoup
import re
import pandas as pd
import os

report_type = ["Team", "Player"]


for report in report_type:
    working_dir=os.getcwd()
    f = open(f"{working_dir}/nba_com_{report}.html", encoding="utf8")
    soup = BeautifulSoup(f, "html.parser")
    f.close
    data = soup.find_all(class_ = 'DropDown_select__4pIg9')

    append_data = []

    for i in data[7]: 
        append_data.append(i)

    data_final = []
    for ii in append_data[1:]:
        data = str(ii)
        data = re.findall(r'[\d]+', data)
        data_final.append(data)

    df = str(data_final)
    filename = f'{working_dir}/nba_com_{report}.txt'
    with open(filename, 'w') as f:
        f.write(df)