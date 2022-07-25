import os
import shutil
from bs4 import BeautifulSoup
from requests.compat import urljoin

links_fp = os.path.join('.', 'links')
resps_fp = os.path.join('.', 'responses')
texts_fp = os.path.join('.', 'texts')

# retrieve and save number of sites from meta file
num_sites = 0
with open('meta.txt') as meta_fh:
    num_sites = int(meta_fh.readline())

# clear out files in existing links folder
if(os.path.isdir(links_fp)):
    shutil.rmtree(links_fp)

os.mkdir(links_fp)

# clear out files in existing texts folder
if(os.path.isdir(texts_fp)):
    shutil.rmtree(texts_fp)

os.mkdir(texts_fp)

# scrape and save links and text
for i in range(1, num_sites + 1):
    # creating response filepath for later use
    resp_filename = 'resp' + str(i) + '.txt'
    resp_fp = os.path.join(resps_fp, resp_filename)

    # scrape links for current site from response file
    orig_url = ''
    a_tags = []
    text = ''
    with open(resp_fp) as resp_fh:
        # retrieve url and make soup
        orig_url = resp_fh.readline()
        resp = resp_fh.read().replace(orig_url, '', 1)
        resp_soup = BeautifulSoup(resp, 'html.parser')

        # scrape links
        a_tags = resp_soup.find_all('a', href=True)

        # scrape text
        text = resp_soup.get_text()
    
    # create and populate link file in the links folder
    links_filename = 'links' + str(i) + '.txt'
    linksfile_fp = os.path.join(links_fp, links_filename)
    with open(linksfile_fp, 'w') as links_fh:
        for a_tag in a_tags:
            links_fh.write(str(a_tag.string) + '\n')
            url = a_tag['href']
            if(url.startswith('/')):
                url = urljoin(orig_url, url)
                # print(url)
            links_fh.write(url + '\n\n')

    # create and populate text file in the texts folder
    text_filename = 'text' + str(i) + '.txt'
    text_fp = os.path.join(texts_fp, text_filename)
    with open(text_fp, 'w') as text_fh:
        text_fh.write(text)
