# First version
# print('Enter ToDo: ')
# todo = input()
# print(todo)

# Improved version
# todo = input("Enter ToDo: ")
# print(todo)

# Create a viriable
# prompt = "Enter ToDo: "
# todo = input(prompt)
# print(todo)

# Create a list
# all_todo = []

# Diferença entre capitalize e title é que capitalize deixa apenas a primeira letra em maiusculo
# Já title deixa todas as primeira letras em maiusculo
"""
while True:
    todo = input("Enter ToDo: ")
    print(todo.capitalize())
    all_todo.append(todo)

    continuar = input("Continuar? [y/n]: ")
    if continuar == "n":
        break

print("\nSua lista:")
for task in all_todo:
    print("- ", task)
"""
#------------------------------
todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a to do: ")
            todos.append(todo)
        case "show":
            #improving the program output
            #print(todos)
            for item in todos:
                print(item.capitalize())
        case "exit":
            break

print("\nBye!")



