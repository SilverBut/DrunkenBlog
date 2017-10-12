# DrunkenBlog 

Drunken is a simple blog structure following Apache license. It synchronously updates with [Silver's Blog](https://blog.iret.xyz). The blog is based on Python, and use Markdown as its source.

The blog is still under development now.

## Legal Statement

Copyright of this repo belongs to Silver.

Unless otherwise stated, you are requested to follow GPLv3 to use code in this repo.

The following related parts are NOT allowed to use this code, unless a statement is signed and published by the author:

* Humensec (http://www.humensec.com)
* Network Behaviour Research Center (NBRC) in Xidian University (http://nbrc.xidian.edu.cn)
* School of Cyber Engineering of Xidian University (http://ce.xidian.edu.cn)
* Leaders, researchers, students and any other people directly related to entities above

ANY POSSIBLE actions will be committed if this statement had been violated.

## Blog Structure 

Based on Markdown files to format the article, and use simple file storage techs to save the markdown file. A built-in render is used to convert markdown files to rendered HTML parts and meta infos. Use Disqus as the comment tool. 

## Functions
* Simple templates
* Article list(sort by date and time)
* Article pages and special pages
* Disqus comment

## Directory List
	\-                            # root folder
	 |--main.py                      # main script
	 |--config.ini.sample           # Example config file
	 |--config.ini                  # config file
	 |--template                     # template folder
	 |--static                       # static file folder, such as .css or err htmls
	 |--documents                    # where *.md exists
	 |--controller                   # will be used to handle requests
	 |--extends                      # plugins and extend modules
	 |--util                         # function modules such as renderer

## How to load config
CMDLine > Config File > Default Settings
