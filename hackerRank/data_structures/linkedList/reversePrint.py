#!/bin/python3

def reversePrint(head):
    if not head:
        return 
    reversePrint(head.next)
    print(head.data)
    return
