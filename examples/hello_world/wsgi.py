import web

urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        return 'Hello, World'


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
