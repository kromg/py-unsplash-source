from setuptools import setup, find_packages

setup(
    name='py_unsplash_source',
    version='0.9.0',
    author='Giacomo Montagner',
    author_email='kromg.kromg@gmail.com',
    packages=find_packages(
        exclude=['tests']
    ),
    # scripts=['/bin/this.py', '/bin/that.py'],
    url='https://github.com/kromg/py-unsplash-source',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    description='Python library to get pictures from source.unsplash.com',
    long_description=open('README.txt').read(),
    zip_safe=True,
    platforms="POSIX",
    test_requires=['pytest', 'requests'],
    install_requires=['requests']
)

