#create /add new logs(append)
with open("log.txt","a") as f:
    f.write("ERROR:Payment failed\n")
    f.write("INFO:Logout\n")
    f.write("ERROR:Server down\n")
#generator
def read_logs(file):
    with open(file,"r") as f:
        for line in f:
            yield line.strip()
#count errors
error_count={}
for line in read_logs("log.txt"):
    if "ERROR" in line:
        error_count[line] = error_count.get(line,0)+1
#output
print("Error Count:")
for error ,count in error_count.items():
    print(error,"->",count)