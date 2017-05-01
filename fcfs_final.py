total_runningTime = 0
processes={}
burst_time=[]
arrival_time=[]
waiting_time=[]
turnaround_time=[]
number_processes = input("Enter the number of processes:")
for i in range (0,number_processes):
	arrive_time=input("Arrival Time of process :")
	arrival_time.append(arrive_time)
	Burst_time=input("Burst Time of process :")
	burst_time.append(Burst_time)
	processes[arrival_time[i]] = [ i, arrival_time[i], burst_time[i]]
print "Pocess       Arrival Time           Burst Time"
for i in range (0,number_processes):
	print"P", i,"            ", arrival_time[i], "                  " , burst_time[i] 
arrival_time.sort()
total_runningTime = processes.get(arrival_time[0])[1]
start_time = total_runningTime
print"\n"
if(total_runningTime>0):
	print '0 -------' , total_runningTime 

for i in range (0,number_processes):
	total_runningTime = total_runningTime + processes.get(arrival_time[i])[2]
        index_To_Put=processes.get(arrival_time[i])[0]
        arriv_time= arrival_time[i]
        w_time= start_time-arriv_time
        f_time=total_runningTime-arriv_time
        waiting_time.insert( index_To_Put,w_time)
        turnaround_time.insert(index_To_Put,f_time)
        print"     P",index_To_Put
	print start_time , "________" , total_runningTime
	start_time = total_runningTime
print"\n"
print "Process              Waiting Time          Turnaround time"
for i in range (0,number_processes):
        print"P", i,"                   ", waiting_time[i] ,"                       ",turnaround_time[i]

