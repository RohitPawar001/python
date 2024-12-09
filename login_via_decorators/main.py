from python.utils import loginInfo


@loginInfo()
def logins(name,age,gender):
    login_list = []
    login_list.append([name,age,gender])
    return login_list

if __name__ == "__main__":
    name = input("enter your name")
    age = int(input("enter your age"))
    gender = input("choose your gender [M/F]").lower()
    
    logins(name,age,gender)