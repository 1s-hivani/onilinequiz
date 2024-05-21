class HostelEntrySystem:
    def __init__(self):
        self.residents = []

    def add_resident(self, name, room_number):
        resident = {"name": name, "room_number": room_number}
        self.residents.append(resident)
        print(f"{name} has been added to room {room_number}.")

    def list_residents(self):
        print("List of residents:")
        for resident in self.residents:
            print(f"Name: {resident['name']}, Room: {resident['room_number']}")

    def search_resident(self, name):
        for resident in self.residents:
            if resident['name'] == name:
                print(f"Resident {name} is staying in room {resident['room_number']}.")
                return
        print(f"Resident {name} not found.")

def main():
    hostel_system = HostelEntrySystem()

    while True:
        print("\nHostel Entry System")
        print("1. Add Resident")
        print("2. List Residents")
        print("3. Search Resident")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter resident's name: ")
            room_number = input("Enter room number: ")
            hostel_system.add_resident(name, room_number)
        elif choice == "2":
            hostel_system.list_residents()
        elif choice == "3":
            name = input("Enter resident's name to search: ")
            hostel_system.search_resident(name)
        elif choice == "4":
            print("Exiting Hostel Entry System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
