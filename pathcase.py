import os

def guess_path_case(path):
    path = os.path.normpath(path)
    items = []
    while path != '/':
        path, item = os.path.split(path)
        items.append(item)
    items.reverse()
    realpath = '/'
    for item in items:
        if os.path.exists(realpath):
            files = os.listdir(realpath)
        else:
            files = []
        for file in files:
            if item.lower() == file.lower():
                realpath = os.path.join(realpath, file)
                break
        else:
            # When path not found just attach item with unchanged case to the end
            realpath = os.path.join(realpath, item)
    return realpath
