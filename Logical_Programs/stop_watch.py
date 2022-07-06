import time


class StopWatch:

    def calculateTime(self):
        print("process has started")
        start_time = time.time()
        input("press Enter key to start the time ")
        print(start_time)
        end_time = time.time()
        input("press Enter key to stop the time ")
        print(end_time)
        elapsed_time = end_time - start_time
        print(elapsed_time)


obj = StopWatch()
obj.calculateTime()
