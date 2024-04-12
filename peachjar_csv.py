import os.path
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("email", type=str, help="The email of the user.")
parser.add_argument("first_name", type=str, help="The first name of the user.")
parser.add_argument("last_name", type=str, help="The last name of the user.")
parser.add_argument("high_school", type=str, help="The initials of the high school designate which feeder schools to add to list.")
args = parser.parse_args()
HBHS = [67, 57, 47, 40, 55, 61, 63, 72, 44, 66, 48, 51, 52, 46]
SHS = [59, 53, 60, 58, 54, 41, 70, 71, 65, 50, 68, 69, 64]
print("args", args.first_name)


# set up the passed in arguments here
first_name = args.first_name 
last_name = args.last_name 
school = "HBHS"

email = args.email
print(email[-9:])
filename = f"{first_name}_{last_name}_peachjar.csv"
if os.path.isfile(filename):
    print("File already exists")
else:
    f = open(filename, "w")
    f.write("sis_id,email,first_name,last_name\n")

    if school == "SHS":
        for i in SHS:
            f.write(f"{i},{email},{first_name},{last_name}\n")
    else:
        for i in HBHS:
            f.write(f"{i},{email},{first_name},{last_name}\n")



    f.close()
