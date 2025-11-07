# this program is going to give award to a person completing a triathlon based on number of minutes completed 
# for the 3 trathlon evens.

swimming = int(input("What is the total time taken for Swimming: "))

cycling = int(input("What is the total time taken for Cycling: "))

running = int(input("What is the total time taken for Running: "))

triathlon = swimming + cycling + running

if (triathlon > 0) and (triathlon <= 100):
    print("Provincial Colours")
elif (triathlon >= 101) and (triathlon <= 105):
    print("Provincial half colours")
elif (triathlon >= 106) and (triathlon <=110):
    print("Pronincial scroll")
else:
    print("No award")