#!/usr/bin/env python
# coding: utf-8

import sys
import os
from bs4 import BeautifulSoup

def convert_section(s, soup):
    sid = s["id"]
    s["id"] = sid + "-item"
    s["class"] = "accordion-item"
    
    header = soup.new_tag("h1")
    header["class"] = "accordion-header"
    header["id"] = sid + "-header"
    s.insert(0, header)

    body = soup.new_tag("div")
    body["id"] = sid + "-collapse"
    body["class"] = "accordion-collapse collapse"
    body["aria-labelledby"] = sid + "-header"
    s.insert(1, body)

    H = s.find("h2")
    H.name = "button"
    H["class"] = "accordion-button collapsed"
    H["type"] ="button"
    H["data-bs-toggle"] = "collapse"
    H["data-bs-target"] = "#" + sid + "-collapse"
    H["aria-expanded"] = "false"
    H["aria-controls"] = sid + "-collapse"
    
    header.insert(0, H)
    
    B = s.find("div", class_="outline-text-2")
    B["class"] = "accordion-body p-3 m-0"
    B["id"] += "-body"
        
    body.insert(0, B)

def convert(infile, outfile):
    section_class = "outline-2"

    with open(infile, 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

    sections = soup.find_all("div", class_=section_class)
    for s in sections:
        convert_section(s, soup)

    body = "---" + os.linesep + "layout: org-notes" + os.linesep + "---" + os.linesep + os.linesep

    for child in soup.body.children:
        body += str(child)
        
    with open(outfile, "w") as file:
        file.write(body)
            
if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
