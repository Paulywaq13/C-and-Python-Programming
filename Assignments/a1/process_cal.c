#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_LINE_LEN 200
#define MAX_EVENTS 1000

typedef struct Event{
    int year, month, day;
    char startTime[MAX_LINE_LEN];
    char endTime[MAX_LINE_LEN];
    char description[MAX_LINE_LEN];
    char location[MAX_LINE_LEN];
    char dweek[MAX_LINE_LEN];
    char timezone[MAX_LINE_LEN];
}Event;

typedef struct Date{
    int year, month, day;
    int startTime;
    int endTime;
}Date;

Event totalEvents[MAX_EVENTS]; /* store all events in an array of Event structs */

int readXMLfile(char *filename, int* startEndDates);
int compareEvents(const void *Event1, const void *Event2);
void printEvents(int readingEvents);
void convertTime(char* str);
time_t createTimeStructEvent(const void *Event);
time_t createTimeStructDates(struct Date *Date);

/**
 * @brief Function: main
        Description: represents the entry point of the program.

        Inputs: 
            - argc: indicates the number of arguments to be passed to the program.
            - argv: an array of strings containing the arguments passed to the program.
        Output: an integer describing the result of the execution of the program:
            - 0: Successful execution.
            - 1: Erroneous execution.
 * 
 * @param argc - indicates the number of arguments to be passed to the program.
 * @param argv - an array of strings containing the arguments passed to the program.
 * @return int - 0: Successful execution.
                 1: Erroneous execution.
 */

int main(int argc, char *argv[])
{   
    
    if(argc > 2){
        
        /* Initialize start and end date details from passed in arguments */
        int startYear, startMonth, startDay;
        int endYear, endMonth, endDay;

        char fileName[MAX_LINE_LEN];/* Create filename character array to hold the file argument passed */

        int readingEvents; /* Initialize amount of Events to be read. */

        char* filePointer = NULL; /* Create pointer to file*/
        int* datePointer = NULL; /* Create pointer to the start and end dates arguments. */


       /* Gather information from arguments and store in above variables */
        sscanf(argv[1], "--start=%d/%d/%d", &startYear, &startMonth, &startDay);
        sscanf(argv[2], "--end=%d/%d/%d", &endYear, &endMonth, &endDay);
        sscanf(argv[3], "--file=%s", fileName);

        int startEndDates[] = {startYear, startMonth, startDay, endYear, endMonth, endDay}; /* Fill int array of the start and end dates */

        datePointer = startEndDates; /* set pointer to int array of startEndDates */
        
        filePointer = fileName; /* Set file pointer to file passed in as argument */

        readingEvents = readXMLfile(filePointer, datePointer); /* Gather amount of Events within dates and parse the file */

        printEvents(readingEvents); /* Print out all valid Events in the specified format */
    }
    else{

        printf("Function requires input of <starting date> <ending date> <xmlFile to parse>"); /* If invalid argument is passed, let user know of valid argument before exiting.  */
        exit(1);
    }

    exit(0);
}

/**
 * @brief Function: readXMLfiles
 * 
 *        Description: Reads the file passed in as an argument and parses the xml information. Additionally, determines if the
 *                     Event is within the date argument specified when running the program and adds it the the Event struct array. 
 * 
 * @param filename - name of file, specififed in terminal when first running the program.
 * @param startEndDates - start and end dates specififed in terminal.
 * @return int - the number of valid dates within the start and end dates. This integer will be used in the printEvents function later.
 */

int readXMLfile(char *filename, int* startEndDates){

    // Reading a file help from https://stackoverflow.com/questions/39568121/using-scanf-to-read-a-text-in-c-programming
    // qsort help from https://stackoverflow.com/questions/11524857/built-in-functions-for-sorting-arrays-in-c
    // qsort help from https://www.youtube.com/watch?v=1enPr_9_lAE&ab_channel=ProgrammingwithSikander
    // mktime help from https://www.youtube.com/watch?v=ayChPtGWcTA&ab_channel=LearningLad
    
    FILE* file = fopen(filename, "r");
    /* If file is null, we return an error message and a 0 int to stop the file.*/
    if(file == NULL){  
        printf("%s", "File is null.");
        return 0;
    }

    char singleLine[MAX_LINE_LEN]; /* initialize singleLine to hold one line in the xml file */

    int readingEvents = 0; /* initialize the number of readingEvents in the file */

    Event currentEvent; /* create Event struct to store xml values of events. */
    
    while(fgets(singleLine, MAX_LINE_LEN, file) != NULL){


        /* Parse the contents of the description tag from the xml file and store it in the Event struct */
        if(strncmp(singleLine, "        <description>", 21) == 0){

            sscanf(singleLine, "        <description>%[^/]", currentEvent.description);
            currentEvent.description[strlen(currentEvent.description) -1] = '\0';
            
        }

        /* Parse the contents of the timzezone tag from the xml file and store it in the corresponding Event struct */
        if(strncmp(singleLine, "        <timezone>", 18) == 0){

            sscanf(singleLine, "        <timezone>%[^/]", currentEvent.timezone);
            currentEvent.timezone[strlen(currentEvent.timezone) -1] = '\0';
            
        }
        /* Parse the contents of the location tag from the xml file and store it in the corresponding Event struct */
        if(strncmp(singleLine, "        <location>", 18) == 0){

            sscanf(singleLine, "        <location>%[^/]", currentEvent.location);
            currentEvent.location[strlen(currentEvent.location) -1] = '\0';
            
        }
        
        /* Parse the contents of the day, month and year tags from the xml file and store it in the corresponding Event structs */
        sscanf(singleLine, "        <day>%i</day>", &currentEvent.day);

        sscanf(singleLine, "        <month>%i</month>", &currentEvent.month);

        sscanf(singleLine, "        <year>%i</year>", &currentEvent.year);

        /* Parse the contents of the dweek tag from the xml file and store it in the Event struct */
        if(strncmp(singleLine, "        <dweek>", 15) == 0){

            sscanf(singleLine, "        <dweek>%[^/]", currentEvent.dweek);
            currentEvent.dweek[strlen(currentEvent.dweek) -1] = '\0';
            
        }
        /* Parse the contents of the start tag from the xml file and store it in the Event struct */
        if(strncmp(singleLine, "        <start>", 15) == 0){

            sscanf(singleLine, "        <start>%[^/]", currentEvent.startTime);
            currentEvent.startTime[strlen(currentEvent.startTime) -1] = '\0';
            
        }
        /* Parse the contents of the end tag from the xml file and store it in the Event struct */
        if(strncmp(singleLine, "        <end>", 13) == 0){

            sscanf(singleLine, "        <end>%[^/]", currentEvent.endTime);
            currentEvent.endTime[strlen(currentEvent.endTime) -1] = '\0';
            
        }

        /* Create Date structs to determine if the currentEvent is within the range of start and end dates. */
        Date currentDate = {currentEvent.year, currentEvent.month, currentEvent.day};

        Date startDate = {startEndDates[0], startEndDates[1], startEndDates[2]};

        Date endDate = {startEndDates[3], startEndDates[4], startEndDates[5]};

        /* If we reach the </event> tag we know this is the end of the event. We know compare event with start and end times to determine if it is valid.  */
        if(strncmp(singleLine, "    </event>", 12) == 0){

            /* Create time structs from dates to calculate the differences. Date structs provide more concise and separate information than Event struct for comaprison. */
            time_t startTime = createTimeStructDates(&startDate);

            time_t endTime = createTimeStructDates(&endDate);

            time_t currentTime = createTimeStructDates(&currentDate);

            /* Determine the difference in seconds between the current, start and end times. */
            int seconds1 = difftime(currentTime, startTime);
            int seconds2 = difftime(currentTime, endTime);

            /* If the current Event is within the start and end range, store Event in totalEvents, the array of Event structs */
            if(seconds1 >= 0 && seconds2 <= 0){

                totalEvents[readingEvents] = currentEvent;
                readingEvents++; /* increment readingEvents count to store the amount of valid Events */

            }
            
        }

    }

    /* QuickSort the array of Events based on the compareEvents function. Sorts the array by earliest to latestes events withing start and end dates. */
    qsort(totalEvents, readingEvents, sizeof(Event), compareEvents);

    /* Close file and return readingEvents for further processing. */
    fclose(file);

    return readingEvents;
}


/**
 * @brief Function: compareEvents
 * 
 *        Description: Compares two events at a time, using the createTimeStructEvent function to be used by qsort for accurate sorting.
 * 
 * @param Event1 
 * @param Event2 
 * @return int - returns difference of seconds between events.
 */

int compareEvents(const void *Event1, const void *Event2){

    // compareEvents help from https://www.youtube.com/watch?v=1enPr_9_lAE&ab_channel=ProgrammingwithSikander

    time_t startTime = createTimeStructEvent(Event1);
    time_t endTime = createTimeStructEvent(Event2);
    
    double seconds = difftime(startTime, endTime);

    return seconds;
}
/**
 * @brief Function: printEvents
 *        
 *        Description: Prints Events to the console. Event array is already sorted, prints to desired stdout, with events of the same date printed together.
 * 
 * @param readingEvents - the amount of events in the array.
 */

void printEvents(int readingEvents){
    
    Event currentEvent; /* Initialize currentEvent instead of stating totalEvents[i] for further clarification and readability. */

    char day[3]; /* Initialize day character string to hold Event day value and not use currentEvent.day for better readaiblity */
    char year[5]; /* Initialize year character string to hold Event year and not use currentEvent.year for better readability */
    int dashCount = 0; /* Initialize dashCount to track amount of dashes to print to console */

    /* Loop through array Event to access each Event structure. */
    for(int i = 0; i<readingEvents; i++){

        dashCount = 0;
        
        char months[12][10] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}; /* Create months 2-D character array in order to switch Event numeric month to alphabet month. */

        currentEvent = totalEvents[i]; /*Initialize currentEvent for better readability */
        

        sprintf(day, "%.2d", currentEvent.day); /* sprintf to place struct day value in day character array */
        sprintf(year, "%.2d", currentEvent.year); /* sprintf to place struct year value in year character array */

        dashCount += strlen(months[currentEvent.month-1])+1; /* Increment dashCount including space */
        dashCount += strlen(day)+2; /* increment dashcount including ',' character and space */
        dashCount += strlen(year)+1; /* increment dashCount including space */
        dashCount += strlen(currentEvent.dweek)+2; /* Increment dash count including '(' and ')' */

        /* If not first Event, determine if Event is on same date as previous Event. If the case, print together separated by new line. */
        if(i!=0){

            if(currentEvent.year == totalEvents[i-1].year){

                if(currentEvent.month == totalEvents[i-1].month){

                    if(currentEvent.day == totalEvents[i-1].day){
                        
                        /* Convert 24-hour start and end time to 12-hour AM-PM format with the convertTime function, which additionally prints the time string. */
                        convertTime(currentEvent.startTime);
                        printf("%s", " to ");
                        convertTime(currentEvent.endTime);

                        /* if last Event do not print new line */
                        if(i+1 == readingEvents){
                            printf(": %s {{%s}} | %s", currentEvent.description, currentEvent.location, currentEvent.timezone);
                            continue;
                        }else{
                            printf(": %s {{%s}} | %s\n", currentEvent.description, currentEvent.location, currentEvent.timezone);
                            continue; 
                        }   
                       

                    }
                    else{
                        printf("\n");
                    }

                }
                else{
                    printf("\n");
                }
            }
        }

        printf("%s %s, %s (%s)\n", months[currentEvent.month-1], day, year, totalEvents[i].dweek);

        /* Loop to print out amount of dashes, if at last dash, we print a dash and a newline, then break out of loop. */
        for(int i = 0; i<dashCount; i++){

            if(i+1 == dashCount){

                printf("%s\n", "-");
                break;  
            }
            
            printf("%s", "-");
        }           

        /* Convert 24-hour start and end time to 12-hour AM-PM times with the convertTime function, which also prints the time. */
        convertTime(currentEvent.startTime);
        printf("%s", " to ");
        convertTime(currentEvent.endTime);

         /* If last Event, do not print new line */
        if(i+1 == readingEvents){
            printf(": %s {{%s}} | %s", currentEvent.description, currentEvent.location, currentEvent.timezone);
        }else{
            printf(": %s {{%s}} | %s\n", currentEvent.description, currentEvent.location, currentEvent.timezone); 
        }                
    }
}


/**
 * @brief Function: convertTime
 *        
 *        Description: Converts a 24 hour time string into a 12 hour time string and prints the adjustment. This code was heavily sourced from the online resource, where citation is placed at the start of the function.
 * 
 * @param str - the 24-hour time string taken from parsing file.
 */
void convertTime(char* str){

    /* Code resourced from https://www.javatpoint.com/c-program-to-convert-24-hour-time-to-12-hour-time */

    /* Get hours portion of string. */
    int hour1 = (int)str[0] - '0';
    int hour2 = (int)str[1] - '0';

    int hours = hour1 * 10 + hour2; /* Add hours together after splitting different positions. */


    char format[2]; /*Initialize format char array to hold 'AM' or 'PM' strings */

    if(hours < 12){
        format[0] = 'A';
        format[1] = 'M';
    }
    else{
        format[0] = 'P';
        format[1] = 'M';
    }

    hours %=12; /* Mod hours by 12 to adjust any hour values greater than 12 */

    /* If hour is the 12th hour, convert to 00 as per custom in AM PM time format. */
    if(hours == 0){
        printf("12:");

    /* Print minutes. */
        for(int i = 3; i<5; i++){
            printf("%c", str[i]);
        }

    }
    else{

        printf("%.2d:", hours); /* print hours in 2 significant digits to obtain 01 instead of 1 for example. */

        for(int i = 3; i<5; i++){
            printf("%c", str[i]);
        }
    }
    /* Print AM or PM */
    printf(" %c%c", format[0], format[1]);

}
/**
 * @brief Function: createTimeStructEvent
 * 
 *        Description: Create a Time Struct from an Event. Used in order to compare events easily in qsort.
 *                     Each event is more easily sorted as a time struct.
 * 
 * @param Event - Event to be sorted
 * @return time_t - time struct of Event
 */
time_t createTimeStructEvent(const void *Event){

    const struct Event *eventPointer1 = Event; /* Create pointer to event */

    char hour[3]; /* initialize variable to hold the hour of event */
    char min[3]; /* initialize variable to hold the minute of event */

    /* Gather hour string and put into hour character array */
    hour[0] = eventPointer1->startTime[0];
    hour[1] = eventPointer1->startTime[1];
    hour[2] = '\0';

    /* Gather minute string and put into min character array */
    min[0] = eventPointer1->startTime[3];
    min[1] = eventPointer1->startTime[4];
    min[2] = '\0';

    struct tm oldTime;
    time_t newTime;

    oldTime.tm_year = eventPointer1->year-1900;
    oldTime.tm_mon = eventPointer1->month;
    oldTime.tm_mday = eventPointer1->day;

    oldTime.tm_hour = atoi(hour); /* Convert hour in integer for eaasy comparison. */
    oldTime.tm_min = atoi(min);  /* convert minute to integer for easy comparison. */
    oldTime.tm_sec = 0;
    oldTime.tm_isdst = 0;

    newTime = mktime(&oldTime);

    return newTime; /* return new time struct version of Event struct */

}
/**
 * @brief Function: createTimeStructDates
 * 
 *        Description: Create a time struct from a Date struct. Date struct is used in order to compare start, current and end dates.
 *                     A time struct version more easily determines if a currentEvent is within the date range. 
 * 
 * @param Date - Date struct passed in.
 * @return time_t - time struct that is returned for comparison.
 */

time_t createTimeStructDates(struct Date *Date){

    struct tm start;
    time_t startTime;

    start.tm_year = Date->year-1900;
    start.tm_mon = Date->month;
    start.tm_mday = Date->day;

    start.tm_hour = 0;
    start.tm_min = 0;
    start.tm_sec = 0;
    start.tm_isdst = 0;

    startTime = mktime(&start);

    return startTime; /* return new time struct of Date struct */
}

