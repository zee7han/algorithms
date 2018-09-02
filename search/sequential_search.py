def seq_search(arr,ele):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True

        else:
            pos += 1

    return found



def ordered_seq_search(arr,ele):

        #The arr must be sorted for ordered search

    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True

        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1

    return found


    lst = [1,2,3,4,5,6,7,8,9,10]

    print("loggggg")

    print(seq_search(lst,6))
    print(seq_search(lst,11))

    print(ordered_seq_search(lst,7))
    print(ordered_seq_search(lst,14))
