from markdown import Extension
from .admonition2message import Admonition2Message

class ActiveHandoutExtension(Extension):

    def extendMarkdown(self, md):
        """ Add Admonition to Markdown instance. """
        md.treeprocessors.register(Admonition2Message(md), 'messages', 1000)