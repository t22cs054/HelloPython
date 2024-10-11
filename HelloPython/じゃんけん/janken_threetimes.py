import random
def janken_threetimes():
    # ぐー, ちょき, パーをそれぞれ0, 1, 2として定義
    hands = {0: "グー", 1: "チョキ", 2: "パー"}
    
    # プレイヤーAとBの勝利数を記録
    a_wins = 0
    b_wins = 0
    round_count = 0

    # 先に2勝したら終了する
    while a_wins < 2 and b_wins < 2:
        round_count += 1
        print(f"\nラウンド {round_count}")

        # プレイヤーAとBの手をランダムに決定
        player_a_hand = random.randint(0, 2)
        player_b_hand = random.randint(0, 2)
        
        # それぞれの手を表示
        print(f"プレイヤーAの手: {hands[player_a_hand]}")
        print(f"プレイヤーBの手: {hands[player_b_hand]}")
        
        # 勝敗判定
        if player_a_hand == player_b_hand:
            print("引き分け。ラウンドを再試行します。")
            round_count -= 1  # 引き分けの際はカウントを戻して再試行
        elif (player_a_hand == 0 and player_b_hand == 1) or (player_a_hand == 1 and player_b_hand == 2) or (player_a_hand == 2 and player_b_hand == 0):
            print("プレイヤーAの勝ち")
            a_wins += 1
        else:
            print("プレイヤーBの勝ち")
            b_wins += 1
        
        # 現在のスコアを表示
        print(f"現在のスコア: プレイヤーA {a_wins} - プレイヤーB {b_wins}")

    # 最終結果を表示
    if a_wins == 2:
        print("プレイヤーAが勝ちました！")
    else:
        print("プレイヤーBが勝ちました！")

