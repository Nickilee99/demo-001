import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! Welcome to this experience !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
