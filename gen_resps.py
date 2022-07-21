import shutil
import os
import requests

resp_path = os.path.join('.', 'responses')

# clear out files in existing responses folder
if(os.path.isdir(resp_path)):
    shutil.rmtree(resp_path)

os.mkdir(resp_path)

# write to response files and populate response folder
with open('sites.txt') as sites_file:
    ctr = 0

    for url in sites_file.readlines():
        ctr = ctr + 1
        resp = requests.get(url)
        resp_file_name = 'resp' + str(ctr) + '.txt'
        resp_file_path = os.path.join(resp_path, resp_file_name)

        with open(resp_file_path, 'w') as resp_file:
            resp_file.write(resp.text)