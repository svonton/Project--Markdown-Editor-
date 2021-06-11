help_message = '''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done'''
text_holder = []

def get_text():
    return input("Text: ")

def plain():
    return get_text()

def bold():
    return f"**{get_text()}**"

def italic():
    return f"*{get_text()}*"

def inline_code():
    return f"`{get_text()}`"

def link():
    labl = input('Label: ')
    url = input('URL: ')
    return f'[{labl}]({url})'

def header():
    lvl = int(input('Level: '))
    return f"{'#' * lvl} {get_text()}\n"

def new_line():
    return '\n'

def zero_check():
    try:
        cntx = input('Number of rows: ')
        while int(cntx) <= 0:
            print('The number of rows should be greater than zero')
            cntx = input('Number of rows: ')
        return int(cntx)
    except ValueError:
        print(f'{cntx} is not an number')


def order_unorder_lists(un_list=False):
    row_num = zero_check()
    print(row_num)
    list = ''
    for i in range(row_num):
        if un_list:
            list += '* ' + input(f'Row #{i + 1}: ') + '\n'
        else:
            list += str(i+1)+'. '+input(f'Row #{i+1}: ')+'\n'
    return list

def save_to_file(cntx):
    with open('output.md', 'w') as f:
        for i in cntx:
            f.write(i)



formatters = {"plain": plain, "bold": bold, "italic": italic, "link": link, "inline-code": inline_code,
              "new-line": new_line, "header": header, 'ordered-list': order_unorder_lists,
              'unordered-list': order_unorder_lists}

while True:
    user_input = input('Choose a formatter: ')
    if user_input in ['!help', '!done']:
        if user_input == '!help':
            print(help_message)
        elif user_input == '!done':
            save_to_file(text_holder)
            break
    elif user_input in formatters.keys():
        if user_input == 'unordered-list':
            text_holder.append(order_unorder_lists(True))
        else:
            text_holder.append(formatters[user_input]())
    else:
        print('Unknown formatting type or command')
    print(*text_holder, sep="")
