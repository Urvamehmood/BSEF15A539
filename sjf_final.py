total_runningTime = 0
processes={}
burst_time=[]
waiting_time=[]
turnaround_time=[]
number_processes = input("Enter the number of processes:")
for i in range (0,number_processes ):
	Burst_time=input("Burst Time of process :")
	burst_time.append(Burst_time)
	processes[burst_time[i]] = [i]

print"Process      Arrival Time         Burst Time"
for i in range (0,number_processes):
	print i,"                ", "0", "               " , burst_time[i] 
burst_time.sort()
start_time = total_runningTime 

for i in range (0,number_processes):
	total_runningTime = total_runningTime + burst_time[i]
        index_to_put= processes.get(burst_time[i])[0]
        waiting_time.insert(index_to_put,start_time)
        turnaround_time.insert(index_to_put,total_runningTime)
       	print start_time , "________" , total_runningTime
	start_time = total_runningTime
print "Process       waiting time            Turnaround time"
for i in range(0,number_processes ):
        print i,"                 ", waiting_time[i], "                  ", turnaround_time[i]
