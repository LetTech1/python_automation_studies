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
all_todo = []

while True:
    todo = input("Enter ToDo: ")
    all_todo.append(todo)

    continuar = input("Continuar? [y/n]: ")
    if continuar == "n":
        break

print("\nSua lista:")
for task in all_todo:
    print("- ", task)




