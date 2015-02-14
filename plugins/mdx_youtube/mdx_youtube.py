# mdx_youtube.py
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

YOUTUBE = r'\!youtube\s+([^;\s]+)(?:\s+([0-9]+)\s+([0-9]+))?\s*;'
DEFAULT_WIDTH = 560
DEFAULT_HEIGHT = 315

class YouTubePattern(Pattern):
        def handleMatch(self, m):
                urlpart = m.group(2) # Markdown uses group 1
                width = m.group(3)
                height = m.group(4)

                if width == None:
                        width = str(DEFAULT_WIDTH)
                if height == None:
                        height = str(DEFAULT_HEIGHT)

                iframe = etree.Element('iframe')
                iframe.attrib['src'] = '//www.youtube.com/embed/' + urlpart
                iframe.attrib['allowfullscreen'] = ''
                iframe.attrib['frameborder'] = '0'
                iframe.attrib['width'] = width
                iframe.attrib['height'] = height
                return iframe

class YouTubeExtension(Extension):
        def extendMarkdown(self, md, md_globals):
                md.inlinePatterns.add('youtube', YouTubePattern(YOUTUBE), '<reference')

def makeExtension(configs=None):
        return YouTubeExtension(configs=configs)