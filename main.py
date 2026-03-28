from tasks import add_task, show_tasks, delete_task

def menu():
    while True:
        print("/1. Aufgabe hinzufügen")
        print("2. Aufgabe anzeigen")
        print("3. Aufgabe löschen")
        print("4. Beenden")

        choice = input("Wähle: ")

        if choice == "1":
            task = input("Neue Aufgabe: ")
            add_task(task)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            index = int(input("Nummer der Aufgabe: "))
            delete_task(index)

        elif choice == "4":
            break

        else:
            print("Ungültige Auswahl")

menu()