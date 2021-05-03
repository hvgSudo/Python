from prettytable import PrettyTable

table = PrettyTable(["Processes", "Arrival Time", "Burst Time",
        "Priority", "Start Time", "Completion Time", 
        "Turn Around Time", "Waiting Time"])

numberOfProcesses = int(input("Enter total number of processes: "))
process = []
waitingTime = [0] * numberOfProcesses
turnAroundTime = [0] * numberOfProcesses
startTime = [0] * numberOfProcesses
completionTime = [0] * numberOfProcesses
burstTime = [0] * numberOfProcesses
isCompleted = [0] * numberOfProcesses

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
    burstTime[i] = process[i][1]

clock = completed = 0

while (completed != numberOfProcesses):
    index = 100
    priority = 100
    for i in range(numberOfProcesses):
        if process[i][0] <= clock and isCompleted[i] == 0:
            if process[i][2] < priority:
                priority = process[i][2]
                index = i
            if process[i][2] == priority:
                if process[i][0] < process[index][0]:
                    priority = process[i][2]
                    index = i
    
    if index != -1:
        if burstTime[index] == process[index][1]:
            startTime[index] = clock
        burstTime[index] -= 1
        clock += 1
    
        if burstTime[index] == 0:
            completionTime[index] = clock
            turnAroundTime[index] = completionTime[index] - process[index][0]
            waitingTime[index] = turnAroundTime[index] - process[index][1]
            isCompleted[index] = 1
            completed += 1
    else:
        clock += 1

for i in range(numberOfProcesses):
    table.add_row([process[i][3], process[i][0], process[i][1],
        process[i][2], startTime[i], completionTime[i],
        turnAroundTime[i], waitingTime[i]])

print(table)
print("Average Waiting time:",sum(waitingTime) / numberOfProcesses)
print("Average Turn Around time:",sum(turnAroundTime) / numberOfProcesses)
print()