import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    question_counter = 1
    
    print('\n' + ('-'*100) + '\nHello! Let\'s explore some US bikeshare data! \n')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while question_counter == 1:
        city_input = input('Select a city: \n 1) Chicago \n 2) New York City \n 3) Washington\n 4) Exit\n')
        
        if city_input == '1' or city_input.lower() == 'chicago':
            city = 'chicago'
            question_counter += 1
        elif city_input == '2' or city_input.lower() == 'new york city' or city_input.lower() == 'nyc':
            city = 'new york city'
            question_counter += 1
        elif city_input == '3' or city_input.lower() == 'washington':
            city = 'washington'
            question_counter += 1
        elif city_input == '4':
            print('\nBye!\n')
            quit()
        else:
            print('\nError! Please enter a number or city name listed above\n')           
        
    print('\n' + city.title() + ' selected')
    
    # get user input for month (all, january, february, ... , june)   
    while question_counter == 2:    
        month_input = input('\nSelect month: \n 0) All \n 1) January \n 2) February \n 3) March \n 4) April \n 5) May \n 6) June \n 7) Restart \n 8) Exit\n')
        
        if month_input == '0' or month_input.lower() == 'all':
            month = 'all'
            question_counter += 1
            print('\nJanuary to June 2017 selected')
        elif month_input == '1' or month_input.lower() == 'january' or month_input.lower() == 'jan':
            month = 'january'
            question_counter += 1            
            print('\nJanuary selected')
        elif month_input == '2' or month_input.lower() == 'february' or month_input.lower() == 'feb':
            month = 'february'
            question_counter += 1
            print('\nFebruary selected')
        elif month_input == '3' or month_input.lower() == 'march' or month_input.lower() == 'mar':
            month = 'march'
            question_counter += 1
            print('\nMarch selected')
        elif month_input == '4' or month_input.lower() == 'april' or month_input.lower() == 'apr':
            month = 'april'
            question_counter += 1
            print('\nApril selected')
        elif month_input == '5' or month_input.lower() == 'may':
            month = 'may'
            question_counter += 1            
            print('\nMay selected')
        elif month_input == '6' or month_input.lower() == 'june' or month_input.lower() == 'jun':
            month = 'june'
            question_counter += 1            
            print('\nJune selected')
        elif month_input == '7':
            print('\nRestarting...')
            get_filters()
        elif month_input == '8':
            print('\nBye!\n')
            quit()
        else:
            print('\nError! Please enter a number or month')       
            
    # get user input for day of week (all, monday, tuesday, ... sunday)   
    while question_counter == 3:
        day_input = input('\nSelect day: \n 0) All \n 1) Monday \n 2) Tuesday' + #Written this way for visibility
        '\n 3) Wednesday \n 4) Thursday \n 5) Friday \n 6) Saturday \n 7) Sunday \n 8) Restart \n 9) Exit\n')
        
        if day_input == '0' or day_input.lower() == 'all':
            day = 'all'
            question_counter += 1
            print('\nAll days selected')
        elif day_input == '1' or day_input.lower() == 'monday' or day_input.lower() == 'mon':
            day = 'monday'
            question_counter += 1
            print('\nMonday selected')
        elif day_input == '2' or day_input.lower() == 'tuesday' or day_input.lower() == 'tue':
            day = 'tuesday'
            question_counter += 1
            print('\nTuesday selected')
        elif day_input == '3' or day_input.lower() == 'wednesday' or day_input.lower() == 'wed':
            day = 'wednesday'
            question_counter += 1
            print('\nWednesday selected')
        elif day_input == '4' or day_input.lower() == 'thursday' or day_input.lower() == 'thu':
            day = 'thursday'
            question_counter += 1
            print('\nThursday selected')
        elif day_input == '5' or day_input.lower() == 'friday' or day_input.lower() == 'fri':
            day = 'friday'
            question_counter += 1
            print('\nFriday selected')
        elif day_input == '6' or day_input.lower() == 'saturday' or day_input.lower() == 'sat':
            day = 'saturday'
            question_counter += 1
            print('\nSaturday selected')
        elif day_input == '7' or day_input.lower() == 'sunday' or day_input.lower() == 'sun':
            day = 'sunday'
            question_counter += 1
            print('\nSunday selected')
        elif day_input == '8':
            print('\nRestarting...')
            get_filters()
        elif day_input == '9':
            print('\nBye!\n')
            quit()
        else:
            print('\nError! Please enter a number or day')            
    
    print('-'*100)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day'] == day.title()]
        
    # Uncomment print statement and comment out return statement to test code    
    #print(df) 

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        df -  Pandas DataFrame containing city data filtered by month and day      
    Returns:
        - Prints busiest month for specified city and time frame in df
        - Prints busiest day for specified city and time frame in df
        - Prints busiest hour for specified city and time frame in df
        - Prints time took to calculate time statistics
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month      
    df['Month'] = df['Start Time'].dt.month    
    popular_month = df['Month'].mode()[0]
    month_name = MONTHS[popular_month - 1] # Taking index 0 into account

    print('The busiest month is ' + month_name.title())

    # display the most common day of week  
    popular_day = df['Day'].mode()[0]

    print('The busiest day of the week is ' + str(popular_day))


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    # Calculate 12 hour time
    if popular_hour > 12:
        popular_hour -= 12
        popular_hour = str(popular_hour) + ":00 PM"
    elif popular_hour == 0:
        popular_hour = "12:00 AM"
    elif popular_hour == 12:
        popular_hour = "12:00 PM"    
    elif popular_hour < 12:
        popular_hour = str(popular_hour) + ":00 AM"
        
    print('The busiest hour is ' + popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        df -  Pandas DataFrame containing city data filtered by month and day      
    Returns:
        - Prints most commonly used start station for specified city and time frame in df
        - Prints most commonly used end station for specified city and time frame in df
        - Prints most frequent trip for specified city and time frame in df
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    busiest_start_station = df['Start Station'].mode()[0]

    print("The most commonly used start station is " + busiest_start_station)

    # display most commonly used end station
    busiest_end_station = df['End Station'].mode()[0]

    print("The most commonly used end station is " + busiest_end_station)

    # display most frequent trip
    
    df['Trip'] = df['Start Station'] + "\nTO: " + df['End Station']
    trip = df['Trip'].mode()[0]
    
    print("\nThe most frequent trip is \nFROM: " + trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        df -  Pandas DataFrame containing city data filtered by month and day    
    Returns:
        - Prints total travel time for specified city and time frame in df
        - Prints average travel time for specified city and time frame in df
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_seconds = int(df['Trip Duration'].sum())
    total_travel = str(datetime.timedelta(seconds = total_seconds))
    
    # format total travel time
    total_seconds = total_travel[-2] + total_travel[-1]
    total_minutes = total_travel[-5] + total_travel[-4]
    total_hours = total_travel[-8] + total_travel[-7]
    total_hours = total_hours.replace(" ", "0")
    
    print("The total time travelled is " + total_travel.replace(total_travel[-9:], " " + #Written this way for visibility
         total_hours + " hours, " + total_minutes + " minutes and " + total_seconds + " seconds"))
         
         
    # display mean travel time
    average_seconds = int(df['Trip Duration'].mean())
    average_time = str(datetime.timedelta(seconds = average_seconds))   
        
    # format average travel time    
    average_seconds = average_time[-2] + average_time[-1]
    average_minutes = average_time[-5] + average_time[-4]
    average_hours = average_time[0]
    
    print("The average travel time is 0" + average_hours + " hours, " + average_minutes + " minutes and " + average_seconds + " seconds ")
    
    # The below code would be used instead if average time reached double digit hours 
    # (however, this is not the case in the current data set)
    
    #average_hours = average_time[-8] + average_time[-7]
    #average_hours = average_hours.replace(" ", "0")
    
    # print("The average time travelled is " + average_time.replace(average_time[-9:], " " + #Written this way for visibility
          # average_hours + " hours, " + average_minutes + " minutes and " + total_seconds + " seconds "))
   
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    
    Args:
        df -  Pandas DataFrame containing city data filtered by month and day
    Returns:
        - Prints user type counts for specified city and time frame in df
        - Prints user gender counts for specified city and time frame in df
        - Prints earliest, most recent, and most common year of birth for users in specified city and time frame in df
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_types = str(df['User Type'].value_counts())
    user_types = user_types.replace("Name: User Type, dtype: int64", "") # formatting
    
    print(user_types)

    # Display counts of gender 
    user_gender = str(df['Gender'].value_counts())
    user_gender = user_gender.replace("Name: Gender, dtype: int64", "") # formatting
    
    print(user_gender)

    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = int(df['Birth Year'].min())   
    print("The earliest user birth year is " + str(earliest_birth_year))
    
    latest_birth_year = int(df['Birth Year'].max())
    print("The most recent user birth year is " + str(latest_birth_year))
    
    common_birth_year = int(df['Birth Year'].mode()[0])
    print("The most common user birth year is " + str(common_birth_year))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def washington_user_stats(df):
    """
        Displays statistics on bikeshare users for Washington.
    
    Args:
        df -  Pandas DataFrame containing Washington data filtered by month and day
    Returns:
        - Prints user type counts for Washington and specified time frame in df
        - Prints missing gender data message
        - Prints missing birth year data message
    """
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_types = str(df['User Type'].value_counts())
    user_types = user_types.replace("Name: User Type, dtype: int64", "") # formatting
    
    print(user_types)

    # Display counts of gender 
    print("User gender data not available")

    # Display earliest, most recent, and most common year of birth
    print("User birth year data not available")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def raw_data(df):
    """
        Displays raw data upon request.
    
    Args:
        df -  Pandas DataFrame containing city data filtered by month and day
    Returns:
        Pandas DataFrame raw data
    """
    
    current = 0
    last = 0
    loop_counter = 0
   
    while True:
        view_df = input('\nView 5 lines of raw data? [Y/N]\n')
        
        if view_df.lower() == 'y' or view_df.lower() == 'yes':
            if loop_counter < 1:
                last += 4
                loop_counter += 1
            elif loop_counter >= 1:
                last += 5
                loop_counter += 1
                
        #if view_df.lower() == 'y' or view_df.lower() == 'yes':
            while current <= last:
                print(df[df.columns[0:-1]].iloc[current])
                current += 1
                
        elif view_df.lower() == 'n' or view_df.lower() == 'no':
            break
            

def main():
    while True:
    
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        if city == 'washington':
            washington_user_stats(df)
        else:
            user_stats(df)
            
        raw_data(df)

        restart = input('\nWould you like to restart? [Y/N].\n')
        if restart.lower() != 'y':
            print('\nBye!\n')
            break


if __name__ == "__main__":
	main()
