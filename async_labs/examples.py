import threading
import time


def thread_worker():
    def worker(thread_id, delay, iterations):
        for i in range(iterations):
            print(f"Поток {thread_id}: Итерация {i + 1} (задержка {delay} сек)")
            time.sleep(delay)  # Имитация работы
        print(f"Поток {thread_id} завершил работу!")

    treads = [
        threading.Thread(target=worker, args=(1, 0.5, 5)),
        # если нужно чтоб поток закончился к концу выполнения всего кода
        threading.Thread(target=worker, args=(2, 0.3, 3)),  # указываете параметр deamon = True
        threading.Thread(target=worker, args=(3, 0.1, 9)),
    ]

    # запуск потоков
    for t in treads:
        t.start()

    # ожидание всех потоков
    for t in treads:
        t.join()

    print("\nВсе потоки завершили работу")


def multiroc():  # нельзя внести в функцию тк нужен мейн поток для реализации (я хз пока как его грамотно разместить тут)
    import multiprocessing
    import time
    from random import randint

    def delayed_task(task_id, delay):
        """Функция с задержкой, имитирующая работу"""
        print(f"▶ Задача {task_id} запущена (задержка {delay} сек)")
        time.sleep(delay)
        print(f"⏹ Задача {task_id} завершена")
        return f"Результат задачи {task_id}"

    def main_function():
        """Основная функция, запускающая мультипроцессорные задачи"""
        # Создаем пул из 3 процессов
        with multiprocessing.Pool(3) as pool:
            # Генерируем 5 задач со случайными задержками от 1 до 3 сек
            tasks = [(i, randint(1, 3)) for i in range(1, 6)]

            # Запускаем задачи асинхронно
            results = [pool.apply_async(delayed_task, task) for task in tasks]

            # Ожидаем завершения всех задач и получаем результаты
            output = [res.get() for res in results]

        # Выводим итоговые результаты
        print("\nВсе задачи завершены! Результаты:")
        for result in output:
            print(f"• {result}")

    if __name__ == "__main__":
        print("🚀 Старт основной функции")
        start_time = time.time()

        main_function()

        end_time = time.time()
        print(f"\n🕒 Общее время выполнения: {end_time - start_time:.2f} сек")


def async_ex():  # так же как и в мультипроцессинге нельзя запускать вне мейн потока и внутри не асинхронных методов
    import asyncio
    from random import randint
    import time

    async def mock_api_request(task_id: int, delay: float) -> str:
        print(f"▶ Задача {task_id} началась (задержка: {delay} сек)")
        await asyncio.sleep(delay)
        print(f"✔ Задача {task_id} завершена")
        return f"Данные задачи {task_id}"

    async def main():
        tasks = [
            mock_api_request(1, 2.5),
            mock_api_request(2, 0.7),
            mock_api_request(3, 1.0)
        ]
        results = await asyncio.gather(*tasks)
        print("\nРезультаты:")
        for result in results:
            print(f"• {result}")

    if __name__ == "__main__":
        start_time = time.time()
        asyncio.run(main())
        end_time = time.time()
        print(f"\nОбщее время выполнения: {end_time - start_time:.2f} сек")
