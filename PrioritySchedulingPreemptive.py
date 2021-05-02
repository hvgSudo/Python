from prettytable import PrettyTable

table = PrettyTable(["Processes", "Arival Time", "Burst Time",
        "Priority", "Completion Time", "Turn Around Time", 
        "Waiting Time", "Response Time"])

readyQueue = list()
completedQueue = list()
waitingQueue = list()
arrivalTime = list()
burstTime = list()
priority = list()
completionTime = list()
turnAroundTime = list()
waitingTime = list()
responseTime = list()
processClock = list()

tat = wt = clock = 0

numberOfProcesses = int(input("Enter total number of processes: "))
a = b = p = 0
for i in range(numberOfProcesses):
    print()
    a = int(input("Enter arrival time for process {:d}: ".format(i+1)))
    b = int(input("Enter burst time for process {:d}: ".format(i+1)))
    p = int(input("Enter priority for process {:d}: ".format(i+1)))
    arrivalTime.append(a)
    burstTime.append(b)
    priority.append(p)

while True:
    if clock == sum(burstTime):
        break
    for i in range(numberOfProcesses):
        if arrivalTime[i] <= clock:
            for j in range(i):
                if priority[i] > priority[j]:
                    readyQueue.append(i)
    clock = clock + 1

for i in range(numberOfProcesses):
    table.add_row(["P{:d}".format(i+1), arrivalTime[i], burstTime[i],
        priority[i], "", "", "", ""])

print(table)
print()