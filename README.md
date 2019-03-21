## March Madness Calculator

This script generates a possible final four for the Men's and Women's March Madness bracket given the win probabilities from 538. Could be modified to do Monte Carlo Simulations, but this is March Madness...so it runs each possibility only once. 

Thanks Otis R for help with probability calculations.

#### Usage for 2019 (from either Unix shell or Mac OS Terminal): 

    git clone https://github.com/svsaraf/march_madness.git
    cd march_madness
    python march_madness_calculator.py


#### Usage if you've tweaked the probabilities in another file

    python march_madness_calculator.py file_name_of_interest


Note that you may have to modify the download from 538 to use this if there are still play-in games - all teams should have a numerical seeding (not 11a for instance). 


#### Example output:

```
$ python march_madness_calculator.py 
Opening and generating possibilities with default file...
mens East
---------------

Round 2:
Duke wins over North Carolina Central           0.9428490958916509 < 0.9940245545631848
Central Florida wins over Virginia Commonwealth         0.8722448276944904 > 0.504988958792
Michigan State wins over Bradley            0.939449366982786 < 0.964466022879
Minnesota wins over Louisville          0.9544805644808375 > 0.677598713327
Louisiana State wins over Yale          0.6036320386292411 < 0.844167125989
Belmont wins over Maryland          0.6376845337214582 > 0.6318474196635837
Saint Louis wins over Virginia Tech         0.9289410376184719 > 0.888465655071
Mississippi State wins over Liberty         0.6318931357110233 < 0.786447979008
Round 3:
Central Florida wins over Duke          0.9870103079062664 > 0.910546336516633
Saint Louis wins over Mississippi State         0.19325851441833541 < 0.4315496705590493
Minnesota wins over Michigan State          0.8733444491800573 > 0.8031599673787785
Louisiana State wins over Belmont           0.2516793024251681 < 0.5890826051731379
Round 4:
Central Florida wins over Saint Louis           0.12236126880573595 < 0.8134984090338175
Minnesota wins over Louisiana State         0.29517204984866185 < 0.5306558051104353
Round 5:
Central Florida wins over Minnesota         0.36300986398658264 < 0.6577112963815107

mens South
---------------

Round 2:
Virginia wins over Gardner-Webb         0.35083705700250645 < 0.981433838804
Oklahoma wins over Mississippi          0.9906212554547451 > 0.470912476653
Tennessee wins over Colgate         0.7677650511781797 < 0.949730551269
Cincinnati wins over Iowa           0.42142702212305283 < 0.6769018052
Purdue wins over Old Dominion           0.5901369370920858 < 0.880954341402
Villanova wins over Saint Mary's (CA)           0.614105936328386 < 0.752671355034
Kansas State wins over UC-Irvine            0.7337249842118669 < 0.766624334373
Oregon wins over Wisconsin          0.950007524427566 > 0.60061374675
Round 3:
Virginia wins over Oklahoma         0.7293927046653188 < 0.8838914732268025
Kansas State wins over Oregon           0.5200462780118448 < 0.5310880898242908
Tennessee wins over Cincinnati          0.5028032226563499 < 0.6822568119011048
Villanova wins over Purdue          0.652469953479483 > 0.5254542635131488
Round 4:
Virginia wins over Kansas State         0.6821685522768045 < 0.7688527127591119
Tennessee wins over Villanova           0.4593083247724137 < 0.6273171190287467
Round 5:
Tennessee wins over Virginia            0.8302191943602544 > 0.5925540696861401

mens West
---------------

Round 2:
Gonzaga wins over Fairleigh Dickinson           0.08575206070667263 < 0.988693023253395
Syracuse wins over Baylor           0.5642794261140305 < 0.602978206888
Montana wins over Michigan          0.9591121351047034 > 0.939970361755
Florida wins over Nevada            0.8242625521234501 > 0.577826723869
Northern Kentucky wins over Texas Tech          0.9390492789497719 > 0.906052266678
Buffalo wins over Arizona State         0.08553700444088186 < 0.6692453446416844
Florida State wins over Vermont         0.6427012211667177 < 0.79029194326
Murray State wins over Marquette            0.9185325532933003 > 0.640227661361
Round 3:
Gonzaga wins over Syracuse          0.8677259891385094 < 0.8711697249441256
Florida State wins over Murray State            0.08750176414381361 < 0.6855834089960668
Florida wins over Montana           0.607167386626073 > 0.4310255276488594
Northern Kentucky wins over Buffalo         0.018212456273264843 < 0.4396042434103166
Round 4:
Florida State wins over Gonzaga         0.9814083636784815 > 0.7384390090718668
Florida wins over Northern Kentucky         0.04168867631317208 < 0.7027672945346335
Round 5:
Florida State wins over Florida         0.34055308561748987 < 0.6433517560171208

mens Midwest
---------------

Round 2:
North Carolina wins over Iona           0.9302811942179935 < 0.977912624507
Utah State wins over Washington         0.16613154332338875 < 0.505994711567
Kentucky wins over Abilene Christian            0.9052715734659992 < 0.969115415455
Wofford wins over Seton Hall            0.24189743516839912 < 0.633499192858
Houston wins over Georgia State         0.18009094270765003 < 0.891457522548
Iowa State wins over Ohio State         0.5595919631819909 < 0.672818443491
Kansas wins over Northeastern           0.22637426737184752 < 0.825215986225
Auburn wins over New Mexico State           0.2737280699948259 < 0.774212863023
Round 3:
North Carolina wins over Utah State         0.694545481400702 < 0.8682475080313233
Kansas wins over Auburn         0.12218323000966524 < 0.42210856635220395
Kentucky wins over Wofford          0.208130164829199 < 0.7204318976831554
Iowa State wins over Houston            0.8288871902220624 > 0.5499330297732369
Round 4:
Kansas wins over North Carolina         0.7862372288142412 > 0.6167991027146796
Iowa State wins over Kentucky           0.6531277896440612 > 0.5946078999464453
Round 5:
Iowa State wins over Kansas         0.9742820761516523 > 0.5538415596025544

womens Chicago
---------------

Round 2:
Notre Dame wins over Bethune-Cookman            0.6220487846198882 < 0.999698517977
Michigan State wins over Central Michigan           0.9450218000130496 > 0.596575986993
Stanford wins over UC-Davis         0.6590619979249475 < 0.959763780988
Brigham Young wins over Auburn          0.2881630142740911 < 0.453960847152
Iowa State wins over New Mexico State           0.26390183642273457 < 0.983691972151
DePaul wins over Missouri State         0.14862865594177987 < 0.829191126008
Wright State wins over Texas A&M            0.9501238088993436 > 0.924923048715
Marquette wins over Rice            0.7734294302165846 < 0.857612997531
Round 3:
Notre Dame wins over Michigan State         0.876325613972507 < 0.9773752573320318
Wright State wins over Marquette            0.10623194171235373 < 0.21545166984851546
Stanford wins over Brigham Young            0.41072179413609633 < 0.9496268306054089
DePaul wins over Iowa State         0.6784378213740945 > 0.6097201203144516
Round 4:
Notre Dame wins over Wright State           0.14898798366474308 < 0.9814747521036877
Stanford wins over DePaul           0.3397291852554344 < 0.5450835829550724
Round 5:
Notre Dame wins over Stanford           0.10254194692751073 < 0.8593963591625773

womens Greensboro
---------------

Round 2:
Baylor wins over Abilene Christian          0.8461758356930944 < 0.999330739863
California wins over North Carolina         0.3371185528230489 < 0.63816803686
Iowa wins over Mercer           0.7687918244277411 < 0.968536021005
Missouri wins over Drake            0.43835912542185196 < 0.664281441236
North Carolina State wins over Maine            0.010016319148323571 < 0.935541727576
Kentucky wins over Princeton            0.31201904852893914 < 0.684416680541
South Carolina wins over Belmont            0.6884538074893777 < 0.899738724143
Florida State wins over Bucknell            0.426607729129159 < 0.840055404594
Round 3:
Baylor wins over California         0.10779100640522277 < 0.9831086294997201
South Carolina wins over Florida State          0.2534547456723718 < 0.7229274227995883
Iowa wins over Missouri         0.3231532623696416 < 0.7503217295273675
Kentucky wins over North Carolina State         0.9222038769009825 > 0.7151095628124798
Round 4:
South Carolina wins over Baylor         0.8822605409705617 > 0.8545018521020715
Iowa wins over Kentucky         0.5090473487190491 < 0.5960849476151454
Round 5:
South Carolina wins over Iowa           0.7248699405360084 < 0.765456900840594

womens Albany
---------------

Round 2:
Louisville wins over Robert Morris          0.006904565019613229 < 0.997174973847
Michigan wins over Kansas State         0.2928961793984569 < 0.666324620303
Connecticut wins over Towson            0.9597788150754999 < 0.998963419198
Buffalo wins over Rutgers           0.7814615940864728 > 0.491231030365
Radford wins over Maryland          0.9792116790849272 > 0.977395089926
Tennessee wins over UCLA            0.8751059200315744 > 0.557352948124
Oregon State wins over Boise State          0.08918530311244155 < 0.959875983169
Arkansas-Little Rock wins over Gonzaga          0.9729372535902236 > 0.874339728814
Round 3:
Louisville wins over Michigan           0.914321115678069 < 0.9331917942603556
Oregon State wins over Arkansas-Little Rock         0.35998968337542814 < 0.958260902523507
Connecticut wins over Buffalo           0.48956955456294526 < 0.9711174029627093
Tennessee wins over Radford         0.9059117967517348 > 0.3291138343042099
Round 4:
Oregon State wins over Louisville           0.9910124699787466 > 0.7633240961768156
Tennessee wins over Connecticut         0.9822523810269856 > 0.9359961082493834
Round 5:
Tennessee wins over Oregon State            0.9993193800582 > 0.40560475648198574

womens Portland
---------------

Round 2:
Mississippi State wins over Southern            0.6247358276185585 < 0.999326240794
South Dakota wins over Clemson          0.36460087989613565 < 0.697805875722
Oregon wins over Portland State         0.42246861485805254 < 0.992037270359
Texas wins over Indiana         0.23864324401520653 < 0.763306047963
Syracuse wins over Fordham          0.40305762452171134 < 0.907797659384
Quinnipiac wins over South Dakota State         0.8129450335788685 > 0.648270274585
Miami (FL) wins over Florida Gulf Coast         0.4353349385165065 < 0.821469709626
Arizona State wins over Central Florida         0.5893618049440772 < 0.688352126265
Round 3:
Mississippi State wins over South Dakota            0.2277411334559296 < 0.9730472868359029
Arizona State wins over Miami (FL)          0.7127413218842007 > 0.6625305565311609
Oregon wins over Texas          0.8195795567041665 < 0.9137595060202912
Syracuse wins over Quinnipiac           0.02196670605103268 < 0.7741246635290051
Round 4:
Mississippi State wins over Arizona State           0.083260553111975 < 0.8456776882912383
Oregon wins over Syracuse           0.2510461850638652 < 0.8868841362623902
Round 5:
Mississippi State wins over Oregon          0.4029831586919428 < 0.4510840560816074