# resources

## project inspiration
https://github.com/bradtraversy/alexis_speech_assistant

## simulating keypress 
https://nitratine.net/blog/post/simulate-keypresses-in-python/

## reference to using selenium
https://stackoverflow.com/questions/34504506/python-how-to-click-a-button-in-a-web-page-using-python


## cromedriver for selenium
https://sites.google.com/a/chromium.org/chromedriver/downloads

## pynput commands
https://pythonhosted.org/pynput/keyboard.html
https://buildmedia.readthedocs.org/media/pdf/pynput/latest/pynput.pdf


# required initial libraries and driver.


## path for selenium chrome driver(https://sites.google.com/a/chromium.org/chromedriver/downloads)
unzip and save it to known location
This was my directory("/Users/matthewpark/Documents/cs50project")


to run python code in vertual environment.(I could not use this part)
"source venv/bin/activate"


## google text to speech 
type in terminal following
"pip install gTTs"

## library to play audio back. 
(I believe this was required to install and use pyaudio)
PyObjC has appkit for playsound

"pip install playsound"
"pip install PyObjC"

## library for pyaudio

"brew install portaudio"
"pip install pyaudio"


## library for simulating keyboard using pynput

pip install pynput

## library for selenium

pip install selenium



# speech.py voice command

(this is home. Say this terms to navigate functions in speech.py)

>search(google search, say your search term here)
>>    yes
>>>        go(up, down, back)
>>>            = this command will scroll up, down, and go back in history
>>>        new search
>>>            = search new terms in the existing search bar
>>>        append
>>>            = append text to existing term(s) in the searh bar
>>>        next
>>>            = allows you to toggle links and other elements in the existing search result
>>>        enter
>>>            = simulate enter. Usee "next" command to highlight the link you would like to click and say enter.
>>>        done
>>>            = exit "search" command and back to home 
>>    no
>>        = exit "search" command and back to home
>    
>lookup article (pubmed search, say your search term here)
>>    yes
>>>        browse
>>>>            go(up, down, back)
>>>>                = this command will scroll up, down, and go back in history
>>>>            new search
>>>>                = search new terms in the existing search bar
>>>>            append
>>>>                = append text to existing term(s) in the searh bar
>>>>            next
>>>>                = allows you to toggle links and other elements in the existing search result
>>>>            done
>>>>                = exit "search" command and back to home
>
>>>        select
>>>>            article
>>>>                = can click specific article in reference to the article number order shown
>>>>            button
>>>>>                filter
>>>>>                    = only works on smaller aspect ratio, this will pull up the filter bar
>>>>>>                   next
>>>>>>                        = use next to highlight the checkbox for filter option
>>>>>>                    enter
>>>>>>                        = use enter to select filter option
>>>>>                full text
>>>>>                    = this function only works once you used article command to open up the specific article. this command will open up the original source of the paper.
>>>>>                done
>>>>>                    = this will exit filter and full text choice -> command: button and article
>>>>            done
>>>>                = this will exit button and article choice -> command: select and browse
>>>        done
>>>            = this will exit select and browse choice -> command: yes and no
>>    no
>>        =this will exit look up article choice and back to home command.
>
>change(tab)
>    = toggle btween existing tabs
>go(down, up, back) 
>    = scrolls up, down, and go back in history
>close
>    = close a tab
>quit
>    = quit browser
>wait
>    = sleeps for the amount of second specified by you. Say integer numer of second you would like the program to sleep(doesn't work for number like 100, because it recognizes as a 'hundred' rather then 100)
>>    yes
>>        = can specify additional time to sleep
>>    no
>>        = exit wait.



# video link

long version
https://youtu.be/91WU7981NHA

short version
https://youtu.be/T2MTJogdVyU# 
