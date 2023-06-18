import datetime
import computa
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executor

def main() -> None:

    quantidade_cores = multiprocessing.cpu_count()

    print(f'Realizando o processamento matemático com {quantidade_cores} core(s).')

    inicio: datetime.datetime = datetime.datetime.now()
    with Executor(max_workers=quantidade_cores) as executor:
        for n in range(1, quantidade_cores + 1):
            ini = 200_000_000 * (n - 1) / quantidade_cores
            fim = 200_000_000 * n / quantidade_cores
            print(f'Core {n} processando de {ini} até {fim}')
            executor.submit(computa.computar, inicio=ini, fim=fim)

    tempo = datetime.datetime.now() -  inicio
    print(f"Terminou em {tempo.total_seconds():.2f} segundos.")

if __name__ == '__main__':
    main()

"""
COM 200.000.000
Python (padrao):                 Terminou em 55.74 segundos.
Cpython (padrao):                Terminou em xx.xx segundos.
Cpython (+recursos de c):        Terminou em 14.67 segundos.
Cpython (+recursos de c + nogil):Terminou em 14.56 segundos.
Cpython (+recursos de c + nogil + multiprocessos):Terminou em 0.18 segundos.
"""