from setuptools import setup

setup(
    name='quexmltolatex',
    version='0.1-dev',

    install_requires=['lxml'],

    scripts=['quexmltolatex'],

    author='Johannes Wienke',
    author_email='languitar@semipol.de',
    url='https://github.com/languitar/quexmltolatex',
    description='Converts queXML structure file to LaTeX, e.g. for '
                'presenting the survey structure in the appendix of a '
                'LaTeX document.',

    license='LGPLv3+',
    keywords=['latex', 'quexml', 'conversion'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'License :: OSI Approved :: '
            'GNU Lesser General Public License v3 or later (LGPLv3+)'
    ])
