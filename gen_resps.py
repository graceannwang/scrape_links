import shutil
import os

# clear out files in existing responses folder
resp_path = os.path.join('.', 'responses')

if(os.path.isdir(resp_path)):
    shutil.rmtree(resp_path)

os.mkdir(resp_path)