# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}

if user1["valid"]:
    print("you right")


def authenticated(fn):
    # code here
    def wrapper(*args, **kwrgs):
        if args[0]["valid"]:

            return fn(*args, **kwrgs)
        else:
            print("not valid")
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
