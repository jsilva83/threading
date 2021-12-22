# Import external packages
import tkinter
import time
import random
import threading
import queue


def button1_thread():
    a_random_nr = 0
    # Check if queue is empty()
    if button1_queue.empty():
        a_random_nr = random.randint(1, 10)
        a_thread = threading.Thread(target=count_5_seconds, args=(a_random_nr,))
        # Add a new thread to the queue.
        button1_queue.put(a_thread)
        a_thread.start()
        print('Thread started ...')
    else:
        print(f'One thread still running!{a_random_nr}')
    return


def count_5_seconds(number_seconds):
    time.sleep(number_seconds)
    label1.config(text=f'5 Seconds up! ({number_seconds})')
    # Remove thread from queue.
    button1_queue.get()
    print('Thread stopped ...')
    return


def pick_random_number():
    a_random_nr = random.randint(1, 100)
    label2.config(text=f'Random number: {a_random_nr}')
    return


# Create a root window.
root = tkinter.Tk()
root.title('Threading example')
root.config(width=300, height=300)
# Create a label that presents messages for button1.
label1 = tkinter.Label(root)
label1.config(text='Hello there!')
label1.pack(pady=10)
# Create a button that executes a pause of 5 seconds.
button1 = tkinter.Button(root)
button1_queue = queue.Queue()
button1.config(text='5 seconds', command=button1_thread)
button1.pack(pady=10)
# Create a button that picks up a random number.
button2 = tkinter.Button(root)
button2.config(text='Pick random number', command=pick_random_number)
button2.pack(pady=10)
# Create a label that outputs the random number.
label2 = tkinter.Label(root)
label2.config(text=' ')
label2.pack(pady=10)
# Listen for events.
root.mainloop()