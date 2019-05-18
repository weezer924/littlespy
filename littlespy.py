from bs4 import BeautifulSoup
RA_Works = 0

f = open('./target.html', 'r')
s = f.read()
soup = BeautifulSoup(s,"html.parser")

mainNewsIndex = soup.find_all("tr")

for index in mainNewsIndex:
  text = index.find(['td'])
  if text is not None:
    print(text.get_text())