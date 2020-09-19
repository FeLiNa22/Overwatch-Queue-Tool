# Overwatch-Queue-Tool

Overwatch queue's are extremely long and no-one can be bothered to wait at their computer for 20 minutes, and if you get up to make a cup of coffee you usually come back to realise you've just been kicked out of the game and have lost 50 SR :(

To solve this problem I have created a notification engine whiich essentially monitors your overwatch queue whilst you go fix yourself a cup of joe.
When you enter a game and your queue ends the program sends you an email, and you can head back to your PC to get that W. 

## HOW IT WORKS

The program works by using text recognition through tesseract and opencv.
It constantly checks the top of your overwatch screen to determine whether you are in a queue.
Once the queue ends an email is sent to your specified account.  

## HOW TO USE

1.) First download the latest version of the application from here - [download now](https://github.com/FeLiNa22/Overwatch-Queue-Tool/releases/download/v1.0-alpha/Overwatch-Queue-Tool.zip)

2.) Unzip the folder wherever you would like. This will create a folder called "Overwatch-Queue-Tool". Go into this folder and double click the "Overwatch Queue Tool.exe" application (*It may take a few seconds to start up*)

3.) You will then see a GUI asking for you to set your email address (please use a valid one)

4.) Open Overwatch and start a queue. Then click the start button in the Overwatch Queue Tool application. **(NOTE - This program works best when Overwatch is in Borderless Windowed mode)**

5.) Stay tabbed on the overwatch screen and then go on with your day, when the queue ends you will be sent an email and you can happily enjoy your game :)

###### IMPORTANT

*Make sure the window for overwatch is the top window (the one your tabbed onto)*

*Do not move around any of the files within the "Overwatch-Queue-Tool" folder*

###### Security
*This application does NOT send any of your information outbound, your email address is all that is used and this data stays on your computer in a "default.dat" file. We do not require any sign up or for you to send any personal information. This app gives you total control. Don't believe me - Check out the source code [here](https://github.com/FeLiNa22/Overwatch-Queue-Tool-Open-Source/)*

## Note for developers

I have made all the source code completely open source, as I believe tools like this should not be commercialised. 
If you do want to fork this project or continue to work on it (PM me).

