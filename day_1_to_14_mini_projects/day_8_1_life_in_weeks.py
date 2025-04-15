# Exercise inspired by Tim Urban’s article titled “Your Life in Weeks” (https://waitbutwhy.com/2014/05/life-weeks.html)


def life_in_weeks(age):
    weeks = 90*52 - age*52
    print(f"If you are destined to live to 90, you have 12 {weeks} weeks left.")

    # Decided to add additional information as requested
    question = input('\nDo you want to know how much it will be in years, months, days, hours, minutes and seconds?'
                     ' Type "yes" or "no"\n--->> ').lower()

    if question == "yes":
        years = 90 - age
        months = years * 12
        days = weeks * 7
        hours = days * 24
        minutes  = hours * 60
        seconds = minutes * 60

        print(f'''
        You have:
            {years} years,
            {months} months,
            {weeks} weeks,
            {days} days,
            {hours} hours,
            {minutes} minutes,
            {seconds} seconds
        left
        ''')
    elif question == "no":
        print("Okay. Good bye!")
    else:
        print('Incorrect input. You only had to type "yes" or "no".')

your_age = int(input("How old are you?\n--->> "))

life_in_weeks(your_age)
