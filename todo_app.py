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
todo = input("Enter ToDo: ")
continuar = input("Continuar? [y/n]")
all_todo = []
i = 0

print(todo)
all_todo.append(todo)
print(continuar)

if continuar == "y":
    print(todo)
    all_todo.append(todo)
    print(continuar)
else:
    for i in all_todo:
        print(i)
