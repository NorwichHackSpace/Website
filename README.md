Norwich Hackspace Website
=======

Code and content that drive the hackspace website

How to edit content
=======
This site uses a static site generator that reads in Markdown files and converts them to HTML. When this content is merged with a template the resulting output is a series of HTML files that drives the site.

The static site generator is called Pelican () 

Installation
=======
Install Python 2.7
Install pip
Run "pip install pelican"
Run "pip install Markdown"

Markdown
=======
Markdown (http://daringfireball.net/projects/markdown/syntax) is a super simple way of adding formatting to text. It is like HTML as in it is a mark up language but has been designed to be as simple as possibe. Lots of Wiki's use Markdown and it is rapidly becoming a standard way of generating rich web content without having to use the rubbish webbased WYSIWYG editors.

Pelican converts the Markdown in the content files to HTML and merges it with a template that comes as part of a theme.
```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.
```

Git
=======