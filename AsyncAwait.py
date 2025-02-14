import asyncio
import time

async def chamada_simulada(delay: int):
    print(f"Iniciando chamada... id: {delay}")
    await asyncio.sleep(delay)
    print(f"Chamada concluída após {delay} segundos")

async def main():
    #iniciando o cronometro
    start = time.time()
    
    #fazendo a chamada do "serviço"
    tarefa1 = asyncio.create_task(chamada_simulada(3))
    tarefa2 = asyncio.create_task(chamada_simulada(2))
    tarefa3 = asyncio.create_task(chamada_simulada(1))
    
    #aguardando terminar o "serviço"
    await tarefa1
    await tarefa2
    await tarefa3
    
    performance = time.time() - start
    print(f"Tempo total de execução: {performance:.2f} s")

asyncio.run(main())