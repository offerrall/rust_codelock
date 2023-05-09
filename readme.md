# Rust Code Lock Utility

## Introduction

Rust Code Lock Utility is a simple Python script that automates the process of unlocking code locks in the game Rust. It binds a key combination to quickly input a 4-digit code, allowing players to unlock code locks more efficiently. The utility also offers a streamer mode, which hides the code when enabled.

## Prerequisites

Before using the Rust Code Lock Utility, make sure you have Python installed on your system. This utility requires the following Python packages:

- pydirectinput
- keyboard

You can install these packages using pip:

```bash
pip install pydirectinput keyboard
```

## How to Use

1. Save the provided code in a Python file, such as `rust_codelock.py`.
2. Run the Python script:

```bash
python rust_codelock.py
```

3. The utility will prompt you to configure the settings:

    - **Key**: Enter the key combination you want to use for unlocking the code lock (e.g., 'F' or 'ctrl+shift+u').
    - **Code**: Enter the 4-digit code you want to use for unlocking (e.g., '1234').
    - **Initial Delay**: Enter the delay (in seconds) before the code starts being entered (e.g., 0.2).
    - **Delay between key presses**: Enter the delay (in seconds) between each key press (e.g., 0.05).
    - **Streamer Mode**: Enter 'Y' for enabling the streamer mode, which hides the code, or 'N' for disabling it.

4. After configuring the settings, the utility will display the current configuration and start running. Press the configured key combination in-game to quickly input the code and unlock the code lock.

5. To stop the utility or change the configuration, press Ctrl+C in the terminal. You will be prompted to change the configuration or exit the program.

**Note:** When the streamer mode is enabled, the code input will be hidden, and the new code will be masked.

## Delay Configuration

The delay between key presses and the initial delay are essential settings that must be configured correctly for the utility to work correctly. 

- `Initial Delay`: This setting defines the amount of time (in seconds) that the utility waits before entering the code. It allows you to have enough time to position your character in front of the code lock before entering the code.

- `Delay between key presses`: This setting defines the amount of time (in seconds) that the utility waits between each key press when entering the code. This delay is necessary to ensure that the game registers each key press and doesn't ignore any.

To determine the best delay settings for your system and in-game environment, you may need to experiment with different values until you find the optimal settings that work best for you. We recommend starting with the default values and adjusting them as needed based on your experience.

