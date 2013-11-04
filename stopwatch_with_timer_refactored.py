# template for "Stopwatch: The Game"
import simplegui
import time

# define global variables
tick = 0
tries = 0
wins = 0
ms = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(tick):
    global ms
    ms = tick % 10
    seconds = tick % 600 / 10
    minutes = tick / 600

    if seconds < 10:
        seconds = "0" + str(seconds)

    return str(minutes) + ":" + str(seconds) + "." + str(ms)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopwatch_running
    timer.start()

def stop():
    global stopwatch_running, tries, wins
    if timer.is_running():
        tries = tries + 1
    timer.stop()
    
    if ms % 10 == 0:
        wins += 1
    
def reset():
    global tick, tries, wins
    tick = 0
    tries = 0
    wins = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tick
    tick += 1

# define draw handler
def draw(canvas):
    global tick
    canvas.draw_text(format(tick), (100, 150), 30, "White")
    canvas.draw_text(str(wins) + " / " + str(tries), (200,50), 20, "Red")

# create frame
frame = simplegui.create_frame("canvas", 300, 300)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start) 
frame.add_button("Stop", stop) 
frame.add_button("Reset", reset) 
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()


# Please remember to review the grading rubric