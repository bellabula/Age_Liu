driving = input("請問你有開過車嗎(有/沒有)?")
if driving != '有' and driving != '沒有':
    print("請回答(有)或(沒有)")
    raise SystemExit #終止程式
age = input("請問你的年齡?")
age = int(age)
if driving == "有":
    if age >= 18:
        print('你通過測驗了')
    else:
        print('奇怪, 你怎麼會開過車')
else:
    if age < 18:
        print('很好 再過', 18-age, '年你就可以去考駕照啦')
    else:
        print('你可以去考駕照拉')