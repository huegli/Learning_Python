import os
import sys

print 'Content-Type: text/html'
print ''
print '<form method="post" action="/" enctype="multipart/form-data">'
print 'Zap Data: <input type="text" name="zap"><br/>'
print 'Zot Data: <input type="text" name="zot"><br/>'
print 'File Data: <input type="file" name="filedat"><br/>'
print '<input type="submit">'

print '<pre>'
print 'Environment keys:'
print ''
for param in os.environ.keys():
    print param, ':', os.environ[param]
print ''

print 'Data'
count = 0
for line in sys.stdin:
    count = count + 1
    print line
    if count > 100:
        break

print '</pre>'
