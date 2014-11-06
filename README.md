Scholar Retriever
=========

Simple script that retrieves Scholar resources in a local folder.


Requirements
------------
* Python 2.6+
* easywebdav

Usage
-----

* Clone this repository 
* ```pip install -r requirements.txt```
* Copy config.example.py to config.py and edit to your liking 
* Run ```python scholarretriever.py ```


Config
------
* username: Your hokie PID
* password: if you leave it as such you will be securely prompted for it
* path: where to download the resources
* verbose: whether to print retrieved/skipped files or not (useful if used as a cronjob)
* classes: a list of a tuple of class names and scholar site ids to retrieve


FAQ
---
* Where do I find the scholar site id?  

For every scholar site you can either find it in the URL:
```https://scholar.vt.edu/portal/site/2cc328f0-1f60-4a25-a007-dcf859335706/``` where the site id is 2cc328f0-1f60-4a25-a007-dcf859335706  
Or you can find it by clicking on "Upload-Download Multiple Resources" in the Resources tab.

Known Issues
------------
Right now a file is only downloaded if it does not exist locally, meaning that if an instructor changes a file with the same filename, you will have to delete it locally first, then run the script again.

Author
-------
Andrei Marcu  
http://andreim.net/