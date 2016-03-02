# Musync

Sync Music from iTunes to Android

###What does this program do ?
Let me put this it this way, say you have a huge  music library which is well organized by some other application say iTunes, if you
have not updated your phone in a while then to copy those new songs, you either copy-paste it from your download folder amid other songs (very carefully pick the new ones) or you go to the recently added playlist on iTunes and see the list of the new songs and copy each one individually, I understand it can be a big problem if you running short of time. 


###PUSHES ONLY THE NEW SONGS FROM YOUR EXISTING MUSIC LIBRARY TO YOUR ANDROID DEVICE
this is what this program does 

###How to run it ?

 Prerequisite installation/requirements

 1. Android Stand-alone SDK Tools only link <a href="http://developer.android.com/sdk/installing/index.html">here</a>
 2. Python v.3.X
 3. Make Utility
 4. Linux/Unix based environment to support shell scripts


 After you installed 1. Android Stand-alone SDK Tools place it you Documents folder, make sure to set the adb path, this is how it's done
 ```
 1. Open Your Terminal

 2. cd ~/
 3. vim .bash_profile
 paste this with your user name in place inside .bash_profile
 -> export PATH=$PATH:/Users/"__Your__user__name"/Documents/android-sdk-macosx/platform-tools 
 4. Save the profile and restart it.

 ```

 Try running 'adb' command in your , you should see adb running.
 Run 'adb devices' to see the list of connected devices.

 If you've reached till here, then it's a cakewalk from here.
 1. Download the repository and unzip it.
 2. In terminal, navigate to the unzipped folder.
 3. Then log your existing music library by using with your username
 ```
 in the terminal, inside the musync folder hit:

 python3 _1_music_log_generator_.py  __YOUR__USER__NAME
 ```
 4. Once the log is saved, now all you have to do is run the make command
 but before that provide the arguments to the files in the make file.
 ```
 Open make file and make the following changes:
 
 python3 _2_push_diffreneces_to_shell_.py __YOUR__USER__NAME DESTINATION_TO_COPY

 save the file and close it.
 ```	
 Caution
 ```
 DESTINATION_TO_COPY ->storage/sdcard1 
 					 ->storage/sdcard0
 					 ->storage/9016-4EF (this was mine ... can be used by USING ESPLORER)
 					 or whatever the is name of your sdcard.
 ```
 5. When even-ever you feel to copy the new songs in your library, all you gotta do is
 navigate to the musync solder in the terminal
 ```
 just hit:

 make
 ```
 That's it folks. Fork it!




