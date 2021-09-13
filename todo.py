import textwrap

def create_todo(todos, title, description, level):
    todo = {
        'title' : title,
        'description' : description,
        'level' : level,
    }
    todos.append(todo)

def main_loop():
    user_input = ""
    while 1:
        print(run_command(user_input))
        user_input = input("> ")
        if user_input.lower().startswith("quit"):
            print("Exiting")
            break

def get_input(fields):
    user_input = {}
    for field in fields:
        user_input[field] = input(field + ">")
    return user_input

def get_function(command_name):
    return commands[command_name][0]

def get_fields(command_name):
    return commands[command_name][1]

def test(todos, abcd, ijkl):
    return "Command 'test' returned:\n" + \
        "abcd: " + abcd + "\nijkl: " + ijkl

todos = []

def capitalize(todo):
    todo['level'] = todo['level'].upper()
    return todo

def show_todos(todos):
        output = ("Item     Title       "
                  "Description          Level\n")
        important = [capitalize(todo) for todo in todos
                    if todo['level'].lower() == 'important']
        unimportant = [capitalize(todo) for todo in todos
                    if todo['level'].lower() == 'unimportant']
        medium = [capitalize(todo) for todo in todos
                    if todo['level'].lower() == 'medium']
        sorted_todos = (important +
                        medium +
                        unimportant)

        for index, todo in enumerate(sorted_todos):
            line = str(index+1).ljust(8)
            for key, length in [('title', 16),
                                ('description', 24),
                                ('level', 16)]:
                line += str(todo[key]).ljust(length)
            output += line + "\n"
        return output

commands = {
    'new': [create_todo, ['title', 'description', 'level']],
    'show' : [show_todos, []],
    'test' : [test, ['abcd', 'ijkl']],
}

def run_command(user_input, data = None):
    user_input = user_input.lower()
    if user_input not in commands:
        return user_input + "?" \
            " I Don't know what that command is."
    else:
        the_func = get_function(user_input)

    if data is None:
        the_fields = get_fields(user_input)
        data = get_input(the_fields)
    return the_func(todos, **data)



if __name__ == '__main__':
    main_loop()
