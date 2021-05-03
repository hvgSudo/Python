from prettytable import PrettyTable

table = PrettyTable(
    ["Processes", "Arrival Time", "Bust Time", "Completion Time", "Turn Around Time", "Waiting Time",
     "Response Time"])
ct = []
tt = []
wt = []
rt = []
process = int(input("\nEnter total number of processes = "))
print("Enter Arrival Time - ")
arrival = []
for i in range(process):
    at = int(input(f"Enter Arrival Time of P{i+1} = "))
    arrival.append(at)
    ct.append(0)
    tt.append(0)
    wt.append(0)
    rt.append(0)
print("\nEnter Bust Time - ")
bust = []
bust_copy = []
for i in range(process):
    bt = int(input(f"Enter Bust Time of P{i+1} = "))
    bust.append(bt)
    bust_copy.append(bt)

clock = 0
ready = []
visited = []
while True:
    ind = 0
    for i in range(process):
        if arrival[i] <= clock and bust_copy[i] != 0 and i not in ready:
            ready.append(i)

    if len(ready) != 0:
        min_bt = bust_copy[ready[0]]
        ind = ready[0]
        for i in range(len(ready)):
            if min_bt > bust_copy[ready[i]]:
                ind = ready[i]
                min_bt = bust_copy[ready[i]]
        if ind not in visited:
            visited.append(ind)
            rt[ind] = clock - arrival[ind]
        clock += 1
        bust_copy[ind] -= 1
        if bust_copy[ind] == 0:
            ct[ind] = clock
            ready.remove(ind)
    else:
        clock += 1
    if clock == sum(bust):
        break
for i in range(process):
    tt[i] = ct[i] - arrival[i]
    wt[i] = tt[i] - bust[i]
for i in range(process):
    table.add_row([f"p{i+1}", arrival[i], bust[i], ct[i], tt[i], wt[i], rt[i]])
print(table)