total_runningTime = 0
waiting_sum=0
turnaround_sum=0
priority=[]
priority_sorted=[]
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
	processes[i] = [ priority[i],burst_time[i]]
print "Process         Priority     Arrival Time           Burst Time"
for i in range (0,number_processes):
	print"P",i+1,"               ", priority[i] ,"            "  ,"0" ,"                 " , burst_time[i] 
        priority_sorted.insert(i,priority[i])
priority_sorted .sort()
start_time = total_runningTime
print"\n"
for j in range (0,number_processes):
        for i in range (0,number_processes):
                number=processes.get(i)[0]
                if(priority_sorted[j]==number):
                	total_runningTime = total_runningTime + processes.get(i)[1]
                        waiting_time.insert(i,start_time)
                        turnaround_time.insert(i,total_runningTime)
                        print"          P",i+1
                	print start_time , "______________" , total_runningTime
                 	start_time = total_runningTime
print"\n"
print"Process              Waiting Time            Turnaround Time"
for i in range (0, number_processes):
        print "P", i+1,"                     ",waiting_time[i],"                   ",turnaround_time[i]
        waiting_sum=waiting_sum+waiting_time[i]
        turnaround_sum=turnaround_sum+turnaround_time[i]
waiting_avg=waiting_sum/number_processes
turnaround_avg=turnaround_sum/number_processes
print "\n"
print "average waiting_time =",waiting_avg
print "average turnaround_time =",turnaround_avg
