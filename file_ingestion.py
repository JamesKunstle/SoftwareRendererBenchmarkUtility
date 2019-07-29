import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

#  contains functions to support CB1 and CB2 file format ingestion
swTimelist = []
glTimeList = []

quad_sw_timelist = []
quad_gl_timelist = []

cube_sw_timelist = []
cube_gl_timelist = []

mesh_sw_timelist = []
mesh_gl_timelist = []

cylinder_sw_timelist = []
cylinder_gl_timelist = []

cone_sw_timelist = []
cone_gl_timelist = []

sphere_sw_timelist = []
sphere_gl_timelist = []

torus_sw_timelist = []
torus_gl_timelist = []

teapot_sw_timelist = []
teapot_gl_timelist = []

cat_sw_timelist = []
cat_gl_timelist = []

deer_sw_timelist = []
deer_gl_timelist = []

bunny_sw_timelist = []
bunny_gl_timelist = []

buddha_sw_timelist = []
buddha_gl_timelist = []

wolf_sw_timelist = []
wolf_gl_timelist = []

tree_sw_timelist = []
tree_gl_timelist = []

fulltimelist = []
average_sw = 0
average_gl = 0

valid_file_types = ["CB1", "F1"]


def read_file(name):
    f = open(name, "r")
    current_line = f.readline()  # type: str
    print(current_line)
    number_samples = 0
    if current_line[0:3] == "CB1":
        read_cb1(name, f)
    if current_line[0:2] == "F1":
        print("F1 filetype correctly identified")
        read_f1_filetype(name, f)
    else:
        print("Invalid filetype.")


def read_cb1(name, f):
    line = f.readline()
    numfirst = int(line)  # the number of discrete timings per model-type.
    more_time(numfirst - 1)

    f.readline()  # dismisses the intermediate blank line.
    current_line = f.readline()

    if current_line[0:2] == "qd":
        print("Found the quad!")
        for i in range(numfirst - 1):
            quad_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            quad_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
    if current_line[0:2] == "cb":
        print("Found the cube!")
        for i in range(numfirst - 1):
            cube_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            cube_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "ms":
        print("Found a mesh!")
        for i in range(numfirst - 1):
            mesh_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            mesh_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "cl":
        print("Found a cylinder!")
        for i in range(numfirst - 1):
            cylinder_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            cylinder_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "cn":
        print("found a cone!")
        for i in range(numfirst - 1):
            cone_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            cone_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "sr":
        print("Found a sphere!")
        for i in range(numfirst - 1):
            sphere_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            sphere_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "to":
        print("Found a torus!")
        for i in range(numfirst - 1):
            torus_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            torus_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "tp":
        print("Found a teapot!")
        for i in range(numfirst - 1):
            teapot_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            teapot_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "ct":
        print("Found a cat!")
        for i in range(numfirst - 1):
            cat_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            cat_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "de":
        print("Found a deer!")
        for i in range(numfirst - 1):
            deer_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            deer_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "bn":
        print("Found a bunny!")
        for i in range(numfirst - 1):
            bunny_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            bunny_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "bd":
        print("Found a religion!")
        for i in range(numfirst - 1):
            buddha_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            buddha_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "wl":
        print("Found a wolf!")
        for i in range(numfirst - 1):
            wolf_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            wolf_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
        current_line = f.readline()
    if current_line[0:2] == "tr":
        print("Found a tree!")
        for i in range(numfirst - 1):
            tree_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
            tree_gl_timelist.append(float(current_line[11:18]))  # value of GL
            current_line = f.readline()  # update the line that we're reading from.
    else:
        print("Not the correct file type!")


def more_time(duration):
    for n in range(int(duration)):
        fulltimelist.append(n + 1)


def read_f1_filetype(name, f):
    line = f.readline()
    numfirst = line
    # numfirst * 2 = total entries. @numfirst, we start reading as second type.
    for n in range(int(numfirst)):
        fulltimelist.append(n + 1)
    for x in range(10, int(numfirst) + 10):
        currentstring = f.readline()
        if float(currentstring[0:-2]) <= 0.00000:
            break
        print(1)
        currentfloat = float(currentstring[0:-2])
        swTimelist.append(currentfloat)

    for x in range(int(numfirst) + 10, (2 * int(numfirst)) + 11):
        currentstring = f.readline()
        if float(currentstring[0:-2]) == 0.00000:
            print("0.00000: ", x, " == ", currentstring)
            continue
        print(2)
        currentfloat = float(currentstring[0:-2])
        glTimeList.append(currentfloat)

    f.close()


def convert_to_fps(array):
    for i in range(len(array)):
        if array[i] != 0:
            array[i] = 1 / array[i]


read_file("SWHWtimer_200.txt")
print("Length of the timelist for gl is: ", len(glTimeList))
print(len(swTimelist))
convert_to_fps(swTimelist)  # Convert the two arrays over to frames per second
convert_to_fps(glTimeList)
plt.plot(fulltimelist, glTimeList, label="GL")
plt.plot(fulltimelist, swTimelist, label="Software")
plt.xlabel("Render")
plt.ylabel("Frames per second")
plt.title("(higher is better)")
plt.suptitle("Sphere: Rasterized and Per-pixel lit")
plt.legend()
plt.show()
