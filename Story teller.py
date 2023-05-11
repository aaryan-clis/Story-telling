import random 
when = ['11 dec' ,'20 june ' , 'yestarday' , 'Today']
who = ['Thanos ',  'Loki' , ' ultron ' , 'Gorr' ]
name = ['Aaryan' , 'Iron man' , 'Thor' ,'Cap america' ]
address = ['Space' , 'Asguard' , 'Moon' , 'Earth']
act = ['ate burger' ,'played football ','hangout','played Ps5 ' ]

print(random.choice(when) + ' ,' + random.choice(who) + ' went to ' + random.choice(address) + ' and ' +  random.choice(act) + ' with '+ random.choice(name) )