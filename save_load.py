import pickle
import os

SAVE_FILE = "save_game.pkl"

def save_game(data):
    with open(SAVE_FILE, 'wb') as file:
        print("save completed")
        pickle.dump(data, file)

def load_game():
    if os.path.exists(SAVE_FILE) and os.path.getsize(SAVE_FILE) > 0:
        with open(SAVE_FILE, 'rb') as file:
            return pickle.load(file)
    return None
