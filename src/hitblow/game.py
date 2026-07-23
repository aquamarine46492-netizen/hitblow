"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""
from .core import judge, make_secret
from .limitPrint import limitPrint
from .time import GameTimer



def play(digits=3):
    while True:
        try:
            digits = int(input("桁数(1～10)："))
            break  # 成功したらループを抜ける
        except ValueError:
            print("エラー：整数を入力してください。")
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    while True:
        try:
            limit = int(input("上限回数: "))
            break  # 成功したらループを抜ける
        except ValueError:
            print("エラー：整数を入力してください。")
    # 別ファイルからタイマー機能をインポートして初期化
    game_timer = GameTimer()
    game_timer.setup()
    
    tries = 0
    score = 0
    print("60秒以内にいっぱい正解しよう")
    while True:
        while True:
            try:
                guess = input("予想 > ").strip()
                break
            except ValueError:
                print("エラー：整数を入力してください。")
        
        

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
