months, days = (
    '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12' 
), ('31', '29', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31')

for m, d in zip(months, days):
    for i in range(1, int(d)+1):
        dd = int(m+str(i).zfill(2))
        if 219 <= dd <= 520:
            sm = 'SPRING'
        elif 521 <= dd <= 822:
            sm = 'SUMMER'
        elif 823 <= dd <= 1121:
            sm = 'FALL'
        else:
            sm = 'WINTER'
        string = f", ('{m+str(i).zfill(2)}', '{sm}')"
        print(string)