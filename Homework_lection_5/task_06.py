global_list = []

def enqueueFunction(item):
    global_list.append(item)
    return global_list

def dequeue_Function():
    if len(global_list) == 0:
        print("The queue is empty.")
        return None
    else:
        removed_item = global_list.pop(0)
        print(f"Removed item: {removed_item}")
        return removed_item
    
enqueueFunction("first_item")
print(global_list)

dequeue_Function()