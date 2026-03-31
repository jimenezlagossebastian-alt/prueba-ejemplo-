from student_logic import *

# -------- MENU -------- #

def show_menu():
    print("\n=================================")
    print(" STUDENT MANAGEMENT SYSTEM")
    print("=================================")
    print("1. Register New Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")
    print("=================================")


def start_app():
    while True:
        show_menu()
        option = input("Select an option (1-6): ").strip()

        try:
            if option == "1":
                s_id = input("Enter ID: ").strip()
                s_name = input("Enter Name: ").strip()
                s_age = input("Enter Age: ").strip()
                s_course = input("Enter Course: ").strip()

                add_student(s_id, s_name, s_age, s_course)
                print("\n>> Student registered successfully!")

            elif option == "2":
                data = get_all()
                if not data:
                    print("\n>> The database is empty.")
                else:
                    print("\n--- Students List ---")
                    for s in data:
                        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")

            elif option == "3":
                search_id = input("Enter ID to search: ").strip()
                found = find_by_id(search_id)

                if found:
                    print("\n>> Record Found:")
                    print(f"ID: {found['id']} | Name: {found['name']} | Age: {found['age']} | Course: {found['course']}")
                else:
                    print("\n>> Error: Student not found.")

            elif option == "4":
                u_id = input("Enter the ID of the student to update: ").strip()

                if find_by_id(u_id):
                    u_name = input("Enter NEW Name: ").strip()
                    u_age = input("Enter NEW Age: ").strip()
                    u_course = input("Enter NEW Course: ").strip()

                    if update_info(u_id, u_name, u_age, u_course):
                        print("\n>> Information updated successfully!")
                    else:
                        print("\n>> Error updating student.")
                else:
                    print("\n>> Error: ID not found.")

            elif option == "5":
                d_id = input("Enter ID to delete: ").strip()

                if remove_student(d_id):
                    print("\n>> Student removed from system.")
                else:
                    print("\n>> Error: Student not found.")

            elif option == "6":
                print("\nExiting program... Goodbye bro!")
                break

            else:
                print("\n>> Invalid option. Please try again.")
        
        except ValueError:
            print("\n>> Error: Invalid value entered.")


# -------- RUN -------- #

if __name__ == "__main__":
    start_app()
