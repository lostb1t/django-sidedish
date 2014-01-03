from setuptools import setup, find_packages

import sidedish

setup(
    name='django-sidedish',
    version='0.1',
    description="A Django app for managing content boxes(dishes)",
    long_description=open('README.md').read(),
    author='Sjoerd Arendsen',
    author_email='sjoerd@optixdesigns.com',
    url='https://github.com/docc/django-sidedish',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=1.4.5",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
)