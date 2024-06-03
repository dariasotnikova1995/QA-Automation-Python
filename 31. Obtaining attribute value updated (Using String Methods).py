def get_href_values_string_methods(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    href_values = []
    start = 0
    while True:
        start_link = content.find('<a ', start)
        if start_link == -1:
            break
        end_link = content.find('>', start_link)
        if end_link == -1:
            break
        tag_content = content[start_link:end_link]
        start_href = tag_content.find('href="')
        if start_href != -1:
            start_quote = start_href + len('href="')
            end_quote = tag_content.find('"', start_quote)
            href = tag_content[start_quote:end_quote]
            href_values.append(href)
        start = end_link + 1
    return href_values
filename = 'wiki_page.txt'
hrefs = get_href_values_string_methods(filename)
print(hrefs)