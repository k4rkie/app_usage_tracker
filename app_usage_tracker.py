from subprocess import run
import time


def check_if_vscode_active():
    print("Press Ctrl+C to exit the program")
    counter = 0
    try:    
        while True:

            # get the active window property
            x_active_win_props = run(['xprop', '-root', '_NET_ACTIVE_WINDOW'], capture_output=True, text=True).stdout

            # extract the window_id of the active window
            x_active_win_id = x_active_win_props.split(" ")[4].replace(",","")

            # use the active window_id to find the wm_class name of the window
            x_active_win_class_prop = run(['xprop', '-id', x_active_win_id, 'WM_CLASS'], capture_output=True, text=True).stdout

            # check if the wm_class prop contains the string "code" which is the class name of vs code
            if x_active_win_class_prop.lower().find("code") != -1 :
                # if yes add 1sec to the counter
                counter += 1
            time.sleep(1)
            print(x_active_win_class_prop)

    # Press Ctrl+C to exit the program
    except KeyboardInterrupt:
        print(f"\nYou spent a total of {counter} seconds in vscode")

check_if_vscode_active()























# Ignore lines below this its just a mess








# time.sleep(5)

# Get the window property of the active window using xprop.
# This is for extracting the window id of active window
# x_active_win_props = run(['xprop', '-root', '_NET_ACTIVE_WINDOW'], capture_output=True, text=True).stdout # stdout give the output of the standard output so that we can store it in a variable

# extract the window_id for the output above but splitting between the spaces" "
# this returns a list so we get the 4th element which is the id itself and remove the trailing comma
# x_active_win_id = x_active_win_props.split(" ")[4].replace(",","")

# find out the class name of the active window using the window_id from above
# x_active_win_class_prop = run(['xprop', '-id', x_active_win_id, 'WM_CLASS'], capture_output=True, text=True).stdout

# Extract the actual class_name from the stdout, split between the spaces" ", removing the comma and quotes
# x_active_window_class_name = x_active_win_class_prop.split(" ")[2].replace(",","").replace('"','')
# x_active_window_class_name = x_active_win_class_prop.lower()

# print(x_active_window_class_name)

# check if the active window is code
# if x_active_window_class_name.find("code") != -1 :
#     print("Vscode is active")
# else:
#     print("Vscode is not active")
