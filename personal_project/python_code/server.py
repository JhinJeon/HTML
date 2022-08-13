# 플레이어가 입력한 단어를 받는 서버

# 0. 필요 라이브러리
import sys
import json
import gamesystem


# 1. 플레이어가 입력한 단어 가져오기

# 임시 테스트용 코드
player_name = 'player'
player_input = list(input())

# 유효하지 않은 문자가 포함된 경우

for p in player_input:
    if p in gamesystem.invalid_str:
        print('다시 입력하세요.')

# 2. 네이버 사전 API에서 단어 검색


# 3-1. 1의 단어를 2에서 찾을 수 없는 경우 다시 입력하라고 보내기


# 3-2. 1의 단어를 2에서 찾을 수 있는 경우 금칙 조건에 위배되지 않는지 확인

for p in player_input:
    if p in gamesystem.default_str:
        print('-'*40)
        print(f'{player_name}님이 금칙어 "{p}" 을(를) 입력했습니다!')
        print(f'{player_name}님이 입력한 단어 :', ''.join(player_input))
        print('-'*40)
        break
else:
    print('다음 플레이어 차례')
