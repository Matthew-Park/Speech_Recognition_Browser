import speech_recognition as sr
import pyaudio
from time import ctime
import webbrowser
import time
import os 
import playsound
import random
from gtts import gTTS
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException





PATH = "/Users/matthewpark/Documents/cs50project/chromedriver"

#ignoring security errors
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(PATH, options=options)

#emulating keyboard.
keyboard = Controller()

#speech recognition library function
r = sr.Recognizer()

#taking in microphone input and converting to string using google speech processing
def audio_input(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('sorry, I did not get that.')
        except sr.RequestError:
            speak('Check your internet connection')
        return voice_data

def respond(voice_data):

    #When search command is used, this counter determines if there is a tab open already and opens a new tab on new search.
    counter = False
    counter_article = False

    #available command options
    print("Options: search, lookup article,change(tab),go(down, up, back) close, quit, wait")

    #search command
    if 'search' in voice_data:

        #checking if the counter is true or false to determine open new tab or not.
        if counter == True:
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
            search = audio_input('What do you want to search for?')
            url = 'https://google.com/search?q=' + search
            # webbrowser.get().open(url)
            driver.get(url)
            speak("Here's what I found for " + search)

        else:
            search = audio_input('What do you want to search for?')
            url = 'https://google.com/search?q=' + search
            # webbrowser.get().open(url)
            driver.get(url)
            speak("Here's what I found for " + search)
            counter = True

        #Option for further assistance
        print('option: yes, no')
        search_continue = audio_input("Is there anythin else I can do?")

        #yes command options.
        if 'yes' in search_continue:
            ## for tabbing to go to next links in google, i need to first tab 17 times
            for i in range(17):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)

            speak('what can i do?')

            # available command within search/yes
            print("commands: go(up, down, back), new search, append, next, enter, done")

            #Loop to continuously listen for proper command.
            while True:
                search_continue2 = audio_input()


                #go up,go down command will scroll up and down. go back command will relode previous page.
                if 'go' in search_continue2:
                    ##move page down
                    if 'down' in search_continue2:
                        speak('scrolling down')
                        scroll_down()
                    ## move page up
                    elif 'up' in search_continue2:
                        speak('scrolling up')
                        scroll_up()
                    ## go back in history
                    elif 'back' in search_continue2:
                        speak('going back')
                        go_back()

                #new search will find element name q within the html code of google webbsite and insert in new search term
                elif 'new search' in search_continue2:
                    current = driver.current_url
                    if 'google' in current:
                        search_again = audio_input('what would you like to search?')
                        search = driver.find_element_by_name('q')
                        search.clear()
                        search.send_keys(search_again)
                        search.send_keys(Keys.RETURN) 
                        print("commands: go(up, down), new search, append, back, next, done")
                    else:
                        speak("Sorry, you can only continue searching from google. Say search to open a new google search tab")
                        speak("what can I do?")
                        print("commands: go(up, down), new search, append, back, next, done")
                        break
                
                # append will append to the previously existing search within the search bar
                elif 'append' in search_continue2:
                    current = driver.current_url
                    if 'google' in current:
                        search_again = ''
                        speak('what would you like to search?')
                        while len(search_again) < 0:
                            search_again = audio_input()
                        
                        search = driver.find_element_by_name('q')
                        search.send_keys(Keys.SPACE)
                        search.send_keys(search_again)
                        search.send_keys(Keys.RETURN)
                        print("commands: go(up, down), new search, append, back, next, done")
                
                # next will tab through next element within html code
                elif 'next' in search_continue2:
                    speak('next')
                    move_next()

                #enter will simulate enter key.
                elif 'enter' in search_continue2 or 'click' in search_continue2:
                    speak('enter')
                    enter()

                # done will exit the search/yes loop and go back to base "directory"
                elif 'done' in search_continue2:
                    speak("browsing command finished")
                    speak("How can I help you")
                    print("Options: search, lookup article,change(tab),go(down, up, back) close, quit, wait")
                    break
        
        # no will continue your base command.
        elif 'no' in search_continue:
            speak('okay')
            speak("How can I help you")
            print("Options: search, lookup article, close, quit, wait")

        # in case someone says a wrong command...
        else:
            speak("Sorry, i did not get that. How can I help you")
            print("Options: search, lookup article, close, quit, wait")


    # loop up article will search articles in pubmed website.
    elif 'look up article' in voice_data:

        #same as before, checking if this function has been run already/ tab already open. 
        if counter_article == True:
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
            search = ''
            search = audio_input('What article do you want to search for?')
            url = 'https://pubmed.ncbi.nlm.nih.gov/?term=' + search
            # webbrowser.get().open(url)
            driver.get(url)
            speak("Here's what I found for " + search)

        else:
            search = audio_input('What article do you want to search for?')
            url = 'https://pubmed.ncbi.nlm.nih.gov/?term=' + search
            # webbrowser.get().open(url)
            driver.get(url)
            speak("Here's what I found for " + search)
            counter_article = True

        # same as before, yes and no command for further voice command.
        print("Options: yes, no")
        speak("Is there anything else I can do for you?")
        
        #Loop to continuously listen for proper input
        while True:
            search_continue = ''
            search_continue = audio_input()
            if 'yes' in search_continue:
                speak('what should i do?')
                print("Browsing commands(say 'browse' to start): go(up, down, back), new search, append , back, next, done")
                print("Select commands(say 'select'to start): article, button")
                print('Say done to stop browseing or selecting')
                while True:
                    command = audio_input()

                    # browse command simulate browsing wihtin this page
                    if 'browse' in command:
                        speak("say your command")
                        print("commands: go(up, down), new search, append, next,change, done")
                        while True:
                            browse_command = audio_input()
                            if 'go' in browse_command:
                                ##move page down
                                if 'down' in browse_command:
                                    speak('down')
                                    scroll_down()
                                ## move page up
                                elif 'up' in browse_command:
                                    speak('up')
                                    scroll_up()
                                ## go back in history
                                elif 'back' in browse_command:
                                    go_back()
                            elif 'new search' in browse_command:
                                current = driver.current_url
                                if 'pubmed' in current:             ## making sure that the current webpage is pubmed.
                                    search_again = audio_input('what would you like to search?')
                                    # speak('what would you like to search?')
                                    # while len(search_again) != 0:
                                    #     search_again = audio_input()
                                    if len(search_again) > 0:         ## making sure that the search term is not empty
                                        search = driver.find_element_by_name('term')
                                        search.click()
                                        select_all_delete()
                                        search.send_keys(search_again)
                                        search.send_keys(Keys.RETURN)
                                        print("commands: go(up, down), new search, append , back, next, done")
                                    else:
                                        speak('Sorry, your search length needs to be larger then 0.')

                                else:
                                    speak("Sorry, you can only continue searching from pubmed. Say search to open a new pubmed search tab")
                                    speak("say your command.")
                                    print("Browsing commands(say 'browse' to start): go(up, down), new search, append, back, next, done")
                                    print("Select commands(say 'select'to start): article, button")
                                    print("Say 'done' to stop browseing or selecting")
                                    break
                            
                            elif 'append' in browse_command:
                                current = driver.current_url
                                if 'pubmed' in current:
                                    search_again = audio_input('what would you like to append?')
                                    # speak('what would you like to append to your search?')
                                    # while len(search_again) < 0:
                                    #     search_again = audio_input()
                                    if len(search_again) > 0:
                                        search = driver.find_element_by_name('term')
                                        search.click()
                                        search.send_keys(Keys.SPACE)
                                        search.send_keys(search_again)
                                        search.send_keys(Keys.RETURN)
                                        print("commands: go(up, down), new search, append,back, next, done")
                                    else:
                                        speak("sorry, you can only append higher then 0 character.")
                                else:
                                    speak("Sorry, you can only continue searching from pubmed. Say search to open a new pubmed search tab")
                                    speak("say your command.")
                                    print("Browsing commands(say 'browse' to start): go(up, down), new search, append, back, next, done")
                                    print("Select commands(say 'select'to start): article, button")
                                    print("Say 'done' to stop browseing or selecting")
                                    break

                            elif 'change' in voice_data:
                                speak("next tab")
                                tab_change()

                            elif 'next' in browse_command:
                                move_next()

                            elif 'enter' in browse_command or 'click' in browse_command:
                                enter()

                            elif 'done' in browse_command:
                                speak("browsing command finished")
                                speak('what should i do?')
                                print("Browsing commands(say 'brouse' to start): go(up, down), keep searching, back, next, done")
                                print("Select commands(say 'select'to start): article, button")
                                print('Say "done" to stop browseing or selecting')
                                break
                    
                    #select command simulates clicking using voice
                    elif 'select' in command:   
                        speak("what would you like to select, button or article?")
                        print('Say ether button or article. say done if you are done making a choice')
                        while True:
                            select_command = audio_input()

                            # allows user to choose articsle number and "click" them
                            if 'article' in select_command:
                                n = audio_input('which article number?')
                                print(n)
                                try:
                                    element = driver.find_element_by_xpath('//*[@id="search-results"]/section[1]/div[1]/div/article[%s]/div[2]/div[1]/a' % n)
                                    element.click()
                                    speak('Anything else i can do?')
                                    print("Browsing commands(say 'brouse' to start): go(up, down), keep searching, back, next, done")
                                    print("Select commands(say 'select'to start): article, button")
                                    print('Say done to stop browseing or selecting')
                                    break
                                except:
                                    speak("sorry I could not find that article.")
                                    speak("How can I help?")
                                    print("Options: browse, select, done")
                                    break
                            
                            # Button refers to elements that is like a button within the website. 
                            elif 'button' in select_command:
                                while True:
                                    b = audio_input('which button?')
                                    print (b)
                                    if "filter" in b:       ## filter option only works when the screen ratio is small in pubmed. the website was designed this way.
                                        try:
                                            element = driver.find_element_by_xpath('//*[@id="search-form"]/div[2]/div/div[1]/button[1]')
                                            element.click()
                                            move_next(2)
                                            speak('Say "next" to navigate options and "enter" to select.')
                                            while True:
                                                c = audio_input()
                                                if 'next' in c:
                                                    move_next()
                                                    speak('next')
                                                if 'enter' in c:
                                                    space()
                                                    speak('enter')
                                                    speak("If you would like select button again, say the buttom command.?")
                                                    print("Command: filter, full text")
                                                    speak("If else, say done")
                                                    break
                                        except:
                                            speak('sorry, I could not click filter button')
                                            speak("what would you like to select, button or article?")
                                            print('Say ether "button" or "article". say "done" if you wish to exit select command')
                                            break
                                            
                                    # full text command allows user to redirect to the source of the article.
                                    elif "full text" in b:
                                        try:
                                            element = driver.find_element_by_xpath('//*[@id="article-page"]/aside/div/div[1]/div[1]/div/a')
                                            element.click()
                                            name = element.get_attribute("title")
                                            speak("Directing to the link %s" % name)
                                            speak('say done to exit select button.')
                                            break
                                        except NoSuchElementException:
                                            element = driver.find_element_by_xpath('//*[@id="article-page"]/aside/div/div[1]/div[1]/div/a[1]')
                                            element.click()
                                            name = element.get_attribute("title")
                                            speak("Directing to the link %s" % name)
                                            speak('say done to exit select command, else choose button or article')
                                            break
                                        except:
                                            speak('sorry, I could not find the full text')
                                            speak("what would you like to select, button or article?")
                                            speak("say done if you wish to stop selecting.")
                                            print('Say ether "button" or "article". say "done" if you wish to exit select command')
                                            break
                                    
                                    # Done exit the select options, you still need to done to choose between button and article.
                                    elif "done" in b:
                                        speak('okay')
                                        speak("what would you like to select, button or article?")
                                        speak("say 'done' if you wish to stop selecting.")
                                        print('Say ether "button" or "article". say "done" if you wish to exit select command')
                                        break
                            
                            # This done exit the select command completely. 
                            elif 'done' in select_command:
                                speak("okay. Selecting command finished.")
                                speak("How can I help")
                                print("Options: browse, select, done")
                                break
                    # this done exit the loop to choose between browse and select. still have to say no.
                    elif 'done' in command:
                        speak("okay")
                        speak('Is there anything else I can do?')
                        print("Options: yes, no")
                        break
            
            # this no will exit the look up article command completely
            elif 'no' in search_continue:
                speak('okay')
                speak('How can I help you?')
                print("Options: search, lookup article, change(tab), go(down, up, back), close, quit, wait")
                break
            
            # safely check
            else:
                speak("Sorry, i did not get that. Is there anything elsee I can do for you?")
                print("Options: yes, no")

    # Changes tab
    elif 'change' in voice_data:
        speak("next tab")
        tab_change()

    # if 'type' in voice_data:
    #     text = audio_input('what would you like to type?')
    #     typeing(text)
    #     speak('done')
    
    # navigate within page, and search history.
    elif 'go' in voice_data:
        if 'down' in voice_data:
            speak('down')
            scroll_down()
        elif 'up' in voice_data:
            speak('up')
            scroll_up()
        elif 'back' in voice_data:
            speak('back')
            go_back()

    # if 'delete' in voice_data:
    #     speak("deleting")
    #     delete()

    # closing tab
    elif 'close' in voice_data :
        speak('closing the tab')
        driver.close()
    
    # closing browser
    elif 'quit' in voice_data:
        speak('exiting browser')
        driver.quit()

    # sleep takes in voice input in second and rest for the given time. 
    elif 'wait' in voice_data or 'hold on' in voice_data:
        second = audio_input('okay, How many seconds should I wait?')
        print(second)
        try:
            second = int(second)
            time.sleep(second)
            speak('finished waiting')

            # this will continue sleep
            while 1:
                text = audio_input('Do you need more time?')
                print(text)
                if 'yes' in text:
                    second = audio_input('how many second?')
                    time.sleep(second)
                    speak('finished waiting')

                if 'no' in text:
                    speak('okay')
                    break
        
        # Safety check
        except:
            speak("Sorry, I do not recognize this number. What can I do for you?")
            pass
        
## here are all key binding functions I used or will likely use(more to come).
def select_all_delete():
    keyboard.press(Key.cmd)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.cmd)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

def space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
def move_next(value = 1):
    for i in range(value):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

def go_back():
    keyboard.press(Key.cmd_l)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    keyboard.release(Key.cmd_l)

def tab_change():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.ctrl)

def scroll_down():
    keyboard.press(Key.page_down)
    keyboard.release(Key.page_down)

def scroll_up():
    keyboard.press(Key.page_up)
    keyboard.release(Key.page_up)

def typeing(text):
    keyboard.type(voice_data)


def speak(audio):
    tts = gTTS(text=audio, lang='en')
    r = random.randint(1,99999999)
    audio_file = "audio_" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio)
    os.remove(audio_file)

def delete():
    keyboard.press(Key.delete)
    time.sleep(2)
    keyboard.release(Key.delete)


#Starting point of the program. the innitial question
time.sleep(1)
speak('How can I help you?')
print("Options: search, lookup article, change(tab), go(down, up, back), close, quit, wait")

## main loop for speech recognition.
while 1:
    voice_data = audio_input()
    print(voice_data)
    respond(voice_data)
