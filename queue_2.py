import tkinter as tk
import heapq

# Create the main window.
window = tk.Tk()
window.geometry("400x300")
window.title("Hospital Priority Queue")

# Create a priority queue to store the items.
queue = []

# Function to insert an item into the queue.
def insert():
  # Get the item and its priority from the user.
  item = entry1.get()
  priority = int(entry2.get())

  # Insert the item into the queue with its priority.
  heapq.heappush(queue, (priority, item))

  # Clear the entries and update the list box.
  entry1.delete(0, tk.END)
  entry2.delete(0, tk.END)
  update_list_box()

# Function to remove the highest priority item from the queue.
def remove():
  # Remove the highest priority item from the queue.
  item = heapq.heappop(queue)

  # Update the list box.
  update_list_box()

# Function to update the items in the list box.
def update_list_box():
  # Clear the list box.
  list_box.delete(0, tk.END)

  # Insert the items from the queue into the list box.
  for item in queue:
    list_box.insert(tk.END, item[1] + " (priority: " + str(item[0]) + ")")

# Create the label, entry, and button for inserting items.
label1 = tk.Label(window, text="Patient:")
entry1 = tk.Entry(window)
button1 = tk.Button(window, text="Insert", command=insert)

# Create the label, entry, and button for removing items.
label2 = tk.Label(window, text="Priority:")
entry2 = tk.Entry(window)
button2 = tk.Button(window, text="Remove", command=remove)

# Create the list box for displaying the items in the queue.
list_box = tk.Listbox(window)

# Position the widgets using the grid layout manager.
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
button1.grid(row=0, column=2)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
button2.grid(row=1, column=2)
list_box.grid(row=2, column=0, columnspan=3)

# Start the event loop.
window.mainloop()