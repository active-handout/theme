from markdown.treeprocessors import Treeprocessor
import xml.etree.ElementTree as etree

class Admonition2Message(Treeprocessor):
    def run(self, root):
        for el in root.findall(".//p[@class='admonition-title']/.."):
            div = etree.Element("div")
            div.attrib['class'] = 'message-body'
            el.attrib['class'] += ' message'
           
            for child in el.findall('*'):
                if 'admonition-title' not in child.get("class", ""):
                    el.remove(child)
                    div.append(child)
                else:
                    child.attrib['class'] = 'message-header'
                    child.tag = 'div'
            
            el.append(div)
