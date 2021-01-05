from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import requests
import matplotlib.pyplot as plt


csv_url = "https://api.covid19india.org/csv/latest/state_wise.csv"
req = requests.get(csv_url)
url_content = req.content
csv_file = open('realtime_data/state_wise.csv', 'wb')
csv_file.write(url_content)
csv_file.close()
state_wise = pd.read_csv("realtime_data/state_wise.csv")
state_wise.head(2)


def home(request):
    c0=state_wise["Confirmed"][0]
    c1=state_wise["Confirmed"][1]
    c2=state_wise["Confirmed"][2]
    c3=state_wise["Confirmed"][3]
    c4=state_wise["Confirmed"][4]
    c5=state_wise["Confirmed"][5]
    c6=state_wise["Confirmed"][6]
    c7=state_wise["Confirmed"][7]
    c8=state_wise["Confirmed"][8]
    c9=state_wise["Confirmed"][9]
    c10=state_wise["Confirmed"][10]
    c11=state_wise["Confirmed"][11]
    c12=state_wise["Confirmed"][12]
    c13=state_wise["Confirmed"][13]
    c14=state_wise["Confirmed"][14]
    c15=state_wise["Confirmed"][15]
    c16=state_wise["Confirmed"][16]
    c17=state_wise["Confirmed"][17]
    c18=state_wise["Confirmed"][18]
    c19=state_wise["Confirmed"][19]
    c20=state_wise["Confirmed"][20]
    c21=state_wise["Confirmed"][21]
    c22=state_wise["Confirmed"][22]
    c23=state_wise["Confirmed"][23]
    c24=state_wise["Confirmed"][24]
    c25=state_wise["Confirmed"][25]
    c26=state_wise["Confirmed"][26]
    c27=state_wise["Confirmed"][27]
    c28=state_wise["Confirmed"][28]
    c29=state_wise["Confirmed"][29]
    c30=state_wise["Confirmed"][30]
    c31=state_wise["Confirmed"][31]
    c32=state_wise["Confirmed"][32]
    c33=state_wise["Confirmed"][33]
    c34=state_wise["Confirmed"][34]
    c35=state_wise["Confirmed"][35]
    c36=state_wise["Confirmed"][36]
    c37=state_wise["Confirmed"][37]
    a0 = state_wise["Active"][0]
    r0=state_wise["Recovered"][0]
    r1=state_wise["Recovered"][1]
    r2=state_wise["Recovered"][2]
    r3=state_wise["Recovered"][3]
    r4=state_wise["Recovered"][4]
    r5=state_wise["Recovered"][5]
    r6=state_wise["Recovered"][6]
    r7=state_wise["Recovered"][7]
    r8=state_wise["Recovered"][8]
    r9=state_wise["Recovered"][9]
    r10=state_wise["Recovered"][10]
    r11=state_wise["Recovered"][11]
    r12=state_wise["Recovered"][12]
    r13=state_wise["Recovered"][13]
    r14=state_wise["Recovered"][14]
    r15=state_wise["Recovered"][15]
    r16=state_wise["Recovered"][16]
    r17=state_wise["Recovered"][17]
    r18=state_wise["Recovered"][18]
    r19=state_wise["Recovered"][19]
    r20=state_wise["Recovered"][20]
    r21=state_wise["Recovered"][21]
    r22=state_wise["Recovered"][22]
    r23=state_wise["Recovered"][23]
    r24=state_wise["Recovered"][24]
    r25=state_wise["Recovered"][25]
    r26=state_wise["Recovered"][26]
    r27=state_wise["Recovered"][27]
    r28=state_wise["Recovered"][28]
    r29=state_wise["Recovered"][29]
    r30=state_wise["Recovered"][30]
    r31=state_wise["Recovered"][31]
    r32=state_wise["Recovered"][32]
    r33=state_wise["Recovered"][33]
    r34=state_wise["Recovered"][34]
    r35=state_wise["Recovered"][35]
    r36=state_wise["Recovered"][36]
    r37=state_wise["Recovered"][37]
    d0=state_wise["Deaths"][0]
    d1=state_wise["Deaths"][1]
    d2=state_wise["Deaths"][2]
    d3=state_wise["Deaths"][3]
    d4=state_wise["Deaths"][4]
    d5=state_wise["Deaths"][5]
    d6=state_wise["Deaths"][6]
    d7=state_wise["Deaths"][7]
    d8=state_wise["Deaths"][8]
    d9=state_wise["Deaths"][9]
    d10=state_wise["Deaths"][10]
    d11=state_wise["Deaths"][11]
    d12=state_wise["Deaths"][12]
    d13=state_wise["Deaths"][13]
    d14=state_wise["Deaths"][14]
    d15=state_wise["Deaths"][15]
    d16=state_wise["Deaths"][16]
    d17=state_wise["Deaths"][17]
    d18=state_wise["Deaths"][18]
    d19=state_wise["Deaths"][19]
    d20=state_wise["Deaths"][20]
    d21=state_wise["Deaths"][21]
    d22=state_wise["Deaths"][22]
    d23=state_wise["Deaths"][23]
    d24=state_wise["Deaths"][24]
    d25=state_wise["Deaths"][25]
    d26=state_wise["Deaths"][26]
    d27=state_wise["Deaths"][27]
    d28=state_wise["Deaths"][28]
    d29=state_wise["Deaths"][29]
    d30=state_wise["Deaths"][30]
    d31=state_wise["Deaths"][31]
    d32=state_wise["Deaths"][32]
    d33=state_wise["Deaths"][33]
    d34=state_wise["Deaths"][34]
    d35=state_wise["Deaths"][35]
    d36=state_wise["Deaths"][36]
    d37=state_wise["Deaths"][37]
    u0=state_wise["Last_Updated_Time"][0]
    u1=state_wise["Last_Updated_Time"][1]
    u2=state_wise["Last_Updated_Time"][2]
    u3=state_wise["Last_Updated_Time"][3]
    u4=state_wise["Last_Updated_Time"][4]
    u5=state_wise["Last_Updated_Time"][5]
    u6=state_wise["Last_Updated_Time"][6]
    u7=state_wise["Last_Updated_Time"][7]
    u8=state_wise["Last_Updated_Time"][8]
    u9=state_wise["Last_Updated_Time"][9]
    u10=state_wise["Last_Updated_Time"][10]
    u11=state_wise["Last_Updated_Time"][11]
    u12=state_wise["Last_Updated_Time"][12]
    u13=state_wise["Last_Updated_Time"][13]
    u14=state_wise["Last_Updated_Time"][14]
    u15=state_wise["Last_Updated_Time"][15]
    u16=state_wise["Last_Updated_Time"][16]
    u17=state_wise["Last_Updated_Time"][17]
    u18=state_wise["Last_Updated_Time"][18]
    u19=state_wise["Last_Updated_Time"][19]
    u20=state_wise["Last_Updated_Time"][20]
    u21=state_wise["Last_Updated_Time"][21]
    u22=state_wise["Last_Updated_Time"][22]
    u23=state_wise["Last_Updated_Time"][23]
    u24=state_wise["Last_Updated_Time"][24]
    u25=state_wise["Last_Updated_Time"][25]
    u26=state_wise["Last_Updated_Time"][26]
    u27=state_wise["Last_Updated_Time"][27]
    u28=state_wise["Last_Updated_Time"][28]
    u29=state_wise["Last_Updated_Time"][29]
    u30=state_wise["Last_Updated_Time"][30]
    u31=state_wise["Last_Updated_Time"][31]
    u32=state_wise["Last_Updated_Time"][32]
    u33=state_wise["Last_Updated_Time"][33]
    u34=state_wise["Last_Updated_Time"][34]
    u35=state_wise["Last_Updated_Time"][35]
    u36=state_wise["Last_Updated_Time"][36]
    u37=state_wise["Last_Updated_Time"][37]
    c240=state_wise["Delta_Confirmed"][0]
    c241=state_wise["Delta_Confirmed"][1]
    c242=state_wise["Delta_Confirmed"][2]
    c243=state_wise["Delta_Confirmed"][3]
    c244=state_wise["Delta_Confirmed"][4]
    c245=state_wise["Delta_Confirmed"][5]
    c246=state_wise["Delta_Confirmed"][6]
    c247=state_wise["Delta_Confirmed"][7]
    c248=state_wise["Delta_Confirmed"][8]
    c249=state_wise["Delta_Confirmed"][9]
    c2410=state_wise["Delta_Confirmed"][10]
    c2411=state_wise["Delta_Confirmed"][11]
    c2412=state_wise["Delta_Confirmed"][12]
    c2413=state_wise["Delta_Confirmed"][13]
    c2414=state_wise["Delta_Confirmed"][14]
    c2415=state_wise["Delta_Confirmed"][15]
    c2416=state_wise["Delta_Confirmed"][16]
    c2417=state_wise["Delta_Confirmed"][17]
    c2418=state_wise["Delta_Confirmed"][18]
    c2419=state_wise["Delta_Confirmed"][19]
    c2420=state_wise["Delta_Confirmed"][20]
    c2421=state_wise["Delta_Confirmed"][21]
    c2422=state_wise["Delta_Confirmed"][22]
    c2423=state_wise["Delta_Confirmed"][23]
    c2424=state_wise["Delta_Confirmed"][24]
    c2425=state_wise["Delta_Confirmed"][25]
    c2426=state_wise["Delta_Confirmed"][26]
    c2427=state_wise["Delta_Confirmed"][27]
    c2428=state_wise["Delta_Confirmed"][28]
    c2429=state_wise["Delta_Confirmed"][29]
    c2430=state_wise["Delta_Confirmed"][30]
    c2431=state_wise["Delta_Confirmed"][31]
    c2432=state_wise["Delta_Confirmed"][32]
    c2433=state_wise["Delta_Confirmed"][33]
    c2434=state_wise["Delta_Confirmed"][34]
    c2435=state_wise["Delta_Confirmed"][35]
    c2436=state_wise["Delta_Confirmed"][36]
    c2437=state_wise["Delta_Confirmed"][37]

    r240=state_wise["Delta_Recovered"][0]
    r241=state_wise["Delta_Recovered"][1]
    r242=state_wise["Delta_Recovered"][2]
    r243=state_wise["Delta_Recovered"][3]
    r244=state_wise["Delta_Recovered"][4]
    r245=state_wise["Delta_Recovered"][5]
    r246=state_wise["Delta_Recovered"][6]
    r247=state_wise["Delta_Recovered"][7]
    r248=state_wise["Delta_Recovered"][8]
    r249=state_wise["Delta_Recovered"][9]
    r2410=state_wise["Delta_Recovered"][10]
    r2411=state_wise["Delta_Recovered"][11]
    r2412=state_wise["Delta_Recovered"][12]
    r2413=state_wise["Delta_Recovered"][13]
    r2414=state_wise["Delta_Recovered"][14]
    r2415=state_wise["Delta_Recovered"][15]
    r2416=state_wise["Delta_Recovered"][16]
    r2417=state_wise["Delta_Recovered"][17]
    r2418=state_wise["Delta_Recovered"][18]
    r2419=state_wise["Delta_Recovered"][19]
    r2420=state_wise["Delta_Recovered"][20]
    r2421=state_wise["Delta_Recovered"][21]
    r2422=state_wise["Delta_Recovered"][22]
    r2423=state_wise["Delta_Recovered"][23]
    r2424=state_wise["Delta_Recovered"][24]
    r2425=state_wise["Delta_Recovered"][25]
    r2426=state_wise["Delta_Recovered"][26]
    r2427=state_wise["Delta_Recovered"][27]
    r2428=state_wise["Delta_Recovered"][28]
    r2429=state_wise["Delta_Recovered"][29]
    r2430=state_wise["Delta_Recovered"][30]
    r2431=state_wise["Delta_Recovered"][31]
    r2432=state_wise["Delta_Recovered"][32]
    r2433=state_wise["Delta_Recovered"][33]
    r2434=state_wise["Delta_Recovered"][34]
    r2435=state_wise["Delta_Recovered"][35]
    r2436=state_wise["Delta_Recovered"][36]
    r2437=state_wise["Delta_Recovered"][37]
    d240=state_wise["Delta_Deaths"][0]
    d241=state_wise["Delta_Deaths"][1]
    d242=state_wise["Delta_Deaths"][2]
    d243=state_wise["Delta_Deaths"][3]
    d244=state_wise["Delta_Deaths"][4]
    d245=state_wise["Delta_Deaths"][5]
    d246=state_wise["Delta_Deaths"][6]
    d247=state_wise["Delta_Deaths"][7]
    d248=state_wise["Delta_Deaths"][8]
    d249=state_wise["Delta_Deaths"][9]
    d2410=state_wise["Delta_Deaths"][10]
    d2411=state_wise["Delta_Deaths"][11]
    d2412=state_wise["Delta_Deaths"][12]
    d2413=state_wise["Delta_Deaths"][13]
    d2414=state_wise["Delta_Deaths"][14]
    d2415=state_wise["Delta_Deaths"][15]
    d2416=state_wise["Delta_Deaths"][16]
    d2417=state_wise["Delta_Deaths"][17]
    d2418=state_wise["Delta_Deaths"][18]
    d2419=state_wise["Delta_Deaths"][19]
    d2420=state_wise["Delta_Deaths"][20]
    d2421=state_wise["Delta_Deaths"][21]
    d2422=state_wise["Delta_Deaths"][22]
    d2423=state_wise["Delta_Deaths"][23]
    d2424=state_wise["Delta_Deaths"][24]
    d2425=state_wise["Delta_Deaths"][25]
    d2426=state_wise["Delta_Deaths"][26]
    d2427=state_wise["Delta_Deaths"][27]
    d2428=state_wise["Delta_Deaths"][28]
    d2429=state_wise["Delta_Deaths"][29]
    d2430=state_wise["Delta_Deaths"][30]
    d2431=state_wise["Delta_Deaths"][31]
    d2432=state_wise["Delta_Deaths"][32]
    d2433=state_wise["Delta_Deaths"][33]
    d2434=state_wise["Delta_Deaths"][34]
    d2435=state_wise["Delta_Deaths"][35]
    d2436=state_wise["Delta_Deaths"][36]
    d2437=state_wise["Delta_Deaths"][37]
    s0=state_wise["State"][0]
    s1=state_wise["State"][1]
    s2=state_wise["State"][2]
    s3=state_wise["State"][3]
    s4=state_wise["State"][4]
    s5=state_wise["State"][5]
    s6=state_wise["State"][6]
    s7=state_wise["State"][7]
    s8=state_wise["State"][8]
    s9=state_wise["State"][9]
    s10=state_wise["State"][10]
    s11=state_wise["State"][11]
    s12=state_wise["State"][12]
    s13=state_wise["State"][13]
    s14=state_wise["State"][14]
    s15=state_wise["State"][15]
    s16=state_wise["State"][16]
    s17=state_wise["State"][17]
    s18=state_wise["State"][18]
    s19=state_wise["State"][19]
    s20=state_wise["State"][20]
    s21=state_wise["State"][21]
    s22=state_wise["State"][22]
    s23=state_wise["State"][23]
    s24=state_wise["State"][24]
    s25=state_wise["State"][25]
    s26=state_wise["State"][26]
    s27=state_wise["State"][27]
    s28=state_wise["State"][28]
    s29=state_wise["State"][29]
    s30=state_wise["State"][30]
    s31=state_wise["State"][31]
    s32=state_wise["State"][32]
    s33=state_wise["State"][33]
    s34=state_wise["State"][34]
    s35=state_wise["State"][35]
    s36=state_wise["State"][36]
    s37=state_wise["State"][37]
    recovery = round((state_wise["Recovered"][0] / state_wise["Confirmed"][0])*100 , 2)








    return render(request, 'home.html', {"active0":a0,"rec":recovery,"update":u0,"confirmed0":c0,"recovered0":r0,"deaths0":d0,"update0":u0,"confirmed240":c240,"recovered240":r240,"deaths240":d240,
                                        "confirmed1":c1,"recovered1":r1,"deaths1":d1,"update1":u1,"confirmed241":c241,"recovered241":r241,"deaths241":d241,
                                        "confirmed2":c2,"recovered2":r2,"deaths2":d2,"update2":u2,"confirmed242":c242,"recovered242":r242,"deaths242":d242,
                                        "confirmed3":c3,"recovered3":r3,"deaths3":d3,"update3":u3,"confirmed243":c243,"recovered243":r243,"deaths243":d243,
                                        "confirmed4":c4,"recovered4":r4,"deaths4":d4,"update4":u4,"confirmed244":c244,"recovered244":r244,"deaths244":d244,
                                        "confirmed5":c5,"recovered5":r5,"deaths5":d5,"update5":u5,"confirmed245":c245,"recovered245":r245,"deaths245":d245,
                                        "confirmed6":c6,"recovered6":r6,"deaths6":d6,"update6":u6,"confirmed246":c246,"recovered246":r246,"deaths246":d246,
                                        "confirmed7":c7,"recovered7":r7,"deaths7":d7,"update7":u7,"confirmed247":c247,"recovered247":r247,"deaths247":d247,
                                        "confirmed8":c8,"recovered8":r8,"deaths8":d8,"update8":u8,"confirmed248":c248,"recovered248":r248,"deaths248":d248,
                                        "confirmed9":c9,"recovered9":r9,"deaths9":d9,"update9":u9,"confirmed249":c249,"recovered249":r249,"deaths249":d249,
                                        "confirmed10":c10,"recovered10":r10,"deaths10":d10,"update10":u10,"confirmed2410":c2410,"recovered2410":r2410,"deaths2410":d2410,
                                        "confirmed11":c11,"recovered11":r11,"deaths11":d11,"update11":u11,"confirmed2411":c2411,"recovered2411":r2411,"deaths2411":d2411,
                                        "confirmed12":c12,"recovered12":r12,"deaths12":d12,"update12":u12,"confirmed2412":c2412,"recovered2412":r2412,"deaths2412":d2412,
                                        "confirmed13":c13,"recovered13":r13,"deaths13":d13,"update13":u13,"confirmed2413":c2413,"recovered2413":r2413,"deaths2413":d2413,
                                        "confirmed14":c14,"recovered14":r14,"deaths14":d14,"update14":u14,"confirmed2414":c2414,"recovered2414":r2414,"deaths2414":d2414,
                                        "confirmed15":c15,"recovered15":r15,"deaths15":d15,"update15":u15,"confirmed2415":c2415,"recovered2415":r2415,"deaths2415":d2415,
                                        "confirmed16":c16,"recovered16":r16,"deaths16":d16,"update16":u16,"confirmed2416":c2416,"recovered2416":r2416,"deaths2416":d2416,
                                        "confirmed17":c17,"recovered17":r17,"deaths17":d17,"update17":u17,"confirmed2417":c2417,"recovered2417":r2417,"deaths2417":d2417,
                                        "confirmed18":c18,"recovered18":r18,"deaths18":d18,"update18":u18,"confirmed2418":c2418,"recovered2418":r2418,"deaths2418":d2418,
                                        "confirmed19":c19,"recovered19":r19,"deaths19":d19,"update19":u19,"confirmed2419":c2419,"recovered2419":r2419,"deaths2419":d2419,
                                        "confirmed20":c20,"recovered20":r20,"deaths20":d20,"update20":u20,"confirmed2420":c2420,"recovered2420":r2420,"deaths2420":d2420,
                                        "confirmed21":c21,"recovered21":r21,"deaths21":d21,"update21":u21,"confirmed2421":c2421,"recovered2421":r2421,"deaths2421":d2421,
                                        "confirmed22":c22,"recovered22":r22,"deaths22":d22,"update22":u22,"confirmed2422":c2422,"recovered2422":r2422,"deaths2422":d2422,
                                        "confirmed23":c23,"recovered23":r23,"deaths23":d23,"update23":u23,"confirmed2423":c2423,"recovered2423":r2423,"deaths2423":d2423,
                                        "confirmed24":c24,"recovered24":r24,"deaths24":d24,"update24":u24,"confirmed2424":c2424,"recovered2424":r2424,"deaths2424":d2424,
                                        "confirmed25":c25,"recovered25":r25,"deaths25":d25,"update25":u25,"confirmed2425":c2425,"recovered2425":r2425,"deaths2425":d2425,
                                        "confirmed26":c26,"recovered26":r26,"deaths26":d26,"update26":u26,"confirmed2426":c2426,"recovered2426":r2426,"deaths2426":d2426,
                                        "confirmed27":c27,"recovered27":r27,"deaths27":d27,"update27":u27,"confirmed2427":c2427,"recovered2427":r2427,"deaths2427":d2427,
                                        "confirmed28":c28,"recovered28":r28,"deaths28":d28,"update28":u28,"confirmed2428":c2428,"recovered2428":r2428,"deaths2428":d2428,
                                        "confirmed29":c29,"recovered29":r29,"deaths29":d29,"update29":u29,"confirmed2429":c2429,"recovered2429":r2429,"deaths2429":d2429,
                                        "confirmed30":c30,"recovered30":r30,"deaths30":d30,"update30":u30,"confirmed2430":c2430,"recovered2430":r2430,"deaths2430":d2430,
                                        "confirmed31":c31,"recovered31":r31,"deaths31":d31,"update31":u31,"confirmed2431":c2431,"recovered2431":r2431,"deaths2431":d2431,
                                        "confirmed32":c32,"recovered32":r32,"deaths32":d32,"update32":u32,"confirmed2432":c2432,"recovered2432":r2432,"deaths2432":d2432,
                                        "confirmed33":c33,"recovered33":r33,"deaths33":d33,"update33":u33,"confirmed2433":c2433,"recovered2433":r2433,"deaths2433":d2433,
                                        "confirmed34":c34,"recovered34":r34,"deaths34":d34,"update34":u34,"confirmed2434":c2434,"recovered2434":r2434,"deaths2434":d2434,
                                        "confirmed35":c35,"recovered35":r35,"deaths35":d35,"update35":u35,"confirmed2435":c2435,"recovered2435":r2435,"deaths2435":d2435,
                                        "confirmed36":c36,"recovered36":r36,"deaths36":d36,"update36":u36,"confirmed2436":c2436,"recovered2436":r2436,"deaths2436":d2436,
                                        "confirmed37":c37,"recovered37":r37,"deaths37":d37,"update37":u37,"confirmed2437":c2437,"recovered2437":r2437,"deaths2437":d2437,

                                        "state0":s0,"state1":s1,"state2":s2,"state3":s3,"state4":s4,"state5":s5,"state6":s6,"state7":s7,"state8":s8,"state9":s9,"state10":s10,"state11":s11,"state12":s12,"state13":s13,"state14":s14,"state15":s15,"state16":s16,
                                        "state17":s17,"state18":s18,"state19":s19,"state20":s20,"state21":s21,"state22":s22,"state23":s23,"state24":s24,"state25":s25,"state26":s26,"state27":s27,"state28":s28,"state29":s29,"state30":s30,"state31":s31,"state32":s32,"state33":s33,
                                        "state34":s34,"state35":s35,"state36":s36,"state37":s37,

     })



columns = ['TrialID', 'Last Refreshed on', 'Public title', 'Scientific title', 'Acronym', 'Primary sponsor',
           'Date registration', 'Date registration3', 'Export date', 'Source Register', 'web address',
           'Recruitment Status', 'other records', 'Inclusion agemin', 'Inclusion agemax',
           'Inclusion gender', 'Date enrollement', 'Target size', 'Study type', 'Study design',
           'Phase', 'Countries', 'Contact Firstname', 'Contact Lastname', 'Contact Address', 'Contact Email',
           'Contact Tel', 'Contact Affiliation', 'Inclusion Criteria', 'Exclusion Criteria',
           'Condition', 'Intervention', 'Primary outcome', 'results date posted', 'results date completed',
           'results url link', 'Retrospective flag', 'Bridging flag truefalse', 'Bridged type', 'results yes no']
df = pd.read_csv('realtime_data/who.csv', names=columns)
data_dict = df.to_dict()

def helpline(request):
    return render(request, 'helpline.html', data_dict)
def resources(request):
    return render(request, 'resources.html')
def about(request):
    return render(request, 'about.html')





