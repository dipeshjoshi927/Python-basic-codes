#(make sure pip and pynstaller are installed/updated)

cd to directory that contains your .py file

pyinstaller ... 
                -F              (all in 1 file)
                -w              (removes terminal window)
                -i icon.ico     (adds custom icon to .exe)
                clock.py        (name of your main python file)

.exe is located in the dist folder