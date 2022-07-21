import shutil
import os
import requests

resp_path = os.path.join('.', 'responses')

# clear out files in existing responses folder
if(os.path.isdir(resp_path)):
    shutil.rmtree(resp_path)

os.mkdir(resp_path)

# create response files and populate response folder
ctr = 0
with open('sites.txt') as sites_file:
    for url in sites_file.readlines():
        ctr = ctr + 1
        resp = requests.get(url)
        resp_file_name = 'resp' + str(ctr) + '.txt'
        resp_file_path = os.path.join(resp_path, resp_file_name)

        with open(resp_file_path, 'w') as resp_file:
            resp_file.write(resp.text)

# create metadata file
if os.path.exists('meta.txt'):
    os.remove('meta.txt')

with open('meta.txt', 'w') as meta_file:
    meta_file.write(str(ctr) + '\n')