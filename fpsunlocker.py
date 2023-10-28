import os
import json
import time

user_home = os.path.expanduser("~")

roblox_directory = "AppData\\Local\\Roblox\\Versions"

target_key = "DFIntTaskSchedulerTargetFps"

new_value = None

def loading_screen():
    os.system("cls")  
    print("Loading", end="", flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print()
    os.system("cls")  

def loading_screen2():
    os.system("cls")  
    print("Finding File", end="", flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print()
    os.system("cls")  

def selection_menu():
    print("\033[94mCafes.lol FPS Unlocker\033[0m")
    print("Select an option:")
    print("1. Run the FPS Unlocker")
    print("2. Check Current FPS Value")
    print("3. Credits")
    print("4. Exit Program")

def get_user_fps_input():
    try:
        fps_value = int(input("Enter the desired FPS value: "))
        return fps_value
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_user_fps_input()

def run_fps_unlocker(user_home, roblox_directory, target_key, new_value):
    loading_screen2()

    new_value = get_user_fps_input()

    file_directory = os.path.join(user_home, roblox_directory)

    found_json_files = False  

    for root, dirs, files in os.walk(file_directory):
        for filename in files:
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        data = json.load(file)
                        if target_key in data:
                            data[target_key] = new_value
                            with open(file_path, "w", encoding="utf-8") as modified_file:
                                json.dump(data, modified_file, indent=4)
                            print("\033[92mCafes.lol FPS Unlocker was successful\033[0m")
                            time.sleep(5)  
                            os.system("cls")  
                            return
                except (json.JSONDecodeError, FileNotFoundError) as e:
                    print(f"Error processing {file_path}: {str(e)}")
                found_json_files = True

    if not found_json_files:
        print("No JSON files were found for modification.")
        time.sleep(2) 

def check_current_fps_value(user_home, roblox_directory, target_key):
    loading_screen2()

    # Construct the full directory path
    file_directory = os.path.join(user_home, roblox_directory)

    current_values = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(file_directory):
        for filename in files:
            # Check if the file is a JSON file
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        data = json.load(file)
                        if target_key in data:
                            current_values.append(data[target_key])
                except (json.JSONDecodeError, FileNotFoundError) as e:
                    print(f"Error processing {file_path}: {str(e)}")

    if not current_values:
        print("No JSON files were found with the FPS value.")
    else:
        print("Current FPS Values:")
        for value in current_values:
            print(value)

    time.sleep(5)  
    os.system("cls")  
    return

def credits():
    os.system("cls")  
    print("Credits:")
    print("This script was created by cafes.lol or 4cafes on discord.")
    input("Press Enter to return to the main menu...")

def main():
    while True:
        loading_screen()
        selection_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            run_fps_unlocker(user_home, roblox_directory, target_key, new_value)
        elif choice == "2":
            check_current_fps_value(user_home, roblox_directory, target_key)
        elif choice == "3":
            credits()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()