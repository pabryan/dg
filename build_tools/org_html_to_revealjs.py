#!/usr/bin/env python
# coding: utf-8

import sys
import os
from bs4 import BeautifulSoup

def convert(infile, outfile):
    classes = ["outline-2", "outline-3"]

    with open(infile, 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

        for cls in classes:
            divs = soup.find_all("div", class_=cls)
            for div in divs:
                div.name = "section"

    body = "---" + os.linesep + "layout: org-slides" + os.linesep + "---" + os.linesep + os.linesep

    for child in soup.body.children:
        body += str(child)

        with open(outfile, "w") as file:
            file.write(body)

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
    
