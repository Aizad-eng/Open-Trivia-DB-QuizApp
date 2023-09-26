import requests
def collect_quiz_questions():
    response = requests.get(url="https://opentdb.com/api.php?amount=5&type=boolean")
    quiz_questions = response.json()["results"]
    print(quiz_questions)
    return quiz_questions


