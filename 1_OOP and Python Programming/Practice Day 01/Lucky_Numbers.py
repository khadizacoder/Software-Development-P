# a, b = map(int, input().split())

# ok = False
# for i in range(a, b+1):
#     st = str(i)
#     lucky = True
#     for s in st:
#         if s != '4' and s != '7':
#             lucky = False
#             break

#     if lucky:
#         print(i, end=" ")
#         ok = True

    
# if not ok :
#     print(-1)






a,b = map(int, input().split())

ok = False
for i in range(a, b+1):
    st = str(i)
    lucky = True

    for s in st:
        if s != '4' and s != '7':
            lucky = False
            break

    if lucky:
        print(i)
        ok = True

if not ok:
    print(-1)






