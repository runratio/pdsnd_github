import pandas as pd
import numpy as np
import time


city_data = {

    'chicago' : 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'All']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

#city_name = input('Which city would you like to see data from?\n')

#df = pd.read_csv(city_data[city_name])

def print_pause(message_to_print): #Print timing
    print(message_to_print)
    time.sleep(1)

def intro():
    print('Hello! Let\'s explore some US bikeshare data!')


def get_filter(): #COLLECTING USER INPUT

    city_name = input('\nWhich city would you like to see data from Chicago, New York or Washington?\n').lower()
    while city_name not in city_data:
        city_name = input('\nPlease select one of the options listed (Chicago, New  York or Washington\n').lower()
    if city_name in city_data:
        print_pause('\nYou have selected {}'.format(city_name).title())

    day = input('\nPlease name the day to filter by, or \'all\' to apply no day filter.\n').title()
    while day not in days:
        day = input('\nPlease select the day of the week that you would like filter by or \'all\' to apply no day filter.\n').title()
    if day in days:
        print_pause('\nYou have selected {}'.format(day))

    month = input('\nPlease name the month to filter by, or \'all\' to apply no month filter.'
    '\nPLEASE ENTER THE MONTH IN NUMBER FORMAT (FOR EXAMPLE 1 FOR January)\n').title()
    while month not in months:
        month = input('\nPlease select the month in number format that you would like to filter by or \'all\' to apply no  month filter\n').title()
    if month in months:
        print_pause('\nYou have selected {}'.format(month))

    return city_name, month, day


def load_data(city_name, month, day): #LOADING DATA FOR SPECIFIED CITY FILTER

    df = pd.read_csv(city_data[city_name])

    #convert start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day of week from Start Time to creat new coloums
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['station_combo'] = df['Start Station'] + (' to ') + df['End Station']

    if month != 'all' and day != 'All':
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == day]

    return(df)


def time_statistics(df): #CALCULATING TIME STATISTICS

    print_pause('\nCalculating the most popular times of travel\n')

    #Most popular month
    print_pause('The most popular month is: Month {} of the calendar year'.format(df['month'].mode()))

    #Most popular day_of_week
    print_pause('The most popular day of the week is: {}'.format(df['day_of_week'].mode()))

    #Most popular start hour
    print_pause('The most popular hour is: {}'.format(df['hour'].mode()))

    print('')
    print_pause('~'*50)


def station_statistic(df): 

    print('\nCalculating the most popular stations & trips\n')

    #most popular starting station
    most_pop_start_station = df['Start Station'].mode()
    print_pause('{} is the most popular start station'.format(most_pop_start_station))

    #most popular ending stations
    most_pop_end_station = df['End Station'].mode()
    print_pause('{} is the most popular end station'.format(most_pop_end_station))

    #most popular combination of start station & end station
    most_pop_combo_station = df['station_combo'].mode()
    print_pause('{} is the most popular combination of start station and end station trips.'.format(most_pop_combo_station))

    print('')
    print_pause('~'*50)



def trip_duration_statistics(df): #CALCULATING TRIP STATISTIC

    print_pause('\nCalculating the total & average trip durations\n')

    #total travel time
    print_pause('The total time travelled is {} seconds'.format(df['Trip Duration'].sum()))

    #average travel time
    print_pause('The average time travelled is {} seconds'.format(df['Trip Duration'].mean()))

    print('')
    print_pause('~'*50)


def user_statistic(df): #USER DATA

    print_pause('\nCalculating user statistics\n')

    #number of users
    print_pause('The number users: {}'.format(df['User Type'].count()))

    #number of users per Gender
    print_pause('The number users: {}'.format(df['User Type'].count()))

    #earliest, most recent and most common year of birth
    print_pause('The youngest user was born in {}'.format(df['Birth Year'].max()))
    print_pause('The oldest user was born in {}'.format(df['Birth Year'].min()))
    print_pause('The most popular birth year of our users is {}'.format(df['Birth Year'].mode()))

    print('')
    print_pause('~'*50)


intro()
city_name, month, day = get_filter()
df = load_data(city_name, month, day)
time_statistics(df)
station_statistic(df)
trip_duration_statistics(df)
user_statistic(df)
