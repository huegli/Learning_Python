try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Nikolai Schlegel',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'nikolai.schlegel@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lexicon'],
    'scripts': [],
    'name': 'Excercise 48, lexicon'
}

setup(**config)
