from typing import Callable
from functools import wraps

def input_error(func: Callable)-> Callable:

    @wraps(func)
    def inner(*args, **kwargs):
        error_messages={
            'value':{'add_contact':'Give me name and phone please.','change_contact':'There is no such contact','show_phone':'Please enter name.'},
            'index':{},
            'key':{'show_phone':'Contact not found.'}
        }
        

        try:
            return func(*args, **kwargs)
        except ValueError:
            return error_messages['value'].get(func.__name__) or "Invalid value."
        except IndexError:
            return error_messages['index'].get(func.__name__) or "Invalid number of arguments."
        except KeyError:
            return error_messages['key'].get(func.__name__) or "Invalid key."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."



def show_contacts(contacts):
    print(contacts)


@input_error
def show_phone(args, contacts):
    name = args[0]
    print(contacts.get(name, "Contact not found."))


      

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        command = command.strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            show_phone(args, contacts)
        elif command == "all":
            show_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()