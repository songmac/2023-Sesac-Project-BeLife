import os
import re
from openai import OpenAI
from dotenv import load_dotenv
import panel as pn
load_dotenv()
client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY')
)
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(
        model= model,
        messages = messages,
        temperature = temperature
    )
    return response.choices[0].message.content
pn.extension()
panels = []
context = [ {'role':'system', 'content':"""
너는 사용자에게 운동프로그램을 추천하기 위한 챗봇이야
사용자에게 먼저 인사를 하고, 총 9개의 질문을 1개씩 해줘. 질문에 대한 답변을 정확하게 받아야지만 다음 질문을 해줘.
답변을 9개 전부 받으면 dataframe을 만들어서 보여줘.
질문은 아래와 같아 :
1. 연령대를 선택해주세요. (1: 학생(초, 중, 고등), 2: 성인, 3: 노인)
2. 건강 상태를 선택해주세요. (1: 디스크, 2: 관절 질환, 3: 혈압 질환, 4: 대사증후군, 5: 해당 없음)
3. 운동 목표를 선택해주세요. (1: 심폐지구력 향상, 2: 근력 향상, 3: 체형 교정, 4: 무관)
4. 선호 지역을 입력해주세요. (예: 관악구)
5. 선호 빈도를 선택해주세요. (1: 주1회, 2: 주2회, 3: 주3회, 4: 주4회 이상)
6. 선호 시간대를 선택해주세요. (1: 새벽, 2: 오전, 3: 오후, 4: 저녁, 5: 무관)
7. 선호 운동을 선택해주세요. (1: 구기및라켓, 2: 레저, 3: 무도, 4: 무용, 5: 민속, 6: 재활, 7: 체력단련및생활운동)
8. 선호 인원수를 선택해주세요. (1: 5명 이하, 2: 5명 이상, 3: 무관)
9. 운동 프로그램을 선택할 때 가장 중요하게 생각하시는 항목을 골라주세요. (1: 연령대, 2: 건강상태, 3: 운동목표, 4: 선호 지역, 5: 선호빈도, 6: 선호시간대, 7: 선호운동, 8: 선호인원수, 9: 무관)
"""} ]
#사용자가 형식에 맞지 않게 답변을 한 경우 처리
address_pattern = re.compile(r'^[가-힣]+구 [가-힣]+동$')
def is_valid_input(reponse, prompt):
    # 여기에서 input_text가 유효한지 여부를 판단하는 로직을 추가
    # 예를 들어, 특정 패턴이나 규칙을 확인할 수 있습니다.
    address_keywords = ["거주지", "동", "구", "사는곳"]
    if reponse in address_keywords :
        if re.match(prompt, address_pattern) :
            return True
    return False  # 유효한 경우 True, 그렇지 않은 경우 False
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    response = get_completion_from_messages(context)
    context.append({'role':'system', 'content':f"{response}"})
    context.append({'role':'system', 'content':f"{prompt}"})
    context.append({'role':'system', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600, styles={'background-color': '#F0FCD4'})))
    panels.append(
        pn.Row('Be_Life:', pn.pane.Markdown(response, width=600, styles={'background-color': '#F0FCD4'})))
    return pn.Column(*panels)
inp = pn.widgets.TextInput(value="안녕하세요", placeholder='답변을 입력해주세요')
button_conversation = pn.widgets.Button(name="입력")
def on_button_click(event):
    inp.value = ""  # 버튼 클릭 시 입력 값을 초기화
button_conversation.on_click(on_button_click)
interactive_conversation = pn.bind(collect_messages, button_conversation)
dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)
dashboard.show()