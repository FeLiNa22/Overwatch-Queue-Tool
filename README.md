# Overwatch-Queue-Tool

Overwatch queue's are extremely long and no-one can be bothered to wait at their computer for 20 minutes, and if you get up to make a cup of coffee you usually come back to realise they have been kicked out of the game and have just lost 50 SR :(

To solve this problem I have created a notification engine whiich essentially monitors your overwatch queue for you, whilst you go fix yourself a cup of joe.
When you enter a game, the program sends you an email, and you can head back to your PC to get that W. 

## HOW IT WORKS

The program works by using text recognition through tesseract and opencv.
It constantly checks the top of your overwatch screen to determine whether you are in a queue.
Once the queue ends an email is sent to your specified account.  

## HOW TO USE

1.) First clone the repository
        
    git clone https://github.com/FeLiNa22/Overwatch-Queue-Tool.git

2.) Then go into the master directory and double click the .exe application

3.) Set your email address (please use a valid one)

4.) Open Overwatch and then click the start button

5.) Tab onto the overwatch screen and then go on with your day
    when the queue ends,  you will be sent an email :)

###### IMPORTANT
  *Make sure the window for overwatch is the top window (the one your tabbed onto)*

