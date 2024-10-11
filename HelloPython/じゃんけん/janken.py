import random
def janken():
    # ぐー, ちょき, パーをそれぞれ0, 1, 2として定義
    hands = {0: "グー", 1: "チョキ", 2: "パー"}
    
    # プレイヤーAとBの手をランダムに決定
    player_a_hand = random.randint(0, 2)
    player_b_hand = random.randint(0, 2)
    
    # それぞれの手を表示
    print(f"プレイヤーAの手: {hands[player_a_hand]}")
    print(f"プレイヤーBの手: {hands[player_b_hand]}")
    
    # 勝敗判定
    if player_a_hand == player_b_hand:
        print("引き分け")
    elif (player_a_hand == 0 and player_b_hand == 1) or (player_a_hand == 1 and player_b_hand == 2) or (player_a_hand == 2 and player_b_hand == 0):
        print("プレイヤーAの勝ち")
    else:
        print( "プレイヤーBの勝ち")