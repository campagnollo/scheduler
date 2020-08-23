import sys
import random
import os.path

def morning_shift(count, rtp_engineers, mex_engineers):
    shift = []
    for x in range(0,int(count/2)):
        shift.append(rtp_engineers.pop(0))
        shift.append(mex_engineers.pop(0))
    return shift, rtp_engineers, mex_engineers

def shift(count, rtp_engineers, mex_engineers):
    shift=[]
    for x in range(0,count):
        if len(rtp_engineers) > len(mex_engineers):
            shift.append(rtp_engineers.pop(0))
        else:
            shift.append(mex_engineers.pop(0))
    return shift, rtp_engineers, mex_engineers

def shift_rotate(shift, rotation_number):
    shift = shift[rotation_number:] + shift[:rotation_number]
    return shift

def print_to_file_shift(morning_shift, second_shift, third_shift):
    with open("MESS.txt", "w+") as f:
        f.write("Morning Shift\n")
        f.write("-----------------\n")
        f.write("Monday\n")
        f.write("*****************\n")
        for name in morning_shift:
            f.write(name + "\n")
        f.write("\n")
        f.write("Tuesday\n")
        f.write("*****************\n")
        morning_shift = shift_rotate(morning_shift, 2)
        for name in morning_shift:
            f.write(name +"\n")
        f.write("\n")
        f.write("Wednesday\n")
        f.write("*****************\n")
        morning_shift = shift_rotate(morning_shift, 2)
        for name in morning_shift:
            f.write(name+"\n")
        f.write("\n")
        f.write("Thursday\n")
        f.write("*****************\n")
        morning_shift = shift_rotate(morning_shift, 2)
        for name in morning_shift:
            f.write(name+"\n")
        f.write("\n")
        f.write("Friday\n")
        f.write("*****************\n")
        morning_shift = shift_rotate(morning_shift, 2)
        for name in morning_shift:
            f.write(name+"\n")
        f.write("\n")
        f.write("\n")

        f.write("2nd Shift\n")
        f.write("-----------------\n")
        f.write("Monday\n")
        f.write("*****************\n")
        for name in second_shift:
            f.write(name + "\n")
        f.write("\n")
        f.write("Tuesday\n")
        f.write("*****************\n")
        second_shift = shift_rotate(second_shift, 3)
        for name in second_shift:
            f.write(name +"\n")
        f.write("\n")
        f.write("Wednesday\n")
        f.write("*****************\n")
        second_shift = shift_rotate(second_shift, 3)
        for name in second_shift:
            f.write(name+"\n")
        f.write("\n")
        f.write("Thursday\n")
        f.write("*****************\n")
        second_shift = shift_rotate(second_shift, 3)
        for name in second_shift:
            f.write(name+"\n")
        f.write("\n")
        f.write("Friday\n")
        f.write("*****************\n")
        second_shift = shift_rotate(second_shift, 3)
        for name in second_shift:
            f.write(name+"\n")
        f.write("\n")
        f.write("\n")

        f.write("3rd Shift\n")
        f.write("-----------------\n")
        f.write("Monday\n")
        f.write("*****************\n")
        for name in third_shift:
            f.write(name + "\n")
        f.write("\n")
        f.write("Tuesday\n")
        f.write("*****************\n")
        third_shift = shift_rotate(third_shift, 3)
        for name in third_shift:
            f.write(name +"\n")
        f.write("\n")
        f.write("Wednesday\n")
        f.write("*****************\n")
        third_shift = shift_rotate(third_shift, 3)
        for name in third_shift:
            f.write(name+"\n")
        f.write("\n")
        f.write("Thursday\n")
        f.write("*****************\n")
        third_shift = shift_rotate(third_shift, 3)
        for name in third_shift:
            f.write(name+"\n")
        f.write("\n")
        f.write("Friday\n")
        f.write("*****************\n")
        third_shift = shift_rotate(third_shift, 3)
        for name in third_shift:
            f.write(name+"\n")
        f.write("\n")
        f.write("\n")



if __name__ == "__main__":

    if os.path.isfile("MESS.txt"):
        with open("RTPEngineers.txt", "r") as f:
            rtp_engineers = f.read().splitlines()[1:] #Don't want to read the first line in each text file

        with open("MEXEngineers.txt" ,"r") as f:
            mex_engineers = f.read().splitlines()[1:] #Don't want to read the first line in each text file

        total_count = len(rtp_engineers) + len(mex_engineers)
        morning_shift_count = 12
        second_shift_count = int((total_count-morning_shift_count)/2) + 1
        third_shift_count = (total_count-morning_shift_count) - second_shift_count

        with open("MESS.txt", "r") as f:
            previous_morning_shift = []
            data = f.read().splitlines()
            for i in range(4,16):
                previous_morning_shift.append(data[i])

        rtp_engineers = [x for x in rtp_engineers if x not in previous_morning_shift]
        mex_engineers = [x for x in mex_engineers if x not in previous_morning_shift]

        random.shuffle(rtp_engineers)
        random.shuffle(mex_engineers)

        morning_shift, rtp_engineers, mex_engineers = morning_shift(morning_shift_count, rtp_engineers, mex_engineers)

        for i in range(0,12):
            if i%2==0:
                rtp_engineers.append(previous_morning_shift[i])
            else:
                mex_engineers.append(previous_morning_shift[i])

        random.shuffle(rtp_engineers)
        random.shuffle(mex_engineers)

        second_shift, rtp_engineers, mex_engineers = shift(second_shift_count, rtp_engineers, mex_engineers)
        third_shift, rtp_engineers, mex_engineers = shift(third_shift_count, rtp_engineers, mex_engineers)

        print_to_file_shift(morning_shift,second_shift,third_shift)


    else:
        with open("RTPEngineers.txt", "r") as f:
            rtp_engineers = f.read().splitlines()[1:] #Don't want to read the first line in each text file

        with open("MEXEngineers.txt" ,"r") as f:
            mex_engineers = f.read().splitlines()[1:] #Don't want to read the first line in each text file

        random.shuffle(rtp_engineers)
        random.shuffle(mex_engineers)

        total_count = len(rtp_engineers) + len(mex_engineers)
        morning_shift_count = 12
        second_shift_count = int((total_count-morning_shift_count)/2) + 1
        third_shift_count = (total_count-morning_shift_count) - second_shift_count


        morning_shift, rtp_engineers, mex_engineers = morning_shift(morning_shift_count, rtp_engineers, mex_engineers)
        second_shift, rtp_engineers, mex_engineers = shift(second_shift_count, rtp_engineers, mex_engineers)
        third_shift, rtp_engineers, mex_engineers = shift(third_shift_count, rtp_engineers, mex_engineers)

        print_to_file_shift(morning_shift,second_shift,third_shift)
