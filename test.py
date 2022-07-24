a = 35

def outer():
    x = 25
    print('Outer() x: ' + str(x) + " outer a: " + str(a)) # a >>> 35
    
    def inner():
        global a
        nonlocal x
        a = 55
        x = 30
        print("Inner() x: " + str(x) + " + inner a: " + str(a)) # >>> a: 55
        
    inner()
    print("Final-res x: " + str(x) + " + final a: " + str(a)) # >>> a: 55
outer()

# `nonlocal` - w merzach odnijeji funkciji
# `global` - w merzach odnoho proekta

count = 0

def count():
    # global count
    # count += 1 # if uncomment without `global` >>> Error
    print(count) # >>> if `count += 1` and `global count` are commented:
    #                                       >>> <function count at 0x7fcc5b38fe20>
# count()