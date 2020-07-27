import setuptools

with open('README.md', 'r') as f:
    lond_description = f.read()

setuptools.setup(
    name='highscanner',
    version='0.0.1',
    author='Highdeger',
    author_email='highdeger@gmail.com',
    description='A simple port scanner with no dependencies',
    long_description=lond_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Highdeger/HighPortScanner',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: System :: Networking'
    ],
    python_requires='>=3.5',
)
