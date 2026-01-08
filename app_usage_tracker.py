from subprocess import run
import time, datetime
import signal, sys
from pathlib import Path

def main():
    print("Press Ctrl+C to exit the program")

    date = datetime.datetime.now()
    today = date.strftime("%Y-%m-%d")

    base_dir = Path.home() / ".local" / "share"
    app_dir = base_dir / "usage_tracker"
    app_dir.mkdir(parents=True, exist_ok=True)
    log_file = app_dir / "app_usage_log.txt"

    # try creating a new file if doesnt exist
    try:
        f = open(log_file, "x")
        counter = 0
        f.close()
    
    # else read the existing file
    except FileExistsError:
        with open(log_file, "r") as f:
            # check if the exists but is empty
            if f.read():
                # reset the file reader pointer to the start"0"
                f.seek(0)
                # read the last line of the file
                read_log_data = f.readlines()[-1]
                # check if the last line/entry is form today
                if read_log_data.split(" ")[0].replace(":","") == today:
                    counter = int(read_log_data.split(" ")[1])
            else:
                counter = 0

    def signalHandler(signum, frame):
        print("\nSystem is about to shutdown, Pack up lil bro")
        with open(log_file, "a") as f:
            f.write(f"\n{today}: {counter} seconds;")
        sys.exit(0)

    # check for any SIGTERM signals for the os and call the handler if TRUE
    signal.signal(signal.SIGTERM, signalHandler)

    # check for any SIGINT signals for the os and call the handler if TRUE
    signal.signal(signal.SIGINT, signalHandler)
    
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
    


main()





























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
