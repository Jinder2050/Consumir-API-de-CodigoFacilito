from pokeapi import pokeapi
import logging


"""
INFO -> 10
debug -> 20
WARNING -> 30
ERROR -> 4
CRITICAL ->4
"""

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':

    logging.debug('>>> Ejecutando')

    pokemons = pokeapi()
    # logging.debug(pokeapi.__doc__)

    logging.debug('>>> Finalizando')