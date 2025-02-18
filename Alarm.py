import time  # Import the time module for time-related functions
from datetime import datetime  # Import datetime class from datetime module for working with dates and times
from playsound import *  # Import all functions from playsound module for playing sound files

def play_alarm_sound():
    # Function to play the alarm sound and print an alert message
    playsound('/path/note.mp3')  # Play the alarm sound from the specified path
    print("\n** ALARM! **\n")  # Print an alert message to the console

def set_alarm():
    # Function to set the alarm time based on user input
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")  # Prompt user for alarm time input
    try:
        datetime.strptime(alarm_time, "%H:%M:%S")  # Try to parse the input string as a time
        return alarm_time  # Return the valid alarm time if parsing is successful
    except ValueError:
        # If parsing fails, notify the user and prompt for input again
        print("Incorrect time format. Please use HH:MM:SS.")  # Print an error message for incorrect time format
        return set_alarm()  # Recursively call set_alarm() to allow user to try again
    
def main():
    # Main function to execute the alarm setting and monitoring process
    alarm_time = set_alarm()  # Call set_alarm() to get the desired alarm time from the user
    print(f"Alarm set for {alarm_time}")  # Print confirmation that alarm time has been set

    while True:
        # Infinite loop to continuously check the current time
        now = datetime.now().strftime("%H:%M:%S")  # Get the current time and format it as HH:MM:SS
        if now == alarm_time:
            # Check if the current time matches the alarm time
            play_alarm_sound()  # Call play_alarm_sound() to play the alarm sound
            break  # Exit the loop after the alarm has been triggered
        time.sleep(1)  # Pause execution for 1 second before checking the time again

if __name__ == "__main__":
    main() 
