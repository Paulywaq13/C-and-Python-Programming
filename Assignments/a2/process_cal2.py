#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 01 08:35:33 2022
@author: rivera

This is a text processor that allows to translate XML-based events to YAML-based events.
CAREFUL: You ARE NOT allowed using (i.e., import) modules/libraries/packages to parse XML or YAML
(e.g., yaml or xml modules). You will need to rely on Python collections to achieve the reading of XML files and the
generation of YAML files.
"""
import sys
import re
import os
import datetime

def get_arguments(list_args):
    """This function extracts the arguments passed with the executable Python file and adds it to a dictionary for better organization and accessibility. 

    Args:
        list_args (list[str]): list of filename arguments. 

    Returns:
    
        Dict: Returns a dictionary with key-value pairs holding the 'start', 'end', 'event', 'circuits' and 'broadcaster' filenames. 
        
    """    
    
    dict_args = {} # initialize dictionary to hold arguments
    
    # add arguments to organized key-value pairs 
    dict_args['start'] = list_args[0]
    dict_args['end'] = list_args[1]
    dict_args['events'] = list_args[2]
    dict_args['circuits'] = list_args[3]
    dict_args['broadcasters'] = list_args[4]
    
    return dict_args # return dcitionary of arguments 

def parse_args(lo_args):
    """This function extracts the files of the arguments passed when executing the Python program and returns a list of the filename strings. 

    Args:
        lo_args (list[str]): list of sys.argv that is passed when running the executable Python program. 

    Returns:
    
        list[Dict]: Returns a list of strings of the filenames of the arguments. 
        
    """    
    
    lo_new_arg = [] # initialize our arguments list holder 
    
    # loop through sys.argv passed in as argument 
    for args in lo_args:
        arg = args.partition("=")[2] # partition arguments by the '=' symbol
        lo_new_arg.append(arg) # append to new list 
        
    lo_new_arg.remove(lo_new_arg[0]) # remove name of Python executable as not need for the rest of program

    return lo_new_arg # return list of only the filenames of the arguments passed

def parse_events(events_file):
    """This function parses the information in the events xml file that hold information in our f1 events. 

    Args:
        events_file (str): The string of our filename to be parsed.

    Returns:
    
        list[Dict]: Returns a list of event dictionaries that hold the information extracted from the xml file. 
        
    """    
    
    lo_events = [] # initialize list to hold event dictionaries
    
    # Check if file exists, if so read the file
    if os.path.isfile(events_file):
        
        file = open(events_file, 'r') # open file passed in as argument 
        
        # if file is empty, we do not need to parse the file, can return an empty string. 
        if file == None:
            return lo_events
        
        event_string = """""" # initialize triple quote string to hold the info fmor xml file
        
        # add each line of file into string
        for line in file:
            line = line.strip()
            event_string += line
            
        file.close() 
        
        event_string = event_string.split("<event>") # split string by <event> tag to single out each individual event
        
        event_string.remove(event_string[0]) # remove <calendar> string as it hold no use 
        
        for event in event_string: # loop through event string to extract information held by tags
            
            event_dict = {} # initialize dictionary to hold each event's info
            
            id = re.search(r'<id>(.*?)</id>', event, re.DOTALL).group(1)  # extract id from id tag
            description = re.search(r'<description>(.*?)</description>', event, re.DOTALL).group(1) # extract description
            location = re.search(r'<location>(.*?)</location>', event, re.DOTALL).group(1) # extract location
            day = re.search(r'<day>(.*?)</day>', event, re.DOTALL).group(1) # extract day
            month = re.search(r'<month>(.*?)</month>', event, re.DOTALL).group(1) # extract month
            year = re.search(r'<year>(.*?)</year>', event, re.DOTALL).group(1) # extract year
            start = re.search(r'<start>(.*?)</start>', event, re.DOTALL).group(1) # extract start time
            end = re.search(r'<end>(.*?)</end>', event, re.DOTALL).group(1) # extract end time 
            broadcasters = (re.search(r'<broadcaster>(.*?)</broadcaster>', event, re.DOTALL).group(1).split(",")) # extract broadcasters
            
            # cast date information into ints in order to store into datetime objects
            day = int(day) 
            month = int(month)
            year = int(year)
            date = datetime.datetime(year, month, day) # create datetime object for easier comparisons of dates
            
            start_hour = int(start[0:2]) # get the starting hour by slicing
            start_min = int(start[3:]) # get start min by slicing
            
            end_hour = int(end[0:2]) # get end hour by slicing
            end_min = int(end[3:]) # get end min by slicing 
            
            # store extracted information into dictionary 
            event_dict['id'] = id
            event_dict['description'] = description
            event_dict['location'] = location
            event_dict['date'] = date
            event_dict['start'] = start
            event_dict['end'] = end
            event_dict['start_datetime'] = datetime.datetime(year, month, day, start_hour, start_min)
            event_dict['end_datetime'] = datetime.datetime(year, month, day, end_hour, end_min)
            event_dict['broadcaster'] = broadcasters
            
            lo_events.append(event_dict) # append dictionary to list 
            
        else:
            return lo_events # return empty list if file does not exist

    return lo_events # return list of event dictionaries 

def parse_circuits(circuits_file):
    """This function parses the information of the circuits xml file into a list of circuit dictionaries. 

    Args:
        circuits_file (str): string of circuits file

    Returns:
    
       list[Dict]: Returns a list of dictionaries containing the circuits information. 
       
    """    
    
    lo_circuits = [] # initialize list that will hold our dictionaries
    
    
    # check if circuits file exists, then we can continue
    if os.path.isfile(circuits_file):
    
        file = open(circuits_file, 'r') # open file passed in as argument 
        
        # if file is empty, we do not need to parse the file, can return empty list
        if file == None:
            return lo_circuits
        
        circuit_string = """""" # initialize triple quote string to hold contents of the file
        
        # add each line to our string for easy identification of tags
        for line in file:
            line = line.strip()
            circuit_string += line
            
        file.close()
            
        circuit_string = circuit_string.split("<circuit>") # split string by <circuit> tag to get each individual circuit
        
        circuit_string.remove(circuit_string[0]) # remove <circuits> tag as it holds no information for use
        
        for circuit in circuit_string: # loop through string to extract information within tags
            
            circuit_dict = {} # initialize dict to hold information
            
            id = re.search(r'<id>(.*?)</id>', circuit, re.DOTALL).group(1) # extract id information
            name = re.search(r'<name>(.*?)</name>', circuit, re.DOTALL).group(1) # extract name information
            location = re.search(r'<location>(.*?)</location>', circuit, re.DOTALL).group(1) # extract location
            timezone = re.search(r'<timezone>(.*?)</timezone>', circuit, re.DOTALL).group(1) # extract timzeone
            direction = re.search(r'<direction>(.*?)</direction>', circuit, re.DOTALL).group(1) # extract direction
            
            # add extarcted information to our dictionary
            circuit_dict['id'] = id
            circuit_dict['name'] = name
            circuit_dict['location'] = location
            circuit_dict['timezone'] = timezone
            circuit_dict['direction'] = direction
            
            lo_circuits.append(circuit_dict) # append dictionary to our list
            
        else:
            return lo_circuits
    
    return lo_circuits # return our list of circuit dictionaries 

def parse_broadcasters(broadcasters_file):
    """This function parses the information of the broadcasters xml file into a list of dictionaries based on the broadcasters values. 

    Args:
        broadcasters_file (str): string of broadcaster file.

    Returns:
    
        list[Dict]: Returns a list of broadcaster dictionaries.
        
    """    
    
    lo_broadcasters = [] # initialize list of broadcasters
    
    # check if file exists, if so read
    if os.path.isfile(broadcasters_file):
        
        file = open(broadcasters_file, 'r') # open file passed in as argument
    
        # if file is empty, we do not need to parse the file, can return empty list. 
        if file == None:
            return lo_broadcasters 
        
        broadcasters_string = """""" # initialize triple quote string to hold the contents of the broadcasters file in a single string variable
        
        # add each line in the file to the braodcaster string
        for line in file:
            line = line.strip()
            broadcasters_string += line
            
        file.close()  # close file since we have extracted the information needed. 
        
        broadcasters_string = broadcasters_string.split("<broadcaster>") # split string by broadcaster tag to get contents
        
        broadcasters_string.remove(broadcasters_string[0]) # remove <broadcasters> tag as it hold no needed information
        
        for broadcaster in broadcasters_string: # loop through string to gather information in each tag and add to dictionary
            
            broadcaster_dict = {} # create broadcaster dictionary
            
            id = re.search(r'<id>(.*?)</id>', broadcaster, re.DOTALL).group(1) # extract id information
            name = re.search(r'<name>(.*?)</name>', broadcaster, re.DOTALL).group(1) # extract name information
            cost = re.search(r'<cost>(.*?)</cost>', broadcaster, re.DOTALL).group(1) # extract cost information
        
            # add the gathered info into the dictionary
            broadcaster_dict['id'] = id
            broadcaster_dict['name'] = name
            broadcaster_dict['cost'] = cost
            
            lo_broadcasters.append(broadcaster_dict) # add dictionary to the list of dictionaries 
        else:
            return lo_broadcasters # return empty list if file does not exist
    
    return lo_broadcasters # return our list of broadcaster dictionaries
    

def get_dates_events(start_date, end_date, lo_events_dict):
    """Gets events that are within the start and end date arguments.

    Args:
        start_date (list): _description_
        
        end_date (list): _description_
        
        lo_events_dict (list): _description_

    Returns:
    
        list[Dict]: Returns a list of valid event dictionaries that are within the start and end dates. 
        
    """
    
    event_within_date = [] # initialize our list that will hold the dictionary events
    
    start_date = start_date.split("/") # start_date in format dd/mm/year, split by / to get each element
    end_date = end_date.split("/") # end_date in format dd/mm/year, split by / to get each element
    
    # Cast our event elements into integers for easier datetime comparison 
    for i in range(0,3): 
        start_date[i] = int(start_date[i])
        end_date[i] = int(end_date[i])
        
    start_date = datetime.datetime(start_date[0], start_date[1], start_date[2]) # date time object of start date
    
    end_date = datetime.datetime(end_date[0], end_date[1], end_date[2]) # datetime object of end date
    
    # loop through events and compare each date with start and end dates. Store valid dates in initialized list 
    for events in lo_events_dict:
        if events['date'] >= start_date and events['date'] <= end_date:
            event_within_date.append(events)
     
    event_within_date = sorted(event_within_date, key=lambda event: event['start_datetime']) # sort newly created list of event dictionaries from earliest date to latest date. 
    
    return event_within_date # return new list of dictionary events that are sorted and within the specified dates. 


def output_yaml(lo_events, lo_circuits_dict, lo_broadcasters_dict):
    """Outputs a yaml file with information on each event within our dates. 

    Args:
        lo_events (list[Dict]): list of dictionary events
        
        lo_circuits_dict (list[Dict]): list of dictionary circuits
        
        lo_broadcasters_dict (list[Dict]): list of distionary broadcasters
        
    Returns:
    
        Void: This function simply outputs a yaml file into the working directory and returns None.
        
    """
    
    with open('output.yaml', 'w') as yam: # begin writing our yaml output file
        
        # if lo_events is empty, we simply output 
        if lo_events == []:
            yam.write('events:')
            return
        
        else:
            yam.write('events:\n') # print events header
        
        for i in range(0, len(lo_events)): # loop through number of events 
            
            # if-else statement to have events that occur on same date in the correct format
            if(i!=0):
                
                if( lo_events[i]["date"] == lo_events[i-1]["date"] ):
                    # if event on same date pass this if-else statement
                    pass 
                else:
                    yam.write('  - 'f'{lo_events[i]["date"].strftime("%d-%m-%Y:")}\n') # if event not on same date, print the date
                    
            else:
                yam.write('  - 'f'{lo_events[i]["date"].strftime("%d-%m-%Y:")}\n') # if first event to output, print the date
                
                  
            yam.write('    - id: 'f'{lo_events[i]["id"]}\n') # f format string to write event id into yaml.file
            yam.write('      description: 'f'{lo_events[i]["description"]}\n') # f format string to write event description into yaml.file
            
            yam.write('      circuit: ')
            
            # loop through circuit dictionary to print matching circuit with event
            for circuits in lo_circuits_dict:
                
                if circuits["id"] == lo_events[i]["location"]:
                    
                    yam.write(f'{circuits["name"] + " (" + circuits["direction"] + ")"}\n')
                    yam.write('      location: 'f'{circuits["location"]}\n')
                    timezone = circuits["timezone"] # store timezone variable for later use from lo_circuits_dict 
                    
            yam.write('      when: 'f'{lo_events[i]["start_datetime"].strftime("%I:%M %p - ")}') # write properly formatted start hour
            yam.write(f'{lo_events[i]["end_datetime"].strftime("%I:%M %p %A, %B %d, %Y ") + "("+ timezone +")"}\n') # write properly formatted end hour and overall date
            
            yam.write('      broadcasters:\n')
            
            # begin looping through broadcaster list of dictionaries to access data
            
            for broadcaster in lo_events[i]["broadcaster"]: # for each of our events, loop through the list that holds the broadcaster ids
                
                for info in lo_broadcasters_dict: # loop though our list of broadcaster dictionary 
                    
                    if info["id"] == broadcaster: # if our broadcaster dictionary is equal to the event broadcaster id we have a match
                        
                        if (i == len(lo_events)-1) and (broadcaster == lo_events[i]["broadcaster"][len(lo_events[i]["broadcaster"])-1]):
                            yam.write('        - 'f'{info["name"]}')
                            
                        else:
                            yam.write('        - 'f'{info["name"]}\n') # write the broadcaster name into the file 
                
        yam.close() # close file after finished writing
                    
    return

def main():
    """The main entry point for the program.
    """
    
    if len(sys.argv) > 5: # if we have the required amount of arguments, perform our code
        
        parsed_args = parse_args(sys.argv) # parse args to be able access info
        
        arg_info = get_arguments(parsed_args) # get argument information
        
        event_file = arg_info['events'] # get event filename
        circuits_file = arg_info['circuits'] # get circuit filename
        broadcasters_file = arg_info['broadcasters'] #get broadcaster filename
        
        start_date = arg_info['start'] # get start date in readable format
        end_date = arg_info['end'] # get end date in readable format
        
        lo_events_dict = parse_events(event_file) # put events into a list of dictionary events
        
        lo_circuits_dict = parse_circuits(circuits_file)  # put circuits into a list of dictionary circuits
        
        lo_broadcasters_dict = parse_broadcasters(broadcasters_file) # put broadcasters into a list of dictionary broadcasters
        
        lo_events_within_dates = get_dates_events(start_date, end_date, lo_events_dict) # get events that are within start and end dates into a list of dictionary events
        
        output_yaml(lo_events_within_dates, lo_circuits_dict, lo_broadcasters_dict) # output yaml file
          
    else:
        
        print("Required arguments for program: <filename> <start_date> <end_date> <events> <circuits> <broadcasters>")
        

if __name__ == '__main__':
    main()
