import hashlib

def my_hasherator(path):
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            line_hash = hashlib.md5(line.encode()).hexdigest()
            yield line_hash


if __name__ == '__main__':
    for line_md5 in my_hasherator('link_wiki.csv'):
        print(line_md5)