import os

def clear_terminal():
    # 'nt' means Windows, otherwise it's Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')