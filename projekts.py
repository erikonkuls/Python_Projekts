
from random import randint
import random

jautajums1={
"Kā sauce centimetra desmitdaļu a)milimetrs b)decimetrs c)kilometrs d)nanometrs":"A",
"Kurā kontinentā aug baobabi a)Eiropa b)Z-amerika c)Āfrika d)Āzija":"C",
"Ja tu skrien un apdzen cilvēku kurš ir 2. vietā kurā vietā tu tagad esi   a) 1  b) 3 c) 2  d)Es nevaru skriet ":"C",
"Kas ir cilvēka galvenais asinsrites orgāns  a) sirds  b) asisnsvadi c)plaušas  d)vēnas ":"A",
"Kurā valstī atrodas atrakciju parks'Legolande'  a)Somija  b)Zviedrija  c)Norvēģija  d)Dānija":"D",
"Kurā kontinentā atrodas lielākais tuksnesis a)Antarktīda b)Āzija c)Āfrika d)D-Amerika":"C",
"Kura ir Daugavas lielākā Pieteka a)Ogre  b)Aiviekste c)Aviekste  d)Pērse":"B",
"Meitenei bija 3 bumbieri bet vecmāmiņa iedeva vēl 3 reies vairāk cik meitenei ir bumbieri a)3  b)9  c)12  d)6":"C",
"Cik ir 3/5 no 75   a)15 b)35 c)45  d)55":"C",
"Cik dienu ir 504 stundas  a)10  b)21 c)7 d)30":"B",
"Kas ir smagāks 100kg cukurs vai Spalvas  a)neviens b)cukurs  c)spalvas d)Olafs":"A",
"Kura no šīm zivīm nav agēdāja a)Karpa b)Plaudis c)nezinu d)Forele ":"D",
"Kurā datumā svin lāčplēša dienu a)18.nov  b)11.nov c)24.dec  d)4.maijs":"B",
"Kāds ir zelta simbols ķīmijā a)Gl b)Zn c)W d)Au":"D",
"Cik ir 2/3 no 36 a)12 b)24 c)48 d)23":"B",
"Cik stārķu sugu ir latvijā a)1  b)2 c)3 d)4":"B",
"Kas ir pie debesī vērojamās krītošās zaviagznes a)komētas b)planētas c)meteorīti d)krītošā zvaigzne ":"C",
"Kāds ir glābšanas dienasta tel. nr.  a)007   b)911  c)112  d)9/11":"C",
"Kura no šīm ir Stobriņu sēne   a)Baravika b)Mušmire c)Gailene d)Beka ":"A",
"Kā sauc vielu kas padara augus zaļus kad tie uzņem saules gaismu  a)Citoplazma  b)Lizosoma c) Vakuola  d)Hlorofils":"D",
"Cik gada mēnešos ir 31 diena a)4   b)9  c)7  d)5":"C",
"Cik gara ir maratona distance a)45,5km  b) 42,195km  c)50km  d)21,1km ":"B",
"Cik plats ir peldbaseina celiņš a)2,5m  b)3m  c)3,5m d)1,75m":"A",
"Kādi ir lielākie koki pasaulē  a)Ozoli  b)Baobabi  c)Sekvojas  d)Priedes ":"C",
"Lielākais kaķis ir a)Kaķis b)Lauva c)Jaguārs  d)Tīģeris ":"D",
"Latvijas lielākais ezersi ir  a)Engure  b)Burtnieku c)Rāzna d)lubāna ":"D",
"Labākā redze pasaulē ir  a)Sunim  b)cilvēkam c)Leopardam  d)Ērglim ":"D",
"Mācību par augiem sauc   a)Anatomija b)Botānika c)zooloģija d)man vienalga ":"B",
"Braila rakstu izmanto a)nedzirdīgi cilvēki  b)neredzīgi cilvēki  c)garīgi atpalikuši cilvēki d)paralizēti cilvēki ":"B",
"Kādas ir pamatkrāsas  a) Balta, melna, pelēka  b) Balta, dzeltena, purpura  c)sarkana, zaļa, zila  d) sarkana, dzeltena, zila ":"C",
"Jebkuru daudzstūri var izveidot no   a)Trapecēm  b)Kvadrātiem  c) Trijstūriem  d) Heksagoniem ":"C",
}

jautajums2 = {
"Cik trilionu km garš ir Gaismas gads a)5.4  b)9.5  c)8.3  d) 12.9": "B",
"Kāds vārds ir uzrakstīts nepareizi katrā vārdnīcā a) Nepareizi b)koks c)Jānis d) Kuģis ": "A",
"Kura no šīm latviešu tautas dejām spējusi iekļūt Ginesa rekordu grāmatā? a) Es mācēju danci vest b)Sudmaliņas c)Gatves deja d) Tūdaliņ tagadiņ" : "C",
"Par kura supervaroņa draugu tiek uzskatīts mērkaķēns Beppo? a) Kaķsievietes b) Supermena c) Zirnekļcilvēka d) Betmena": "B",
"Kens Estons bija viens no izcilākajiem pagājušā gadsimta futbola tiesnešiem pasaulē. Ko viņš ieviesa futbola spēles tiesāšanā? a) 11m soda sitienu b)Kompensācijas laiku c) Dzēriena pauzi d)Sarkanās un dzeltenās kartītes": "D",
"Kurā no Latvijas novadiem atrodas ciems Gambija? a) Kuldīgas b) Sabiles c) Cēsu d)Talsu  ":"D",
" Pirmie gaisa balona pasažieri bija trīs dzīvnieki. Kurš no šiem te neiederas? a) Suns b) Gailis c) Aita d) Pīle " : "A",
"Uz olimpiskā karoga attēloti pieci apļi. Kādā krāsā nav neviens no apļiem? a) Dzeltenā b) Oranžā c)Zilā d) Melnā":"B",
"Kurš no šiem terminiem tiek lietots gan medicīnā, gan mūzikā? a)Triole  b)Uzraudzība  c) Bemols  d) Perkusija": "D",
" Ko pēta malakologi? a) Sliekas  b) Mikroorganismus c) Gliemežus   d) Tauriņus  ":"C",
"Cik gadu vecumā Volfgangs Amadejs Mocarts sāka komponēt savus pirmos skaņdarbus? a) 3 gadu b) 5 gadu c) 11 gadu d) 8 gadu":"B",
"1547, kurš kļuva par 1. Krievijas caru? a) Ivans III Lielais  b) V.Putins  c) Ivans IV  d) Ivans II Skaistais  ":"C",
"Ja indiešu restorānā pasūtīsiet “murgh” no ēdienkartes, kādu gaļu jūs saņemsiet?  a) Vistu  b) Lielopu  c) Cūkas  d) Mājdzīvnieku " :"A",
"Kurām sugām starp sauszemes dzīvniekiem ir vislielākās acis? a)Zilonis   b)Žirafe   c)Strauss   d) Tīgeris  " : "C",
"Kurš ir vienīgais karalis kāršu kavā bez ūsām?  a)Kārava karalis  b)kreica karalis  c)Pīķa karalis  d) Erca karalis " :"D",
"Kurā valstī katru gadu notiek pasaules čempionāts sievu nēsāšanai a)Norvēģijā  b)Latvijā  c)Igaunijā  d)Somijā ": "D",
"Cik gadu vecumā tik sists Jēzus Kristus krustā a)33 b)25  c)35  d)30":"A",
"Cik zobu ir pieaugušam cilvēkam  a) 36  b)32  c) 34  d)30 ":"B",
"Kas ir visgarākais a)pēda b)metrs c)Jūdze  d) kilometrs ":"C",
"Cietākais dārgakmens pasaulē ir   a)Dimants b)Briljants  c)Pērle d)Zelts ":"A",
"Svarcelšanas stienis bez diskiem sver  a)10kg b)20kg c)25kg d)30kg  ":"B",
"Visātrākais zīdītājs pasaulē ir a)Āzijas gazele  b)Zirgs c) Gepards  d)Leopards ":"C",
"Kādu ātrumu var attīstī Burniekzivs  a)20km/h  b) 45km/h  c)55km/h  d)100km/h":"D",
"Skābekļa simbols periodiskajā tabulā ir  A) O  b)N  c)Sc  d) Li":"A",
"Zinātnieki smalkus objektus pēta ar   a)Mikroskopu  b)Teleskopu  c) stetoskopu  d) pavaskops":"A",
"Grieķu alfabēta trešais burrts ir  a)Alfa b)Delta c)Omega d)Gamma ":"D",
"Kura ir vispirktākā grāmata pasaulē  a)Harijs poters   b)harijs poters 2   c) Bībele  d)Vējiem līdzi":"C",
"Kurā valstī izdomāja tējas maisiņu  a)ASV  b)Ķīnā  c)Japānā  d)Francijā ":"A",
"Bulgārijas galvaspilsēta ir  a) Taiga b)Sofija  c)Timpu   d)Varšava ":"B",
"Kā sauc baltos asins ķermenīšus   a)eritrocīti  b) Trombocīti  c)Leikocīti  d)Plazma ":"C",
"Kāds ir kalcija simbols periodiskajā tabulā  a)K  b) Ca  c)Cl  d)Ag":"B"
}
jautajums3={
"Nosauciet Latvijas garāko Ezeru a) Lubānas b) Engures  c) Burtnieku d) Puzes" :"B",
"Kurā gadā Senejā Grieķijā notika pirmās olimpiskās spēles a)753.g.p.m.ē   ba)755.g.p.m.ē) c)7776.g.p.m.ē  d)534.g.p.m.ē" :"C",
"Pirmo alfabētu izgudroja senejā Divupē a)jā  b)nē  c) nezinu  d)Vienalga" :"B",
"Nosauciet laika mērvienību SI sistēmai a)minūtes b)stundas c)milisekundes d) sekundes":"D",
"Kā sauc bruņinieku ordeni, kuru 1202. gadā nodibināja bīskaps Alberts a)Livonijas Ordenis b)Zobeņbrāļu Ordenis c)Teitoņu ordesnis d)Alberts nenodibināja ordeni":"B",
"cik ilgā laikā saules gaisma sasniedz zemi  a)8min b)8min 20 sek  c)8min 43 sek d)9min":"B",
"Kurā gadā notika saules kauja a)1236.g  b)1215.g  c)1576.g  d)1387.g":"A",
"Kurai valstij pieder Grenlande  a)Islandei  b)Norvēģijai c) Igaunijai  d)Dānijai ":"D",
"Nosauc ceturto lielāko salu pasaulē a)Grenlande  b)Islande  c)Madagaskara  d) Austrālija":"C",
"Cik rāpuļu sugas ir latvijā a)5  b)7  c)9  d)11":"B",
"Cik virsotņu ir taisnstūra skaldnim a)4  b)6  c)8  d)10":"C",
"Kurā gadā Latvija iestājās Eiropas savienībā  a)2000 b)2004 c)2014 d)2024":"B",
"Kurš Latvijā dzīvojošs putns mazuļus perē ziemas mēnešos a)vārna  b)kaija  c)krustknābis  d)stārķis ":"C",
"Kā sauc zemes virsmai tuvāko pazemes ūdeņu slāni a)gruntsūdens  b)ūdens krātuve c) virsūdesns d)nezinu/neinteresē":"A",
"Kurā gadā dibināts Teiču dabas rezervāts  a)1980  b)1982  c)1999  d)1902":"B",
"Cik auksts ir absolūtā nulle pēc celsija a) -117,45  b)-543,32  c)0  d)-273,15":"D",
"Cilvēka ķermenī garākais nervs ir  a)Vidusnervs  b)Sēžas  c)Augšstilba  d)Nervs kuru stiepj skola ":"B",
"Cik asiņu ir cilvēka organismā  a)3L  b) 5L  c) 7L  d)9L":"B",
"2003 gada hokeja čempioni ir a)Kanāda b)Zviedrija c)Latvija d)Somija ":"A",
"Kura is pasaules vecākā pilsēta  a)Jērika  b)Roma  c)Maskava d)Atēnas ":"A",
"Ja kvadrāta perimetrs ir 24cm cik kvadrātcentimetri ir tā laukums a)6  b)12  c)36  d)24":"C",
"Pirms Everests tika atklāts kura bija uagstākā virsotne uz pasaules  a)Lodze  b)Kančendžanga c)Manaslu d)Everests":"D",
"Pitagors neēda pupiņas jo vinām tās  a)viņam tās negaršoja b)viņš uzskatīja ka tajās ir dvēsele  c)viņš nezināja kas tas tāds ir  d) viņam likās tās indīgas ":"B",
"Vidējais puieauguša cilvēka smadzeņu svars ir   a)1.6kg b)2kg  c)2,34kg   d)1,3kg":"D",
"Kurā gadā tika dibināta holivuda  a)1907.g  b)1910.g  c)1915.g d)1920.g ":"A",
"Antofobija ir  a)Bailes no puķēm  b)bailes no anatomijas  c)bailes no lietus d)bailes no stikla pudelēm":"A",
"Stafetes kociņs jānodod noteiktā metru zonā cik gara ir tā zona  a)5m  b)10m  c)20m  d)15m":"C",
"Pirmais pulkstenis ar dzeguzi tika izgudruts kurā valstī  a)Latvijā  b)Anglijā  c)Vācijā  d)Itālijā ":"C",
"Kāda ir Liepājas pilsētas himmna  a)'Pilsēta kurā piedzimst vējs'  b) 'Liedagā'  c)'Liepājai'  d)mini ":"A",
"Atoma centrālā daļa ir  a) elektroni b) Protoni c)neitroni  d)kodols  ":"D",
"Kas ir eritrocīti  a)sarkanie asisns ķermenīši b)baltie asins ķermenīši c)limfmezgli d)caurspīdīgie asins ķermenīši ":"A",

}




atslegas1= list(jautajums1.keys())
atslegas2= list(jautajums2.keys())
atslegas3= list(jautajums3.keys())
spiedšeit=("{https://ltv.lsm.lv/raidijumi/gudrs-vel-gudraks/pieteikuma-anketa}")
url=({spiedšeit})
papildiespeja=["A","B","C","D"]
skaits = 0
pareizas_atbildes = 0
message=("Lai atbildēt uz jautājumu tev ir jāizvēlās viena no dotajām atbildēm ierakstot tikai atbilžu varianta burtu \n Lai izmantotu papildiespēju paprasīt ko saka māte google uzraksti 'papildiespeja' \n lai beigtu spēli nospied burtu 'q'! \n Kādu grūtības pakāpi tu vēlies?: Viegls(1) Viduvējs(2) vai Grūts(3) ieraksti ciparu ")
print(message)
x = input()
while True:
    
    if x== "2":
        gadijums = randint(0, len(atslegas2)-1)
    

        atbilde = input( {atslegas2[gadijums]})
        if atbilde.lower() == "q":
            print("Paldies par spēli!")
            print(f"Tu atbildēji pareizi uz {pareizas_atbildes} / {skaits}")
        
            print("Tagad tu esi gatavs doties uz grūto līmeni!")
            break
        elif atbilde.lower()=="papildiespeja":
            print(jautajums2[atslegas2[gadijums]])
            pareizas_atbildes+=1
            skaits+=1
            
        elif atbilde.capitalize() == jautajums2[atslegas2[gadijums]]:
            print("pareizi!")
            pareizas_atbildes +=1
            skaits+=1
        else:
            skaits +=1
            print(f"Nepareizi, pareizā atbilde bija {jautajums2[atslegas2[gadijums]]}")
            
            
    elif x=="1":
        gadijums = randint(0, len(atslegas1)-1)
        atbilde = input( {atslegas1[gadijums]})
        if atbilde.lower() == "q":
            print("Paldies par spēli!")
            print(f"Tu atbildēji pareizi uz {pareizas_atbildes} / {skaits}")
            print("Tagad tu esi gatavs doties uz viduvējo līmeni!")
        elif atbilde.lower()=="papildiespeja":
            print(jautajums1[atslegas1[gadijums]])
            pareizas_atbildes+=1
            skaits+=1
            
        elif atbilde.capitalize() == jautajums1[atslegas1[gadijums]]:
            print("pareizi!")
            pareizas_atbildes +=1
            skaits+=1
        else:
            skaits +=1
            print(f"Nepareizi, pareizā atbilde bija {jautajums1[atslegas1[gadijums]]}")
            
            
    else:
        gadijums = randint(0, len(atslegas3)-1)
        atbilde = input( {atslegas3[gadijums]})
        if atbilde.lower() == "q":
            print("Paldies par spēli!")
            print(f"Tu atbildēji pareizi uz {pareizas_atbildes} / {skaits}")
            print("Tagad tu esi gatavs priekš gudrs vēl gudrāks konkurs")
            print("Neaizmirsti pieteikties uz gudrs vēl gudrāks - Dodies uz šo linku!")
            print(url)
            break
        elif atbilde.lower()=="papildiespeja":
            print(jautajums3[atslegas3[gadijums]])
            pareizas_atbildes+=1
            skaits+=1
            
        elif atbilde.capitalize() == jautajums3[atslegas3[gadijums]]:
            print("pareizi!")
            pareizas_atbildes +=1
            skaits+=1
        else:
            skaits +=1
            print(f"Nepareizi, pareizā atbilde bija {jautajums3[atslegas3[gadijums]]}")
    
            
            