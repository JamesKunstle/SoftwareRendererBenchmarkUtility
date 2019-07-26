import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')


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


def sum_numbers(n1, n2):
    return n1 + n2


def read_f1_filetype(name):
    # reads a file of type F1 and writes the contents to the arrays swTimeList and glTimeList
    f = open(name, "r")
    current_line = f.readline()  # type: str
    if current_line == "F1\n":
        line = f.readline()
        numfirst = line
        # numfirst * 2 = total entries. @numfirst, we start reading as second type.
        for n in range(int(numfirst)):
            fulltimelist.append(n + 1)
        for x in range(int(numfirst)):
            currentstring = f.readline()
            currentfloat = float(currentstring[0:-2])
            swTimelist.append(currentfloat)

        for x in range(int(numfirst), (int(numfirst) + int(numfirst))):
            currentstring = f.readline()
            currentfloat = float(currentstring[0:-2])
            glTimeList.append(currentfloat)
    else:
        print("Incorrect file format!")

    f.close()


def more_time(duration):
    for n in range(int(duration)):
        fulltimelist.append(n + 1)


def read_cb1_filetype(name):
    f = open(name, "r")
    current_line = f.readline()  # type: str
    number_samples = 0
    if current_line == "CB1\n":  # if we're working with the correct file type:

        line = f.readline()
        numfirst = int(line)  # the number of discrete timings per model-type.
        more_time(numfirst-1)

        f.readline() # dismisses the intermediate blank line.
        current_line = f.readline()

        if current_line[0:2] == "qd":
            print("Found the quad!")
            for i in range(numfirst-1):
                quad_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                quad_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
        if current_line[0:2] == "cb":
            print("Found the cube!")
            for i in range(numfirst-1):
                cube_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                cube_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "ms":
            print("Found a mesh!")
            for i in range(numfirst-1):
                mesh_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                mesh_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "cl":
            print("Found a cylinder!")
            for i in range(numfirst-1):
                cylinder_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                cylinder_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "cn":
            print("found a cone!")
            for i in range(numfirst-1):
                cone_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                cone_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "sr":
            print("Found a sphere!")
            for i in range(numfirst-1):
                sphere_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                sphere_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "to":
            print("Found a torus!")
            for i in range(numfirst-1):
                torus_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                torus_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "tp":
            print("Found a teapot!")
            for i in range(numfirst-1):
                teapot_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                teapot_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "ct":
            print("Found a cat!")
            for i in range(numfirst-1):
                cat_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                cat_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "de":
            print("Found a deer!")
            for i in range(numfirst-1):
                deer_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                deer_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "bn":
            print("Found a bunny!")
            for i in range(numfirst-1):
                bunny_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                bunny_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "bd":
            print("Found a religion!")
            for i in range(numfirst-1):
                buddha_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                buddha_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "wl":
            print("Found a wolf!")
            for i in range(numfirst-1):
                wolf_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                wolf_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
            current_line = f.readline()
        if current_line[0:2] == "tr":
            print("Found a tree!")
            for i in range(numfirst-1):
                tree_sw_timelist.append(float(current_line[3:10]))  # value of the software renderer
                tree_gl_timelist.append(float(current_line[11:18]))  # value of GL
                current_line = f.readline()  # update the line that we're reading from.
    else:
        print("Not the correct file type!")





def convert_to_fps(array):
    for i in range(len(array)):
        if array[i] != 0:
            array[i] = 1 / array[i]


"""
read_f1_filetype("teapot.txt")
convert_to_fps(swTimelist)  # Convert the two arrays over to frames per second
convert_to_fps(glTimeList)
plt.plot(fulltimelist, glTimeList, label="GL")
plt.plot(fulltimelist, swTimelist, label="Software")
"""

read_cb1_filetype("rotate2_cb1.txt")

convert_to_fps(mesh_gl_timelist)
convert_to_fps(mesh_sw_timelist)
convert_to_fps(cylinder_gl_timelist)
convert_to_fps(cylinder_sw_timelist)
convert_to_fps(cone_gl_timelist)
convert_to_fps(cone_sw_timelist)
convert_to_fps(buddha_sw_timelist)
convert_to_fps(buddha_gl_timelist)


plt.plot(fulltimelist, mesh_gl_timelist, label="Mesh GL")
plt.plot(fulltimelist, mesh_sw_timelist, label="Mesh SW")
plt.plot(fulltimelist, cylinder_gl_timelist, label="Cylinder GL")
plt.plot(fulltimelist, cylinder_sw_timelist, label="Cylinder SW")
plt.plot(fulltimelist, cone_gl_timelist, label="Cone GL")
plt.plot(fulltimelist, cone_sw_timelist, label="Cone SW")
plt.plot(fulltimelist, buddha_gl_timelist, label="Buddha GL")
plt.plot(fulltimelist, buddha_sw_timelist, label=" Buddha SW")


plt.xlabel("Render")
plt.ylabel("Frames per second")
plt.title("(higher is better)")
plt.suptitle("Teapot: All options")
plt.legend()
plt.show()