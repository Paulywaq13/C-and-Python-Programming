#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_LINE_LEN 200
#define MAX_EVENTS 1000

/*
    Function: main
    Description: represents the entry point of the program.
    Inputs: 
        - argc: indicates the number of arguments to be passed to the program.
        - argv: an array of strings containing the arguments passed to the program.
    Output: an integer describing the result of the execution of the program:
        - 0: Successful execution.
        - 1: Erroneous execution.
*/
struct Event{
    int year, month, day, time;
    char description[50];

};

int main(int argc, char *argv[])
{   
    /* Starting calling your own code from this point. */
    // Ideally, please try to decompose your solution into multiple functions that are called from a concise main() function.
    if(argc > 2){
        // do something
        char* startDate = argv[1];
        char* endDate = argv[2];
        //char* xml = argv[3];
        //char text[100];

        //scan startDate
        
        int start_year, start_month, start_day;
        int end_year, end_month, end_day;
        
        //getline(startDate);
       
        sscanf(startDate, "--start=%d/%d/%d", &start_year, &start_month, &start_day);
        sscanf(endDate, "--end=%d/%d/%d", &end_year, &end_month, &end_day);

        printf("%d %d %d\n", start_year, start_month, start_day);
        printf("%d %d %d\n", end_year, end_month, end_day);
        
        // get xml data
        
        FILE* fPointer;
        fPointer = fopen("aston-martin-release.xml", "r");
        char singleLine[150];
        //char description[50];
        char *sp;
        //char d[100];

        while(!feof(fPointer)){

            fgets(singleLine, 150, fPointer);

            sp = strtok(singleLine, "<");
            sp = strtok(NULL, "</");
            
            //printf("%s\n", sp);
            printf("%s", singleLine);
            //strcpy(d, sp);
            /*
            char *portion2 = strtok(sp, d);
            printf("%s\n", portion2); 
            */
        
                       
            //int result = strcmp(singleLine, "        <description>Aston Martin F1 2022 Car Release</description>");
            //sscanf(sp, "description>%s", description);
            //printf("%s\n", description);
            //puts(singleLine);
        }
        

        fclose(fPointer);

    }
    else{
        printf("Start this assignment early my g\n");
    }


    exit(0);
}






