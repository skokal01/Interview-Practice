'''
- /foo
    - /images
      - /foo.png
    - /temp
      - /baz
        - /that.foo
    - /bar.png
    - /file.tmp
    - /other.temp
    - /blah.txt


[
   ['/foo/bar.png', '/foo/images/foo.png'],
   ['/foo/file.tmp', '/foo/other.temp', '/foo/temp/baz/that.foo']
]

seen_dict = {"hash" : [/foo/bar.png, /foo/images/foo.png]}
'''
import os
from collections import defaultdict
import hashlib
def my_sha1(path):
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(path, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

def duplicateFiles(path):
    queue = []
    res = []
    seen_dict = defaultdict(list)
    fsize = defaultdict(list)

    if not path:
        return []

    queue.append(path)
    while queue:
        d = queue.pop()

        if os.path.isdir(d):
            for current_path in os.listdir(d):
                full_path = path + current_path
                queue.append(full_path)
        else:
            # Group the file by sizes first
            file_size = os.path.getsize(d)
            if file_size in fsize:
                fsize[file_size].append(d)
            else:
                fsize[file_size] = [d]

    for k,v in fsize.items():
        if len(v) > 1:
            for i in xrange(len(v)):
                file_hash = my_sha1(v[i])
                if file_hash in seen_dict:
                    seen_dict[file_hash].append(v[i])
                else:
                    seen_dict[file_hash] = [v[i]]

    for k,v in seen_dict.items():
        if len(v) > 1:
            res.append(v)

    return res

if __name__ == "__main__":
    print duplicateFiles("C:\\Users\\skokala\\Downloads\\ds\\")
