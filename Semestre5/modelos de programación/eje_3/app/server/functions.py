import random
import threading
import time

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def generate_random_number():
    return random.randint(1, 10)

def generate_numbers_thread(numbers, lock):
    while True:
        with lock:
            if len(numbers) < 5:
                numbers.append(generate_random_number())
        time.sleep(1)

def format_message(message):
    return message.encode('utf-8')

def decode_message(message):
    return message.decode('utf-8')
