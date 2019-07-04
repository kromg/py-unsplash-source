from setuptools import setup, find_packages

setup(
    name='py_unsplash_source',
    version='1.0',
    packages=find_packages(
        exclude=['tests']
    ),
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    description='Python library to get pictures from source.unsplash.com',
    # long_description=open('README.txt').read(),
    zip_safe=True,
    platforms="POSIX",
    test_require=['pytest', 'requests'],
    install_requires=['requests']
)
