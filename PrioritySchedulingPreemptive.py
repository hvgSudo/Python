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

tat = wt = clock = count = 0

numberOfProcesses = int(input("Enter total number of processes: "))
a = b = p = 0
for i in range(numberOfProcesses):
    print()
    arrivalTime.append(int(input("Enter arrival time for process {:d}: ".format(i+1))))
    burstTime.append(int(input("Enter burst time for process {:d}: ".format(i+1))))
    priority.append(int(input("Enter priority for process {:d}: ".format(i+1))))

# the processes will be added to a waiting queue based on their arrival time
# the processes will be based on their arrival time 
while True:
    if arrivalTime[count] == clock:
        readyQueue.append(count)
    count = count + 1
    clock = clock + 1

for i in range(numberOfProcesses):
    table.add_row(["P{:d}".format(i+1), arrivalTime[i], burstTime[i],
        priority[i], completionTime[i], turnAroundTime[i],
        waitingTime[i], responseTime[i]])

print(table)
print()