
inches_in_cm = 0.393700787
cm_in_foot = 30.480

height = 170
height_to_use = height

foot_value = 0

while height_to_use > cm_in_foot:
    foot_value = foot_value +1
    height_to_use = height_to_use - cm_in_foot
    
    
inches_value = int(round(height_to_use * inches_in_cm , 0))

print(f"I am {height}cm tall, i.e. {foot_value} feet and {inches_value} inches.")

                   
    
