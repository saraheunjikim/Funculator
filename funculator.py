from tkinter import *

phrase = []
phrase_string = ''


# To press any button
def press(item):
    global phrase, phrase_string
    plus.config(state='normal')
    multiply.config(state='normal')
    if item == 'Corn Muffin':
        disableButtons()
        if phrase == ['Welcome to Funculator!']:
            phrase = ['Does grandma muffin taste good?']
        else:
            phrase.append('Does grandma muffin taste good?')
    elif item == 'Choc Muffin':
        disableButtons()
        if phrase == ['Welcome to Funculator!']:
            phrase = ['This is my favorite muffin!']
        else:
            phrase.append('This is my favorite muffin!')
    elif item == 'Cupcake':
        disableButtons()
        if phrase == ['Welcome to Funculator!']:
            phrase = ['The icing is so good, but so fat!']
        else:
            phrase.append('The icing is so good, but so fat!')
    elif item == 'Milk':
        disableButtons()
        if phrase == ['Welcome to Funculator!']:
            phrase = ['Good for your bones. Hot and cold!']
        else:
            phrase.append('Good for your bones. Hot and cold!')
    elif item == 'Orange Juice':
        disableButtons()
        if phrase == ['Welcome to Funculator!']:
            phrase = ['OJ? Need vitamin C?? >_<']
        else:
            phrase.append('OJ? Need vitamin C?? >_<')
    elif item == 'Tea':
        disableButtons()
        if phrase == ['Welcome to Funculator!']:
            phrase = ['I love a cuppa! <3']
        else:
            phrase.append('I love a cuppa! <3')
    elif item == 'AND':
        phrase.append(' and ')
        plus.config(state='disabled')
        multiply.config(state='disabled')
        normalButtons()
    elif item == 'DOUBLE':
        phrase.append(' x2 ')
        plus.config(state='disabled')
        multiply.config(state='disabled')
        disableButtons()

    phrase_string = ''
    for ele in phrase:
        phrase_string += ele
    return equation.set(phrase_string)


# This is enter
def finalPress():
    global phrase, phrase_string
    if phrase[0] in ['Does grandma muffin taste good?', 'This is my favorite muffin!',
                     'The icing is so good, but so fat!', 'Good for your bones. Hot and cold!',
                     'OJ? Need vitamin C?? >_<', 'I love a cuppa! <3', 'Tea is the best!'] \
            and len(phrase) is 1:
        phrase = phrase[0] + ', it is!'
    elif phrase[0] == 'Does grandma muffin taste good?':
        if phrase[1] == ' and ':
            phrase.clear()
            phrase = 'Yes, one grandma muffin is NOT enough!'
        if phrase[1] == ' x2 ':
            phrase.clear()
            phrase = 'Eww, two granny muffins.....'
    elif phrase[0] == 'This is my favorite muffin!':
        if phrase[1] == ' and ':
            phrase.clear()
            phrase = 'Yummmm, enjoy!'
        if phrase[1] == ' x2 ':
            phrase.clear()
            phrase = 'Ok, please share with your friend'
    elif phrase[0] == 'The icing is so good, but so fat!':
        if phrase[1] == ' and ':
            phrase.clear()
            phrase = 'Good choice!'
        if phrase[1] == ' x2 ':
            phrase.clear()
            phrase = 'Ok, TOO MUCH SUGAR!'
    elif phrase[0] == 'Good for your bones. Hot and cold!':
        if phrase[1] == ' and ':
            phrase.clear()
            phrase = 'Milk goes well with anything!'
        if phrase[1] == ' x2 ':
            phrase.clear()
            phrase = 'You MUST want to be taller!'
    elif phrase[0] == 'OJ? Need vitamin C?? >_<':
        if phrase[1] == ' and ':
            phrase.clear()
            phrase = 'Orange Juices is great with anything!'
        if phrase[1] == ' x2 ':
            phrase.clear()
            phrase = 'VITAMIN C OVERDOSE!'
    elif phrase[0] == 'I love a cuppa! <3':
        if phrase[1] == ' and ':
            phrase.clear()
            phrase = 'Tea is the best!'
        if phrase[1] == ' x2 ':
            phrase.clear()
            phrase = 'Good for you!'

    return equation.set(phrase)


# Clear the content
def clearContent():
    normalButtons()
    global phrase, phrase_string
    phrase = ["Welcome to Funculator!"]
    phrase_string = ''
    for ele in phrase:
        phrase_string += ele
    return equation.set(phrase_string)


# Disable all food buttons
def disableButtons():
    button1.config(state='disabled')
    button2.config(state='disabled')
    button3.config(state='disabled')
    button4.config(state='disabled')
    button5.config(state='disabled')
    button6.config(state='disabled')


def normalButtons():
    button1.config(state='normal')
    button2.config(state='normal')
    button3.config(state='normal')
    button4.config(state='normal')
    button5.config(state='normal')
    button6.config(state='normal')


# Driver code
if __name__ == '__main__':
    # create application window
    app = Tk()

    # title
    app.title("Muffin's Funculator")

    # geometry
    app.geometry('323x161')

    # background color
    app.configure(bg='pink')

    equation = StringVar()
    windows = Entry(app, textvariable=equation)
    windows.grid(columnspan=5, ipadx=100, ipady=10)
    equation.set('Welcome to Funculator!')

    # Create buttons and other accessories
    button1 = Button(app, text=' Corn Muffin ', fg='yellow', bg='purple',
                     command=lambda: press('Corn Muffin'), height=2, width=10)
    button1.grid(row=2, column=0, sticky="NSEW")

    button2 = Button(app, text=' Choc Muffin ', fg='brown', bg='pink',
                     command=lambda: press('Choc Muffin'), height=2, width=10)
    button2.grid(row=2, column=1, sticky="NSEW")

    button3 = Button(app, text=' Cupcake ', fg='pink', bg='navy',
                     command=lambda: press('Cupcake'), height=2, width=10)
    button3.grid(row=2, column=2, sticky="NSEW")

    button4 = Button(app, text=' Milk ', fg='white', bg='violet',
                     command=lambda: press('Milk'), height=2, width=10)
    button4.grid(row=3, column=0, sticky="NSEW")

    button5 = Button(app, text=' Orange Juice ', fg='orange', bg='blue',
                     command=lambda: press('Orange Juice'), height=2, width=10)
    button5.grid(row=3, column=1, sticky="NSEW")

    button6 = Button(app, text='Tea', fg='red', bg='black',
                     command=lambda: press('Tea'), height=2, width=10)
    button6.grid(row=3, column=2, sticky="NSEW")

    plus = Button(app, text='AND', fg='black', bg='white',
                  command=lambda: press('AND'), height=2, width=10)
    plus.config(state='disabled')
    plus.grid(row=4, column=0, sticky="NSEW")

    multiply = Button(app, text='DOUBLE', fg='black', bg='white',
                      command=lambda: press('DOUBLE'), height=2, width=10)
    multiply.config(state='disabled')
    multiply.grid(row=4, column=1, sticky="NSEW")

    equal = Button(app, text='ENTER', fg='black', bg='white',
                   command=finalPress, height=2, width=10)
    equal.grid(row=2, column=4, sticky="NSEW")

    clear = Button(app, text='CLEAR', fg='black', bg='white',
                   command=clearContent, height=2, width=10)
    clear.grid(row=4, column=2, sticky="NSEW")

# start the GUI
app.mainloop()
