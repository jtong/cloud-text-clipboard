import web
#/copy?text=xxxx 得到paste的url，使用url访问，得到结果
urls = (
    '/copy', 'copy',
    '/paste/(.*)', 'paste'
)
app = web.application(urls, globals())

clipboard = []
class copy:
    def GET(self):
        clipboard.append(web.input().text)
        return "/paste/"+str(len(clipboard)-1)

class paste:
    def GET(self, id):
        return clipboard.pop(int(id))

if __name__ == "__main__":
    app.run()
