# This file contains functions used by other scripts
import time
import os
import pyautogui
import subprocess

def instruction_finder():
    '''
    This function searches for funtions to be executed inside
    of the container.
    The video's script name must be 'script.md'.
    Returns: A list of functions to be executed.
    Function's structure:
    {command: , media_format: , file_name: }
    '''
    todo = []
    with open('script.md') as f:
        datafile = [line for line in f.readlines() if line.strip()]

        # Here the program should also skip the header.
        for line in datafile:
            if '---' in line and '(instructions:' in line +1:
                to_add = {
                        "command": line+2,
                        "media_format": line+3,
                        "file_name": line +4
                        }

            elif '---' in line and '(instructions:' not in line +1:

                print("Line %s has no instructions")%(line+1)
                
                break

    return todo


# ----------------------------------------------------------------------- #
#                             Recording
# ----------------------------------------------------------------------- #

def start_rec(instructions):
    '''
    Starts asciinema and sets the name of the
    recording to the file_name variable.
    Returns: Should be recording.
    '''
    title = instructions["file_name"]
    subprocess.Popen([
        'asciinema',
        'rec',
        title])


def stop_rec():
    '''
    Stops asciinema using 'ctrl + d'
    '''
    pyautogui.hotkey('ctrl', 'd')

    return 'Sould have stopped'
# ----------------------------------------------------------------------- #
#                         Instrucion executer
# ----------------------------------------------------------------------- #

def run_command(instructions):
    '''
    Input: some text to type in the
    terminal. Must be of type string
    Returns: The string 'Done!'.
    '''
    command = instructions["command"]
    # The typing should only be done inside of the terminal window
    os.system('clear')

    start_rec(instructions)
    time.sleep(1)

    pyautogui.write(command, interval=0.1) #The interval shoud be randomized at some point. 

    pyautogui.press('enter')

    stop_rec()

    return 'Done!'



def instruction_executer(instructions_list):
    '''
    Writes functions in a terminal using 
    pyautogui.

    Input: A list of instructions to execute.
    The format of each instruction is a dict
    containing: the command, the media format 
    and the file name.

    Returns: A string saying 'Done!'.
    '''
    for i in instructions_list:
        if i["media_type"] == 'gif':
            run_command(i)

    return 'Done!'
        

