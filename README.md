# DrunkenBlog 

Drunken is a simple blog. It synchronously updates with [Silver's Blog](http://sonyis.science). The blog is based on Python, and use Markdown as its source.

The blog is still under development now.

## Blog Structure 

Based on Markdown files to format the article, and use simple file storage techs to save the markdown file. A small render is used to convert markdown files to rendered HTML parts and meta infos, which will be stored in Redis as the cache, and will remove old cache in time. Server will automatically sync markdown source file by the way you'd like to use, such as Google Drive, Dropbox, etc. Use Disqus as the comment tool. 

## Functions 
* Auto sync 
* Search by Tag/Time 
* Special Pages, such as "About" 
* Simple templates 

## Directory List
	\			#root folder
	|--main.py		# main script
	|--template		# template folder
	|--static		# static file folder, such as .css
	|--documents	# where *.md exists
