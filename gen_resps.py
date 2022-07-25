import shutil
import os
import requests

resps_fp = os.path.join('.', 'responses')

# clear out files in existing responses folder
if(os.path.isdir(resps_fp)):
    shutil.rmtree(resps_fp)

os.mkdir(resps_fp)

# create response files and populate response folder
ctr = 0
with open('sites.txt') as sites_fh:
    for url in sites_fh.readlines():
        ctr = ctr + 1
        resp = requests.get(url)
        resp_filename = 'resp' + str(ctr) + '.txt'
        resp_fp = os.path.join(resps_fp, resp_filename)

        with open(resp_fp, 'w') as resp_fh:
            resp_fh.write(url)
            resp_fh.write(resp.text)

# create metadata file
if os.path.exists('meta.txt'):
    os.remove('meta.txt')

with open('meta.txt', 'w') as meta_fh:
    meta_fh.write(str(ctr) + '\n')