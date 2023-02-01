import openpyxl
from openpyxl import Workbook , load_workbook 


book = load_workbook("dars.xlsx")
sheet = book.active

birad = '<b> 1-A sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["D10"].value+'\n2-dars: '+sheet["D11"].value+'\n3-dars: '+sheet["D12"].value+'\n4-dars: '+sheet["D13"].value+'</i>'
biras = '<b> 1-A sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["D18"].value+'\n2-dars: '+sheet["D19"].value+'\n3-dars: '+sheet["D20"].value+'\n4-dars: '+sheet["D21"].value+'</i>'
birac = '<b> 1-A sinf chorshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["D26"].value+'\n2-dars: '+sheet["D27"].value+'\n3-dars: '+sheet["D28"].value+'\n4-dars: '+sheet["D29"].value+ ' </i>'
birap = '<b> 1-A sinf payshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["D34"].value+'\n2-dars: '+sheet["D35"].value+'\n3-dars: '+sheet["D36"].value+'\n4-dars: '+sheet["D37"].value+ '\n5-dars: '+sheet["D38"].value+'</i>'
biraj = '<b> 1-A sinf juma kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["D42"].value+'\n2-dars: '+sheet["D43"].value+'\n3-dars: '+sheet["D44"].value+'\n4-dars: '+sheet["D45"].value+ '\n5-dars: '+sheet["D46"].value+ '\n6-dars: '+sheet["D47"].value+' </i>'
birash = '<b> 1-A sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '

birbd = '<b> 1-B sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["E10"].value+'\n2-dars: '+sheet["E11"].value+'\n3-dars: '+sheet["E12"].value+'\n4-dars: '+sheet["E13"].value+ '\n5-dars: '+sheet["E14"].value+' </i>'
birbs = '<b> 1-B sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["E18"].value+'\n2-dars: '+sheet["E19"].value+'\n3-dars: '+sheet["E20"].value+'\n4-dars: '+sheet["E21"].value+'</i>'
birbc = '<b> 1-B sinf chorshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["E26"].value+'\n2-dars: '+sheet["E27"].value+'\n3-dars: '+sheet["E28"].value+'\n4-dars: '+sheet["E29"].value+ ' </i>'
birbp = '<b> 1-B sinf payshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["E34"].value+'\n2-dars: '+sheet["E35"].value+'\n3-dars: '+sheet["E36"].value+'\n4-dars: '+sheet["E37"].value+ '</i>'
birbj = '<b> 1-B sinf juma kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["E42"].value+'\n2-dars: '+sheet["E43"].value+'\n3-dars: '+sheet["E44"].value+'\n4-dars: '+sheet["E45"].value+ '\n5-dars: '+sheet["E46"].value+ '\n6-dars: '+sheet["E47"].value+' </i>'
birbsh = '<b> 1-B sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '


birvd = '<b> 1-V sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["F10"].value+'\n2-dars: '+sheet["F11"].value+'\n3-dars: '+sheet["F12"].value+'\n4-dars: '+sheet["F13"].value+ '\n5-dars: '+sheet["F14"].value+' </i>'
birvs = '<b> 1-V sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["F18"].value+'\n2-dars: '+sheet["F19"].value+'\n3-dars: '+sheet["F20"].value+'\n4-dars: '+sheet["F21"].value+'</i>'
birvc = '<b> 1-V sinf chorshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["F26"].value+'\n2-dars: '+sheet["F27"].value+'\n3-dars: '+sheet["F28"].value+'\n4-dars: '+sheet["F29"].value+ ' </i>'
birvp = '<b> 1-V sinf payshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["F34"].value+'\n2-dars: '+sheet["F35"].value+'\n3-dars: '+sheet["F36"].value+'\n4-dars: '+sheet["F37"].value+ '\n5-dars: '+sheet["F38"].value+'</i>'
birvj = '<b> 1-V sinf juma kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["F42"].value+'\n2-dars: '+sheet["F43"].value+'\n3-dars: '+sheet["F44"].value+'\n4-dars: '+sheet["F45"].value+ '\n5-dars: '+sheet["F46"].value+' </i>'
birvsh ='<b> 1-V sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '



birgd = '<b> 1-G sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["G10"].value+'\n2-dars: '+sheet["G11"].value+'\n3-dars: '+sheet["G12"].value+'\n4-dars: '+sheet["G13"].value+ ' </i>'
birgs = '<b> 1-G sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["G18"].value+'\n2-dars: '+sheet["G19"].value+'\n3-dars: '+sheet["G20"].value+'\n4-dars: '+sheet["G21"].value+'</i>'
birgc = '<b> 1-G sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["G26"].value+'\n2-dars: '+sheet["G27"].value+'\n3-dars: '+sheet["G28"].value+'\n4-dars: '+sheet["G29"].value+ ' </i>'
birgp = '<b> 1-G sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["G34"].value+'\n2-dars: '+sheet["G35"].value+'\n3-dars: '+sheet["G36"].value+'\n4-dars: '+sheet["G37"].value+ '\n5-dars: '+sheet["G38"].value+'</i>'
birgj = '<b> 1-G sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["G42"].value+'\n2-dars: '+sheet["G43"].value+'\n3-dars: '+sheet["G44"].value+'\n4-dars: '+sheet["G45"].value+ '\n5-dars: '+sheet["G46"].value+ '\n6-dars: '+sheet["G47"].value+' </i>'
birgsh ='<b> 1-G sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '


ikiad = '<b> 2-A sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["H10"].value+'\n2-dars: '+sheet["H11"].value+'\n3-dars: '+sheet["H12"].value+'\n4-dars: '+sheet["H13"].value+ '\n5-dars: '+sheet["H14"].value+ ' </i>'
ikias = '<b> 2-A sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["H18"].value+'\n2-dars: '+sheet["H19"].value+'\n3-dars: '+sheet["H20"].value+'\n4-dars: '+sheet["H21"].value+'\n5-dars: ' +sheet["H22"].value+ '</i>'
ikiac = '<b> 2-A sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["H26"].value+'\n2-dars: '+sheet["H27"].value+'\n3-dars: '+sheet["H28"].value+'\n4-dars: '+sheet["H29"].value+ '\n5-dars: '+sheet["H30"].value+ ' </i>'
ikiap = '<b> 2-A sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["H34"].value+'\n2-dars: '+sheet["H35"].value+'\n3-dars: '+sheet["H36"].value+'\n4-dars: '+sheet["H37"].value+'</i>'
ikiaj = '<b> 2-A sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["H42"].value+'\n2-dars: '+sheet["H43"].value+'\n3-dars: '+sheet["H44"].value+'\n4-dars: '+sheet["H45"].value+ '\n5-dars: '+sheet["H46"].value+ '\n6-dars: '+sheet["H47"].value+' </i>'
ikiash ='<b> 2-A sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '


ikibd = '<b> 2-B sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["I10"].value+'\n2-dars: '+sheet["I11"].value+'\n3-dars: '+sheet["I12"].value+'\n4-dars: '+sheet["I13"].value+ '\n5-dars: '+sheet["I14"].value+ ' </i>'
ikibs = '<b> 2-B sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["I18"].value+'\n2-dars: '+sheet["I19"].value+'\n3-dars: '+sheet["I20"].value+'\n4-dars: '+sheet["I21"].value+'\n5-dars: ' +sheet["I22"].value+ '</i>'
ikibc = '<b> 2-B sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["I26"].value+'\n2-dars: '+sheet["I27"].value+'\n3-dars: '+sheet["I28"].value+'\n4-dars: '+sheet["I29"].value+ '\n5-dars: '+sheet["I30"].value+ ' </i>'
ikibp = '<b> 2-B sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["I34"].value+'\n2-dars: '+sheet["I35"].value+'\n3-dars: '+sheet["I36"].value+'\n4-dars: '+sheet["I37"].value+'\n5-dars: ' +sheet["I38"].value+'</i>'
ikibj = '<b> 2-B sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["I42"].value+'\n2-dars: '+sheet["I43"].value+'\n3-dars: '+sheet["I44"].value+'\n4-dars: '+sheet["I45"].value+ '\n5-dars: '+sheet["I46"].value+ ' </i>'
ikibsh ='<b> 2-B sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '



ikivd = '<b> 2-V sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["J10"].value+'\n2-dars: '+sheet["J11"].value+'\n3-dars: '+sheet["J12"].value+'\n4-dars: '+sheet["J13"].value+ '\n5-dars: '+sheet["J14"].value+ ' </i>'
ikivs = '<b> 2-V sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["J18"].value+'\n2-dars: '+sheet["J19"].value+'\n3-dars: '+sheet["J20"].value+'\n4-dars: '+sheet["J21"].value+ '\n5-dars: '+sheet["J22"].value+ '</i>'
ikivc = '<b> 2-V sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["J26"].value+'\n2-dars: '+sheet["J27"].value+'\n3-dars: '+sheet["J28"].value+'\n4-dars: '+sheet["J29"].value+ '\n5-dars: '+sheet["J30"].value+ ' </i>'
ikivp = '<b> 2-V sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["J34"].value+'\n2-dars: '+sheet["J35"].value+'\n3-dars: '+sheet["J36"].value+'\n4-dars: '+sheet["J37"].value+ '\n5-dars: '+sheet["J38"].value+'</i>'
ikivj = '<b> 2-V sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["J42"].value+'\n2-dars: '+sheet["J43"].value+'\n3-dars: '+sheet["J44"].value+'\n4-dars: '+sheet["J45"].value+ '\n5-dars: '+sheet["J46"].value+ ' </i>'
ikivsh ='<b> 2-V sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '


uchlarad = '<b> 3-A sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["K10"].value+'\n2-dars: '+sheet["K11"].value+'\n3-dars: '+sheet["K12"].value+'\n4-dars: '+sheet["K13"].value+ '\n5-dars: '+sheet["K14"].value+ ' </i>'
uchlaras = '<b> 3-A sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["K18"].value+'\n2-dars: '+sheet["K19"].value+'\n3-dars: '+sheet["K20"].value+'\n4-dars: '+sheet["K21"].value+ '</i>'
uchlarac = '<b> 3-A sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["K26"].value+'\n2-dars: '+sheet["K27"].value+'\n3-dars: '+sheet["K28"].value+'\n4-dars: '+sheet["K29"].value+ '\n5-dars: '+sheet["K30"].value+ ' </i>'
uchlarap = '<b> 3-A sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["K34"].value+'\n2-dars: '+sheet["K35"].value+'\n3-dars: '+sheet["K36"].value+'\n4-dars: '+sheet["K37"].value+ '\n5-dars: '+sheet["K38"].value+'</i>'
uchlaraj = '<b> 3-A sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["K42"].value+'\n2-dars: '+sheet["K43"].value+'\n3-dars: '+sheet["K44"].value+'\n4-dars: '+sheet["K45"].value+ '\n5-dars: '+sheet["K46"].value+ '\n6-dars: '+sheet["K47"].value+ ' </i>'
uchlarash ='<b> 3-A sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '


uchlarbd = '<b> 3-B sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["L10"].value+'\n2-dars: '+sheet["L11"].value+'\n3-dars: '+sheet["L12"].value+'\n4-dars: '+sheet["L13"].value+ '\n5-dars: '+sheet["K14"].value+ ' </i>'
uchlarbs = '<b> 3-B sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["L18"].value+'\n2-dars: '+sheet["L19"].value+'\n3-dars: '+sheet["L20"].value+'\n4-dars: '+sheet["L21"].value+ '\n5-dars: '+sheet["L22"].value+ '</i>'
uchlarbc = '<b> 3-B sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["L26"].value+'\n2-dars: '+sheet["L27"].value+'\n3-dars: '+sheet["L28"].value+'\n4-dars: '+sheet["L29"].value+ '\n5-dars: '+sheet["L30"].value+ ' </i>'
uchlarbp = '<b> 3-B sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["L34"].value+'\n2-dars: '+sheet["L35"].value+'\n3-dars: '+sheet["L36"].value+'\n4-dars: '+sheet["L37"].value+'</i>'
uchlarbj = '<b> 3-B sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["L42"].value+'\n2-dars: '+sheet["L43"].value+'\n3-dars: '+sheet["L44"].value+'\n4-dars: '+sheet["L45"].value+ '\n5-dars: '+sheet["L46"].value+ '\n5-dars: '+sheet["L47"].value+ ' </i>'
uchlarbsh ='<b> 3-B sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '

uchlarvd = '<b> 3-V sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["M10"].value+'\n2-dars: '+sheet["M11"].value+'\n3-dars: '+sheet["M12"].value+'\n4-dars: '+sheet["M13"].value+' </i>'
uchlarvs = '<b> 3-V sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["M18"].value+'\n2-dars: '+sheet["M19"].value+'\n3-dars: '+sheet["M20"].value+'\n4-dars: '+sheet["M21"].value+ '\n5-dars: '+sheet["M22"].value+ '</i>'
uchlarvc = '<b> 3-V sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["M26"].value+'\n2-dars: '+sheet["M27"].value+'\n3-dars: '+sheet["M28"].value+'\n4-dars: '+sheet["M29"].value+ '\n5-dars: '+sheet["M30"].value+ ' </i>'
uchlarvp = '<b> 3-V sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["M34"].value+'\n2-dars: '+sheet["M35"].value+'\n3-dars: '+sheet["M36"].value+'\n4-dars: '+sheet["M37"].value+'\n5-dars: ' +sheet["M38"].value+ '</i>'
uchlarvj = '<b> 3-V sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["M42"].value+'\n2-dars: '+sheet["M43"].value+'\n3-dars: '+sheet["M44"].value+'\n4-dars: '+sheet["M45"].value+ '\n5-dars: '+sheet["M46"].value+ '\n5-dars: '+sheet["M47"].value+ ' </i>'
uchlarvsh ='<b> 3-V sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '

#----- 4-sinflar-----

tortlarad = '<b> 4-A sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["N10"].value+'\n2-dars: '+sheet["N11"].value+'\n3-dars: '+sheet["N12"].value+'\n4-dars: '+sheet["N13"].value+'\n5-dars: ' +sheet["N14"].value+' </i>'
tortlaras = '<b> 4-A sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["N18"].value+'\n2-dars: '+sheet["N19"].value+'\n3-dars: '+sheet["N20"].value+'\n4-dars: '+sheet["N21"].value+ '\n5-dars: '+sheet["N22"].value+ '</i>'
tortlarac = '<b> 4-A sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["N26"].value+'\n2-dars: '+sheet["N27"].value+'\n3-dars: '+sheet["N28"].value+'\n4-dars: '+sheet["N29"].value+ '\n5-dars: '+sheet["N30"].value+ ' </i>'
tortlarap = '<b> 4-A sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["N34"].value+'\n2-dars: '+sheet["N35"].value+'\n3-dars: '+sheet["N36"].value+'\n4-dars: '+sheet["N37"].value+'\n5-dars: ' +sheet["N38"].value+ '</i>'
tortlaraj = '<b> 4-A sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["N42"].value+'\n2-dars: '+sheet["N43"].value+'\n3-dars: '+sheet["N44"].value+'\n4-dars: '+sheet["N45"].value+ '\n5-dars: '+sheet["N46"].value+' </i>'
tortlarash ='<b> 4-A sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '

tortlarbd = '<b> 4-B sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["O10"].value+'\n2-dars: '+sheet["O11"].value+'\n3-dars: '+sheet["O12"].value+'\n4-dars: '+sheet["O13"].value+'\n5-dars: ' +sheet["O14"].value+' </i>'
tortlarbs = '<b> 4-B sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["O18"].value+'\n2-dars: '+sheet["O19"].value+'\n3-dars: '+sheet["O20"].value+'\n4-dars: '+sheet["O21"].value+ '\n5-dars: '+sheet["O22"].value+ '</i>'
tortlarbc = '<b> 4-B sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["O26"].value+'\n2-dars: '+sheet["O27"].value+'\n3-dars: '+sheet["O28"].value+'\n4-dars: '+sheet["O29"].value+ ' </i>'
tortlarbp = '<b> 4-B sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["O34"].value+'\n2-dars: '+sheet["O35"].value+'\n3-dars: '+sheet["O36"].value+'\n4-dars: '+sheet["O37"].value+'\n5-dars: ' +sheet["O38"].value+ '</i>'
tortlarbj = '<b> 4-B sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["O42"].value+'\n2-dars: '+sheet["O43"].value+'\n3-dars: '+sheet["O44"].value+'\n4-dars: '+sheet["O45"].value+ '\n5-dars: '+sheet["O46"].value+'\n6-dars: '+sheet["O47"].value+' </i>'
tortlarbsh ='<b> 4-B sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '

tortlarvd = '<b> 4-V sinf dushanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["P10"].value+'\n2-dars: '+sheet["P11"].value+'\n3-dars: '+sheet["P12"].value+'\n4-dars: '+sheet["P13"].value+'\n5-dars: ' +sheet["P14"].value+' </i>'
tortlarvs = '<b> 4-V sinf seshanba kungi dars jadvali </b> <i> \n\n1-dars: '+sheet["P18"].value+'\n2-dars: '+sheet["P19"].value+'\n3-dars: '+sheet["P20"].value+'\n4-dars: '+sheet["P21"].value+ '\n5-dars: '+sheet["P22"].value+ '</i>'
tortlarvc = '<b> 4-V sinf chorshanba kungi dars jadvali </b><i>\n\n1-dars: '+sheet["P26"].value+'\n2-dars: '+sheet["P27"].value+'\n3-dars: '+sheet["P28"].value+'\n4-dars: '+sheet["P29"].value+ ' </i>'
tortlarvp = '<b> 4-V sinf payshanba kungi dars jadvali </b> <i>\n\n1-dars: '+sheet["P34"].value+'\n2-dars: '+sheet["P35"].value+'\n3-dars: '+sheet["P36"].value+'\n4-dars: '+sheet["P37"].value+'\n5-dars: ' +sheet["P38"].value+ '</i>'
tortlarvj = '<b> 4-V sinf juma kungi dars jadvali   </b> <i> \n\n1-dars: '  +sheet["P42"].value+'\n2-dars: '+sheet["P43"].value+'\n3-dars: '+sheet["P44"].value+'\n4-dars: '+sheet["P45"].value+ '\n5-dars: '+sheet["P46"].value+'\n6-dars: '+sheet["P47"].value+' </i>'
tortlarvsh ='<b> 4-V sinf shanba kungi dars yo\'q  \nDam olish kuni</b> '

#----- 4-sinflar tugadi-----
