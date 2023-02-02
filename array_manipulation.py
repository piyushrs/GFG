def solution(a):
    b = []
    while a:
        b.append(a.pop(0))
        if a: b.append(a.pop())
    
    return all(i<j for i,j in zip(b, b[1:]))

a = [1,4,5,6,3]
print(solution(a))