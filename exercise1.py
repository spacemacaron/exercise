# 리스트 반복하기

characters = ['앨리스', '도도새', '3월 토끼']
for charater in characters: 
    print(characters)
# ['앨리스', '도도새', '3월 토끼']
# ['앨리스', '도도새', '3월 토끼']
# ['앨리스', '도도새', '3월 토끼']


# 문자열 반복
for letter in '체셔고양이':
    print(letter)

    
# 체
# 셔
# 고
# 양
# 이

# 들여쓰기는 중요~
nums = [0, 1, 2]
for num in nums:
    print(num)
    print(nums)

    
# 0
# [0, 1, 2]
# 1
# [0, 1, 2]
# 2
# [0, 1, 2]

nums = [0, 1, 2]
for num in nums:
    print(num)
print(nums)
    
# 0
# 1
# 2
# [0, 1, 2]

for  num in range(3):
    print(num)

    
0
1
2

#순서열 만들기 range의 입력값이 두 개일 때에는 앞 숫자부터 뒤 숫자 전까지의
#순서열을 만든다 

for y in range(1, 10):
    print(2, 'x', y, '=', 2*y)

    
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18

