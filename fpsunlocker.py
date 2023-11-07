import time
print("Imported TIME")
time.sleep(0.2)
import json
print("Imported JSON")
time.sleep(0.2)
import os
print("Imported OS")
time.sleep(0.2)
import glob
print("Imported GLOB")
time.sleep(0.2)
import ctypes
print("Imported CTYPES")
time.sleep(0.2)
import platform
print("Imported PLATFORM")
time.sleep(0.2)


def set_console_title(title):
    if platform.system() == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif platform.system() == "Darwin":  
        print(f"\033]0;{title}\a", end='', flush=True)

new_title = "Cafes.lol FPS Unlocker"
set_console_title(new_title)

class RobloxFFlags:
    def __init__(self, version_folder):
        self.settings_file_path = os.path.join(version_folder, "ClientSettings", "ClientAppSettings.json")
        self.object = {}
        self.target_fps_mod = False
        self.alt_enter_mod = False
        self.read_disk()

    def read_disk(self):
        if os.path.isfile(self.settings_file_path):
            with open(self.settings_file_path, "r", encoding="utf-8") as file:
                self.object = json.load(file)

    def write_disk(self):
        try:
            os.makedirs(os.path.dirname(self.settings_file_path), exist_ok=True)
            with open(self.settings_file_path, "w", encoding="utf-8") as file:
                json.dump(self.object, file, indent=4)
            return True
        except:
            return False

    def read_json_opt(self, key, data_type):
        if key in self.object and isinstance(self.object[key], data_type):
            return self.object[key]
        return None

    def update_flag(self, key, new_value):
        current_value = self.read_json_opt(key, type(new_value))
        if current_value != new_value:
            if new_value is not None:
                self.object[key] = new_value
            else:
                self.object.pop(key, None)
            return True
        return False

    def target_fps(self):
        return self.read_json_opt("DFIntTaskSchedulerTargetFps", int)

    def set_target_fps(self, cap_opt):
        if cap_opt is not None:
            cap_opt = 9999999999 if cap_opt == 0 else cap_opt
        if self.update_flag("DFIntTaskSchedulerTargetFps", cap_opt):
            self.target_fps_mod = True
        return self

    def alt_enter(self):
        return self.read_json_opt("FFlagHandleAltEnterFullscreenManually", bool)

    def set_alt_enter_flag(self, alt_enter_opt):
        if self.update_flag("FFlagHandleAltEnterFullscreenManually", alt_enter_opt):
            self.alt_enter_mod = True
        return self

    def apply(self, prompt):
        if self.target_fps_mod or self.alt_enter_mod:
            if prompt:
                user_input = input("Do you want to apply the changes (Y/N)? ").strip().lower()
                if user_input != "y":
                    return False
            return self.write_disk()
        return False

def find_newest_version():
    username = os.getlogin()
    versions_dir = f"C:\\Users\\{username}\\AppData\\Local\\Roblox\\Versions\\"
    version_folders = glob.glob(os.path.join(versions_dir, "*"))
    newest_version_folder = max(version_folders, key=os.path.getctime)
    return newest_version_folder

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Select your operating system:")
    print("1. Windows")
    print("2. Mac [UNTESTED PLEASE TELL US IF IT WORKS IN OUR DISCORD]")
    choice = input("Enter your OS: ")

    if choice == "1":
        newest_version = find_newest_version()
        if newest_version:
            json_file_path = os.path.join(newest_version, "ClientSettings", "ClientAppSettings.json")

        if json_file_path is None or not os.path.exists(json_file_path):
            print("ROBLOX file not found. This code will not work.")
            time.sleep(2)
            exit(1)
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[94mCafes.lol FPS Unlocker\033[0m")
            print("1. FPS Unlocker")
            print("2. Check Current FPS Lock")
            print("3. Credits")
            print("4. Exit")
        
            choice = input("Enter your choice: ")
        
            if choice == "1":
                flags = RobloxFFlags(newest_version)
                try:
                    target_fps_value = int(input("Enter the desired FPS value (0 to remove limit): "))
                    flags.set_target_fps(target_fps_value)
                    flags.set_alt_enter_flag(True)
                    print(f"Roblox version found: {os.path.basename(newest_version)}")

        
                    if flags.apply(True):
                        print("\033[92mFPS Unlocker Successful\033[0m")
                        time.sleep(5)
                    else:
                        print("\033[91mFPS Not Changed\033[0m")
                        time.sleep(2.5)
                except ValueError:
                    print("\033[91mInvalid Input.\033[0m")
                    time.sleep(2.5)
            elif choice == "2":
                flags = RobloxFFlags(newest_version)
                target_fps = flags.target_fps()
                if target_fps is not None:
                    print(f"Current Target FPS: {target_fps}")
                    time.sleep(5)
                else:
                    print("No Target FPS value found. Redo the FPS Unlocker process if this continues. Go to our Discord on cafes.lol for help.")
                    time.sleep(2.5)
            elif choice == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Made by 4Cafes")
                print("Discord.gg/jQReR3tKBj")
                print("cafes.lol/fpsunlocker")
                input("Press Enter to return to the main menu...")
            elif choice == "4":
                print("Exiting...")
                time.sleep(2)
                break
            else:
                print("Invalid choice. Please select a valid option.")
    elif choice == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            try:
                target_fps_input = input("Enter the FPS value you want the new cap to be: ")
                targetFpsMac = int(target_fps_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer value for FPS.")

        robloxPath = "/Applications/Roblox.app"

        if not os.path.exists(robloxPath):
            robloxPath = os.path.expanduser("~") + robloxPath

        if not os.path.exists(robloxPath):
            print("Roblox installation folder couldn't be found. Are you on Windows?")
            time.sleep(5)
            exit()

        clientSettingsPath = os.path.join(robloxPath, "Contents/MacOS/ClientSettings")

        if not os.path.exists(clientSettingsPath):
            os.mkdir(clientSettingsPath)

        settings = {"DFIntTaskSchedulerTargetFps": targetFpsMac}
        settings_file = os.path.join(clientSettingsPath, "ClientAppSettings.json")

        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=2)

        print("\033[92mFPS Unlocker Successful\033[0m")
        time.sleep(5)
        os._exit(1)
    
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
