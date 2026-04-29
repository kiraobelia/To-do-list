def main():
    tasks = []
    
    while True:
        print("\n--- Меню To-Do List ---")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            if not tasks:
                print("Список задач пуст.")
            else:
                print("\nВаши задачи:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        
        elif choice == '2':
            new_task = input("Введите текст задачи: ")
            tasks.append(new_task)
            print("Задача добавлена!")
            
        elif choice == '3':
            task_to_remove = input("Введите название задачи для удаления: ")
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print("Задача удалена.")
            else:
                print("Ошибка: задача не найдена.")
                
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
