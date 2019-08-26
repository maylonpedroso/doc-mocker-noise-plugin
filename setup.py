import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='doc-mocker-noise-plugin',
    version='0.0.1',
    author='Maylon Pedroso',
    author_email='maylonpedroso@gmail.com',
    description='Noise plugin for Document Mocker',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/maylonpedroso/doc-mocker-noise-plugin',
    packages=['doc_mocker.plugins'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
