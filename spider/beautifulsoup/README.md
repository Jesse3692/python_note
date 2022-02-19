# beautifulsoup 使用

## 通过标签截取 html

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
coin_address = soup.find_all('div', attrs={'class': 'coin-address'})
```

## 删除指定标签

`clear` 是清空，而不是删除
`decompose` 是直接删除指定标签

### 使用`decompose`方法删除指定标签

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
remove_tag_list = soup.find_all('div', attrs={'class': 'coin-address'})
for tag_item in remove_tag_list:
    tag_item.decompose()
```

### 使用`clear`方法清空指定标签

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
remove_tag_list = soup.find_all('div', attrs={'class': 'coin-address'})
for tag_item in remove_tag_list:
    tag_item.clear()
```
