import time 

class loginInfo:
    def __init__(self):
        pass
    
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            results = func(*args,**kwargs)
            with open("login_db.txt","a") as file_obj:
                file_obj.write(f"{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} with name {results[0]}")
            return results
        return wrapper