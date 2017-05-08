total_runningTime = 0
waiting_sum=0
turnaround_sum=0
Burst_sorted=[]
processes={}
burst_time=[]
waiting_time=[]
turnaround_time=[]
print "                  SHORTEST JOB FIRST SCHEDULING ALGORITHM             "
print "\n"
number_processes = input("Enter the number of processes:")
print "\n"
for i in range (0,number_processes):
	Burst_time=input("Burst Time of process :")
	burst_time.append(Burst_time)
	processes[i] = [burst_time[i]]
print "\n"
print "Process              Arrival Time           Burst Time"
for i in range (0,number_processes):
	print"P",i+1,"                       "  ,"0" ,"                " , burst_time[i] 
        Burst_sorted.insert(i,burst_time[i])
Burst_sorted .sort()
start_time = total_runningTime
print"\n" 
print "                           GANTT CHART                         "
print "\n"
for j in range (0,number_processes):
        for i in range (0,number_processes):
                number=processes.get(i)[0]
                if(Burst_sorted[j]==number):
                	total_runningTime = total_runningTime + processes.get(i)[0]
                        waiting_time.insert(i,start_time)
                        turnaround_time.insert(i,total_runningTime)
                        print"        P",i+1
                	print start_time , "_____________" , total_runningTime
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
