#! /usr/bin/env python3

from requests import request
import argparse

desc = '--- Enumerador de Metodos HTTP/HTTPS ---'

parser = argparse.ArgumentParser(description=desc)
parser.add_argument ('-u', '--url', metavar='alvo', required=True, help='URL do site')

args = parser.parse_args()

def main (URL):
    methodResp = {'permitidos': [], 'negados': []}
    methodLista = ['GET', 'POST', 'TRACE', 'OPTIONS', 'HEAD', 'PUT', 'DELETE', 'COPY', 'CONNECT']
    print (f'[ OK ] Url: {args.url}')
    print (f'[+] Metodos a testar: ')
    for i in methodLista:
        print (f'{i}', end=' ')
    print ('\n\n')

    for method in methodLista:
        response = request (method, args.url)
        if response.status_code != 200:
            methodResp['negados'].append (method)
        else:
            print (f'[+] Metodo permitido: {method}')
            methodResp['permitidos'].append (method)

    print (f'\n\n[ OK ] Relatorio final: ')
    for i in methodResp['negados']:
        print (f'[ NEGADO ]: {i}')
    print ()
    for i in methodResp['permitidos']:
        print (f'[ PERMITIDO ]: {i}')

if __name__ == '__main__':
    main (args.url)

