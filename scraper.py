```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

url = "https://www.amazon.com/s?k=laptop"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

titles = [t.get_text(strip=True) for t in soup.select("h2.a-size-mini a span")]
prices = [p.get_text(strip=True) for p in soup.select(".a-price-whole")]

data-a-price-whole")]

df = pd.DataFrame({"Title": titles[:20], "Price": prices[:20]})
df.to_csv("laptops.csv", index=False)
print("Successfully saved 20 laptops to laptops.csv")
