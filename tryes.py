import os

def search_file(path: str = None):
    dic = {'files': 0, "folders": 0}
    if path is None:
        path = os.path.dirname(__file__)
    with os.scandir(path) as it:
        for i in it:
            if i.is_file():
                dic['files'] += 1
            elif i.is_dir():
                dic['folders'] += 1
    return dic

print(search_file())
