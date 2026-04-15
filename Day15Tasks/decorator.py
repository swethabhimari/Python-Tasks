#decorator creation
roles={"admin":True,"User":False}
#check condition
def check_access(func):
    def wrapper(role):
        if roles.get(role):
            return func(role)
        else:
            print("Access Denied")
            return None
    return wrapper
@check_access
def delete_data(role):
    print("Data deleted by:",role)
delete_data("admin")
delete_data("user")