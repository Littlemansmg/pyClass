# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import re


def htmlsplit():
    header = ''
    html_list = []
    for i in html_code:
        if i.startswith('<h1>'):
            header = re.split('; |, |<h1>|</h1>|\n', i)
        elif i.startswith('<ul>') or i.startswith('</ul>'):
            pass
        elif '<li>' in i:
            html_list.append(re.split('; |, |<li>|</li>|\n', i))
    return header, html_list


def main():
    head, html_list = htmlsplit()
    print("HTML Converter\n")
    print(head[1])
    for i in html_list:
        print('* {}'.format(i[1]))


if __name__ == "__main__":
    html_code = []

    try:
        with open('html.txt', 'r') as file:
            for line in file:
                html_code.append(line)
    except FileNotFoundError:
        print("Can't find html.txt\nBye!")
        exit()

    main()
