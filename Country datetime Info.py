import datetime

def get_country_info(country_name):
    try:
        # Get the current date and time
        now = datetime.datetime.now()

        # Print the country name and current date and time
        print(f"Country: {country_name}")
        print(f"Current Date and Time: {now}")

        # Get the day of the week (0 = Monday, 6 = Sunday)
        day_of_week = now.weekday()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(f"Day of the Week: {days_of_week[day_of_week]}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
user_country = input("Enter a country name: ")
get_country_info(user_country)

