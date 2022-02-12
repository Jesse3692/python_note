# beautifulsoup使用

通过标签截取部分html

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
coin_address = soup.find_all('div', attrs={'class': 'coin-address'})
```