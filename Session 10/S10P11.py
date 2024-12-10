import re

def extract_date_from_url(url):
    match = re.search(r'(\d{4})/(\d{2})/(\d{2})', url)
    if match:
        return match.groups()
    return None

# Test case
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date_from_url(url))  # ('2016', '09', '02')
