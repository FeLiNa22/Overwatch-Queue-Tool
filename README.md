# Overwatch-Queue-Tool

Overwatch queue's are extremely long and no-one can be bothered to wait at their computer for 20 minutes, and if you get up to make a cup of coffee you usually come back to realise you've just been kicked out of the game and have lost 50 SR :(

To solve this problem I have created a notification engine whiich essentially monitors your overwatch queue whilst you go fix yourself a cup of joe.
When you enter a game and your queue ends the program sends you an email, and you can head back to your PC to get that W. 

## HOW IT WORKS

The program works by using text recognition through tesseract and opencv.
It constantly checks the top of your overwatch screen to determine whether you are in a queue.
Once the queue ends an email is sent to your specified account.  

## HOW TO USE

1.) First clone the repository
        
    git clone https://github.com/FeLiNa22/Overwatch-Queue-Tool.git

2.) Then go into the master directory and double click the .exe application

3.) Set your email address (please use a valid one)

4.) Open Overwatch, click the start button and then start a queue. **(NOTE - This program works best when Overwatch is in Borderless Windowed mode)**

5.) Stay tabbed on the overwatch screen and then go on with your day
    when the queue ends you will be sent an email :)

###### IMPORTANT
*Make sure the window for overwatch is the top window (the one your tabbed onto)*

###### Security
*This application does not send any information outbound, all we require is your email address and this data stays on your computer in a "default.dat" file. We do not require any sign up, or for you to send any personal information. This app gives you total control. Don't belive me - Check out the source code [here](https://github.com/FeLiNa22/Overwatch-Queue-Tool-Open-Source)*
