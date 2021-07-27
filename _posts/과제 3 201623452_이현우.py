"""
도서관 대출 프로그램

 """




print('[ 도서 대출 반납 프로그램 ]')


Month_to_day = {'JAN' : 31, 'FEB' : 28, 'MAR' : 31, 'APR' : 30, 'MAY' : 31, 'JUN' : 30, 'JUL' : 31, 'AUG' : 31, 'SEP' : 30, 'OCT' : 31, 'NOV' : 30, 'DEC' : 31}

Month_to_month = {'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6, 'JUL' : 7, 'AUG' : 8, 'SEP' : 9, 'AUG' : 10, 'OCT' : 11, 'DEC' : 12}

Calendar = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

Calendar_Y = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

# 각 월에 대한 정보를 딕셔너리로 미리 정의해놓는다.


Book={}        # 대출 도서의 딕셔너리
Book_B={}      # 반납 도서의 딕셔너리

def Calculator(Ban_Book):

        
    D_Y = int(Book[Ban_Book][0])    #대출 년도를 정수형으로 변수에 저장
    B_Y = int(Book_B[Ban_Book][0])  #반납 년도를 정수형으로 변수에 저장


    D_M = Month_to_month[Book[Ban_Book][1]]    #대출 월변수에 저장
    B_M = Month_to_month[Book_B[Ban_Book][1]]  #대출 월 변수에 저장



    D_D = int(Book[Ban_Book][2])
    B_D = int(Book_B[Ban_Book][2])


    

    if D_Y%4 == 0 and B_Y%4 == 0:        # 둘 다 윤년일 때
        if D_M < B_M:  

            Y = 366*(B_Y - D_Y)
            M = 0
            for i in range(1,B_M - D_M):   # 대출 월, 반납 월 사이의 월 을 딕셔너리로 조회해 일 수를 계산
                M = M + Calendar_Y[D_M + i]
            D = Calendar_Y[D_M] - D_D + B_D

        elif D_M == B_M:

            Y = 366*(B_Y - D_Y)
            M = 0
            if D_D >= B_D:
                D = D_D - B_D
            else:
                D = B_D - D_D

        else:
            Y = 366*(B_Y - D_Y -1)
            M1 = 0
            for i in range(1,12-D_M+1):
                M1 = M1 + Calendar_Y[D_M+i]
            M2 = 0
            for i in range(1,B_M):
                M2 = M2 + Calendar_Y[i]
            M = M1+M2
            D = Calendar_Y[D_M] - D_D + B_D


    elif D_Y%4 == 0 and B_Y%4 != 0:        # 대출 년도만 윤년
        if D_M < B_M:  

            Y = 366*(B_Y - D_Y)
            M = 0
            for i in range(1,B_M - D_M):
                M = M + Calendar_Y[D_M + i]
            D = Calendar_Y[D_M] - D_D + B_D

        elif D_M == B_M:

            Y = 366*(B_Y - D_Y)
            M = 0
            if D_D >= B_D:
                D = D_D - B_D
            else:
                D = B_D - D_D

        else:
            Y = 366*(B_Y - D_Y -1)
            M1 = 0
            for i in range(1,12-D_M+1):
                M1 = M1 + Calendar_Y[D_M+i]
            M2 = 0
            for i in range(1,B_M):
                M2 = M2 + Calendar_Y[i]
            M = M1+M2
            D = Calendar_Y[D_M] - D_D + B_D
        

    elif D_Y%4 != 0 and B_Y%4 == 0:  # 반납 년도만 윤년
        if D_M < B_M:  

            Y = 365*(B_Y - D_Y)
            M = 0
            for i in range(1,B_M - D_M):
                M = M + Calendar[D_M + i]
            D = Calendar[D_M] - D_D + B_D

        elif D_M == B_M:

            Y = 365*(B_Y - D_Y)
            M = 0
            if D_D >= B_D:
                D = D_D - B_D
            else:
                D = B_D - D_D

        else:
            Y = 365*(B_Y - D_Y -1)
            M1 = 0
            for i in range(1,12-D_M+1):
                M1 = M1 + Calendar[D_M+i]
            M2 = 0
            for i in range(1,B_M):
                M2 = M2 + Calendar_Y[i]
            M = M1+M2
            D = Calendar[D_M] - D_D + B_D

    else:                            # 둘 다 윤년 아님
        if D_M < B_M:

            Y = 365*(B_Y - D_Y)
            M = 0
            for i in range(1,B_M - D_M):
                M = M + Calendar[D_M + i]
            D = Calendar[D_M] - D_D + B_D

        elif D_M == B_M:

            Y = 365*(B_Y - D_Y)
            M = 0
            if D_D >= B_D:
                D = D_D - B_D
            else:
                D = B_D - D_D

        else:
            Y = 365*(B_Y - D_Y -1)
            M1 = 0
            for i in range(1,12-D_M+1):
                M1 = M1 + Calendar[D_M+i]
            M2 = 0
            for i in range(1,B_M):
                M2 = M2 + Calendar[i]
            M = M1+M2
            D = Calendar[D_M] - D_D + B_D


    return Y + M + D        
            
        

    





def Daechul():
    while 1:
        date_d = input('>>> [대출일] 년, 월, 일을 입력하세요.(예 : 2020 JAN 20):')
        date_D = date_d.split()

        if (date_D[1] in Month_to_month) == True:  # 월이 제대로 입력 받았으면 딕셔너리에 포함되어 있음.
            while 1:
                number_D = int(input('>>> 대출 권수 입력:'))

                if number_D > 3 or (len(Book)+number_D) > 3:  #한번에 입력받은 숫자가 3 이하여도, 딕셔너리가 2개 이상이 되면 오류처리
                    print('대출 가능한 권수를 초과했습니다.')

                else:
                    for i in range(0,number_D):  #입력받은 권수 만큼 도서명을 입력받음
                        Book[input('>>> 대출할 도서명 입력:')] = date_D
                    break
            break
            
        else:
            print('월 입력이 잘못되었습니다.')


def Bannap():
    
    if len(Book) >= 1:
        
        print('*'*18,end='')
        print('현재 대출 현황',end='')
        print('*'*18)
        Book_list = list(Book.keys())  #딕셔너리의 키 값이 도서명이므로 도서명 출력을 위해 리스트 변환
        for i in range(0,len(Book)):
            a=1
            print('[%d]'%a,end=' ')
            print('대출일:',end=' ')
            print(Book[Book_list[i]][0],end='년 ')  #변환된 리스트에서 0번째인 년 출력
            print(Month_to_month[ Book [ Book_list[i]][1] ],end='월 ') #첫번째인 월 출력
            print(int(Book[Book_list[i]][2]),end='일, ') #두번째인 일 출력
            print('도서명:',end=' ')
            print(list(Book.keys())[i]) #key 값인 도서명을 list 이용해 출력
            a=a+1
        print('*'*50)

        while 1:
                        
            date_b = input('>>> [반납일] 년, 월, 일을 입력하세요.(예 : 2020 MAR 10):')
            date_B = date_b.split()

            if (date_B[1] in Month_to_month) == True: 
                Ban_Book = input('>>> 반납할 도서명 입력:')
                Book_B[Ban_Book] = date_B
                print('< %s > 도서의 대출일은 ' %Ban_Book,end='')
                print('%s년 %d월 %d일이고,'%(Book[Ban_Book][0],Month_to_month [ Book [ Ban_Book ] [1] ],int(Book[Ban_Book][2])),end=' ')
                print('반납일은 %s년 %d월 %d일입니다.' %(Book_B[Ban_Book][0],Month_to_month [ Book_B[Ban_Book][1] ],int(Book_B[Ban_Book][2])))
                print('대출 기간은 총 %d일 입니다.'%Calculator(Ban_Book))
                if Calculator(Ban_Book) > 50:
                    print('%d일 연체되었습니다.' %(Calculator(Ban_Book) - 50))
                print('반납이 완료되었습니다.')
                del(Book[Ban_Book])
                break
        

            else:
                print('월 입력이 잘못되었습니다.')
    else:
        print('반납할 도서가 없습니다.')





while 1:
    print('[ 1. 대출, 2. 반납 ]')
    Choose = int(input('>>> 서비스 번호를 선택하세요 :'))
    if Choose == 1:
        Daechul()
        Conti = input('>>> 계속 하시겠습니까? (y 또는 n):')  # 함수의 실행이 끝나면 다시 입력을 받음
        if Conti == 'y':   # 여부를 변수로 저장해서 입력 받아 변수의 값에 따라 판별
            continue
        else:
            break

    elif Choose == 2:
        Bannap()
        Conti = input('>>> 계속 하시겠습니까? (y 또는 n):')
        if Conti == 'y':
            continue
        else:
            break
    else:
        print('서비스 번호를 잘못 입력했습니다.')
    
    



    
