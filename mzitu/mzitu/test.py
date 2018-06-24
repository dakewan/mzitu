from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
asdf
    <div class="title">
        <b>The Dormouse's story总共</b>
        <h1>f</h1>
    </div>
<div class="story">Once upon a time there were three little sisters; and their names were
    <a  class="sister0" id="link1">Els<span>f</span>ie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.
</div>
ad<br/>sf
<p class="story">...</p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, features="lxml")
tag = soup.find('a')
print(tag)
tag = soup.find(name='a', attrs={'class': 'sister'}, recursive=True, text='Lacie')
tag = soup.find(name='a', class_='sister', recursive=True, text='Lacie')
print(tag)