# Simulasi CPU Schedulling FCFS 

proses = ["P1","P2","P3","P4"]
arrival_time = [0,1,2,3]
burst_time = [6,8,7,3]

n= len(proses)

completion_time  = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n 

#FCFS
completion_time[0] = burst_time[0]
for i in range (1,n):
    completion_time[i] = completion_time[i-1] + burst_time[i]

#TAT DAN Waiting Time 
for i in range(n):
 turnaround_time[i]= completion_time[i] - arrival_time[i]
waiting_time[i] = turnaround_time[i] - burst_time[i]

print("FCFS")
print("-------------------------------")
print("proses\ tArrival\ tBurst\ tWaiting\ tTurnaround")
print("-------------------------------")

for i in range (n):
    print(f"{proses[i]}\t{arrival_time[i]}\t{burst_time[i]}\t"
          f"{waiting_time[i]}\t{turnaround_time[i]}")