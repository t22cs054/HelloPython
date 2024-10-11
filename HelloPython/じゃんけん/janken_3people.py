import random

def janken_three_players():
    # グー, チョキ, パーをそれぞれ0, 1, 2として定義
    hands = {0: "グー", 1: "チョキ", 2: "パー"}
    
    # プレイヤーA, B, Cの手をランダムに決定
    player_a_hand = random.randint(0, 2)
    player_b_hand = random.randint(0, 2)
    player_c_hand = random.randint(0, 2)
    
    # それぞれの手を表示
    print(f"プレイヤーAの手: {hands[player_a_hand]}")
    print(f"プレイヤーBの手: {hands[player_b_hand]}")
    print(f"プレイヤーCの手: {hands[player_c_hand]}")
    
    # 全員が同じ手の場合は引き分け
    if player_a_hand == player_b_hand == player_c_hand:
        print("全員が同じ手で引き分けです。")
    
    # 勝者を判定する関数
    def is_winner(hand, others):
        return all((hand == 0 and o == 1) or (hand == 1 and o == 2) or (hand == 2 and o == 0) for o in others)
    
    # 各プレイヤーの手を基に勝者を判定
    if is_winner(player_a_hand, [player_b_hand, player_c_hand]):
        print("プレイヤーAが勝ちました！")
    elif is_winner(player_b_hand, [player_a_hand, player_c_hand]):
        print("プレイヤーBが勝ちました！")
    elif is_winner(player_c_hand, [player_a_hand, player_b_hand]):
        print("プレイヤーCが勝ちました！")
    else:
        print("引き分けです。")