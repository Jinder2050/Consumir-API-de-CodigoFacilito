from pokemapi import pokeapi
import logging


"""
INFO -> 10
debug -> 20
WARNING -> 30
ERROR -> 4
CRITICAL ->4
"""
logging.basicConfig(level=logging.INFO)

def main():
    logging.info(pokeapi())


if __name__ == '__main__':

    logging.debug('>>> Ejecutando')

    main()

    logging.debug('>>> Finalizando')