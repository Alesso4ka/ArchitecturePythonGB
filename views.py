from catalog import flowers
from framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', flowers=flowers, date=request.get('date', None))


class About:
    def __call__(self, request):
        return '200 OK', render('about.html', date=request.get('date', None))


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))
