
# Keylogger with Data Exfiltration

This Python script is a basic keylogger that captures keyboard input, stores it with timestamps, writes the captured data to a text file, and can send the data to a remote server.

⚠️ **This code is for educational purposes only. Do not use it on systems or networks you do not own or do not have explicit permission to test. Unauthorized use is illegal.**

---

## Features

- Records all keypresses along with the time.
- Groups keypresses by minute.
- Prints the captured data when the user types `show`.
- Saves the data to `keystrokes.txt`.
- Sends `keystrokes.txt` to a remote server.
- Stops the program gracefully when pressing `Ctrl + Shift + F`.

---

## How It Works

1. **Keyboard Hook**  
   The script uses the `keyboard` module to capture keypress events.
   
2. **Data Storage**  
   Keypresses are stored in a dictionary with timestamps (minute level).  
   The data structure looks like:
   ```python
   { timestamp : [list_of_keys_pressed] }
   ```

3. **Display Trigger**  
   If the user types the word `show`, all the captured data will be printed.

4. **Graceful Exit**  
   When the user presses `Ctrl + Shift + F`:
   - The captured data is written to `keystrokes.txt`.
   - The file is sent to a remote server via an HTTP POST request.
   - The program exits cleanly.

---

## Requirements

- Python 3.x
- Modules:
  - `keyboard`
  - `requests`

To install the required modules:
```bash
pip install keyboard requests
```

---

## Usage

1. **Run the script**  
   ```bash
   python keylogger.py
   ```

2. **To display captured data**  
   Type: `show`

3. **To stop the program and send data**  
   Press: `Ctrl + Shift + F`

---

## Files

- `keylogger.py` — Main script
- `keystrokes.txt` — Output file containing captured data (created automatically)

---

## Legal Disclaimer

This project is intended for educational use only. It is the responsibility of the user to comply with all applicable laws and regulations. The author assumes no liability for any misuse or damage caused by this script.

---
