# 辅助函数，用于判断用户输入是isbn编号还是关键字
def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit:
        isbn_or_key = 'isbn'

    short_q = word.replace('-', '')
    if '-' in word and len(short_q) == 10 and short_q.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key
