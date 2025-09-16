def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def flo(a,b):
    return a//b\
    
    operation = input("enter the operator:")
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))

    if operation == "+":
        print(add(num1,num2))

    elif operation == "-":
        print(sub(num1,num2))

    elif operation == "*":
        print(mul(num1,num2))

    elif operation == "/":
        print(div(num1,num2))

    elif operation == "//":
        print(flo(num1,num2))

    else:
        print("invalid operation") 

    

Project: Python Command-Line Employee Management System
Due Date: [Insert Due Date Here]
Project Objective:
Your task is to build a simple command-line program to manage employee records for a small company. This project will test your understanding of lists, dictionaries, loops, and conditional statements (if/elif/else).
Core Requirements:
Your program must perform the following actions based on user input.
1. Data Structure:
 * You must store all employee data in a single Python list.
 * Each employee within the list should be represented as a dictionary.
 * Each employee dictionary must contain the following keys:
   * 'id' (Integer, e.g., 101)
   * 'name' (String, e.g., "Ravi Kumar")
   * 'department' (String, e.g., "Sales")
   * 'salary' (Float or Integer, e.g., 50000)
2. Program Flow:
 * When the program starts, it should display a menu of options to the user.
 * The program must run in a continuous loop, showing the menu again after each action is completed.
 * The loop should only terminate when the user chooses the "Exit" option.
Menu and Features to Implement:
Your program must display the following menu and implement the logic for each choice:
--- Employee Management System ---
1. Add New Employee
2. View All Employees
3. Search Employee by ID
4. Update Employee Details
5. Delete Employee
6. Exit
----------------------------------
Enter your choice:

Feature Descriptions:
 * 1. Add New Employee:
   * Prompt the user to enter the ID, name, department, and salary for a new employee.
   * Create a new employee dictionary with the provided information.
   * Add this new dictionary to your main list of employees.
   * Display a confirmation message like "Employee added successfully!"
 * 2. View All Employees:
   * If no employees have been added yet, print a message like "The employee database is empty."
   * If there are employees, loop through the list and print the details of each employee in a clean, readable format.
 * 3. Search Employee by ID:
   * Ask the user to enter an Employee ID to search for.
   * Search your list for an employee dictionary with a matching ID.
   * If an employee with that ID is found, display all of their details.
   * If no employee is found with that ID, print a "Employee not found." message.
 * 4. Update Employee Details:
   * Ask the user for the ID of the employee they wish to update.
   * If the employee is found, ask the user what new information they want to provide (e.g., a new name, department, or salary) and update the corresponding value in that employee's dictionary.
   * If the employee is not found, print an appropriate message.
 * 5. Delete Employee:
   * Ask the user for the ID of the employee to delete.
   * Find and remove the correct employee dictionary from your list.
   * Print a confirmation message upon successful deletion.
   * If no employee with that ID is found, print an error message.
 * 6. Exit:
   * The program should print a goodbye message and then terminate.
 * Invalid Input:
   * If the user enters a menu choice that is not on the list (e.g., 7 or abc), the program should print an "Invalid choice" message and display the menu again.
Bonus Challenges (Optional):
For those who finish early, try implementing these additional features:
 * Prevent Duplicate IDs: When a user tries to add a new employee, check if the ID they entered already exists in your list. If it does, inform the user and ask for a different ID.
 * Input Validation: When adding an employee, ensure the ID and salary entered are valid numbers. If the user enters text instead of a number, display an error message and prompt them again without crashing the program.
Submission:
Please submit your complete Python code in a single file named employee_manager.py.
Good luck!
