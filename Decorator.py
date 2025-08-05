# decorators : adding functionality without altering function


def auth(root):
    def wrapper(user_name : str):
        user_id = str(input("Enter (user id / user email) : "))
        password = str(input("Enter Password : "))
        
        if user_id == password:
            root(user_name)
        else:
            print("Wrong Credentials, Please retry using authentic credentials..")
            return
    return wrapper

@auth
def root(user_name : str):
    print(f"Welcome {user_name}, What you want to buy today ?")
    
    
root("Ujjwal")
