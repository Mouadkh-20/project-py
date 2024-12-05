import time

def countdown_timer(seconds):
    """
    A simple countdown timer that prints the remaining time.
    
    Args:
        seconds (int): The number of seconds for the countdown.
    """
    print(f"Countdown timer started for {seconds} seconds.")
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        timer_display = f"{minutes:02d}:{secs:02d}"
        print(timer_display, end="\r")  # Overwrites the same line
        time.sleep(1)
        seconds -= 1
    print("Timer finished!                   ")

def start_timer():
    """
    Interactive timer program that asks the user to set a countdown.
    """
    try:
        user_input = int(input("Enter the number of seconds for the countdown: "))
        countdown_timer(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    start_timer()