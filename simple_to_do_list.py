# class ToDoList implements all the operations of ToDoList 
class ToDoList:
    def __init__(self,name:str) -> None:
        self.name = name
        self.list = {self.name:[]}
        
    # add_task function ads's tasks into the ToDoList    
    def add_task(self) -> None:
        no_of_tasks = int(input("enter the no of tasks do you want to add : "))
        for i in range(no_of_tasks):
            task = input("enter th task yo add to the to do list : ")
            if task not in self.list[self.name]:
                self.list[self.name].append(task)
                print("task has been added successfully")
            else:
                choice = input("the task alreadypresent in the list, do you want to complete/delete this task (y/n) : ")
                if choice == "y":
                    operation = input("which operation do you want to perform 1. complet task 2. delete task 3. display task : ")
                    print("please enter valid operation")
                    if operation == "1":
                        self.completed_task()
                    elif operation == "2":
                        self.delete_task()
                    elif operation == "3":
                        self.display_task()
                
      
    # completed_task function removes task from the ToDoList if it is completed           
    def completed_task(self) -> None:
        task = input("enter the task that you have completed : ")
        if task in self.list[self.name]:
            self.list[self.name].remove(task)
            print("task has been completed")
        else:
            no_task = input("the task that you have entered which have not been in the to do list, do you want to add this task (y/n)? : ")
            if no_task == "y":
                self.list[self.name].append(task)
                print("task added successfully")
    
    # delete_task function delete the task from the ToDoList 
    def delete_task(self) -> None:
        task_to_delete = input("enter the task which you want to delete : ")
        if task_to_delete in self.list[self.name]:
            self.list[self.name].remove(task_to_delete)
            print("task has been deleted successfully")
        else:
            display = input("please enter the valid task, do you want to see list (y/n) ? : ")
            if display == "y":
                self.display_task()
                
        
    # display_task function displays all the uncompleted tasks from the ToDoList     
    def display_task(self) ->None:
        if len(self.list[self.name]) != 0:
            print("--------------------------")
            print(f" {self.name}'s ToDoList")
            print("---------------------------")
            for i in self.list[self.name]:
                print(i)
            print("---------------------------")
        else:
            print("yours to do list is empty")
            add = input("do you want add the task into the ToDoList (y/n)? : ")
            if add == "y":
                self.add_task()
                
            
    
if __name__ == "__main__":
    
    name = input("enter your name to generate your ToDoList : ")
    todays_tasks = ToDoList(name)
    
    while True:
        operation = input("would you like to \n 1. add \n 2. complete \n 3. delete \n 4. display task \n 5. Exit \n : ")
        if operation == "1":
            todays_tasks.add_task()
        elif operation == "2":
            todays_tasks.completed_task()
        elif operation == "3":
            todays_tasks.delete_task()
        elif operation == "4":
            todays_tasks.display_task()
        elif operation == "5":
            break
        else:
            print("please neter valid operation")