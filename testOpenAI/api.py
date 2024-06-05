# api.py

# 패키지 설치 : openai

from openai import OpenAI

# 발급받은 API 키 설정
OPENAI_AI_KEY = 'KEY 입력'
client = OpenAI(api_key=OPENAI_AI_KEY)
print(client)


def ask(question, message_history=[], model='gpt-3.5-turbo'):
    if len(message_history) == 0: # 최초 질문이면
        message_history.append(
            {
                'role' : 'system',
                'content' : 'You are a helpful assistant. You must answer in Korean.'
            }
        )
    # 사용자 질문
    message_history.append(
        {
            'role' : 'user',
            'content' : question,
        }
    )

    # GPT 에 질문을 전달해서 답변을 생성
    completion = client.chat.completions.create(
        model=model,
        messages=message_history
    )
    # 사용자 질문에 대한 답변을 추가
    message_history.append(
        {
            'role' : 'assistant',
            'content' : completion.choices[0].message.content
        }
    )
    # 답변을 반환
    return message_history
# -------------------------------------------------------------------------

# 실행
# 최초 질문
message_history = ask('대한민국의 수도는 어디인가요?', message_history=[])
# 최초 답변
print(message_history[-1])
# 두번째 질문
message_history = ask('이전의 내용을 영어로 답변해 주세요?', message_history=message_history)
# 두번째 답변
print(message_history[-1])
