"""Verify visible brief content against its payload without requiring byte-identical CSS."""
from html.parser import HTMLParser
import re


class Visible(HTMLParser):
    def __init__(self): super().__init__(); self.skip=0; self.text=[]
    def handle_starttag(self,tag,attrs):
        if tag in ('style','script','head'): self.skip+=1
    def handle_endtag(self,tag):
        if tag in ('style','script','head'): self.skip=max(0,self.skip-1)
    def handle_data(self,text):
        if not self.skip and text.strip(): self.text.append(re.sub(r'\s+',' ',text).strip())


def verify(payload,document):
    import render_one_page
    try: expected,_=render_one_page.render(payload)
    except (ValueError,KeyError,TypeError) as exc: return False,'Invalid brief payload: '+str(exc)
    a,b=Visible(),Visible(); a.feed(expected); b.feed(document)
    tokens=lambda p:re.findall(r'\w+|[^\w\s]',' '.join(p.text))
    return tokens(a)==tokens(b),'Visible brief content/order must reproduce its current payload; harmless styling/inline emphasis does not change this comparison'
