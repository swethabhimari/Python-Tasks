
try:
    with open("log.txt","a") as f:
        while True:
            log = input("Enter log(type 'exit' to stop): ") #takes input from user
            if log.lower() == "exit":
               break
        
            f.write(log + "\n")
except Exception as e:
    print("File Error:",e)