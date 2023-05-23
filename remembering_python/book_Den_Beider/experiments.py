minutes, start_hours, start_minutes = int(input()), int(input()), int(input())

res = start_hours * 60 + start_minutes + minutes
res_h = res // 60
res_m = res % 60
while res_h > 24:
    res_h -= 24
print(res_h, res_m)
