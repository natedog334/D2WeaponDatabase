class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options
        self.options.append(Option("Exit", lambda: exit()))

    def show(self):
        print(self.title)
        for index, option in enumerate(self.options, start=1):
            print('\t' + str(index) + " " + option.text)

        action = input("> ")
        while not validate_action(action, len(self.options)):
            print(f"Invalid option '{action}'. Please try again.")
            action = input("> ")
        self.options[int(action) - 1].on_select()


class Option:
    def __init__(self, text, on_select):
        self.text = text
        self.on_select = on_select

def validate_action(action, num_options):
    try:
        action = int(action)
    except ValueError:
        return False

    if action > num_options or action <= 0:
        return False

    return True

