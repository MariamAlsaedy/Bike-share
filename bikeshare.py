import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']


DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nWhat is the name of the city to analyze data? (E.g. Input either chicago, new york city, washington)\n")
        if city_name.lower() in CITY_DATA:
            #We were able to get the name of the city to analyze data.
            city = CITY_DATA[city_name.lower()]
        else:
            print("undifiend input")

    # get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTHS:
        month_name = input("\nWhat is the name of the month to filter data? (E.g. Input either 'all' to apply no month filter or january, february, ... , june)\n")
        if month_name.lower() in MONTHS:
            #We were able to get the name of the month to analyze data.
            month = month_name.lower()
        else:
            print("undifiend input")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAYS:
        day_name = input("\nWhat is the name of the day to filter data? (E.g. Input either 'all' to apply no day filter or monday, tuesday, ... sunday)\n")
        if day_name.lower() in DAYS:
            #We were able to get the name of the month to analyze data.
            day = day_name.lower()
        else:
            print("undifiend input")
    print('-'*40)
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
    df =  pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
       month = MONTHS.index(month)

        # filter by month to create the new dataframe
       df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popularmonth=df['month'].mode()[0]
    print(f"The Most Common Month is :  {popularmonth}" ) 


    # display the most common day of week
    popularday=df['day_of_week'].mode()[0]
    print(f"The Most Common Day In The Week  is :  {popularday}" )

    # display the most common start hour
    popularhour=df['hour'].mode()[0]
    print(f"The Most Common Hour  In The Day  is : {popularhour} " )



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popularstart_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", popularstart_station)


    # display most commonly used end station
    popularend_station = df['End Station'].mode()[0]
    print("The most commonly used End station :", popularend_station)


    # display most frequent combination of start station and end station trip
    combination = df[['Start Station', 'End Station']].mode().loc[0]
    print(f"The most commonly used start station and end station : {combination[0]}, {combination[1]}")
            


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)


    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(f"Total travel time :{ mean_travel}")
    

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df['User Type'].value_counts()
     
    print("The count of user types from the given fitered data is: \n" + str(user_counts))

    
    # Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))
    
    


    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    # the most common birth year
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)
    # the most recent birth year
    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)
    # the most earliest birth year
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()