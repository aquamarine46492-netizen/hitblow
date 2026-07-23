import time

class GameTimer:
    def __init__(self):
        self.time_limit = 0.0
        self.start_time = 0.0

    def setup(self):
        """① 開始時に呼び出してタイマーを設定する"""
        self.time_limit = 60.0
        self.start_time = time.time()

    def check_and_print(self):
        """ループの最後で呼び出して、残り時間を表示し、時間切れなら True を返す"""
        elapsed_time = time.time() - self.start_time
        remaining_time = self.time_limit - elapsed_time
        
        if remaining_time <= 0:
            print("時間切れです！ゲームオーバー。")
            return True  # ループを終了させるフラグ
            
        print(f"残り時間：{max(0.0, remaining_time):.1f} 秒")
        return False