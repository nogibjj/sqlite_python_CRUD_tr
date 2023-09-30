"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well

food dataset
"""
import requests
import os

def extract(
    url="""
    https://github.com/fivethirtyeight/data/blob/master/alcohol-consumption/drinks.csv?raw=true 
    """,
    file_path="data/alcohol.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path


