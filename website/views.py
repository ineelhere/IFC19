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
    c = state_wise["Confirmed"][0]
    r = state_wise["Recovered"][0]
    d = state_wise["Deaths"][0]
    u = state_wise["Last_Updated_Time"][0]

    c24 = state_wise["Delta_Confirmed"][0]
    r24 = state_wise["Delta_Recovered"][0]
    d24 = state_wise["Delta_Deaths"][0]

    can = state_wise["Confirmed"][28]
    ran = state_wise["Recovered"][28]
    dan = state_wise["Deaths"][28]
    uan = state_wise["Last_Updated_Time"][28]
    c24an = state_wise["Delta_Confirmed"][28]
    r24an = state_wise["Delta_Recovered"][28]
    d24an = state_wise["Delta_Deaths"][28]

    cap=state_wise["Confirmed"][9]
    rap=state_wise["Recovered"][9]
    dap=state_wise["Deaths"][9]
    uap=state_wise["Last_Updated_Time"][9]
    c24ap=state_wise["Delta_Confirmed"][9]
    r24ap=state_wise["Delta_Recovered"][9]
    d24ap=state_wise["Delta_Deaths"][9]

    car=state_wise["Confirmed"][33]
    rar=state_wise["Recovered"][33]
    dar=state_wise["Deaths"][33]
    uar=state_wise["Last_Updated_Time"][33]
    c24ar=state_wise["Delta_Confirmed"][33]
    r24ar=state_wise["Delta_Recovered"][33]
    d24ar=state_wise["Delta_Deaths"][33]

    cas=state_wise["Confirmed"][20]
    ras=state_wise["Recovered"][20]
    das=state_wise["Deaths"][20]
    uas=state_wise["Last_Updated_Time"][20]
    c24as=state_wise["Delta_Confirmed"][20]
    r24as=state_wise["Delta_Recovered"][20]
    d24as=state_wise["Delta_Deaths"][20]

    cbr=state_wise["Confirmed"][10]
    rbr=state_wise["Recovered"][10]
    dbr=state_wise["Deaths"][10]
    ubr=state_wise["Last_Updated_Time"][10]
    c24br=state_wise["Delta_Confirmed"][10]
    r24br=state_wise["Delta_Recovered"][10]
    d24br=state_wise["Delta_Deaths"][10]

    cch=state_wise["Confirmed"][21]
    rch=state_wise["Recovered"][21]
    dch=state_wise["Deaths"][21]
    uch=state_wise["Last_Updated_Time"][21]
    c24ch=state_wise["Delta_Confirmed"][21]
    r24ch=state_wise["Delta_Recovered"][21]
    d24ch=state_wise["Delta_Deaths"][21]

    cchh=state_wise["Confirmed"][23]
    rchh=state_wise["Recovered"][23]
    dchh=state_wise["Deaths"][23]
    uchh=state_wise["Last_Updated_Time"][23]
    c24chh=state_wise["Delta_Confirmed"][23]
    r24chh=state_wise["Delta_Recovered"][23]
    d24chh=state_wise["Delta_Deaths"][23]

    cdnhdd=state_wise["Confirmed"][34]
    rdnhdd=state_wise["Recovered"][34]
    ddnhdd=state_wise["Deaths"][34]
    udnhdd=state_wise["Last_Updated_Time"][34]
    c24dnhdd=state_wise["Delta_Confirmed"][34]
    r24dnhdd=state_wise["Delta_Recovered"][34]
    d24dnhdd=state_wise["Delta_Deaths"][34]

    cdl=state_wise["Confirmed"][4]
    rdl=state_wise["Recovered"][4]
    ddl=state_wise["Deaths"][4]
    udl=state_wise["Last_Updated_Time"][4]
    c24dl=state_wise["Delta_Confirmed"][4]
    r24dl=state_wise["Delta_Recovered"][4]
    d24dl=state_wise["Delta_Deaths"][4]

    cgoa=state_wise["Confirmed"][26]
    cgj=state_wise["Confirmed"][3]
    chr=state_wise["Confirmed"][17]
    chp=state_wise["Confirmed"][24]
    cjk=state_wise["Confirmed"][15]
    cjr=state_wise["Confirmed"][19]
    cka=state_wise["Confirmed"][13]
    ckl=state_wise["Confirmed"][18]
    clh=state_wise["Confirmed"][27]
    cld=state_wise["Confirmed"][36]
    cmp=state_wise["Confirmed"][6]
    cmh=state_wise["Confirmed"][1]
    cmn=state_wise["Confirmed"][29]
    cmg=state_wise["Confirmed"][31]
    cmz=state_wise["Confirmed"][32]
    cng=state_wise["Confirmed"][35]
    cor=state_wise["Confirmed"][16]
    cpy=state_wise["Confirmed"][30]
    cpb=state_wise["Confirmed"][11]
    crj=state_wise["Confirmed"][5]
    csk=state_wise["Confirmed"][37]
    csu=state_wise["Confirmed"][14]
    ctn=state_wise["Confirmed"][2]
    cts=state_wise["Confirmed"][12]
    ctr=state_wise["Confirmed"][22]
    cup=state_wise["Confirmed"][7]
    cuk=state_wise["Confirmed"][25]
    cwb=state_wise["Confirmed"][8]
    rgoa=state_wise["Recovered"][26]
    rgj=state_wise["Recovered"][3]
    rhr=state_wise["Recovered"][17]
    rhp=state_wise["Recovered"][24]
    rjk=state_wise["Recovered"][15]
    rjr=state_wise["Recovered"][19]
    rka=state_wise["Recovered"][13]
    rkl=state_wise["Recovered"][18]
    rlh=state_wise["Recovered"][27]
    rld=state_wise["Recovered"][36]
    rmp=state_wise["Recovered"][6]
    rmh=state_wise["Recovered"][1]
    rmn=state_wise["Recovered"][29]
    rmg=state_wise["Recovered"][31]
    rmz=state_wise["Recovered"][32]
    rng=state_wise["Recovered"][35]
    ror=state_wise["Recovered"][16]
    rpy=state_wise["Recovered"][30]
    rpb=state_wise["Recovered"][11]
    rrj=state_wise["Recovered"][5]
    rsk=state_wise["Recovered"][37]
    rsu=state_wise["Recovered"][14]
    rtn=state_wise["Recovered"][2]
    rts=state_wise["Recovered"][12]
    rtr=state_wise["Recovered"][22]
    rup=state_wise["Recovered"][7]
    ruk=state_wise["Recovered"][25]
    rwb=state_wise["Recovered"][8]
    dgoa=state_wise["Deaths"][26]
    dgj=state_wise["Deaths"][3]
    dhr=state_wise["Deaths"][17]
    dhp=state_wise["Deaths"][24]
    djk=state_wise["Deaths"][15]
    djr=state_wise["Deaths"][19]
    dka=state_wise["Deaths"][13]
    dkl=state_wise["Deaths"][18]
    dlh=state_wise["Deaths"][27]
    dld=state_wise["Deaths"][36]
    dmp=state_wise["Deaths"][6]
    dmh=state_wise["Deaths"][1]
    dmn=state_wise["Deaths"][29]
    dmg=state_wise["Deaths"][31]
    dmz=state_wise["Deaths"][32]
    dng=state_wise["Deaths"][35]
    dor=state_wise["Deaths"][16]
    dpy=state_wise["Deaths"][30]
    dpb=state_wise["Deaths"][11]
    drj=state_wise["Deaths"][5]
    dsk=state_wise["Deaths"][37]
    dsu=state_wise["Deaths"][14]
    dtn=state_wise["Deaths"][2]
    dts=state_wise["Deaths"][12]
    dtr=state_wise["Deaths"][22]
    dup=state_wise["Deaths"][7]
    duk=state_wise["Deaths"][25]
    dwb=state_wise["Deaths"][8]
    ugoa=state_wise["Last_Updated_Time"][26]
    ugj=state_wise["Last_Updated_Time"][3]
    uhr=state_wise["Last_Updated_Time"][17]
    uhp=state_wise["Last_Updated_Time"][24]
    ujk=state_wise["Last_Updated_Time"][15]
    ujr=state_wise["Last_Updated_Time"][19]
    uka=state_wise["Last_Updated_Time"][13]
    ukl=state_wise["Last_Updated_Time"][18]
    ulh=state_wise["Last_Updated_Time"][27]
    uld=state_wise["Last_Updated_Time"][36]
    ump=state_wise["Last_Updated_Time"][6]
    umh=state_wise["Last_Updated_Time"][1]
    umn=state_wise["Last_Updated_Time"][29]
    umg=state_wise["Last_Updated_Time"][31]
    umz=state_wise["Last_Updated_Time"][32]
    ung=state_wise["Last_Updated_Time"][35]
    uor=state_wise["Last_Updated_Time"][16]
    upy=state_wise["Last_Updated_Time"][30]
    upb=state_wise["Last_Updated_Time"][11]
    urj=state_wise["Last_Updated_Time"][5]
    usk=state_wise["Last_Updated_Time"][37]
    usu=state_wise["Last_Updated_Time"][14]
    utn=state_wise["Last_Updated_Time"][2]
    uts=state_wise["Last_Updated_Time"][12]
    utr=state_wise["Last_Updated_Time"][22]
    uup=state_wise["Last_Updated_Time"][7]
    uuk=state_wise["Last_Updated_Time"][25]
    uwb=state_wise["Last_Updated_Time"][8]
    c24goa=state_wise["Delta_Confirmed"][26]
    c24gj=state_wise["Delta_Confirmed"][3]
    c24hr=state_wise["Delta_Confirmed"][17]
    c24hp=state_wise["Delta_Confirmed"][24]
    c24jk=state_wise["Delta_Confirmed"][15]
    c24jr=state_wise["Delta_Confirmed"][19]
    c24ka=state_wise["Delta_Confirmed"][13]
    c24kl=state_wise["Delta_Confirmed"][18]
    c24lh=state_wise["Delta_Confirmed"][27]
    c24ld=state_wise["Delta_Confirmed"][36]
    c24mp=state_wise["Delta_Confirmed"][6]
    c24mh=state_wise["Delta_Confirmed"][1]
    c24mn=state_wise["Delta_Confirmed"][29]
    c24mg=state_wise["Delta_Confirmed"][31]
    c24mz=state_wise["Delta_Confirmed"][32]
    c24ng=state_wise["Delta_Confirmed"][35]
    c24or=state_wise["Delta_Confirmed"][16]
    c24py=state_wise["Delta_Confirmed"][30]
    c24pb=state_wise["Delta_Confirmed"][11]
    c24rj=state_wise["Delta_Confirmed"][5]
    c24sk=state_wise["Delta_Confirmed"][37]
    c24su=state_wise["Delta_Confirmed"][14]
    c24tn=state_wise["Delta_Confirmed"][2]
    c24ts=state_wise["Delta_Confirmed"][12]
    c24tr=state_wise["Delta_Confirmed"][22]
    c24up=state_wise["Delta_Confirmed"][7]
    c24uk=state_wise["Delta_Confirmed"][25]
    c24wb=state_wise["Delta_Confirmed"][8]
    r24goa=state_wise["Delta_Recovered"][26]
    r24gj=state_wise["Delta_Recovered"][3]
    r24hr=state_wise["Delta_Recovered"][17]
    r24hp=state_wise["Delta_Recovered"][24]
    r24jk=state_wise["Delta_Recovered"][15]
    r24jr=state_wise["Delta_Recovered"][19]
    r24ka=state_wise["Delta_Recovered"][13]
    r24kl=state_wise["Delta_Recovered"][18]
    r24lh=state_wise["Delta_Recovered"][27]
    r24ld=state_wise["Delta_Recovered"][36]
    r24mp=state_wise["Delta_Recovered"][6]
    r24mh=state_wise["Delta_Recovered"][1]
    r24mn=state_wise["Delta_Recovered"][29]
    r24mg=state_wise["Delta_Recovered"][31]
    r24mz=state_wise["Delta_Recovered"][32]
    r24ng=state_wise["Delta_Recovered"][35]
    r24or=state_wise["Delta_Recovered"][16]
    r24py=state_wise["Delta_Recovered"][30]
    r24pb=state_wise["Delta_Recovered"][11]
    r24rj=state_wise["Delta_Recovered"][5]
    r24sk=state_wise["Delta_Recovered"][37]
    r24su=state_wise["Delta_Recovered"][14]
    r24tn=state_wise["Delta_Recovered"][2]
    r24ts=state_wise["Delta_Recovered"][12]
    r24tr=state_wise["Delta_Recovered"][22]
    r24up=state_wise["Delta_Recovered"][7]
    r24uk=state_wise["Delta_Recovered"][25]
    r24wb=state_wise["Delta_Recovered"][8]
    d24goa=state_wise["Delta_Deaths"][26]
    d24gj=state_wise["Delta_Deaths"][3]
    d24hr=state_wise["Delta_Deaths"][17]
    d24hp=state_wise["Delta_Deaths"][24]
    d24jk=state_wise["Delta_Deaths"][15]
    d24jr=state_wise["Delta_Deaths"][19]
    d24ka=state_wise["Delta_Deaths"][13]
    d24kl=state_wise["Delta_Deaths"][18]
    d24lh=state_wise["Delta_Deaths"][27]
    d24ld=state_wise["Delta_Deaths"][36]
    d24mp=state_wise["Delta_Deaths"][6]
    d24mh=state_wise["Delta_Deaths"][1]
    d24mn=state_wise["Delta_Deaths"][29]
    d24mg=state_wise["Delta_Deaths"][31]
    d24mz=state_wise["Delta_Deaths"][32]
    d24ng=state_wise["Delta_Deaths"][35]
    d24or=state_wise["Delta_Deaths"][16]
    d24py=state_wise["Delta_Deaths"][30]
    d24pb=state_wise["Delta_Deaths"][11]
    d24rj=state_wise["Delta_Deaths"][5]
    d24sk=state_wise["Delta_Deaths"][37]
    d24su=state_wise["Delta_Deaths"][14]
    d24tn=state_wise["Delta_Deaths"][2]
    d24ts=state_wise["Delta_Deaths"][12]
    d24tr=state_wise["Delta_Deaths"][22]
    d24up=state_wise["Delta_Deaths"][7]
    d24uk=state_wise["Delta_Deaths"][25]
    d24wb=state_wise["Delta_Deaths"][8]

    return render(request, 'home.html', {'confirmed':c, 'recovered':r, "update":u,
    'confirmed24':c24, 'deaths':d, 'recovered24':r24, "deaths24":d24, "update":u,
     "confirmedan":can,"recoveredan":ran,"deathsan":dan,"confirmed24an":c24an,"recovered24an":r24an,"deaths24an":d24an,"updatean":uan,
     "confirmedap":cap,"recoveredap":rap,"deathsap":dap,"confirmed24ap":c24ap,"recovered24ap":r24ap,"deaths24ap":d24ap,"updateap":uap,
     "confirmedar":car,"recoveredar":rar,"deathsar":dar,"confirmed24ar":c24ar,"recovered24ar":r24ar,"deaths24ar":d24ar,"updatear":uar,
     "confirmedas":cas,"recoveredas":ras,"deathsas":das,"confirmed24as":c24as,"recovered24as":r24as,"deaths24as":d24as,"updateas":uas,
     "confirmedbr":cbr,"recoveredbr":rbr,"deathsbr":dbr,"confirmed24br":c24br,"recovered24br":r24br,"deaths24br":d24br,"updatebr":ubr,
     "confirmedch":cch,"recoveredch":rch,"deathsch":dch,"confirmed24ch":c24ch,"recovered24ch":r24ch,"deaths24ch":d24ch,"updatech":uch,
     "confirmedchh":cchh,"recoveredchh":rchh,"deathschh":dchh,"confirmed24chh":c24chh,"recovered24chh":r24chh,"deaths24chh":d24chh,"updatechh":uchh,
     "confirmeddnhdd":cdnhdd,"recovereddnhdd":rdnhdd,"deathsdnhdd":ddnhdd,"confirmed24dnhdd":c24dnhdd,"recovered24dnhdd":r24dnhdd,"deaths24dnhdd":d24dnhdd,"updatednhdd":udnhdd,
     "confirmeddl":cdl,"recovereddl":rdl,"deathsdl":ddl,"confirmed24dl":c24dl,"recovered24dl":r24dl,"deaths24dl":d24dl,"updatedl":udl,
      "confirmedgoa":cgoa,"recoveredgoa":rgoa,"deathsgoa":dgoa,"confirmed24goa":c24goa,"recovered24goa":r24goa,"deaths24goa":d24goa,"updatedgoa":ugoa,
     "confirmedgj":cgj,"recoveredgj":rgj,"deathsgj":dgj,"confirmed24gj":c24gj,"recovered24gj":r24gj,"deaths24gj":d24gj,"updatedgj":ugj,
     "confirmedhr":chr,"recoveredhr":rhr,"deathshr":dhr,"confirmed24hr":c24hr,"recovered24hr":r24hr,"deaths24hr":d24hr,"updatedhr":uhr,
     "confirmedhp":chp,"recoveredhp":rhp,"deathshp":dhp,"confirmed24hp":c24hp,"recovered24hp":r24hp,"deaths24hp":d24hp,"updatedhp":uhp,
     "confirmedjk":cjk,"recoveredjk":rjk,"deathsjk":djk,"confirmed24jk":c24jk,"recovered24jk":r24jk,"deaths24jk":d24jk,"updatedjk":ujk,
     "confirmedjr":cjr,"recoveredjr":rjr,"deathsjr":djr,"confirmed24jr":c24jr,"recovered24jr":r24jr,"deaths24jr":d24jr,"updatedjr":ujr,
     "confirmedka":cka,"recoveredka":rka,"deathska":dka,"confirmed24ka":c24ka,"recovered24ka":r24ka,"deaths24ka":d24ka,"updatedka":uka,
     "confirmedkl":ckl,"recoveredkl":rkl,"deathskl":dkl,"confirmed24kl":c24kl,"recovered24kl":r24kl,"deaths24kl":d24kl,"updatedkl":ukl,
     "confirmedlh":clh,"recoveredlh":rlh,"deathslh":dlh,"confirmed24lh":c24lh,"recovered24lh":r24lh,"deaths24lh":d24lh,"updatedlh":ulh,
     "confirmedld":cld,"recoveredld":rld,"deathsld":dld,"confirmed24ld":c24ld,"recovered24ld":r24ld,"deaths24ld":d24ld,"updatedld":uld,
     "confirmedmp":cmp,"recoveredmp":rmp,"deathsmp":dmp,"confirmed24mp":c24mp,"recovered24mp":r24mp,"deaths24mp":d24mp,"updatedmp":ump,
     "confirmedmh":cmh,"recoveredmh":rmh,"deathsmh":dmh,"confirmed24mh":c24mh,"recovered24mh":r24mh,"deaths24mh":d24mh,"updatedmh":umh,
     "confirmedmn":cmn,"recoveredmn":rmn,"deathsmn":dmn,"confirmed24mn":c24mn,"recovered24mn":r24mn,"deaths24mn":d24mn,"updatedmn":umn,
     "confirmedmg":cmg,"recoveredmg":rmg,"deathsmg":dmg,"confirmed24mg":c24mg,"recovered24mg":r24mg,"deaths24mg":d24mg,"updatedmg":umg,
     "confirmedmz":cmz,"recoveredmz":rmz,"deathsmz":dmz,"confirmed24mz":c24mz,"recovered24mz":r24mz,"deaths24mz":d24mz,"updatedmz":umz,
     "confirmedng":cng,"recoveredng":rng,"deathsng":dng,"confirmed24ng":c24ng,"recovered24ng":r24ng,"deaths24ng":d24ng,"updatedng":ung,
     "confirmedor":cor,"recoveredor":ror,"deathsor":dor,"confirmed24or":c24or,"recovered24or":r24or,"deaths24or":d24or,"updatedor":uor,
     "confirmedpy":cpy,"recoveredpy":rpy,"deathspy":dpy,"confirmed24py":c24py,"recovered24py":r24py,"deaths24py":d24py,"updatedpy":upy,
     "confirmedpb":cpb,"recoveredpb":rpb,"deathspb":dpb,"confirmed24pb":c24pb,"recovered24pb":r24pb,"deaths24pb":d24pb,"updatedpb":upb,
     "confirmedrj":crj,"recoveredrj":rrj,"deathsrj":drj,"confirmed24rj":c24rj,"recovered24rj":r24rj,"deaths24rj":d24rj,"updatedrj":urj,
     "confirmedsk":csk,"recoveredsk":rsk,"deathssk":dsk,"confirmed24sk":c24sk,"recovered24sk":r24sk,"deaths24sk":d24sk,"updatedsk":usk,
     "confirmedsu":csu,"recoveredsu":rsu,"deathssu":dsu,"confirmed24su":c24su,"recovered24su":r24su,"deaths24su":d24su,"updatedsu":usu,
     "confirmedtn":ctn,"recoveredtn":rtn,"deathstn":dtn,"confirmed24tn":c24tn,"recovered24tn":r24tn,"deaths24tn":d24tn,"updatedtn":utn,
     "confirmedts":cts,"recoveredts":rts,"deathsts":dts,"confirmed24ts":c24ts,"recovered24ts":r24ts,"deaths24ts":d24ts,"updatedts":uts,
     "confirmedtr":ctr,"recoveredtr":rtr,"deathstr":dtr,"confirmed24tr":c24tr,"recovered24tr":r24tr,"deaths24tr":d24tr,"updatedtr":utr,
     "confirmedup":cup,"recoveredup":rup,"deathsup":dup,"confirmed24up":c24up,"recovered24up":r24up,"deaths24up":d24up,"updatedup":uup,
     "confirmeduk":cuk,"recovereduk":ruk,"deathsuk":duk,"confirmed24uk":c24uk,"recovered24uk":r24uk,"deaths24uk":d24uk,"updateduk":uuk,
     "confirmedwb":cwb,"recoveredwb":rwb,"deathswb":dwb,"confirmed24wb":c24wb,"recovered24wb":r24wb,"deaths24wb":d24wb,"updatedwb":uwb,
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
def research(request):
    return render(request, 'research.html')
