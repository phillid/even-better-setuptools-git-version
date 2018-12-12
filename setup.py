"""A setup script for the package to distribute it to PyPi."""
import subprocess
from setuptools import setup


def get_tag():
    """Return the last tag for the git repository."""
    return subprocess.getoutput('git tag --sort=version:refname --merged | tail -n1')


def README():
    """Return the contents of the README file for this project."""
    with open('README.md') as README_file:
        return README_file.read()


setup(
    name='better-setuptools-git-version',
    version=get_tag(),
    url='https://github.com/vivin/better-setuptools-git-version',
    author='Vivin Paliath',
    author_email='vivin.paliath@gmail.com',
    description='Automatically set package version using git tags.',
    long_description=README(),
    long_description_content_type='text/markdown',
    keywords='setuptools git version-control',
    license='MIT',
    classifiers=[
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
    ],
    py_modules=['better_setuptools_git_version'],
    install_requires=[
        'setuptools >= 8.0',
    ],
    entry_points={
        'distutils.setup_keywords': [
            'version_config = better_setuptools_git_version:validate_version_config'
        ],
        'console_scripts': [
            'better-setuptools-git-version = better_setuptools_git_version:get_version'
        ]
    }
)
