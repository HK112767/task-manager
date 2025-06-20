import datetime

def user_information(usnm, pssd):  
    name = input("Enter your name: ")
    address = input("Your address: ")
    age = input("Your age: ")
    usnm_ = usnm +" task.txt"
    f = open(usnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Address1 :")

    f.write(address)
    f.write('\n')
    f.write("Age :")
    f.write(age)
    f.write('\n')
    f.close()


def signup():
    print("Please enter the username by which you wanna access your account")
    username = input("please enter here:  ")
    password = input("Enter a password:  ")
    user_information(username, password)
    print("Sir/Ma'am please proceed towards log in")
    login()


def login():
    print("Please enter your username ")
    user_nm = input("Enter here: ")
    
    # Password as entered while logging in
    pssd_wr = (input("Enter the password: "))+'\n'
    try:
        usernm = user_nm+" task.txt"
        f_ = open(usernm, 'r')
        
        # variable 'k' contains the password as saved
        # in the file
        k = f_.readlines(0)[0]
        f_.close()
        
        # Checking if the Password entered is same as 
        # the password saved while signing in
        if pssd_wr == k:   
            print(
                "1--TO VIEW YOUR DATA \n2--TO ADD TASK \n3--UPDATE TASK \n4--VIEW TASK STATUS")
            a = input()
            
            if a == '1':
                view_data(usernm)
            elif a == '2':
                # add task
                task_information(usernm)
            elif a == '3':
                task_update(user_nm)
            elif a == '4':
                task_update_viewer(user_nm)
            else:
                print("Wrong input! Please try again")
        else:
            print("YOUR PASSWORD OR USERNAME IS WRONG")
            login()

    except Exception as e:
        print(e)
        login()


def view_data(username):
    ff = open(username, 'r')
    print(ff.read())
    ff.close()


def task_information(username):
    print("Enter no. of task you want to add: ")
    j = int(input())
    f1 = open(username, 'a')
    
    for i in range(1, j+1):
        task = input("Enter the task: ")
        target = input("Enter the target: ")
        pp = "TASK "+str(i)+' :'
        qq = "TARGET "+str(i)+" :"
        
        f1.write(pp)
        f1.write(task)
        f1.write('\n')
        f1.write(qq)
        f1.write(target)
        f1.write('\n')
        print("Do u want to stop? press 0 to stop or enter to continue")
        s = input()
        if s == '0':
            break
    f1.close()


def task_update(username):
    username = username+" TASK.txt"
    print("Please enter the tasks which are completed: ")
    task_completed = input()
    
    print("Enter task which are still not started by you: ")
    task_not_started = input()
    
    print("Enter task which you are doing: ")
    task_ongoing = input()
    
    fw = open(username, 'a')
    DT = str(datetime.datetime.now())
    fw.write(DT)
    fw.write("\n")
    fw.write("COMPLETED TASK \n")
    fw.write(task_completed)
    fw.write("\n")
    fw.write("ONGOING TASK \n")
    fw.write(task_ongoing)
    fw.write("\n")
    fw.write("NOT YET STARTED\n")
    fw.write(task_not_started)
    fw.write("\n")


def task_update_viewer(username):
    ussnm = username+" TASK.txt"
    o = open(ussnm, 'r')
    print(o.read())
    o.close()


if __name__ == '__main__':
    print("WELCOME TO TASK MANAGER")
    print("Are you new to this software?")
    a = int(input("Type 1 if new otherwise press 0 :: "))
    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have provided wrong input!")
