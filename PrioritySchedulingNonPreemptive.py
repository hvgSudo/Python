from prettytable import PrettyTable

table = PrettyTable(["Processes", "Arrival Time", "Burst Time",
        "Priority", "Start Time", "Completion Time", 
        "Turn Around Time", "Waiting Time"])

numberOfProcesses = int(input("Enter total number of processes: "))
process = []

for i in range(numberOfProcesses):
    lst = []
    for j in range(4):
        lst.append(0)
    process.append(lst)
for i in range(numberOfProcesses):
    print()
    print(f"PROCESS {i + 1}")
    process[i][0] = int(input("Arrival time: "))
    process[i][1] = int(input("Burst time: "))
    process[i][2] = int(input("Priority: "))
    process[i][3] = i + 1

def getWaitingTime(waitingTime):
    waitingTime[0] = 0
    lst = [0] * numberOfProcesses
    lst[0] = 0
    for i in range(1, numberOfProcesses):
        lst[i] = process[i - 1][1] + lst[i - 1]
        waitingTime[i] = lst[i] - process[i][0]
        if waitingTime[i] < 0:
            waitingTime[i] = 0

def getTurnAroundTime(turnAroundTime, waitingTime):
    for i in range(numberOfProcesses):
        turnAroundTime[i] = process[i][1] + waitingTime[i]

waitingTime = [0] * numberOfProcesses
turnAroundTime = [0] * numberOfProcesses
startTime = [0] * numberOfProcesses
completionTime = [0] * numberOfProcesses

getWaitingTime(waitingTime)
getTurnAroundTime(turnAroundTime, waitingTime)

startTime[0] = 0
completionTime[0] = startTime[0] + turnAroundTime[0]

for i in range(1, numberOfProcesses):
    startTime[i] = completionTime[i - 1]
    completionTime[i] = process[i][0] + turnAroundTime[i]

for i in range(numberOfProcesses):
    table.add_row([process[i][3], process[i][0], process[i][1],
        process[i][2], startTime[i], completionTime[i],
        turnAroundTime[i], waitingTime[i]])

print(table)
print("Average Waiting time:",sum(waitingTime) / numberOfProcesses)
print("Average Turn Around time:",sum(turnAroundTime) / numberOfProcesses)
print()