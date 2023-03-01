import argparse # native with python


def input_parser():
    # initialize an empty parser
    parser = argparse.ArgumentParser() 
    # add an argument to the parser
    parser.add_argument("--name", type=str) 
    # parse the arguments from the command line
    args = parser.parse_args() 
    # get name
    name = args.name
    # return the name
    return name
    
#print(args.name) # now, it'll print just the name

def hello(name):
    print("Hello, my name is " + name + "!")

def main():
    # run input parse to get name
    name = input_parser()
    # pass name to hello function
    hello(name)

main()

# Once I run python3 src/scripting.py  in the terminal, it will run this file and print out "Hello, my name is Rocky!" in the terminal.