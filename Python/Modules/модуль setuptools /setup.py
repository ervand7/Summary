# это пример файла setup.py
# pip install setuptools
import setuptools

setuptools.setup(
    name="устанавливаемая_библиотека",
    version="версия_библиотеки",
    author="автор",
    include_package_data=True,
    description="описание",
    packages=[
        'корневая_папка',
        'корневая_папка.папка1',
        'корневая_папка.папка2',
        'корневая_папка.папка3',
        'корневая_папка.папка4'
    ],
    install_requires=[
        'requests==2.23.0',
        'pyyaml==5.3.1',
        'pytest==5.4.2',
        'pytest-instafail==0.4.1.post0',
        'pytest-html==2.1.1',
        'pytest-testrail==2.8.3',
        'pytest-rerunfailures==9.0',
        'pytest-xdist==1.32.0',
        'pymongo==3.10.1',
        'psycopg2-binary==2.8.5',
        'python-telegram-bot==12.7',
        'emoji==0.5.4',
        'pysocks==1.7.1',
        'python-dateutil==2.8.1',
        'selenium==3.141.0',
        'jsondiff==1.2.0',
        'jsonschema==3.2.0',
        'redis==3.5.2',
        'mimesis==4.0.0',
        'lxml==4.5.1',
        'textblob==0.15.3',
        'html2text==2020.1.16',
        'pychrome==0.2.3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
