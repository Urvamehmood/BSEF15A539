total_runningTime = 0
priority=[]
processes={}
burst_time=[]
waiting_time=[]
turnaround_time=[]
number_processes = input("Enter the number of processes:")
for i in range (0,number_processes):
	priority_no=input("Priority number of process :")
	priority.append(priority_no)
	Burst_time=input("Burst Time of process :")
	burst_time.append(Burst_time)
	processes[priority[i]] = [i , burst_time[i]]
print "Process         Priority     Arrival Time           Burst Time"
for i in range (0,number_processes):
	print i,"               ", priority[i] ,"            "  ,"0" ,"                 " , burst_time[i] 
priority.sort()
start_time = total_runningTime
for i in range (0,number_processes):
	total_runningTime = total_runningTime + processes.get(priority[i])[1]
        index_to_put=processes.get(priority[i])[0]
        waiting_time.insert(index_to_put,start_time)
        turnaround_time.insert(index_to_put,total_runningTime)
	print start_time , "________" , total_runningTime
	start_time = total_runningTime
print"Process              Waiting Time            Turnaround Time"
for i in range (0, number_processes):
        print i,"                     ",waiting_time[i],"                   ",turnaround_time[i]
