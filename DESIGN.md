how you implemented your project and why you made the design decisions you did. Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

Reasoning for my programming design decition.

I got the idea for this project from the demo shown from the in-class lecture previously. Although My project runs in the terminal and does not have an actual "design" aspect in terms of graphics, I decided to structure commands like the typical file system, where specific commands are nested within each other. I decided to take this approach because I realized that the string search function is not an instantaneous process, and takes time to process. 

To overcome this issue, I decided to nest commands within subcategories to minimize the string search for each voice command as much as possible. In my code, specific commands repeat within different levels. I initially did not want to take this approach as it will slow down my program. However, I realized that the ease of use for this program is additionally essential. Thus, I decided to allow the user access to these functions at different levels and figure out an alternative way to speed up my program. 

I have not implemented the faster string search methods yet. I plan to do more research and eventually adapt the most efficient string search method I can find to make this program more useable. I am planning to create more keyboard shortcut functions and potentially mouse implementation also. I did use selenium to simulate clicks for buttons; however, I would like to provide more functionalities to make the user experience as smooth as possible.

One additional approch I might look into is the eye movemnt tracking software. With this implimentation and a decent camera, users will be able to use their eye movement to type, scroll, and click without using a voice. I am thinking of combining this two method to create complete keyboard and mouse replacement tools wheere it is not solely focused on web browsing.

The primary reason why I decided to tackle this project was due to the lack of accessibility for those who can not use the keyboard and mouse. Especially when it comes to research, I do not know of any tools available to make research more accessible. Although there might be very few individuals with these problems, I believe that this tool will be highly impactful for those who truly need it.
