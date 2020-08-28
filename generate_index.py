from horoscope import generate_prophecies
from datetime import datetime as dt


def generate_page(head, body):
    page = f'<html>{head}{body}</html>'
    return page


def generate_head(title):
    head = f'<head><meta charset="utf-8"><title>{title}</title></head>'
    return head


def generate_body(header, paragraphs):
    body = f'<h1>{header}</h1>'
    link = generate_link('about.html', 'О реализации')
    for p in paragraphs:
        body += f'<p>{p}</p>'
    body += link
    return f'<body>{body}</body>'


def generate_link(url, name_of_link):
    link = f'<a href="{url}">{name_of_link}</a>'
    return link


def save_page(title, header, paragraphs, output='index.html'):
    file_index = open(output, 'w')
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs=paragraphs))
    print(page, file=file_index)
    file_index.close()


today = dt.now().date()


save_page(
    title='Гороскоп на сегодня',
    header='Ваши предсказания на ' + str(today),
    paragraphs=generate_prophecies(total_num=3, num_sentences=4)
)
