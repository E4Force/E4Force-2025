import utime

start_=0
end_=0
elapsed_ = 0
def start():
    global start_
    start_ = utime.time_ns()
    
def end():
    global end_
    end_ = utime.time_ns()
    
def elapsed():
    
    global start_, end_, elapsed_
    
    elapsed_ = int((end_-start_) / 1_000_000)
    
    print( elapsed_)
    return elapsed_