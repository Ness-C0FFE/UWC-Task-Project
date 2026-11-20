# Advanced "To Do List" Application 
# - My Docs: -
'''
    To Do List :
        _This Just Text App To Test My Level And Improve It.
            _I Used All Things Thits I learned By Elzero Python Course.
    I Used Here :
        _Data Time Module.
        _File Handling.
        _Dict/Nested_Dict/Global Dict.
        _Dictionary Module.
        _Lists.
        _For/While Loop.
        _Functions.
        _Try-Except.
        _If Condational.
        _Nested Condational.
        _Date Type.
        _Docs/Documentation.
        _Type Hinting.
        _Built In Functions.
        _debugging.

'''

# Title Of App:/.
App_Title : str = ' To Do List '
print(
    "=" * 28 + "\n" + 
     App_Title.center(28, "=")
     + "\n" + "=" * 28
    )

# Import Date Time Module
import datetime 

# - Global Dict (Tasks): -
task_dict : dict = {
    "Code":{"Task": "Coding Today", "Data": "24 February 2026", "Statu": "Done"},
    "Shower":{"Task": "Take A Shower", "Data": "4 August 2026", "Statu": "Not Done"}
}

# - Add Task Func -
def add_task():

    print(" -- Add+ Task -- " + "\n")

    add_task_name = input(
          "Enter Your Task Name: "
        ).strip().capitalize()

    try:
        if add_task_name not in task_dict:

            adding_task = input("Enter Your Tasking: ").strip().capitalize()
            print("Task Adding successfully!")
            
            time_now = datetime.datetime.now()
            date = time_now.strftime("%d %B %Y")
            task_dict[add_task_name] = {
                "Task": adding_task,"Data": date,"Statu": "Not Done"
                }
            main_func()
        else:
            print(f"'{add_task_name}' Already In Your List")
            main_func()
    except:

        print("Wrang Input!")
        main_func()

# - Show User Task Func - 
def show_tasks():

    print("Your Tasks: \n")

    for task, task_info in task_dict.items():

        print(f"Task Name: '{task}'\n_Task: {task_info['Task']}\n_Data: {task_info['Data']}\n_Statu: {task_info['Statu']}\n")

    meniu = [
        "0.Back To Main Hub",
        "1.Edit Task",
        "2.Delete Task"
    ]
    for m in meniu:
        print(m)
    user_choise = input("Enter Your Choise: ").strip().capitalize()
    try:
        if user_choise == "0":
            main_func()
        elif user_choise == "1":
            edit_task()
        elif user_choise == "2":
            delete_task()
        else:
            print("Invalid Choise, Please Try Again")
            main_func()
    except:
        print("There Is Some Errors But Dont Worry We Work To Fix It\n")

    main_func()

# - Task Deleting Func - 
def delete_task():

    print(" -- Delete -- ","\n")

    task_delete = input("Enter The Task You Want To Delete: ").strip().capitalize()

    try:
        if task_delete in task_dict:
            del task_dict[task_delete] # Delete Task From Task_Dict
            print(f"Task '{task_delete}' Deleted successfully!") # Send A Msg That Tell User Has Task Was Deleted successfully
            main_func() # - Back To Main Fucntion/Meniu
        else:
            print(f"'{task_delete}' Not In List, Please Try Again")
            main_func()
    except:
        print("Invaild Input, Please Try Again")
        main_func()

# - Task Editing Func -
def edit_task():

    print(" -- Edit -- ","\n")

    task_edit = input("Enter The Task You Want To Edit: ").strip().capitalize()

    try:
        if task_edit in task_dict:
            editing_task = input("Enter Your New Tasking: ").strip().capitalize()
            task_dict[task_edit]['Task'] = editing_task
            print(f"Task '{task_edit}' Editing successfully!") # Send A Msg That Tell User Has Task Was Deleted successfully
            main_func() # - Back To Main Fucntion/Meniu
        else:
            print(f"'{task_edit}' Not In List, Please Try Again")
            main_func()
    except:
        print("Invaild Input, Please Try Again")
        main_func()

# - Marking Task Func - 
def mark_task():

    print(" -- Task Marking -- " + "\n")
    task_marking = input("Enter The Task You Want To Marking: ").strip().capitalize()

    try:
        if task_marking in task_dict:
            if task_dict[task_marking]['Statu'] == 'Done':
                print("This Task already Done")
                main_func()
            else:
                task_dict[task_marking]['Statu'] = 'Done'
                print(f'Task: "{task_marking}" Done')
                main_func()       
        else:
            print(f"'{task_marking}' Not Found!, Please Try Again")
            main_func()

    except:
        print("Invalid Input, You Typed False Input")
        main_func()

# - Main Menu Func -
def main_func():

    choice_list : list = [ # - Choice List That User Can Choice With It
        "\n" + 
        "1.Add Task",
        "2.Show Tasks",
        "3.Mark Task", 
        " - Exit - \n"
        ]
    for choice in choice_list: # - For Loop To Print The List
        print(choice)

    '''
    Choice_Dict:
        I Made It To Make My App Dynamic And Easy To Improve In Future.            
    '''

    # Dynamic Dictionary Choise For Easy Experas For User
    choice_dict : dict = {
        "Add":{"Add", "Add task", "One", "1"},
        "Show":{"My task","Task List","Show task", "Show my task", "Two","2"},
        "Mark":{"Mark","Mark task","Three","3"}
    }

    user_choice : None = None # Variable with None Statu To Use It With Loop

    while user_choice != "Exit":

        user_choice = input(
                  'Enter Your Choice(1, 2, 3)\nOr Enter "Exit" To Close The App: '
                ).strip().capitalize()
        print(f"Your Choise Is: '{user_choice}'\n")

        if user_choice == "Exit":
            print("\n - App Closed - \n")
            
        else:
            try: # - Try To Choice
                if user_choice in choice_dict['Add']: 
                    add_task()

                elif user_choice in choice_dict['Show']:
                    if task_dict == {}:
                        print("There Is No Task found To Show It, Add Task Firstly\n")
                    else:
                        show_tasks()

                elif user_choice in choice_dict['Mark']:
                    if task_dict == {}:
                        print("There Is No Task found To Mark It, Add Task Firstly\n")
                    else:
                        mark_task()

                else:
                    print("Invalid Choice, Please Try Again\n")

            except : # - Except If There Is Wrong/Errors In App
                print("There Is Some Errors But Dont Worry We Work To Fix It\n")
main_func()