import pydirectinput
import keyboard
import time
from configparser import ConfigParser
from os.path import exists
from getpass import getpass

def code_lock_unlock(code: str, initial_delay: float, delay: float) -> None:
    time.sleep(initial_delay)
    for number in code:
        pydirectinput.press(number)
        time.sleep(delay)

def keyboard_bind(key: str, callback) -> None:
    keyboard.add_hotkey(key, callback)

def keyboard_unbind(key: str) -> None:
    keyboard.remove_hotkey(key)
    
def keyboard_unbind_all() -> None:
    keyboard.unhook_all_hotkeys()

def run(key: str, code: str, initial_delay: float = 0.5, delay: float = 0.05) -> None:
    keyboard_bind(key, lambda: code_lock_unlock(code, initial_delay, delay))
    while True:
        time.sleep(1)

def is_valid_key_combination(key: str) -> bool:
    try:
        keyboard.parse_hotkey(key)
        return True
    except ValueError:
        return False

class ConfigFile:
    
    dir_config = "config.txt"

    def write_config(self, config_dict) -> None:
        config = ConfigParser()
        default = config["DEFAULT"]
        default["key"] = config_dict["key"]
        default["code"] = config_dict["code"]
        default["initial_delay"] = str(config_dict["initial_delay"])
        default["delay"] = str(config_dict["delay"])
        default["streamer_mode"] = str(config_dict["streamer_mode"])
        
        with open(self.dir_config, "w") as config_file:
            config.write(config_file)
        
    def read_config(self) -> dict:
        try:
            config = ConfigParser()
            config.read(self.dir_config)
            
            key = config["DEFAULT"]["key"]
            code = str(int(config["DEFAULT"]["code"]))
            initial_delay = float(config["DEFAULT"]["initial_delay"])
            delay = float(config["DEFAULT"]["delay"])
            streamer_mode = config["DEFAULT"]["streamer_mode"]
            streamer_mode = True if streamer_mode == "True" else False
            
            dict_config = {"key": key, "code": code, "initial_delay": initial_delay, "delay": delay, "streamer_mode": streamer_mode}  
            return dict_config
        
        except Exception as e:
            print("No config found. Using default config.")
            self.write_config({"key": "ctrl+shift+u", "code": "1234", "initial_delay": 0.5, "delay": 0.1, "streamer_mode": False})
            return self.read_config()
        
    def configure_settings(self) -> None:
        current_config = self.read_config()
        print("Enter the settings for the Rust Code Lock utility:")

        while True:
            try:
                key = input(f"Key (e.g. 'F' or 'ctrl+shift+u') [current: {current_config['key']}, keep: k]: ")
                if key.lower() == 'k':
                    key = current_config['key']
                elif not key or not is_valid_key_combination(key):
                    raise ValueError("Invalid or empty key combination")

                if current_config["streamer_mode"]:
                    print("Code input will be hidden due to streamer mode.")
                    code = getpass("Code (e.g. '1234') [keep: k]: ")
                else:
                    code = input(f"Code (e.g. '1234') [current: {current_config['code']}, keep: k]: ")

                if code.lower() == 'k':
                    code = current_config['code']
                else:
                    if not code:
                        raise ValueError("Code cannot be empty")

                    code = str(int(code))
                    if len(code) != 4:
                        raise ValueError("Code must be 4 digits")

                initial_delay_input = input(f"Initial Delay (e.g. 0.2) [current: {current_config['initial_delay']}, keep: k]: ")
                if initial_delay_input.lower() == 'k':
                    initial_delay = current_config['initial_delay']
                else:
                    initial_delay = float(initial_delay_input)
                    if initial_delay < 0:
                        raise ValueError("Initial Delay must be greater than or equal to 0")

                delay_input = input(f"Delay between key presses (e.g. 0.05) [current: {current_config['delay']}, keep: k]: ")
                if delay_input.lower() == 'k':
                    delay = current_config['delay']
                else:
                    delay = float(delay_input)
                    if delay < 0:
                        raise ValueError("Delay must be greater than or equal to 0")

                streamer_mode_input = input(f"Streamer Mode (Y/N) [current: {'Y' if current_config['streamer_mode'] else 'N'}, keep: k]: ")
                if streamer_mode_input.lower() == 'k':
                    streamer_mode = current_config['streamer_mode']
                else:
                    streamer_mode = True if streamer_mode_input.lower() == 'y' else False

                break
            except ValueError as e:
                print(f"Error: {e}. Please enter valid input.")
        
        input_data = {
            "key": key,
            "code": code,
            "initial_delay": initial_delay,
            "delay": delay,
            "streamer_mode": streamer_mode
        }
        
        self.write_config(input_data)

 