import psutil
cpu_times = psutil.cpu_times()
print(cpu_times)

cpu_count = psutil.cpu_count(logical=True)
print(cpu_count)

disk_usage = psutil.disk_usage("/")
print(disk_usage)

print(psutil.pids())

print(psutil.process_iter(['pid', 'name', 'username']))

#######################################################################
#Q19
nome_processo = input("Qual o processo você deseja encontrar? ")

for proc in psutil.process_iter(['pid', 'name', 'username']):
    #print(proc.info)
    #if proc.info["username"] == "IFRN\\1724026":
    #    print(proc.info)
    if proc.info["name"].lower() == nome_processo.lower():
        print("Sim. Este processo está em execução")

#######################################################################