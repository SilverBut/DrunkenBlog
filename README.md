# DrunkenBlog 

Drunken is a simple blog structure following Apache license. It synchronously updates with [Silver's Blog](http://sonyis.science). The blog is based on Python, and use Markdown as its source.

The blog is still under development now.

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
	 |--config.yaml.sample           # Example config file
	 |--config.yaml                  # config file
	 |--template                     # template folder
	 |--static                       # static file folder, such as .css or err htmls
	 |--documents                    # where *.md exists
	 |--controller                   # will be used to handle requests
	 |--extends                      # plugins and extend modules
	 |--util                         # function modules such as renderer

## How to load config
CMDLine > Config File > Default Settings
