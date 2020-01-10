# 1. 모듈 가져오기
import random # 모듈가져오기
import time   # 시간
 
# 2. 전역번수 정의
GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE         = False
types = list('♠◆♥♣')
nums  = list('A23456789')+['10']+list('JQK')
cards = [ i+j for i in types for j in nums ]
score_table = dict()
for key in nums:score_table[ key ] = nums.index( key ) +1
# 트럼트 K는 패널티를 주어서 -5점이다
score_table[ 'K' ] = -5
# 함수지향적 프로그램으로 작성 중에 추가된 변수
player_name             = None
myTotalScore            = 0
game_level              = tmp
# 3. 함수를 나열
# 함수 지향적 프로그램은 반드시(대체적으로) 시작점이 존재한다
# 시작점, 엔트리포인트 

def main():
    step1()
    # 26번의 gameTitle 과 step2() 안의 gameTitle은 서로 다른 변수다
    # 그냥 편의상 이름만 동일하게 사용했다 (이후 코드 안 고치기 위해)
    gameTitle = step2()
    step3()
    step4()
    ======
    step5()
    step6()
    step7()

def step1():
    print( "Enjoy Custom Game world" )

    step2():
    while True:
        tmp = input("게임 제목을 입력하시오, 단 {}자 \이내로 입력 가능합니다. => ".format(GAME_TITLE_LEN_MAX)).strip()       
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.") 
        else:
            gameTitle = tmp
            break
    print( 'gameTitle', gameTitle )
    # gameTitle은 절차적 코드에서는 그냥 사용해도 되나,
    # 함수지향적으로 전개해서 함수 내부로 가면 지역변수가 된다.
    # 함수 밖에서 사용이 불가하므로, 값을 리턴하거나,
    # 아예 전역 변수로 빼야 한다
    return gameTitle

    step3():
        tmp = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n=>" % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>PLAYER_NAME_LEN_MAX:
            print("%s자가 초과되었습니다." % str(PLAYER_NAME_LEN_MAX) ) 
        else:
            player_name = tmp
            # 플레이어의 이름으로 저장된 점수를 읽어서 로드 
            # 만약 없으면 0점 으로 시작
            myTotalScore       = 0 # 나의 총 점수
            break
    
    step4():
    while True:
        tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            print('정확하게 입력하세요')
            continue
        if not tmp.isnumeric():
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue
        tmp = int(tmp)
        if tmp>9 or tmp<1:
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue    
        game_level = tmp
        break

else:# test or dev(개발) 버전으로 코드가 작동
    gameTitle   = 'test game'
    player_name = 'guest'
    game_level  = 1
    myTotalScore= 0 # 나의 총 점수
    step5():
    pass
    step6():
    pass
    step7():
    pass


# 4. 프로그램 시작  
    # __name__ 이 변수는 그냥 사용이 가능하고
    # 값이 프로그램을 구동하는 방식에 따라 2가지로 변경된다
    # 1) python 파일명.py로 구동 => __name__=> '__main__' 으로 세팅
    # 2) 누군가가 파일명.py를 가져와서 사용 => __name__=> '파일명'
    print('__name__', __name__) 
    if__name__=='__main__':
        main()