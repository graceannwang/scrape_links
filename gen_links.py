import os
import shutil
from bs4 import BeautifulSoup

links_fp = os.path.join('.', 'links')
resps_fp = os.path.join('.', 'responses')

# clear out files in existing links folder
if(os.path.isdir(links_fp)):
    shutil.rmtree(links_fp)

os.mkdir(links_fp)

# retrieve and save number of sites from meta file
num_sites = 0
with open('meta.txt') as meta_fh:
    num_sites = int(meta_fh.readline())

# scrape links and add to new link file for each site
for i in range(1, num_sites + 1):
    resp_filename = 'resp' + str(i) + '.txt'
    resp_fp = os.path.join(resps_fp, resp_filename)

    # scrape links for current site
    a_tags = []
    with open(resp_fp) as resp_fh:
        resp_soup = BeautifulSoup(resp_fh, 'html.parser')
        a_tags = resp_soup.find_all('a', href=True)
    
    # create and populate link file
    links_filename = 'links' + str(i) + '.txt'
    linksfile_fp = os.path.join(links_fp, links_filename)

    with open(linksfile_fp, 'w') as links_fh:
        for a_tag in a_tags:
            links_fh.write(str(a_tag.string) + '\n')
            links_fh.write(a_tag['href'] + '\n\n')
