from setuptools import setup, find_packages

setup(
    name='py_unsplash_source',
    version='0.1dev',
    packages=find_packages(
        exclude=['tests']
    ),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    zip_safe=True,
    platforms="POSIX",
    test_require=['pytest'], install_requires=['pytest']
)
