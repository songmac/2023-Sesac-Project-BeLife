import re
#챗봇 구현 class

location_pattern = r'^[가-힣]+구$'

#대답에 따라 사용자 응답 유효성 검사
def is_valid_input(index, response):
    if index == 1 : #연령대
        if response in ['1', '2', '3'] :
            return True
        else : False
    elif index == 2 : #위치
        return bool(re.match(location_pattern, response))
    elif index == 3 : #장애여부
            if response in ['1', '2'] :
                return True
            else : False
    elif index == 4 : #운동목표
            if response in ['1', '2', '3', '4', '5', '6', '7'] :
                return True
            else : False
    elif index == 5 : #선호 운동
            if response in ['1', '2', '3', '4','5', '6', '7', '8'] :
                return True
            else : False
    elif index == 6 : #운동 시간대
            if response in ['1', '2', '3', '4', '5'] :
                return True
            else : False
    elif index == 7 : #주당 운동 빈도
            if response in ['1', '2', '3', '4', '5'] :
                return True
            else : False
    elif index == 8 : #중요항목
            if response in ['1', '2', '3', '4', '5', '6', '7'] :
                return True
            else : False
    else : 
        return True

#프로그램 추천을 위한 answer값
modeling_answers = []
#해당하는 프로그램 정보를 추출하기 위한 answer값
cosine_answers = []

#chatbot
class ExerciseChatbot:
    def __init__(self):
        #self.user_data = {}
        self.questions = [
            "먼저, 당신의 연령대가 어떻게 되나요?\n1: 학생(초,중,고), 2: 성인(대학생 포함), 3: 노인",
            "당신이 운동을 할때 선호하는 '지역구'을 알려주세요 (예시: 중구, 종로구, 마포구 등)",
            "장애로 인해 운동시 활동에 불편한 점이 있나요? (1: 없음, 2: 있음)",
            "이제는 운동에 대한 선호에 대해 알아보겠습니다.\n어떤 목표로 운동을 하시려나요?\n1: 수명 연장 \n2: 심폐 기능 향상 \n3: 근력 향상 \n4: 유연성 향상 \n5: 체중 및 신체구성(체지방) \n6: 기분개선 \n7: 무관",
            "어떤 종류의 운동을 선호하시나요?\n1: 구기 및 라켓\n2: 레저\n3: 무도\n4: 무용\n5: 민속\n6: 재활\n7: 체력단련 및 생활운동\n8: 무관",            
            "어떤 시간대에 운동하는 것을 선호하시나요?\n 1: 아침\n 2: 오전\n 3: 오전오후\n 4: 오후\n 5: 저녁 \n 6: 무관 ",
            "주당 몇 회를 하는 운동을 원하시나요?\n 1: 주1회\n 2: 주2회\n 3: 주3회\n 4: 주4회 이상\n 5: 무관",
            "현재 항목 중 가장 중요하게 여기는 것이 무엇인가요?\n1: 운동 목표\n2: 연령대\n3: 선호 지역\n4: 선호 시간대\n5: 선호 운동 \n6: 무관",
            "질문이 끝났습니다. 우리가 추천하는 운동 프로그램은 아래와 같습니다"
        ]
        # 질문과 응답 기록을 저장
        self.chat_history = []  
        #현재 어떤 질문을 물어봐야하는지 나타내는 것
        self.current_question_index = 0

    #질문을 구분하기 위해 1씩 증가
    def ask_next_question(self):
        if self.current_question_index < len(self.questions):
            next_question = self.questions[self.current_question_index]
            self.current_question_index += 1
            print(next_question)
            print("현재 ask_next_question : ", {self.current_question_index})
            return next_question
        else:
            "질문을 마치겠습니다"
        
    #챗봇의 현재 사용자의 채팅 기록
    def process_user_response(self, response):
        current_question = self.questions[self.current_question_index - 1]
        self.chat_history.append({'role': 'assistant', 'message': current_question})
        if is_valid_input(self.current_question_index, response) :
            self.chat_history.append({'role': 'user', 'message': response})
            #print(response)
            # 선택한 번호에 해당하는 키 값을 출력 
            #streamlit인 경우 index가 0으로 시작하여 +1, panel인 경우 +1을 빼야함
            key = get_key_from_response(self.current_question_index +1, response)
            print("현재 process_user_repose : ", {self.current_question_index})
            print(f"답변 번호에 해당하는 키 값: {key}")
            #프로그램을 추천할때 분류가 필요한 항목만 입력(연령대, 위치, 장애여부,운동빈도)
            modeling_answers.append(key)
            if self.current_question_index in [1,2,3,6,7] :
                cosine_answers.append(key)
        else :
            self.chat_history.append({'role': 'assistant', 'message': "죄송합니다. 입력 형식이 잘못되었습니다. 다시 입력해주세요"})
            self.current_question_index -= 1 #잘못된 답변을 했을때 다시 이전 질문으로 돌아가기 위함
    
    #사용자가 모든 질문에 답했는지 여부를 확인
    def is_finished(self):
        return self.current_question_index >= len(self.questions)
    
    def is_all_questions_answered(self):
        return self.current_question_index == len(self.questions)

    def get_chat_history(self):
        return self.chat_history

def get_key_from_response(index, response):
    print("key index",index)
    key_mappings = [
        {'1': '학생', '2':'성인', '3':'노인'},
        {},
        {'1': '무', '2':'유'}, 
        {'1':'수명 연장', '2': '심폐 기능 향상', '3':'근력 및 근육강화', '4':'유연성 향상', '5':'체중 및 신체구성(체지방)조절', '6':'기분 개선', '7' : '무관'},
        {'1':'구기 및 라켓', '2':'레저', '3':'무도', '4':'무용', '5':'민속', '6':'재활', '7':'체력단련및생활운동', '8' : '무관'},
        {'1':'아침', '2':'오전', '3':'오전오후', '4':'오후', '5':'저녁', '6':'무관'},
        {'1': '주1회', '2':'주2회', '3':'주3회', '4': '주4회 이상' , '5' : '무관'},
        {'1':'운동 목표', '2':'연령대', '3':'선호 지역', '4':'선호 시간대', '5':'선호 운동', '6':'무관'}
    ]
    return key_mappings[index-1].get(response, response)