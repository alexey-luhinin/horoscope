import horoscope

def save_page(filename):
    file_about = open(filename, 'w')
    print(page('Про эту страницу'), file=file_about)
    file_about.close()

def page(title):
    page = header(title) + body()
    return f'<html>{page}</html>'


def header(title):
    head = f'<head><meta charset="utf-8"><title>{title}</title></head>'
    return head


def image(url):
    img = f'<img src="{url}" width="100" height="100"> '
    return img


def link(url, name_of_link):
    link = f'<a href="{url}">{name_of_link}</a>'
    return link


def generate_list(input_list):
    num_list = ''
    for numl in input_list:
        num_list += f'<li>{numl}</li>'
    output_list = f'<ol>{num_list}</ol>'
    return output_list


def body():
    h1 = f'<h1>О чем все это</h1>'
    img = image('https://www.survivalkit.com/blog/wp-content/uploads/2017/09/img-37.jpg')
    times = generate_list(horoscope.times)
    advices = generate_list(horoscope.advices)
    promices = generate_list(horoscope.promises)
    link_index = link('index.html', 'Перейти к гороскопу')

    return h1 + img + times + advices + promices + link_index

save_page('about.html')
