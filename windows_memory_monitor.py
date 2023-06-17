import psutil

processes = []
total = 0

for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
    try:
        memory = proc.info['memory_info'].rss/1024/1024
        processes.append([proc.info['name'], memory])
        total += proc.info['memory_info'].rss/1024/1024
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
top_processes = sorted(processes,key=lambda x:x[1],reverse=True)[:10]
top_processes = [f'{p[0]} {p[1]:.0f}MB' for p in top_processes]
top_processes =  ', '.join(top_processes)


print('top process: ',top_processes)
print(f'total used {total:,.1f}MB')


  