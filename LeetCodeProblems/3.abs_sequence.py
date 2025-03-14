

def print_sequence(num):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = []
    core = list(letters[num-1::-1])
    core2 = list(letters[1:num])
    print(core)

    result = []
    for i in range(1,num+1):
        final = "-".join(core[:i]+core2[num-i:num])

        final = final.center((num*4-3), "-")
        
        result.append(final)

    for i in result:
        print(i)

print_sequence(5)