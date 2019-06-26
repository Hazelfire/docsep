"""
File: main.py
Author: Sam Nolan
Email: sam.nolan@rmit.edu.au
Github: https://github.com/Hazelfire
Description: simple document splitter
"""

from collections import namedtuple
import xml.etree.ElementTree as ET


Document = namedtuple("Document", ["subdocuments", "name", "body"])

def create_document(node):
    """ Creates a document """
    return Document(
        subdocuments={child.tag: create_document(child) for child in node},
        name=node.tag,
        body=node.text
    )

def parse(contents):
    """ Returns an array of documents to use """
    xml = '<?xml version="1.0" encoding="UTF-8" ?><document>"' + contents +  "</document>"
    document = ET.fromstring(xml)
    return {child.tag: create_document(child) for child in document}
