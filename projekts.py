

#Šajā semestrī Jānītim ir jāpiedalās gudrs un vēl gudrāks, bet viņš nav sagatavojies un tagad ir pats pēdējais laiks, lai
# sagatavotos gudrs vel gudraks.

#Jānīša mamma - tikai 2 dienas un tik daudz ir jāzin lai varētu konkurēt gudrs vēl gudrāks, lūdzu palīdzi jānītim sagatavoties.

#izmanot papildiespējas kā spēlē do you want to be be a millioniare (50/50) (zvans mātei google jeb pareiza atbilde)
# (paprasa iedomātai tautai jeb izvēlas random atbildi) pievienot laika limitu 
# 

#https://www.lsm.lv/raksts/arpus-etera/speles/tests-gudrs-vel-gudraks-izaicina--parbaudi-savas-zinasanas.a434254/

from random import randint

jautajums = {
"Cik trilionu km garš ir Gaismas gads (izvēlies burtu) a)5.4  b)9.5  c)8.3  d) 12.9": "B",
"Kāds vārds ir uzrakstīts nepareizi katrā vārdnīcā a) Nepareizi b)koks c)Jānis d) Kuģis ": "A",
"Kura no šīm latviešu tautas dejām spējusi iekļūt Ginesa rekordu grāmatā? a) Es mācēju danci vest b)Sudmaliņas c)Gatves deja d) Tūdaliņ tagadiņ" : "C",
"Par kura supervaroņa draugu tiek uzskatīts mērkaķēns Beppo? a) Kaķsievietes b) Supermena c) Zirnekļcilvēka d) Betmena": "B",
"Kens Estons bija viens no izcilākajiem pagājušā gadsimta futbola tiesnešiem pasaulē. Ko viņš ieviesa futbola spēles tiesāšanā? a) 11m soda sitienu b)Kompensācijas laiku c) Dzēriena pauzi d)Sarkanās un dzeltenās kartītes": "D",
"Kurā no Latvijas novadiem atrodas ciems Gambija? a) Kuldīgas b) Sabiles c) Cēsu d)Talsu  ":"D",
" Pirmie gaisa balona pasažieri bija trīs dzīvnieki. Kurš no šiem te neiederas? a) Suns b) Gailis c) Aita d) Pīle " : "A",
"Uz olimpiskā karoga attēloti pieci apļi. Kādā krāsā nav neviens no apļiem? a) Dzeltenā b) Oranžā c)Zilā d) Melnā":"B",
"Kurš no šiem terminiem tiek lietots gan medicīnā, gan mūzikā? a)Triole  b)Uzraudzība  c) Bemols  d) Perkusija": "D",
" Ko pēta malakologi? a) Sliekas  b) Mikroorganismus c) Gliemežus   d) Tauriņus  ":"C"
}
atslegas= list(jautajums.keys())

skaits = 0
pareizas_atbildes = 0
print("Lai atbildēt uz jautājumu tev ir jāizvēlās viena no dotajām atbildēm ierakstot tikai atbilžu varianta burtu")
while True:
    gadijums = randint(0, len(atslegas)-1)

    atbilde = input( {atslegas[gadijums]})
    if atbilde.lower() == "q":
        print("Paldies par spēli!")
        break
    elif atbilde.capitalize() == jautajums[atslegas[gadijums]]:
        print("pareizi!")
        pareizas_atbildes +=1
    else:
        print("Ej mācīties!")
    skaits +=1
print(f"Tu atbildēji pareizi uz {pareizas_atbildes} / {skaits}")