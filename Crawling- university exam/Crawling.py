
import subprocess 
start = 2000001
end   = 2074719
file = open("raw_data.txt","w")
for sbd in range(start,end):
    command = 'curl -F "sobaodanh=0'+ str(sbd) + '" diemthi.hcm.edu.vn/Home/Show'
    result  = subprocess.check_output(command,shell=True) 
    file.write(str(result)+"\n")
