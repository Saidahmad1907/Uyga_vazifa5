from datetime import datetime

def check_date(sana1, sana2):
    sana1_obj = datetime.strptime(sana1, '%Y-%m-%d')
    sana2_obj = datetime.strptime(sana2, '%Y-%m-%d')
    
    farq = sana2_obj - sana1_obj
    kunlar_soni = farq.days
    
    return kunlar_soni

sana1 = '2024-07-01'
sana2 = '2024-07-19'

print(f"{sana1} va {sana2} orasida {check_date(sana1, sana2)} kun bor.")
