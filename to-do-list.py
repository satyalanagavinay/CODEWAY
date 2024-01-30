tasks = []

class Daily:
    
    def take_task(self):
        task = input("\nEnter the task:\t")
        tasks.append(task)
        print("Task Added Successfully...!!")

    def delete_task(self):
        if tasks:
            tasks.pop()
            print("Task Delete Successfully...!!")
        else:
            print("\nNo tasks to delete.")

    def view(self):
        if tasks:
            print("\nTask List:")
            for task in tasks:
                print(f"\t{task}")
        else:
            print("\nNo tasks available.")

a = Daily()
while True:
    print("\n1.Take Task\n2.Delete Task\n3.View Tasks\n4.Exit\n")
    i=int(input())
    if i<5 and i>0:
        if i==1:
            a.take_task()
        if i==2:
            a.delete_task()
        if i==3:
            a.view()
        if i==4:
            print("Thanks For Using...!!")
            break
    else:
        print("Choose from above Options Only !!!")
        break
