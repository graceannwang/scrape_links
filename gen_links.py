# clear out old links in links folder

# retrieve and save number of responses from meta folder
# loop thru all response files in responses folder
# for each file:
    # scrape and save new links
    # add these new links to a new link file

import os
import shutil
from bs4 import BeautifulSoup

link_path = os.path.join('.', 'links')

# clear out files in existing links folder
if(os.path.isdir(link_path)):
    shutil.rmtree(link_path)

os.mkdir(link_path)