# scrape_links

As of 07/22/22 1:02pm

## Overview 

Given a list of sites, scrape and save the links from each site.

## File/folder descriptions

***sites.txt***: The list of sites to scrape. Each site must be on its own line.

***meta.txt***: The number of sites in sites.txt.

***gen_resps.py***: Requests the html responses from the sites in sites.txt and saves them in the *responses* folder.

***gen_links.py***: For each response file in *responses*, scrapes all links and saves them in the *links* folder

***responses***: Each response file in the *responses* folder corresponds to a particular site from sites.txt. For a response file *respX.txt*, the *X* integer corresponds to the line number in *sites.txt* the site is associated with.

***links***: Each links file in the *links* folder corresponds to a particular response from *responses* and site from *sites.txt*. For a links file *linksX.txt*, the *X* integer corresponds to the line number in *sites.txt* the site is associated with.

