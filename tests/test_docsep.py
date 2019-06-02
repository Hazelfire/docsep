"""
File: test_docsep.py
Author: Sam Nolan
Email: sam.nolan@rmit.edu.au
Github: https://github.com/Hazelfire
Description: Tests docsep overall functionality
"""

from docsep import parse

def test_docsep():
    """ Tests whether docsep can split a simple document """
    document = """
    <head>
    This is a head
    </head>
    <body>
    This is the body
    </body>
    """
    documents = parse(document)

    assert documents[0].name == "head"
    assert documents[0].body.strip() == "This is a head"

    assert documents[1].name == "body"
    assert documents[1].body.strip() == "This is the body"


