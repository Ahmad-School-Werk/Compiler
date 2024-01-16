import tkinter as tk
from app import (
    VERSION_GUI,
    VERSION_CODE_GUI
)

class Compiler:
    variables = {}
    lists = {}
    
    def __init__(self) -> None:
        print(f"This app is made with Ahmad Al Dibo \n the version is '{VERSION_GUI}'")

    def print_command(self, arguments):
        if arguments:
            result = ""
            for arg in arguments[1:]:
                value = self.variables.get(arg, self.lists.get(arg, arg))
                result += str(value) + " "
            return result.strip()

    def assign_variable(self, arguments):
        if len(arguments) > 2 and arguments[1] == "=":
            variable_name, variable_value = arguments[0], " ".join(map(str, arguments[2:]))
            self.variables[variable_name] = variable_value
            return f"Variable {variable_name} assigned successfully"
        else:
            return "Error: Variables are not assigned!"

    def assign_list(self, arguments):
        if len(arguments) > 3 and arguments[0] == "List" and arguments[2] == '=':
            list_name, list_value = arguments[1], " ".join(map(str, arguments[3:]))
            self.lists[list_name] = list_value
            return f"List {list_name} assigned successfully"
        else:
            return "Error: List is not assigned correctly!"

    def run(self, line):
        arguments = line.split()

        if arguments:
            command = arguments[0].lower()

            if command == "exit":
                return False

            elif command == "print":
                return self.print_command(arguments)

            elif command.isidentifier():
                return self.assign_variable(arguments)
            elif command == "list":
                return self.assign_list(arguments)

            else:
                return "Error: Invalid command - " + " ".join(arguments)

        return True

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Interpreter GUI")

        self.input_label = tk.Label(root, text="Script:")
        self.input_label.pack()

        self.input_text = tk.Text(root, width=50, height=10)
        self.input_text.pack()

        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()

        self.output_text = tk.Text(root, width=50, height=10, state="disabled")
        self.output_text.pack()

        self.run_button = tk.Button(root, text="Run", command=self.run_script)
        self.run_button.pack()

    def run_script(self):
        script_line = self.input_text.get("1.0", tk.END).strip()
        result = interpreter.run(script_line)
        self.update_output(result)

    def update_output(self, result):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    interpreter = Compiler()

    root = tk.Tk()
    app = App(root)
    root.mainloop()


"""
This code is write it with Ahmad Al Dibo
for contact:
    -Ahmadaldibo288@gmail.com / youtuba5478@gmail.com

"""