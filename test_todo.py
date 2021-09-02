import todo

def test_create_todo():
    todo.todos = []
    todo.create_todo(todo.todos,
        title = "Make som stuff",
        description = "Stuff needs to be programmed",
        level = "Important")

    assert len(todo.todos) == 1, "Todo was not created!"
    assert todo.todos[0]['title'] == "Make som stuff"
    assert (todo.todos[0]['description'] ==
        "Stuff needs to be programmed")
    assert todo.todos[0]['level'] == "Important"

    print("ok - create_todo")

test_create_todo()

def test_get_function():
    assert todo.get_function('new') == todo.create_todo
    print("ok - get_function")

test_get_function() 
