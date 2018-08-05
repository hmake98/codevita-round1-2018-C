import string
char_list = []
count_char = 0
count_char_for_first = 0
count_char_for_sec = 0
count_char_for_th = 0
char_num = int(input("enter char numbers: "))
if(char_num >= 1 and char_num <= 4):
    for i in range(0, char_num):
        char = input("enter char: ")
        char_list.append(char)

    print(char_list)
    
    for i in char_list:
        if(type(i) is str == True):
            if(check_num == 1):
                if(i in string.ascii_lowercase):
                    sen = "This sentence contains "+i+"'s"
                    print(sen)
                    for j in sen:
                        if(i == j):
                            count_char += 1
                    print(i+":"+count_char)
                    new_sen = "This sentence contains "+count_char+" "+i+"'s"
                    print(new_sen)
            elif(check_num == 2):
                if(i in string.ascii_lowercase):
                    sen2 = "This sentence contains "+i+"'s and "+char_list[index(i)+1]+"'s"
                    print(sen2)
                    for j in sen2:
                        if(i == j):
                            count_char_for_first += 1
                        elif(char_list[index(i)+1] == j):
                            count_char_for_sec += 1
                    print(count_char_for_first)
                    print(count_char_for_sec)
                    new_sen1 = "This sentence contains "+count_char_for_first+" "+i+"'s and "+count_char_for_sec+" "+char_list[index(i)+1]+"'s"
                    print(new_sen1)
            elif(check_num == 3):
                if(i in string.ascii_lowercase):
                    sen3 = "This sentence contains "+i+"'s and "+char_list[index(i)+1]+"'s and "+char_list[index(i)+2]+"'s"
                    print(sen3)
                    for j in sen3:
                        if(i == j):
                            count_char_for_first += 1
                        elif(char_list[index(i)+1] == j):
                            count_char_for_sec += 1
                        elif(char_list[index(i)+2] == j):
                            count_char_for_th += 1
                    print(count_char_for_first)
                    print(count_char_for_sec)
                    print(count_char_for_th)
                    new_sen2 = "This sentence contains "+count_char_for_first+" "+i+"'s and "+count_char_for_sec+" "+char_list[index(i)+1]+"'s and "+count_char_for_th+" "+char_list[index(i)+2]+"'s"
                    print(new_sen2)
                    '''if(check_num == 1):
                        sen = "This sentence contains two"+i+"'s."
                            if(i in sen == True):
                                count_char = count_char + 1
                            print(count_char)
                        elif(check_num == 2):
                            sen = "This sentence contains three"+i+"'s and three "+char_list[index(i)+1]+"'s OR This sentence contains three a's and two r's."
                                if(i in sen == True and char_list[index(i)+1] in sen == True):
                                count_char = count_char + 1
                                count_char = count_char + 1
                                print(count_char)
                                print(count_char2)
                        elif(check_num == 3):
                            sen = "This sentence contains one"+i+", one "+char_list[index(i)+1]+" and one "+char_list[index(i)+2]+"."
                                if(i in sen == True and char_list[index(i)+1] in sen == True and char_list[index(i)+2] in sen == True):
                                count_char = count_char + 1
                                count_char2 = count_char2 + 1
                                count_char3 = count_char3 + 1
                                print(count_char)
                                print(count_char2)
                                print(count_char3)'''
else:
    print("enter valid number")
