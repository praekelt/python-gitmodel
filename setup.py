from distutils.core import setup

setup(
    name='praekelt-python-gitmodel',
    version='0.1.3',
    test_suite='gitmodel.test',
    packages=[
        'gitmodel',
        'gitmodel.serializers',
        'gitmodel.utils',
    ],
    install_requires=['pygit2', 'python-dateutil', 'decorator'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.rst').read(),
)
