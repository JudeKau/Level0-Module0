from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    points=0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    name=simpledialog.askstring(title='Greeter', prompt="What is thirteen squared?")
    #      // 3.  Use an if statement to check if their answer is correct
    if name=="169":
        messagebox.showinfo(title='Greeter', message="You are correct")
    else:
        messagebox.showinfo(title='Greeter', message="You are wrong")
    #      // 4.  if the user's answer was correct, add one to their score 
    if name=="169":
        messagebox.showinfo(title='Greeter', message="Points: 1")
    else:
        messagebox.showinfo(title='Greeter', message="Points: 0")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    name=simpledialog.askstring(title='Greeter', prompt="Is 50,050,053 divisible by nine?")
    if name=="yes":
        messagebox.showinfo(title='Greeter', message="You are correct")
    else:
        messagebox.showinfo(title='Greeter', message="You are wrong")
    if name=="yes":
        messagebox.showinfo(title='Greeter', message="Points: 2")
    else:
        messagebox.showinfo(title='Greeter', message="Points: 0")
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
