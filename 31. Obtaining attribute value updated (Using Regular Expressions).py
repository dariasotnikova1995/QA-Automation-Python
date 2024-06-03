import re
def get_href_values_regex(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    href_pattern = re.compile(r'<a [^>]*href="([^"]+)"')
    href_values = href_pattern.findall(content)
    return href_values
filename = 'wiki_page.txt'
hrefs = get_href_values_regex(filename)
print(hrefs)