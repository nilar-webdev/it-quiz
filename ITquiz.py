import time


class Question:
    # 問題を作るときに、問題文・選択肢・正解を保存する
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    # ユーザーの回答が正しいか確認する
    def check_answer(self, user_answer):
        return user_answer == self.answer


# 問題を作成する
question1 = Question(
    "1. RAMについて、正しくない説明はどれですか？",
    [
        "a. 情報を一時的に保存するメモリ",
        "b. 実行中のプログラム情報を保存する",
        "c. 電源を切ると情報が消える",
        "d. 補助記憶装置とも呼ばれる",
    ],
    "d",
)

question2 = Question(
    "2. OSの機能ではないものはどれですか？",
    [
        "a. 電源を切った後もコンピューターを動かす",
        "b. ユーザーとハードウェアをつなぐ",
        "c. 周辺機器を管理する",
        "d. ハードウェアを利用できるようにする",
    ],
    "a",
)

question3 = Question(
    "3. コンピューターネットワークを表すものはどれですか？",
    [
        "a. 複数のコンピューターを接続したもの",
        "b. コンピューターのメモリ",
        "c. 入力装置",
        "d. プログラミング言語",
    ],
    "a",
)


# 問題をリストに入れる
questions = [question1, question2, question3]


def run_quiz(question_list):
    correct_count = 0

    print("Python クイズを開始します！")
    print("回答は a、b、c、d のどれかを入力してください。\n")

    # リストから問題を1つずつ取り出す
    for question in question_list:
        print(question.text)

        # 選択肢を1つずつ表示する
        for choice in question.choices:
            print(choice)

        # ユーザーの回答を受け取る
        user_answer = input("回答: ").lower().strip()

        # a、b、c、d以外が入力された場合
        while user_answer not in ["a", "b", "c", "d"]:
            print("a、b、c、dのいずれかを入力してください。")
            user_answer = input("回答: ").lower().strip()

        # 回答をチェックする
        if question.check_answer(user_answer):
            print("正解です！")
            correct_count += 1
        else:
            print(f"不正解です。正解は「{question.answer}」です。")
        print()
        time.sleep(1)

    # 最終スコアを計算する
    total_questions = len(question_list)
    score = correct_count / total_questions * 100

    print("=" * 40)
    print("クイズが終了しました。")
    print(f"問題数：{total_questions}")
    print(f"正解数：{correct_count}")
    print(f"スコア：{score:.1f}点")
    print("=" * 40)


# クイズを実行する
run_quiz(questions)