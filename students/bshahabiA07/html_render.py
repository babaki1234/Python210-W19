#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""
import pytest

# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None,**kwargs):
        self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
    # loop through the list of contents:
     open_tag = ["<{}".format(self.tag)]
     open_tag.append(">\n")
     out_file.write("".join(open_tag))
     #out_file.write("<{}>\n".format(self.tag))
     for content in self.contents:
         if content is not None:
          try:
            content.render(out_file)
          except AttributeError:
            out_file.write(content)
         out_file.write("\n")
     out_file.write("</{}>\n".format(self.tag))
	 
class Body(Element):
    tag = 'body'
class Html(Element):
    tag = 'html'
class P(Element):
    tag = 'p'
	
class OneLineTag(Element):
 def render(self, out_file):
    # loop through the list of contents:
       for content in self.contents:
           out_file.write("<{}>".format(self.tag))
           if content is not None:
            try:
                content.render(out_file)
            except AttributeError:
               out_file.write(self.contents[0])		   
           out_file.write("</{}>\n".format(self.tag))
 def append(self,content):
          raise NotImplementedError
def test_one_line_tag_append():
    e = OneLineTag("the initial content")
    with pytest.raises(NotImplementedError):
         e.append("some more content")
         file_contents = render_result(e).strip()
         print(file_contents)
		 
class Title(OneLineTag):
     tag = "title"
	 
class Head(Element):
     tag = 'head'

	 
class SelfClosingTag(Element):
 def _open_tag():
    tag = ["<{}>".format(self.tag)]
    return tag
	

    def render(self, out_file):
     tag = self._open_tag()[:-1] + " />\n"
     out_file.write(tag)
     #loop through the list of contents:
     out_file.write(self._open_tag())
     out_file.write("\n")
     for content in self.contents:
            try:
               content.render(out_file)
            except AttributeError:
             out_file.write(content)
             out_file.write("\n")
             out_file.write(self._close_tag())
             out_file.write("\n")
    
	  
class Hr(SelfClosingTag):
     tag = "hr"
	 
	  
 
	  
	   