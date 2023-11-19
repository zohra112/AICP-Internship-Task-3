# AICP Internship Task 3, An Electricity bill Calculator according to units

# Function to get the student ID
def getStudentID():
    """Gets the student ID from the user.

    Returns:
        str: The entered student ID.
    """
    student_id = input("Enter your Student ID: ")
    return student_id

def costSlab1(student_id, source_data):
    """Calculates and displays the cost for slab 1.

    Args:
        student_id (str): The student ID.
        source_data: A two-dimensional list containing the electricity consumption data.

    Returns:
        None.
    """

    # Displaying the cost for slab 1 along with student ID
    print(f"Bill for {student_id} - Slab 1 (Unit range: 0-100) is:", end=" ")
    print(*source_data[0])

def costSlab2(source_data):
    """Calculates and displays the cost for slab 2.

    Args:
        source_data: A two-dimensional list containing the electricity consumption data.

    Returns:
        None.
    """

    # This chunk is displaying the cost for slab2
    print("Bill for Slab 2 (Unit range: 101-200) is:", end=" ")
    print(*source_data[1])

def costSlab3(source_data):
    """Calculates and displays cost for slab 3.

    Args:
        source_data: A two-dimensional list containing the electricity consumption data.

    Returns:
        None.
    """

    # This chunk is displaying the cost for slab 3
    print("Bill for Slab 3 (Unit range is 201-300) is:", end=" ")
    print(*source_data[2])

# Function to display the main menu
def displayMainMenu(student_id, source_data):
    """Displays the main menu.

    Args:
        student_id (str): The student ID.
        source_data: A two-dimensional list containing the electricity consumption data.

    Returns:
        None.
    """
    print()
    print("**Main Menu**")
    print(f"Student ID: {student_id}")
    print("1. Display the bill for slab 1 and slab 2.")
    print("2. Display the bill for slab 3.")
    print("Any other key to exit.")

    # Get the user's choice
    choice = input("Enter your choice: ")

    # Perform the selected operation
    if choice == "1":
        costSlab1(student_id, source_data)
        costSlab2(source_data)
    elif choice == "2":
        costSlab3(source_data)
    else:
        print("Invalid Choice")
        exit()

# Main function
def main():
    # Source  2d data matrix
    source_data = [
        [550, 650, 750],
        [1800, 2250, 2550],
        [4200, 4600, 4800]
    ]

    # To Print the electricity bill heading
    print("*********** Electricity Bill ***********\n")

    # Get the student ID
    student_id = getStudentID()

    # To keep on repeating the menu
    while True:
        displayMainMenu(student_id, source_data)

if __name__ == "__main__":
    main()
