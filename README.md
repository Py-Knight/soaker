# Soaker

## A simple Web App to calculate the finish time of an industrial furnace process.

I created this app to make life easier for myself and fellow Operatives in a previous role, working within the Aerospace sector. 

I frequently needed to know what time a furnace run would end (**Soak end time**).

The **Soak start time**  is determined when the metal has been heated to the required temperature, it is held at that temperature until the desired internal structural changes take place. The length of time held at the required temperature is called the **Soaking period**.
The **Soaking period** depends on the chemical analysis of the metal and the mass of the part or parts. The whole process is called **Soaking**.

Soaker, is a basic time calculator. It takes the **Soak start time**, adds a predefined **Soaking period** (in minutes) and returns the time at which the process will finish (**Soak end time**).
It is at this point when the furnace needs to be manually advanced, on to the cool down phase of the process.  The reason for this is so that the Operator can check the log file (usually a combination of line graph's) to make sure, certain parameters are within the permitted specifications. If the specifications have not been met, then various **Standard Operating Procedures** need to be addressed. This is a crucial aspect, as the components were typically internal parts of commercial aircraft engines.

------

<p align="center">
  <img src="soaker_screenshot.png?raw=true" alt="Screenshot"/>
</p>

------

