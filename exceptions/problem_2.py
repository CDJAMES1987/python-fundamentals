'''
Problem 2

def process_age(age):
    pass

def read_config(config: dict, key: str):
    pass
process_age — raise a ValueError if age is negative or over 150, otherwise return "valid"
read_config — try to get a key from the dict, raise a KeyError 
with a helpful message if missing, use finally to print "config lookup complete" regardless
'''


def process_age(age):
    if age > 150 or age < 0:
        raise ValueError("Age must be between 0 and 150")
    return 'valid'


def read_config(config: dict, key: str):
    try:
        return config[key]
    except KeyError:
        raise KeyError(f"Key '{key}' not found in config")
    finally:
        print('config lookup complete')


if __name__ == '__main__':
    process_age(age=49)
    read_config(config={'A': 1}, key='C')
