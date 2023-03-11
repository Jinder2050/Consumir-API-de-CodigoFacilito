from pokeapi import pokeapi
import logging


"""
INFO -> 10
debug -> 20
WARNING -> 30
ERROR -> 4
CRITICAL ->4
"""

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':

    logging.debug('>>> Ejecutando')
    pokemons = pokeapi()
    logging.debug(pokemons)

    logging.debug('Finalizando')    