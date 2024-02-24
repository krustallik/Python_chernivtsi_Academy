import psutil

# Отримати інформацію про використання процесора
cpu_usage = psutil.cpu_percent(interval=1)
print(f'CPU Usage: {cpu_usage}%')

# Отримати інформацію про використання пам'яті
memory_info = psutil.virtual_memory()
print(f'Total Memory: {memory_info.total} bytes')
print(f'Used Memory: {memory_info.used} bytes')
print(f'Free Memory: {memory_info.free} bytes')

# Отримати інформацію про всі процеси
process_list = psutil.process_iter()
for process in process_list:
    try:
        # Отримати інформацію про кожен процес
        process_name = process.name()
        process_pid = process.pid
        process_cpu_percent = process.cpu_percent()
        process_memory_info = process.memory_info()
        print(f'Process: {process_name}, PID: {process_pid}')
        print(f'CPU Percent: {process_cpu_percent}%')
        print(f'Memory Info: {process_memory_info}')
        print('-' * 30)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        # Ігноруємо винятки, якщо процес не існує або нема доступа
        pass

#програма виписує інформпацію про кожен процес запущений на компютері
