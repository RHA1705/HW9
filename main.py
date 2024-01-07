'''Data storage'''
user_data_dict = {}


def input_error(func):
    '''Decorator for working with exeptions'''
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except KeyError:
            result = f'User not found'
        except ValueError:
            result = f'Phone number incorrect'
        except IndexError:
            result = f'One of parameters missed'
        return result
    return inner


def main():
    '''Main function to work with user input'''
    while True:
        command = input()
        exit_list = ['exit', 'close', 'good bye']
        if command in exit_list:
            print('Good bye!')
            break
        else:
            print(parser(command))

def parser(user_input):
    '''Function define key words (user commands)'''
    if user_input.lower().startswith('hello'):
        return 'How can I help you?'
    elif user_input.lower().startswith('add'):
        return handler_add(user_input)
    elif user_input.lower().startswith('change'):
        return handler_change(user_input)   
    elif user_input.lower().startswith('phone'):
        return handler_phone(user_input)
    elif user_input.lower().startswith('show all'):
        return handler_show_all(user_input)

@input_error
def handler_add(user_input):
    '''Function define actions if user command is "add"'''
    user_data = user_input.split(' ')
    check_phone_number(user_input)
    user_data_dict.update({user_data[1] : user_data[2]})
    return 'User added succesfully!'

@input_error
def handler_change(user_input):
    '''Function define actions if user command is "change"'''
    user_data = user_input.split(' ')
    check_phone_number(user_input)
    if user_data[1] in user_data_dict:
        user_data_dict.update({user_data[1] : user_data[2]})
        return 'User updated succesfully!'
    else:
        raise KeyError

@input_error    
def handler_phone(user_input):
    '''Function define actions if user command is "phone"'''
    user_data = user_input.split(' ')
    user_phone = user_data_dict.get(user_data[1])
    return f'User phone number is: {user_phone}'

@input_error
def handler_show_all(user_input):
    '''Function define actions if user command is "show all"'''
    users_data = []
    for key, value in user_data_dict.items():
        row = f'For name {key} phone is {value}'
        users_data.append(row)

    return ', '.join(users_data)
    
def check_phone_number(user_input):
    '''Function checks whether all characters are numbers'''
    user_data = user_input.split(' ')
    if not user_data[2].isalnum():
        raise ValueError

if __name__ == '__main__':
    main()