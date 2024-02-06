# Given start date
start_date = datetime(2023, 7, 7)

# Current date (automatically set to today)
current_date = datetime.now()

# Calculate the number of days between the start date and current date
days_elapsed = (current_date - start_date).days

# Calculate the number of years that have passed
years_elapsed = days_elapsed / 365  # Assuming an average of 365 days per year

# Calculate the allowed kilometers based on the number of years
allowed_kilometers = 10000 * years_elapsed

print(
 f"Je zou op dit moment {allowed_kilometers:.0f}km hebben mogen rijden.")