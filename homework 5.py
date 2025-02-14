import inspect
import tkinter

print(inspect.ismodule(tkinter))
print(inspect.isclass(tkinter))
print(inspect.isfunction(tkinter))
print(inspect.getmodule(tkinter.Tk))
print(inspect.getmodule(list)) 

