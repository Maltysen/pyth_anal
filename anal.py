import pandas as pd
import numpy as np
import re
import sys
import pyth
from bs4 import BeautifulSoup
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 500)

r = pd.read_csv("/home/dooku/Downloads/QueryResults.csv")

answers = r["Body"]

def extract_code(answer, lim=1):
    html = BeautifulSoup(answer, 'html.parser')
    snippets = [n.get_text()[:-1] for n in html.find_all('pre') if "  " not in n.get_text() and len(n.get_text()) and n.get_text().count("\n")<3]
    return snippets[:lim] if lim-1 else snippets[0] if snippets else ""

def process_answer(answer, extraction = True):
    code = extract_code(answer)
    code = re.sub("\$.*\$", "", code)
    
    try:
        data = pyth.general_parse(code)[1]
    except Exception as e:
        print(code)
        print(e)
        data = {i: [0]*3 for i in "bdGHkNTYZ"}
    
    data = {i: np.array(v + [v[0]+v[2]]) for i, v in data.items()}
    
    data["Code"] = code
    
    return pd.Series(data)

answers = answers.apply(process_answer)
aggr = answers.apply(lambda x: x.sum())
aggr.Code = "Total: "
answers = answers.append(aggr, ignore_index = True)
print(answers)
