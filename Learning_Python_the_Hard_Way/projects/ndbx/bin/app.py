import web
import cgi
import os

# Maximum input of 1 MB for POST
cgi.maxlen = 1024 * 1024; # 1 MB

# remove previous pic
have_pic = False
if os.path.isfile("./static/picture.jpg"):
    os.remove("./static/picture.jpg")


urls = (
        '/', 'Index',
        '/upload', 'Upload'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.index(have_pic=have_pic)

class Upload(object):
    def GET(self):
        return render.upload()

    def POST(self):
        global have_pic
        try:    
            form = web.input(picfile={}, scale="100%")
        except ValueError:
            return "File too large"
        else: 
            if 'picfile' in form:
                filepath=form.picfile.filename.replace('\\','/') # Windows -> Linux slashes
                filename=filepath.split('/')[-1] # pick up last part (filename & extension
                fileext=filename.split('.')[-1] # extension
                if 'jpg' in fileext:
                    fout = open("./static/picture.jpg",'w')
                    fout.write(form.picfile.file.read())
                    fout.close()
                    have_pic = True
                    raise web.seeother('/')
                else:
                    return "JPG's only"

if __name__ == "__main__":
    app.run()
