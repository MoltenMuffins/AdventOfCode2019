# !/usr/bin/python
import re
import os
import urllib.request

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_page(url):
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
    except:
        print("Request Unsuccessful")
    
    html_bytes = response.read()
    html = html_bytes.decode("utf8")

    return html
    
def parse_page(html):
    expression = r'<article class="day-desc">(.*)</article>'
    page_content = re.search(expression, html, flags=re.S)

    # Here we define a list of strings to be replaced
    # as well as their replacees
    replace_ls = [
        ('<article class="day-desc">', ''),
        ('</article>', ''),
        ('<h2>', '# '),
        ('<h2 id="part2">', '## '),
        ('</h2>', '\n'),
        ('<p>', ''),
        ('</p>', '\n'),
        ('<ul>', ''),
        ('</ul>', ''),
        ('<li>', '- '),
        ('</li>', ''),
        ('<pre><code>', '```\n'),
        ('</code></pre>', '```\n'),
        ('<code>', '`'),
        ('</code>', '`'),
        ('<em>', '*'),
        ('</em>', '*'),
        ('--- ', ''),
        (' ---', '')
    ]

    # Iteratively replace html tags with their md
    # equalivents
    part1_text = page_content.group(0)
    for tag, md in replace_ls:
        part1_text = part1_text.replace(tag, md)

    part2_text = page_content.group(1)
    if part2_text:
        for tag, md in replace_ls:
            part2_text = part2_text.replace(tag, md)

        return part1_text + '\n' + part2_text
    else:
        return part1_text


def md_writer(content, save_path):
    with open(save_path, 'w+') as f:
        f.write(content)

if __name__ == "__main__":
    day_num = int(input('Input AOC day to convert to markdown: '))
    # url = 'https://adventofcode.com/2019/day/{}#part2'.format(day_num)
    save_path = os.path.join(dir_path, os.pardir, 'day{:02d}'.format(day_num), 'puzzle.md')
    if os.path.isfile(save_path):
        save_path = save_path.replace('puzzle', 'puzzle_copy')

    read_path = os.path.join(dir_path, 'html_dump' ,'day{:02d}.html'.format(day_num))
    file = open(read_path, 'r')
    # page = get_page(url)

    md_raw = parse_page(file.read())
    md_writer(md_raw, save_path)
    print('Done')