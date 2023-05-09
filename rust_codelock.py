from rust_codelock_utils import (
    run,
    keyboard_unbind_all,
    ConfigFile,
)

def main():
    config = ConfigFile()
    settings = config.read_config()

    key = settings["key"]
    code = settings["code"]
    initial_delay = settings["initial_delay"]
    delay = settings["delay"]
    streamer_mode = settings["streamer_mode"]

    try:
        code_str = code if not streamer_mode else "****"
        print(f"Key: {key}, Code: {code_str}, Initial Delay: {initial_delay}, Delay: {delay}, Streamer Mode: {streamer_mode}")
        print("Press Ctrl+C to stop or change the configuration")
        print("-" * 50)
        run(key, code, initial_delay, delay)
    except KeyboardInterrupt:
        print("Stopping...")
        keyboard_unbind_all()

if __name__ == "__main__":
    while True:
        main()
        response = input("Do you want to change the configuration? (Y/N): ")
        if response.lower() == 'y':
            config = ConfigFile()
            config.configure_settings()
        else:
            break

        
