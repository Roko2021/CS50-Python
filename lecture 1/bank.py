answer = input('Greating: ')

new_answer = answer.lower().strip()

if 'hello' in new_answer:
    print('$0')
if 'h' in new_answer[0]:
    print('$20')
else:
    print('$100')