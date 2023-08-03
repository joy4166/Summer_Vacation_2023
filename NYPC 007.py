class Player():
    def __init__(self, position, overall, price, pay, name):
        self.position = position
        self.overall = int(overall)
        self.price = price
        self.pay = pay
        self.name = name

    def get_position(self):
        return self.position

    def get_overall(self):
        return self.overall

    def get_price(self):
        return self.price

    def get_pay(self):
        return self.pay

    def get_name(self):
        return self.name


N, M = map(int, input().split())
player_list = []
gk_list = []
df_list = []
mf_list = []
fw_list = []
for _ in range(N):
    player_info = input().split()
    player_list.append(Player(player_info[0], player_info[1], player_info[2], player_info[3], player_info[4]))

for player in player_list:
    if player.get_position() == "GK":
        gk_list.append(player)
    elif player.get_position() == "DF":
        df_list.append(player)
    elif player.get_position() == "MF":
        mf_list.append(player)
    else:
        fw_list.append(player)

gk_overall = sorted(gk_list, key=lambda x: x.get_overall(), reverse=True)
df_overall = sorted(df_list, key=lambda x: x.get_overall(), reverse=True)
mf_overall = sorted(mf_list, key=lambda x: x.get_overall(), reverse=True)
fw_overall = sorted(fw_list, key=lambda x: x.get_overall(), reverse=True)

total_overall = 0
try:
    total_overall = gk_overall[0].get_overall() + df_overall[0].get_overall() + df_overall[1].get_overall() + df_overall[2].get_overall() + df_overall[3].get_overall()\
        + mf_overall[0].get_overall() + mf_overall[1].get_overall() + mf_overall[2].get_overall() + mf_overall[3].get_overall() + mf_overall[4].get_overall()\
        + fw_overall[0].get_overall()
except:
    total_overall = -1
print(total_overall)
