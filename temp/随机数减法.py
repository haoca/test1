import json
import random
while 1:
    a = random.randint(10,19)
    b = random.randint(1,10)
    while (a%10)>=b or a%10==0:
        a = random.randint(10,19)
        b = random.randint(1,9)
    c = a-b
    c = str(c)
    d = input('a = '+str(a)+ '\nb = '+str(b)+'\nplease input answer:\n')
    if c == d:
        print('\nright\n')
    else :
        print('\nwrong\n')
        
        quit()
    print(a,b,c+'\n')
# keyword = [None]*5
# for i in range(5):
#     print(i)
# langue_list = ['english','chinese','spanish']
# # langue_list.copy(langue_list.append['sb'])
# a=[1,2,3,4]
# print(keyword)
# print(langue_list[0])
# print(langue_list)
# person_dict['langue'] = langue_list 
# staff_dict = {}
# staff_dict['user'] = person_dict
# # Convert dictionary to JSON object
# person_json = json.dumps(person_dict)
# Print JSON object
# print(staff_dict)
# print(person_dict)
# print()
# print(type(person_json))
