# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Sahil Patel",
    author_email="sahilpatel2339@gmail.com",
    maintainer='Sahil Patel',
    maintainer_email='sahilpatel2339@gmail.com',
    name='main',
    version='0.1',
    description='A Django app to scrape facebook page ',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/sah1l/fb-scraper',
    license='GPL',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django==1.9.4',
    ],
    packages=find_packages(exclude=["project","project.*"]),
    include_package_data=True,
    zip_safe = False
)
