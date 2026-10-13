#File for making basic 


#Assuming, 3x640x640 input, as in yolo11s_PALretrained.onnx
#Assume normalised

input_size = 64*64*3
output_size = 84*5
s = ""
#Declaration of constants
for i in range(0, input_size):
    s += "(declare-const X_"+str(i)+" Real) \n"

for i in range(0, output_size):
    s += "(declare-const Y_"+str(i)+" Real) \n"
    
#Input Constraints
for i in range(0, input_size):
    s += "(assert (>= X_"+str(i)+" 0.0)) \n"
    s += "(assert (<= X_"+str(i)+" 0.01)) \n"

#Output Constraints
s += "(assert (>= Y_0 0.0)) \n"
s += "(assert (<= Y_1 1.0))"


print(s)
