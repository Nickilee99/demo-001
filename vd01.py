import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! LE DINH NGUYEN 2175406 !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

