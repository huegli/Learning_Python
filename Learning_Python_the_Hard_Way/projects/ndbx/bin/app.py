import web

urls = (
        '/', 'Index',
        '/upload', 'Upload'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.index()

class Upload(object):
    def GET(self):
        return render.upload()

    def POST(self):
        form = web.input(picfile={}, scale="100%")
        if 'picfile' in form:
            fout = open("./static/picture.jpg",'w')
            fout.write(form.picfile.file.read())
            fout.close()
        return render.show(pic = form['picfile'].filename, scale = form.scale)

if __name__ == "__main__":
    app.run()
