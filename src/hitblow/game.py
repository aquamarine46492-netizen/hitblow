from .core import judge, make_secret
from .limitPrint import limitPrint
from .time import GameTimer


def play(digits=3):
    digits = int(input("桁数："))
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    # 別ファイルからタイマー機能をインポートして初期化
    game_timer = GameTimer()
    game_timer.setup()
    
    limit = int(input("上限回数："))    
    tries = 0
    score = 0
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")
        limitPrint(limit-tries)
        if limit-tries==0:
            break
        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====

            tries = 0
            score += 1
            print(f"{score} 回目の正解！ {tries} 回で当たり（答え {secret}）")
            secret = make_secret(digits)
        
        # ===== ① の続き（時間チェック） =====
        # 時間切れならループを抜ける
        if game_timer.check_and_print():
            break
    print(f"score:{score}")