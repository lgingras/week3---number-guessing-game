# template for "Stopwatch: The Game"
import simplegui
import time

# define global variables

position = [100, 150]
t = 0
ms = 0
#ss = str(0)
times_stopped = 0
stopped_whole = 0
stopwatch_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global formatted_time, ms

    # determine milliseconds
    ms = t
    ms = str(ms)
    ms = ms[-1:]
#    print "ms = ", ms
   
    t = t / 10
    
    # determine minutes
    if t < 60:
        mm = 0
    elif t >= 60:
        mm = (t / 60)
    else:
        print "determining mm failed"        
#    print "mm = ", mm

    #determine seconds
    ss = t % 60
#    print "ss = ", ss

    
    # convert into strings 
    mm = str(mm)
    ss = str(ss)

    # add leading 0s if needed
    if len(mm) == 1:
        mm = "0" + mm
    if len(ss) == 1:
        ss = "0" + ss

    # return a formatted time
    return (mm + ":" + ss + "." + ms)

# define event handlers for buttons; "Start", "Stop", "Reset"
def startbutton():
    global stopwatch_running
    timer.start()
    stopwatch_running = True
    print "startbutton stopwatch_running val: ", stopwatch_running

def stopbutton():
    global times_stopped, ms, stopped_whole, stopwatch_running
    if stopwatch_running == True:
        times_stopped = times_stopped + 1
        print "times_stopped = ", times_stopped   
    timer.stop()
    stopwatch_running = False
    
    if ms == "0":
        stopped_whole = stopped_whole + 1
    print "stopped_whole: ", stopped_whole
    print "stopbutton stopwatch_running val: ", stopwatch_running    
     
    
def resetbutton():
    global t, times_stopped, stopped_whole
    t = 0
    times_stopped = 0
    stopped_whole = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t = t + 1

# define draw handler
def draw(canvas):
    global t
    canvas.draw_text(format(t), position, 30, "White")
    canvas.draw_text(str(stopped_whole), (200,50), 20, "Red")
    canvas.draw_text(" / ", (225, 50), 20, "Red")
    canvas.draw_text(str(times_stopped), (250,50), 20, "Red")


# create frame
frame = simplegui.create_frame("canvas", 300, 300)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", startbutton) 
frame.add_button("Stop", stopbutton) 
frame.add_button("Reset", resetbutton) 
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
#timer.start()

# Please remember to review the grading rubric