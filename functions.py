from os import write


def logTime (time):
    with open("art_time_log.txt", "a") as f:
              f.write(f"{time}\n")
    print(f"Logged {time} hours to art_time_log.txt")

def showProgress():
       try:
              with open("art_time_log.txt", "r") as f:
                     minutes = f.readlines()
              total_time = sum(float(m.strip()) for m in minutes)
              print(f"Total time spent on art: {total_time} hours")
       except FileNotFoundError:
              print("No log file found. Please log some time first.")

