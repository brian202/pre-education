"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""
def Triangle(x, y):
    result = (x * y) / 2
    return result

x = int(input("가로를 입력하세요 >> "))
y = int(input("높이를 입력하세요 >> "))

print(Triangle(x, y))

