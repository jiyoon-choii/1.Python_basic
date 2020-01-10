GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9

print( "Enjoy Custom Game world" )
while True:
    tmp = input("게임 제목을 입력하시오, 단 {}자 이내로 입력 가능합니다. => ").format(GAME_TITLE_LEN_MAX).strip()
    if not tmp :
        print ("정확하게 입력하세요!")
    elif len(tmp) > GAME_TITLE_LEN_MAX:
        print ( GAME_TITLE_LEN_MAX +"자가 초과되었습니다." )
    else tmp = gameTitle:
        break

while True:
    tmp = input( "플레이어의 닉네임을 입력하시오, 단 %자로 제한한다\n =>" % PLAYER_NAME_LEN_MAX).strip()
    if not tmp :
        print ("정확하게 입력하세요!")
    elif tmp > PLAYER_NAME_LEN_MAX :
        print ( "%자가 초과되었습니다" % PLAYER_NAME_LEN_MAX )
    else tmp = plyaerName:
        break

while True:
    tmp = input( "게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
    if not tmp :
        continue
    if not tmp.isnumeric():
         continue 
    tmp = int(timp)
    if tmp > 9 or tmp < 1:
        continue
    if game_level = tmp:
        break

############################################################################################

types = list('♠◆♥♣')
nums  = list('A23456789')+['10']+list('JQK')
cards = [ i*j for i in types for j in nums] 
score_table = dict()
for key in nums:
    score_table [ key ] = nums.index(key)+1
import random
random.shuffle(cards)
my_cards = [:8:2]
my_first_cards = my_cards[:2]
com_cards = [:9:2]
com_first_cards = com_cards[:2]

cnt = 0
while True : 
    choice = input( '1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?' )
    if choice == '1' and cnt<2 :
        cnt += 1
        my_first_cards = my_cards[:2+cnt]
        com_first_cards = com_cards[:2+cnt]
    elif choice == '2':
        myScore  = 0:
        comScore = 0
        for n in my_first_cards: myScore    += score_table[ n[:1] ]
        for n in com_first_cards : comScore += score_table[ n[:1] ]

        print ('myScore', myScore)
        print ('comScore', comScore)

    if myScore > comScore :
            print('You Win, try again? 1.yes, 2.no')
       comScore > myScore :
            print('You Lose, try again? 1.yes, 2.no')
        myScore = comScore :
            print('무승부, try again? 1.yes, 2.no')
            break
    else:
        print('정확하게 1 or 2를 입력하세요')
        if cnt==2:
            print('이미 추가 카드를 다 받았습니다. 2번만 선택할수 있습니다.')
)

