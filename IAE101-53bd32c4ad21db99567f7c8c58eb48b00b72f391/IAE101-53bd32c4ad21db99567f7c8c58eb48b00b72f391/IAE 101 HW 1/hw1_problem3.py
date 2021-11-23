# PUT YOUR NAME HERE
# PUT YOUR SBU ID NUMBER HERE
# PUT YOUR NETID (BLACKBOARD USERNAME) HERE
#
# IAE 101 (Fall 2021)
# HW 1, Problem 3

def getSeconds(hours, minutes, seconds):
    return int(hours) * (60 ** 2) + int(minutes) * 60 + int(seconds)
    #hs = int(hours) * 60 * 60
    #ms = int(minutes) * 60
    #ss = int(seconds)
    #return hs + ms + ss


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE VALUE ASSIGNED TO time1 TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    time1 = "11:11:14"
    h1, m1, s1 = time1.split(":")
    print('getSeconds("' + time1 + '") is', getSeconds(h1, m1, s1))
    print()
    time2 = "00:01:02"
    h2, m2, s2 = time2.split(":")
    print('getSeconds("' + time2 + '") is', getSeconds(h2, m2, s2))
    print()
    time3 = "05:00:30"
    h3, m3, s3 = time3.split(":")
    print('getSeconds("' + time3 + '") is', getSeconds(h3, m3, s3))
    print()
    time4 = "00:00:00"
    h4, m4, s4 = time4.split(":")
    print('getSeconds("' + time4 + '") is', getSeconds(h4, m4, s4))
    print()
    time5 = "02:18:49"
    h5, m5, s5 = time5.split(":")
    print('getSeconds("' + time5 + '") is', getSeconds(h5, m5, s5))
    print()
