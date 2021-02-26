isciler=[
    {
        'ad':'Memmed',
        'maas':'600AZN'
    },
    {
        'ad':'Cemile',
        'maas':'500AZN'
    },
    {
        'ad':'Saleh',
        'maas':'1200AZN'
    },
    {
        'ad':'Gulnar',
        'maas':'980AZN'
    },
    {
        'ad':'Aynur',
        'maas':'1380AZN'
    }
]
# Maaş listi almaq
def getSalary(isciler):
    salaries = []
    for isci in isciler:
        salary = isci['maas'][:isci["maas"].index("AZN")]
        salaries.append(salary)
    return salaries

print(getSalary(isciler))
# Cəmlərini hesablamaq
def sumOfSalary(isciler):
    sum = 0
    for salary in getSalary(isciler):
       
        sum+=int(salary)
    return sum
print(sumOfSalary(isciler))
# 18% vergidən sonrakı maaşlar
def calculateSalariesAfterTax(isciler,tax):
    afterTax = []
    for salary in getSalary(isciler):
        salary= float(salary)-float(salary)*tax
        afterTax.append(salary)
    return afterTax
print(calculateSalariesAfterTax(isciler,0.18))
# Maaş ortalaması ortalamadan yüksək işçiləri tapmaq

def findBetterThanAverage(isciler):
    salaries = getSalary(isciler)
    avg=sumOfSalary(isciler)/len(salaries)
   
    for isci in isciler:
        isci["maas"]=int(isci["maas"][:-3])
        if isci["maas"]>avg:
            print(isci["ad"])
findBetterThanAverage(isciler)
    

