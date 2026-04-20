class RSRA:
    def __init__(self):
        pass
    def ruletable(self,train,obstacle,lever):
        if obstacle=="detected":
            return "Neutral","on","red"
        elif lever=="active":
            return "Active","on","green"
        elif train=="detected":
            return "Active", "off","green"
        else:
            return "Neutral","off","red"
agent=RSRA()
while True:
    t_sen = input("train (detected/no): ").lower()
    o_sen = input("obstacle (detected/no): ").lower()
    emg_lever = input("lever (active/neutral): ").lower()
    percept=(t_sen,o_sen,emg_lever)
    gate_arm,siren,t_signal=agent.ruletable(t_sen,o_sen,emg_lever)
    print(f"percept: {percept} -> action: ({gate_arm}, {siren}, {t_signal})\n")

    if input("do you want to exit? (y/n): ").lower() == 'y':
        break
