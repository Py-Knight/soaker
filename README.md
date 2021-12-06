# soaker
A simple web app to calculate the finish time of an industrial furnace process.

I created this app to make life easier for myself and fellow Operatives in a previous role, working within the Aerospace sector.

I frequently needed to know what time a furnace run would end (the soak end time).
The whole process is called SOAKING. After the metal is heated to the required temperature, it is held at that temperature until the desired internal structural changes take place.
The length of time held at the required temperature is called the SOAKING PERIOD.
The soaking period depends on the chemical analysis of the metal and the mass of the part.

Soaker, is a basic time calculator. It takes the SOAK start time, adds a predefined SOAKING PERIOD (in minutes) and returns the time at which the process will finish.
It is at this point when the furnace needs to be manually advanced, to begin the cool down phase of the process. 
