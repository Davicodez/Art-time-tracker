import functions

def main():
    print("Welcome to the Art Time Log!")
    while True:
        print("Please select an option:")
        print("1. Log time spent on art")
        print("2. Show total time spent on art")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            time = input("Enter the time spent on art in hours (e.g 1.5): ")
            try:
                time_float = float(time)
                functions.logTime(time_float)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            functions.showProgress()
        elif choice == '3':
            print("Exiting the Art Time Log. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.") 

if __name__ == "__main__":
    main()