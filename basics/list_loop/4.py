input_id = input("아이디를 입력하세요.\n")
# real_egoing = "egoing"
# real_bill1224 = "bill1224"
members = ['egoing', 'bill1224']
for member in members:
    if member == input_id:
        print('Hello!, '+member)
        import sys
        sys.exit()
print('who are you?')

# if real_egoing == in_str :
#   print("Hello, egoing")
# elif real_bill1224 == in_str :
#   print("Hello, bill1224")
# else :
#   print("Who are you")
