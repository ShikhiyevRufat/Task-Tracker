from src.task_manager import add_task, delete_task, update_task, get_status, read_tasks

def start_app():
    print("*"*30 + " Welcome to Task Tracker! " + "*"*30 + "\n")

    while True:
        print("\nMenyu:\n" \
              "1 - Tapşırıq əlavə et\n" \
              "2 - Tapşırığı sil\n" \
              "3 - Tapşırığı yenilə (status)\n" \
              "4 - Bütün tapşırıqları göstər\n" \
              "5 - Yalnız tamamlanmış ('done') tapşırıqlar\n" \
              "6 - Yalnız başlanmamış ('not done') tapşırıqlar\n" \
              "7 - Yalnız davam edən ('in progress') tapşırıqlar\n" \
                )
        
        user_choice = input("Seçiminiz (1-7): ")

        if user_choice == '1':
            title = input("Title of task: ")
            description = input("Description of task: ")
            add_task(title, description)
        elif user_choice == '2':
            task_id = input("Write you task id which you want delete: ")
            delete_task(task_id)
        elif user_choice == "3":
            task_id = input("Write task id which you want update: ")
            status = input("Update status (done | not done | in progress): ")
            update_task(task_id, status)
        elif user_choice == "4":
            print(get_status())
        elif user_choice == "5":
            print(get_status("done"))
        elif user_choice == "6":
            print(get_status("not done"))
        elif user_choice == "7":
            print(get_status("in progress"))
