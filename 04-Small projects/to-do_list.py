task = []


def main():
    while True:
        print("<=====To-do List=====>")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            note = input("Enter task:")
            task.append(note)
            print(task)
        elif choice == 2:
            if len(task)== 0:
                print("No tasks available.")
            else:
                for i in range(len(task)):
                    print(i)
        elif:

main()

