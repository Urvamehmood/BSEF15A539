total_runningTime = 0
processes={}
burst_time=[]
arrival_time=[]
arrival_sorted=[]
waiting_time=[]
turnaround_time=[]
waiting_sum=0
turnaround_sum=0
number_processes = input("Enter the number of processes:")
for i in range (0,number_processes):
	arrive_time=input("Arrival Time of process :")
	arrival_time.append(arrive_time)
	Burst_time=input("Burst Time of process :")
	burst_time.append(Burst_time)
	processes[i] = [ arrival_time[i], burst_time[i]]
print "Process       Arrival Time           Burst Time"
for i in range (0,number_processes):
	print " P", i+1,"            ", arrival_time[i], "                  " , burst_time[i]
for i in range (0,number_processes):
        arrival_sorted.insert(i,arrival_time[i]) 
arrival_sorted.sort()
total_runningTime = arrival_sorted[0]
start_time = total_runningTime
print "\n"
if(total_runningTime>0):
	print '0 -------' , total_runningTime 
for j in range (0,number_processes):
        for i in range (0,number_processes):
                number=processes.get(i)[0]
                if(arrival_sorted[j]==number):
                	total_runningTime = total_runningTime + processes.get(i)[1]
                        arriv_time= number
                        w_time= start_time-arriv_time
                        f_time=total_runningTime-arriv_time
                        waiting_time.insert( i,w_time)
                        turnaround_time.insert(i,f_time)
                        print "     P",i+1
                	print start_time , "________" , total_runningTime
                	start_time = total_runningTime
print "\n"
print "Process              Waiting Time          Turnaround time"
for i in range (0,number_processes):
        print "P", i+1,"                   ", waiting_time[i] ,"                       ",turnaround_time[i]
        waiting_sum=waiting_sum+waiting_time[i]
        turnaround_sum=turnaround_sum+turnaround_time[i]
waiting_avg=waiting_sum/number_processes
turnaround_avg=turnaround_sum/number_processes
print "\n"
print "Average waiting_time= ",waiting_avg
print "Average turnaround_time= ",turnaround_avg
