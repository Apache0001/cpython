import datetime
import computa

def main():
    inicio = datetime.datetime.now()

    computa.computar(fim=200_000_000)

    tempo = datetime.datetime.now() -  inicio

    print(f"Terminou em {tempo.total_seconds():.2f} segundos.")


if __name__ == '__main__':
    main()

"""
COM 50.000.000
Python (padrao): Terminou em 14.43 segundos.
Cpython (padrao):Terminou em 9.57 segundos.
Cpython (+recursos de c):Terminou em 0.00 segundos.
Cpython (+recursos de c + nogil):Terminou em 0.00 segundos.
"""

"""
COM 200.000.000
Python (padrao):                 Terminou em 55.74 segundos.
Cpython (padrao):                Terminou em xx.xx segundos.
Cpython (+recursos de c):        Terminou em 14.67 segundos.
Cpython (+recursos de c + nogil):Terminou em 14.56 segundos.
"""