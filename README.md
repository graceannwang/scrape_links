# scrape_links

As of 07/26/22 11:11am

## Overview 

Given a list of sites, scrape and save the links and content from each site.

## File/folder descriptions

***sites.txt***: The list of sites to scrape. Each site must be on its own line.

***meta.txt***: The number of sites in sites.txt.

***gen_resps.py***: Requests the html responses from the sites in sites.txt and saves them in the *responses* folder.

***gen_links_texts.py***: For each response file in *responses*, (1) scrapes and saves all links in the *links* folder and (2) scrapes and saves the page content in the *texts* folder.

***responses***: Each resps.txt file corresponds to a particular site from sites.txt. For a response file *respX.txt*, the *X* integer corresponds to the line number in *sites.txt* the site is associated with.

***texts***: Each text.txt file corresponds to a particular site from sites.txt. For a text file *textX.txt*, the *X* integer corresponds to the line number in *sites.txt* the site is associated with.


***links***: Each links.txt file corresponds to a particular site from sites.txt. For a links file *linksX.txt*, the *X* integer corresponds to the line number in *sites.txt* the site is associated with.

