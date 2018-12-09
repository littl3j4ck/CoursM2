#Script HERO de alexandre Mondani EII17-19#
#Pour Programmation avancé#
import math
#=====================================#
#creation de la classe Personnage
class Character:
        Name = "blank"
        Cape = False
        Money = False
        Tech = False
        Power = "NON"
#======================================#
#initialisation des 14 personnages
List_Hero          = []
List_Gain           =[]
SpiderBoy           = Character()
SpiderBoy.Name      = "spider-man"
SpiderBoy.Power     = "OUI"
SpiderBoy.Hero      = True
List_Hero.append(SpiderBoy)
Poutine             = Character()
Poutine.Name        = "poutine"
Poutine.Money       = True
Poutine.Tech        = True
Poutine.Power       = "?"
Poutine.Hero        = False
List_Hero.append(Poutine)
Batman              = Character()
Batman.Name         = "batman"
Batman.Cape         = True
Batman.Money        = True
Batman.Tech         = True
Batman.Hero         = True
List_Hero.append(Batman)
Joker               = Character()
Joker.Name          = "joker"
Joker.Money         = True
Joker.Tech          = True
Joker.Hero          = False
List_Hero.append(Joker)
Rorcha              = Character()
Rorcha.Name         = "Rorcha"
Rorcha.Power        = "?"
Rorcha.Hero         = True
List_Hero.append(Rorcha)
Deadpoule           = Character()
Deadpoule.Name      = "deapool"
Deadpoule.Tech      = True
Deadpoule.Power     = "OUI"
Deadpoule.Hero      = True
List_Hero.append(Deadpoule)
Merckel             = Character()
Merckel.Name        = "merckel"
Merckel.Money       = True
Merckel.Tech        = True
Merckel.Hero        = False
List_Hero.append(Merckel)
Artagnan            = Character()
Artagnan.Name       = "d'artagnan"
Artagnan.Cape       = True
Artagnan.Hero       = False
List_Hero.append(Artagnan)
Cesar               = Character()
Cesar.Name          = "césar"
Cesar.Cape          = True
Cesar.Money         = True
Cesar.Tech          = True
Cesar.Hero          = False
List_Hero.append(Cesar)
Telsa               = Character()
Telsa.Name          = "tesla"
Telsa.Tech          = True
Telsa.Power         = "?"
Telsa.Hero          = True
List_Hero.append(Telsa)
Edison              = Character()
Edison.Name         = "edison"
Edison.Money        = True
Edison.Tech         = True
Edison.Hero         = False
List_Hero.append(Edison)
Homer               = Character()
Homer.Name          ="homer"
Homer.Hero          = False
List_Hero.append(Homer)
Sherlock            = Character()
Sherlock.Name       = "sherlock"
Sherlock.Money      = True
Sherlock.Power      = "?"
Sherlock.Hero       = True
List_Hero.append(Sherlock)
Moriarty            = Character()
Moriarty.Name       = "Moriarty"
Moriarty.Money      = True
Moriarty.Tech       = True
Moriarty.Power      = "?"
Moriarty.Hero       = False
List_Hero.append(Moriarty)
#==================================#

NbrHero = 0
NoCape = 0
Cape = 0

NoMoney = 0
Money = 0

NoTech = 0
Tech = 0

NoPower = 0
Power = 0
MyBePower = 0

Hero = 0
NoHero = 0

while NbrHero < len(List_Hero):
    if List_Hero[NbrHero].Cape == False:
        NoCape += 1
    else:
        Cape += 1
    
    if List_Hero[NbrHero].Money == False:
        NoMoney += 1
    else:
        Money += 1

    if List_Hero[NbrHero].Tech == False:
        NoTech += 1
    else:
        Tech += 1
    
    if List_Hero[NbrHero].Power == "OUI":
        Power += 1
    elif List_Hero[NbrHero].Power =="?":
        MyBePower += 1
    else:
        NoPower += 1

    if List_Hero[NbrHero].Hero == False:
        NoHero += 1
    else:
        Hero += 1
    NbrHero += 1


#Calcul des entropies

EntropyHero = -((Hero/NbrHero)*(math.log2(Hero/NbrHero))) - ((NoHero/NbrHero)*(math.log2(NoHero/NbrHero)))
EntropyHero = round(EntropyHero,2)


#Calcul Gain Hero/Money
NbrHero = 0
HeroMoney = 0
NoHeroMoney = 0
HeroNoMoney = 0
NoHeroNoMoney = 0

while NbrHero < len(List_Hero):
    if List_Hero[NbrHero].Hero == True and List_Hero[NbrHero].Money == True:
        HeroMoney += 1
    elif List_Hero[NbrHero].Hero == False and List_Hero[NbrHero].Money == True:
        NoHeroMoney += 1
    elif List_Hero[NbrHero].Hero == True and List_Hero[NbrHero].Money == False:
        HeroNoMoney += 1
    else :
        NoHeroNoMoney += 1
    NbrHero +=1

EntropyYesHeroYesMoney = ((HeroMoney/(HeroMoney+NoHeroMoney))*(math.log2(HeroMoney/(HeroMoney+NoHeroMoney))))
EntropyNoHeroYesMoney = ((NoHeroMoney/(HeroMoney+NoHeroMoney))*(math.log2(NoHeroMoney/(HeroMoney+NoHeroMoney))))

EntropyYesHeroNoMoney = ((HeroNoMoney/(HeroNoMoney+NoHeroNoMoney))*(math.log2(HeroNoMoney/(HeroNoMoney+NoHeroNoMoney))))
EntropyNoHeroNoMoney = ((NoHeroNoMoney/(HeroNoMoney+NoHeroNoMoney))*(math.log2(NoHeroNoMoney/(HeroNoMoney+NoHeroNoMoney))))
if HeroMoney < NoHeroMoney:
    EntropyHeroMoney1 = -EntropyYesHeroYesMoney-EntropyNoHeroYesMoney
else:
    EntropyHeroMoney1 = -EntropyNoHeroYesMoney-EntropyYesHeroYesMoney

if HeroNoMoney < NoHeroNoMoney:
    EntropyHeroMoney2 = -EntropyYesHeroNoMoney-EntropyNoHeroNoMoney
else:
    EntropyHeroMoney2 = -EntropyNoHeroNoMoney-EntropyYesHeroNoMoney

EntropyHeroMoney = (((HeroMoney+NoHeroMoney)/NbrHero)*EntropyHeroMoney1)+(((HeroNoMoney+NoHeroNoMoney)/NbrHero)*EntropyHeroMoney2)
EntropyHeroMoney = round(EntropyHeroMoney,2)

GainHeroMoney = EntropyHero-EntropyHeroMoney
List_Gain.append(GainHeroMoney)

#Calcul Gain Hero/Cape
NbrHero = 0
HeroCape = 0
NoHeroCape = 0
HeroNoCape = 0
NoHeroNoCape = 0

while NbrHero < len(List_Hero):
    if List_Hero[NbrHero].Hero == True and List_Hero[NbrHero].Cape == True:
        HeroCape += 1
    elif List_Hero[NbrHero].Hero == False and List_Hero[NbrHero].Cape == True:
        NoHeroCape += 1
    elif List_Hero[NbrHero].Hero == True and List_Hero[NbrHero].Cape == False:
        HeroNoCape += 1
    else :
        NoHeroNoCape += 1
    NbrHero +=1

EntropyYesHeroYesCape = ((HeroCape/(HeroCape+NoHeroCape))*(math.log2(HeroCape/(HeroCape+NoHeroCape))))
EntropyNoHeroYesCape = ((NoHeroCape/(HeroCape+NoHeroCape))*(math.log2(NoHeroCape/(HeroCape+NoHeroCape))))

EntropyYesHeroNoCape = ((HeroNoCape/(HeroNoCape+NoHeroNoCape))*(math.log2(HeroNoCape/(HeroNoCape+NoHeroNoCape))))
EntropyNoHeroNoCape = ((NoHeroNoCape/(HeroNoCape+NoHeroNoCape))*(math.log2(NoHeroNoCape/(HeroNoCape+NoHeroNoCape))))

if HeroCape < NoHeroCape:
    EntropyHeroCape1 = -EntropyYesHeroYesCape-EntropyNoHeroYesCape
    
else:
    EntropyHeroCape1 = -EntropyNoHeroYesCape-EntropyYesHeroYesCape



if HeroNoCape < NoHeroNoCape:
    EntropyHeroCape2 = -EntropyYesHeroNoCape-EntropyNoHeroNoCape
else:
    EntropyHeroCape2 = -EntropyNoHeroNoCape-EntropyYesHeroNoCape

EntropyHeroCape = (((HeroCape+NoHeroCape)/NbrHero)*EntropyHeroCape1)+(((HeroNoCape+NoHeroNoCape)/NbrHero)*EntropyHeroCape2)
EntropyHeroCape = round(EntropyHeroCape,2)

GainHeroCape = EntropyHero-EntropyHeroCape
GainHeroCape = round(GainHeroCape,2)
List_Gain.append(GainHeroCape)

#gain tech/heros

NbrHero = 0
HeroTech = 0
NoHeroTech = 0
HeroNoTech = 0
NoHeroNoTech = 0

while NbrHero < len(List_Hero):
    if List_Hero[NbrHero].Hero == True and List_Hero[NbrHero].Tech == True:
        HeroTech += 1
    elif List_Hero[NbrHero].Hero == False and List_Hero[NbrHero].Tech == True:
        NoHeroTech += 1
    elif List_Hero[NbrHero].Hero == True and List_Hero[NbrHero].Tech == False:
        HeroNoTech += 1
    else :
        NoHeroNoTech += 1
    NbrHero +=1


EntropyYesHeroYesTech = ((HeroTech/(HeroTech+NoHeroTech))*(math.log2(HeroTech/(HeroTech+NoHeroTech))))
EntropyNoHeroYesTech = ((NoHeroTech/(HeroTech+NoHeroTech))*(math.log2(NoHeroTech/(HeroTech+NoHeroTech))))

EntropyYesHeroNoTech = ((HeroNoTech/(HeroNoTech+NoHeroNoTech))*(math.log2(HeroNoTech/(HeroNoTech+NoHeroNoTech))))
EntropyNoHeroNoTech = ((NoHeroNoTech/(HeroNoTech+NoHeroNoTech))*(math.log2(NoHeroNoTech/(HeroNoTech+NoHeroNoTech))))

if HeroTech < NoHeroTech:
    EntropyHeroTech1 = -EntropyYesHeroYesTech-EntropyNoHeroYesTech
    
else:
    EntropyHeroTech1 = -EntropyNoHeroYesTech-EntropyYesHeroYesTech

if HeroNoTech < NoHeroNoTech:
    EntropyHeroTech2 = -EntropyYesHeroNoTech-EntropyNoHeroNoTech
else:
    EntropyHeroTech2 = -EntropyNoHeroNoTech-EntropyYesHeroNoTech

EntropyHeroTech = (((HeroTech+NoHeroTech)/NbrHero)*EntropyHeroTech1)+(((HeroNoTech+NoHeroNoTech)/NbrHero)*EntropyHeroTech2)
EntropyHeroTech = round(EntropyHeroTech,2)

GainHeroTech = EntropyHero-EntropyHeroTech
GainHeroTech = round(GainHeroTech,2)
List_Gain.append(GainHeroTech)
#Gain hero/pouvoir

NbrHero = 0
HeroPower = 0
NoHeroPower = 0
HeroNoPower = 0
NoHeroNoPower = 0
HeroMBPower = 0
NoHeroMBPower = 0

while NbrHero < len(List_Hero):
    if List_Hero[NbrHero].Hero == True and List_Hero[NbrHero].Power == "OUI":
        HeroPower += 1
    elif List_Hero[NbrHero].Hero == False and List_Hero[NbrHero].Power == "OUI":
        NoHeroPower += 1
    elif List_Hero[NbrHero].Hero == True and List_Hero[NbrHero].Power == "NON":
        HeroNoPower += 1
    elif List_Hero[NbrHero].Hero == False and List_Hero[NbrHero].Power == "NON":
        NoHeroNoPower += 1
    elif List_Hero[NbrHero].Hero == True and List_Hero[NbrHero].Power == "?":
        HeroMBPower += 1
    else:
        NoHeroMBPower +=1
    NbrHero +=1

EntropyYesHeroYesPower = ((HeroPower/(HeroPower+NoHeroPower))*(math.log2(HeroPower/(HeroPower+NoHeroPower))))
if NoHeroPower > 0 :
    EntropyNoHeroYesPower = ((NoHeroPower/(HeroPower+NoHeroPower))*(math.log2(NoHeroPower/(HeroTech+NoHeroPower))))
else :
    EntropyNoHeroYesPower = 0
EntropyYesHeroNoPower = ((HeroNoPower/(HeroNoPower+NoHeroNoPower))*(math.log2(HeroNoPower/(HeroNoPower+NoHeroNoPower))))
EntropyNoHeroNoPower = ((NoHeroNoPower/(HeroNoPower+NoHeroNoPower))*(math.log2(NoHeroNoPower/(HeroNoPower+NoHeroNoPower))))

EntropyYesHeroMBPower = ((HeroMBPower/(HeroMBPower+NoHeroMBPower))*(math.log2(HeroMBPower/(HeroMBPower+NoHeroMBPower))))
EntropyNoHeroMBPower =((NoHeroMBPower/(NoHeroMBPower+HeroMBPower))*(math.log2(NoHeroMBPower/(HeroMBPower+NoHeroMBPower))))

if HeroPower < NoHeroPower:
    EntropyHeroPower1 = -EntropyYesHeroYesPower-EntropyNoHeroYesPower
    
else:
    EntropyHeroPower1 = -EntropyNoHeroYesPower-EntropyYesHeroYesPower

if HeroNoPower < NoHeroNoPower:
    EntropyHeroPower2 = -EntropyYesHeroNoPower-EntropyNoHeroNoPower
else:
    EntropyHeroPower2 = -EntropyNoHeroNoPower-EntropyYesHeroNoPower
if NoHeroMBPower < HeroMBPower:
    EntropyHeroPower3 = -EntropyNoHeroMBPower-EntropyYesHeroMBPower
else:
    EntropyHeroPower3= -EntropyYesHeroMBPower-EntropyNoHeroMBPower

EntropyHeroPower = (((HeroPower+NoHeroPower)/NbrHero)*EntropyHeroPower1)+(((HeroNoPower+NoHeroNoPower)/NbrHero)*EntropyHeroPower2)+(((HeroPower+NoHeroPower)/NbrHero)*EntropyHeroPower3)
EntropyHeroPower = round(EntropyHeroPower,2)

GainHeroPower = EntropyHero-EntropyHeroPower
GainHeroPower = round(GainHeroPower,2)
List_Gain.append(GainHeroPower)






