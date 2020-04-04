from pygame import mixer
import time

def currenttime():
    ctime = time.asctime(time.localtime(time.time()))  # Local time
    return ctime

def musicplay(file_name , stopper):
    """ starts playing music after a regular interval """
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.stop()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()      # stops music when string is entered
            break

def logs(msg):
    """ Function will log the activity is the user in a file with a timestamp """
    f = open("log.txt" , "a")
    f.write(f"{msg} {currenttime}\n")

if __name__ == '__main__':
    ctime = currenttime()    # Store the current time
    init_water = time()      # initialize water drinking time
    init_eyes = time()       # initialize eye relaxation time
    init_exercise = time()   # initialize exercise time
    watertime =  10         # Interval for water activity
    eyestime = 20           # Interval for eye relaxation
    exercisetime = 30      # Interval for exercise
    while True:
        if time() - init_water > watertime:
            print("Time to drink water. Enter (d) to stop the alarm")
            musicplay("water.mp3" , "d")
            init_water = time()      # Re - initialize water time
            logs("Drank water at time : ")
            
        if time() - init_eyes > watertime:
            print("Time to relax your eyes. Enter (e) to stop the alarm")
            musicplay("eyes.mp3" , "e")
            init_eyes = time()      # Re - initialize eyes relaxation time
            logs("Relaxed eyes at time : ")
            
        if time() - init_exercise > exercisetime:
            print("Time to do exercise, Enter (x) to stop the alarm")
            musicplay("exercise.mp3" , "x")
            init_exercise = time()  # Re - initialise exercise time
            logs("exercised at time : ")
