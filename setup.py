from setuptools import setup, find_packages
import re

from hodots import __version__

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()

extras_require = {
    'docs': [
        'sphinx',
        'sphinxcontrib_trio',
        'sphinxcontrib-websupport',
        'typing-extensions',
    ]
}

packages = [
    'hodots',
    'hodots.post'
]

setup(
    name='hodots.py',
    author='leafstudiosDot',
    url='https://github.com/leafstudiosDot/hodots.py',
    project_urls={
        'API Documentation': 'https://docs.hodots.com/',
        'Documentation': 'https://hodotspy.readthedocs.io/en/latest/',
        'Issue tracker': 'https://github.com/leafstudiosDot/hodots.py/issues',
    },
    version=__version__,
    packages=find_packages(exclude=['test']),
    license='MIT',
    description='API Wrapper for hodots. written in Python',
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.11.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)