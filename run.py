from wsgiref.simple_server import make_server

from framework.main import Framework
from urls import fronts
from views import routes


application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print(f'Запуск на порту 8080...')
    httpd.serve_forever()
