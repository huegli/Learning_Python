from distutils.core import setup

with open('README') as file:
    readme = file.read()

setup(
    name='nikolais_attackoftheorcs',
    version='2.0.1',
    packages=['wargame'],
    url='http://testpypi.python.org/pypi/nikolais_attackoftheorcs/',
    license='LICENSE.txt',
    description='my fantasy game',
    long_description=readme,
    author='Nikolai Schlegel',
    author_email='nikolai.schlegel@gmail.com',
)



