import argparse
import calendar
import time

time_now = calendar.timegm(time.gmtime())

parser = argparse.ArgumentParser(description='--t "<epoch time value>"')
parser.add_argument("--t", default=time_now, help="'current epoch time is `date +%s`'")
args = parser.parse_args()
t = args.t


def epoch():
    # print current epoch if no argument & exit
    if t == time_now:
        print("Current EPOCH time is: " + (str(t)))
        exit()

    human_time = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(int(t)))
    print("Human-readable date:\n" + human_time)


epoch()
