import random
import threading
import time

def generate_random_number():
    return random.randint(1, 10)

def generate_numbers_thread(numbers, lock):
    while True:
        with lock:
            numbers.append(generate_random_number())
        time.sleep(2)

def format_message(message):
    return message.encode('utf-8')

def decode_message(message):
    return message.decode('utf-8')
