dict_distances={4:3,3:6,5:8,6:14,2:20,7:22,1:25}
array=[]
sum_of_kms_3=0
sum_of_kms_6=0
sum_of_kms_8=0
sum_of_kms_14=0
sum_of_kms_20=0
sum_of_kms_22=0
sum_of_kms_25=0
for popul,distance in dict_distances.items():
    if popul==4:
        continue
    sum_of_kms_3=sum_of_kms_3+distance
print(sum_of_kms_3)
for popul,distance in dict_distances.items():
    if popul==3:
        continue
    sum_of_kms_6=sum_of_kms_6+distance
print(sum_of_kms_6)
for popul,distance in dict_distances.items():
    if popul==6:
        continue
    sum_of_kms_14=sum_of_kms_14+distance
print(sum_of_kms_14)
for popul,distance in dict_distances.items():
    if popul==5:
        continue
    sum_of_kms_8=sum_of_kms_8+distance
print(sum_of_kms_8)
for popul,distance in dict_distances.items():
    if popul==2:
        continue
    sum_of_kms_20=sum_of_kms_20+distance
print(sum_of_kms_20)
for popul,distance in dict_distances.items():
    if popul==7:
        continue
    sum_of_kms_22=sum_of_kms_22+distance
print(sum_of_kms_22)
for popul,distance in dict_distances.items():
    if popul==1:
        continue
    sum_of_kms_25=sum_of_kms_25+distance
print(sum_of_kms_25)
array.append(sum_of_kms_3)
array.append(sum_of_kms_6)
array.append(sum_of_kms_8)
array.append(sum_of_kms_14)
array.append(sum_of_kms_20)
array.append(sum_of_kms_22)
array.append(sum_of_kms_25)
#print(array)
print("Minimum distance to go it's %d"%min(array)) 
