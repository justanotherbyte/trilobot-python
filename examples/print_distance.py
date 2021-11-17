import time
from trilobot import Trilobot


if __name__ == '__main__':
    tb = Trilobot()
    
    while not tb.read_button(tb.BUTTON_A):

        #Take 10 measurements rapidly
        for i in range(10):
            clockcheck = time.perf_counter()
            distance = tb.read_distance(timeout=25, samples=3)
            print("Rapid:  Distance is {:.1f} cm (took {:.4f} sec)".format(distance,(time.perf_counter() - clockcheck) ) )
            time.sleep(0.01)

        #Take 10 measurements allowing longer time for measuring greater distances
        for i in range(10):
            clockcheck = time.perf_counter()
            distance = tb.read_distance(timeout=200, samples=9)
            print("Slower: Distance is {:.1f} cm (took {:.4f} sec)".format(distance,(time.perf_counter() - clockcheck) ) )
            time.sleep(0.01)

