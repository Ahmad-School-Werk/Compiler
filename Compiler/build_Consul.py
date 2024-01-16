from app import (
    VERSION_CONSUL,
    VERSION_CODE_CONSUL
)


class Compiler:
    variables = {}
    lists = {}
    
      

    @staticmethod
    def print_command(arguments):
        if arguments:
            for arg in arguments[1:]:
                value = Compiler.variables.get(arg, Compiler.lists.get(arg, arg))
                print(value, end=" ")
            print()

    @staticmethod
    def assign_variable(arguments):
        if len(arguments) > 2 and arguments[1] == "=":
            variable_name, variable_value = arguments[0], " ".join(map(str, arguments[2:]))
            Compiler.variables[variable_name] = variable_value
        else:
            print("Error: Variables are not assigned!")

    @staticmethod
    def assign_list(arguments):
        if len(arguments) > 3 and arguments[0] == "List" and arguments[2] == '=':
            list_name, list_value = arguments[1], " ".join(map(str, arguments[3:]))
            Compiler.lists[list_name] = list_value
            print("List assigned successfully")
        else:
            print("Error: List is not assigned correctly!")

    def run(self, line):
        arguments = line.split()

        if arguments:
            command = arguments[0].lower()

            if command == "exit":
                return False

            elif command == "print":
                self.print_command(arguments)

            elif command.isidentifier():
                self.assign_variable(arguments)
            elif command == "list":
                self.assign_list(arguments)

            else:
                print("Error: Invalid command -", arguments)

        return True
    

if __name__ == "__main__":
    code = input(">>>")
    compiler = Compiler()
    compiler.run(code)