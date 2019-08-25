from flask import Blueprint

from app import web
from helper import is_isbn_or_key
from yushu_book import YuShu_Book


@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShu_Book.search_by_isbn(q)
    else:
        result = YuShu_Book.search_by_keyword(q)
    return result
