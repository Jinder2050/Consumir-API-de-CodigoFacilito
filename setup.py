from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Consumir el API de PokeAPI'
PACKAGE_NAME = 'pokemapi'
AUTHOR = 'Jinder2050'
EMAIL = ' '
GITHUB_URL = 'https://github.com/Jinder2050/pokemapi'

setup(
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    entry_points = {
        "console_scripts":
            ["pycody=pokemapi.__main__:main"]
    },
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [
        'pokemonapi',
        'pokeapi',
        'pokemapi'
    ],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)