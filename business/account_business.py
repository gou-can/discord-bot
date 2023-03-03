import discord

from cache import Cache
from items import account_itmes
# from redis_tool import get_key
# from redis_tool import tool as redis_ctl
from configger import config

_alpha_role_txt = "Click to get alpha call role!"
_alpha_role_msg_id = 0
_alpha_role_emoji = "🚀"
# GenesisCodeList = ['c5dj9w', 'kd24mp', '7kc8a2', 'u1h37h', 'ydvqff', 'kpfd55', '2pz895', '9emijn', 'mgkb3w', '4edyua', 'b2srdu', 'pgsmv2', 'agbjgg', 'frqrg1', 'yaeent', 'wh9hfw', 'u7wi9s', 'gtckxs', '9covyu', '1zqksi', '2wrr6p', 'vh15ak', 'qrxu1w', 'pekpfv', 'zcy7ar', 'ghpojp', 'm8fg47', 'm4z6i1', 'xsz7j4', '55y3r3', 'hhtznn', 'gkskj5', 'wm8gsh', 'kkwb2p', 'ihbrks', 'kxq8sh', 'z752xt', 'ewgaar', 'iipz64', '5m8gbc', 'rgwsq9', 'a9vanz', 'ma5j11', 'tw1ofg', '7o2o4i', 'z44sdk', 'tmp9jr', 'dx48b9', 'autpum', 'u65u19', '9zvkg3', 'ob1uvn', 'ksbo6q', 'iryp9b', 'qb8nd2', '6v79ae', 'vxvm97', 'g8a8ko', '72hsxc', '8k76ry', '7vrrwm', '9exhua', 'efegw5', 'mniy1q', 'ybuw5j', '4nyf2s', 'pg44v3', 'vvyebn', '8msg4v', '3bkftj', 'gj4rrb', '5gq5jh', 'vmqzak', '1hcb1t', 'qa6q8e', 'pwmkwu', '7xucw2', 'i1zw2e', 'k93gq7', 'f76sua', 'bqpz32', 'oaj1j6', 'w13y4t', 'doffx9', 'pn18py', '3yg8pk', 'vdsvy5', '985tn1', '6jk8iy', '67hipk', '6sr6nn', 'kgorts', '88cmuq', '31ycr3', 'j8f9yw', 'y42nw8', 'vyotdg', '5cfzkj', '2ok2qi', 'nmytte', 'zq6z38', 'iacj11', 'jmw7nx', 'y8gpt2', 'kcxvke', 'kdrhz4', 'sw64d3', 'naj3z2', 'parnvs', '6osp7u', 'g8yyd3', 'qyu429', 'ce7svu', 'd626az', 'esrt9k', 'tyb925', 'f8js4u', 'ewqguc', '8c12ew', 'ooo8b4', 'uraup4', 'bmpytu', 'daauko', '8qbi2i', 'pzinge', 'hy5dug', 'xaojwe', '71yxzn', 'kfqk94', 'ad5zrk', 'k6w7rn', 'gwg8mj', 'qdp1ab', 'smnuz4', '41kprx', '4odcqs', '8yjtev', '947pgm', 'joty2w', 't1xjku', '8zceny', 'pwxmq3', 'z9jtor', '58gs8e', '7xj4y9', 'ythbof', 'y1qyzp', 'c9wd9e', 'tsgg7s', 'ow1ik3', 'g7quu5', '2w5gsr', 's2k2fy', 'qqbv37', 'wiaxnj', '3qe2iz', 'rg6hz2', '1oft48', '26wqa8', 'btb2kt', 'bsu1py', '4wbigy', '45kns3', 'oaif4e', '624rnx', 'd55jio', 'itoo1p', 'g7gmvj', 'w25t5u', 'fiqycq', 'tpnwd4', '5xisuj', '9mdoig', '3mqsf2', '9ocdon', 'tadpat', '8cnr79', 'ouc82k', 'zwib3k', '69mk8k', 'psquwu', '66b8jg', 'dysm1n', '7wpt63', '94sjg7', 'pu7rt8', 'pogi1y', 'yd73fs', 'jqh6tn', 'nzv8s6', '3734i4', 'i4yqzv', '355hqq', 'eh19uj', 'fjgr3m', 'd8k6b9', '5riibc', 'g3just', 'c1df8i', 'mtr2pu', 'qg3t5v', 'hzhvgv', 'njdrja', '98j8at', 'zgbru8', '848b2p', 'otvyda', '3w5z12', 'hcwg23', 'dajvr1', 'p3hss7', 'onrq6p', 'djc1zu', 'psbfjv', '94xwi6', '12froi', 'wmh74e', '43g7g7', 'vy8vbr', 'mk3fh5', 'oqs94d', 'n8218w', 'i9agvd', 'au9nqm', 'x9pto2', 'dr11ja', 'bnaq56', 'i8c9w6', 'i5xja7', '5hpgwv', 'oimire', '55vkup', 'wfp7w6', 'iow784', 'fpktkj', 'mdehok', '2w2to2', 'krsy4w', 'huagyg', 'mptd1h', 'tze9r8', 'ugko97', 'werw6f', 'amc3br', '6hb1dk', 'ikis9d', 'ye3cso', 'p8ejog', '35rdbo', 'kwjrm8', '326vzi', 'ni4ab8', 'pqaw31', '4xhnes', 'x3u322', '8azytc', 'dhbim2', 'jhwcr7', 'u439q1', 'ogrnw9', 'dzkdeh', 'xcau53', '2ckd72', 'iercgd', '2n6qh9', 'mjdrci', 'szpzzw', 'auq6io', '9p8t4i', 'k5gmor', 'ze276u', '66pdd3', '99mnfw', 'srt8yz', '9td83w', 'a7dmti', 'vaytc2', 'ardr3i', 'ch294q', 'vwdusk', 'qadyb2', 'ea9vhk', 'k9rvs2', 'co51ta', 't1nowv', 'zzzyta', 'fhpwg8', 'n27364', '4i551b', 'mgytq5', 'upzfmu', 'ptvxav', 'uwm9j1', '8oky3g', '83u19z', 'jy1pbg', 'serjpk', 'x53y2u', 'qx55xh', 'gc1ptn', 'j2maxe', '8gnutv', 'd6ccsi', 'ex6hde', '5t3nkj', 'uqds7m', 'xs61if', 'mijt3m', 'icf59e', 'jsun9n', '3csyqt', 'ayizyy', '7vuou4', 'cu78y1', 't5vqu2', '7g1kn3', 'zh3zkn', 'mdrgz1', '75vt3y', 'bjdez5', 'xmp25q', 'umgb95', 'nzc823', 'zzjfuw', '4xm7ih', '2mj59p', 'g3vjzu', 'pffdzo', 'jetd9w', '724vrv', 'p8w6b5', 'gyt1ey', 'aqfak5', '57fjhy', '3x5265', '7prq31', 'fxh2xq', 'pt1779', '5tfyhk', '1hwtx9', '276c6m', 'k14swn', 'wy5krb', 'fh98e8', 'ycstsz', '6mhwdc', 'ddfcmu', 'nzdhz9', 'osq2g1', '4fcia6', 'ovm9m4', 'xfck7d', 's8mes6', 'a9imsf', 'dikz3p', 'ffxx38', 'c2po5z', 'oyr5we', '2upjm9', '8hpicv', 'hgv5d8', 'fwnjfk', 'z86zv8', 'drvgeg', 'ewznhu', '93qiy4', 'msued4', 'tgvate', '7itjm7', '8s3mto', '3it91u', 'bmkay6', 'mnncid', 'dnuuwi', '1diy8m', '1yt92y', 'jygd1c', 'skq8hz', '3th7vr', '1jr9rj', 'b2powg', 'zy5f1d', 'jb5t73', 'xfqpg8', 'g3b5fz', 'onwpej', 'cwij1k', 'qevotv', 'ngazby', 'i92pkk', 'idheox', '3bfadf', 'w1oyt8', 'hf6ghj', 'zhjutm', '219nso', 't4mtaq', '68c6cf', 'boisa6', 'wv7tgs']
# GenesisCodeList += ['i683xq', 'toqrd4', '1tjrwa', 'gm3pe6', 'qs7jhf', 'yjpfd3', 'p6pu5g', '1ie45x', 'vtxw26', 't2ewaj', 'q8vtbe', 'wgr8y9', 'ejmdd9']
#
# Lock = False
# og_dt = {1032260065954103327: 'b2srdu', 886970990972796998: 'pgsmv2', 784032723378765824: 'agbjgg', 701042544347316226: 'frqrg1', 434494993952931840: 'yaeent', 253832248653119488: 'wh9hfw', 930799112339742762: 'u7wi9s', 984655773068062750: 'gtckxs', 879256295734140938: '9covyu', 895348433689378866: '1zqksi', 890869255329968171: '2wrr6p', 973943204879683614: 'vh15ak', 906984360513785966: 'qrxu1w', 890856035127013386: 'pekpfv', 1014912745830883349: 'zcy7ar', 958899699774009364: 'ghpojp', 162239013170708480: 'm8fg47', 935079967895748618: 'm4z6i1', 871229599567208508: 'xsz7j4', 991274915112157236: '55y3r3', 888657636998910013: 'hhtznn', 948242831787589695: 'gkskj5', 917989878124392498: 'wm8gsh', 406154132068499457: 'kkwb2p', 978191262375092284: 'ihbrks', 943390971146690631: 'kxq8sh', 861270943741640704: 'z752xt', 159985870458322944: 'ewgaar', 804684634985201685: 'iipz64', 904789418999701554: '5m8gbc', 1051755863355957268: 'rgwsq9', 1009054771627425792: 'a9vanz', 966275949509353472: 'ma5j11', 967981332124827720: 'tw1ofg', 861486215395672094: '7o2o4i', 901899693087400006: 'z44sdk', 895433969573707826: 'tmp9jr', 362229078998384641: 'dx48b9', 449244466663129099: 'autpum', 929445167814033418: 'u65u19', 826494911976177704: '9zvkg3', 944172223084756992: 'ob1uvn', 981189875413950555: 'ksbo6q', 803951159060463617: 'iryp9b', 930586771333468291: 'qb8nd2', 341970778650181643: '6v79ae', 406215819413028864: 'vxvm97', 845617496429166592: 'g8a8ko', 968295920481493043: '72hsxc', 999289653251280918: '8k76ry', 294095723266572288: '7vrrwm', 880237415485280286: '9exhua', 962959902198890556: 'efegw5', 874120979780091915: 'mniy1q', 512160974409564161: 'ybuw5j', 879295503878209597: '4nyf2s', 907066453683998731: 'pg44v3', 793783348165607424: 'vvyebn', 951044184284991498: '8msg4v', 277245433452167168: '3bkftj', 852944879793340416: 'gj4rrb', 767482613199274025: '5gq5jh', 557628352828014614: 'vmqzak', 538762610225709057: '1hcb1t', 936623390842830908: 'qa6q8e', 892020402010865694: 'pwmkwu', 943731952933015572: '7xucw2', 1005859610525192212: 'i1zw2e', 940319269638512722: 'k93gq7', 905144895877034025: 'f76sua', 477530207042011147: 'bqpz32', 368105370532577280: 'oaj1j6', 933964555854446622: 'w13y4t', 244123024943480833: 'doffx9', 340064503364452353: 'pn18py', 1032217686475808778: '3yg8pk', 837900644148707338: 'vdsvy5', 917251273470931045: '985tn1', 231890837540306944: '6jk8iy', 895075282803900446: '67hipk', 994794514181009449: '6sr6nn', 932269363237621770: 'kgorts', 941532458585817180: '88cmuq', 940192101382098947: '31ycr3', 139616392323268609: 'j8f9yw', 932299332630245417: 'y42nw8', 871662497059471402: 'vyotdg', 836313060393484348: '5cfzkj', 918941964018274376: '2ok2qi', 908900495618371635: 'nmytte', 371210518066888710: 'zq6z38', 299461710543323137: 'iacj11', 909076850989465621: 'jmw7nx', 1033768378260783124: 'y8gpt2', 804630524244525058: 'kcxvke', 956917642688618506: 'kdrhz4', 958895711418740766: 'sw64d3', 897106711981219941: 'naj3z2', 920255420675813387: 'parnvs', 744848162199699617: '6osp7u', 997450010193047653: 'g8yyd3', 625479536598843423: 'qyu429', 550680964070637570: 'ce7svu', 959524323691995266: 'd626az', 492937624030543879: 'esrt9k', 813425924376100865: 'tyb925', 914193187181035591: 'f8js4u', 998439330177630360: 'ewqguc', 879020284798193705: '8c12ew', 670214662523977748: 'ooo8b4', 964771406019694602: 'uraup4', 595471069645635606: 'bmpytu', 1010565374619689030: 'daauko', 507506684936192023: '8qbi2i', 1049628295462932551: 'pzinge', 746903913680207883: 'hy5dug', 498506510331150337: 'xaojwe', 900002901294977094: '71yxzn', 367788057837174805: 'kfqk94', 922860901286178827: 'ad5zrk', 904644874039599105: 'k6w7rn', 897553465981669496: 'gwg8mj', 975437106304389151: 'qdp1ab', 504429901701578763: 'smnuz4', 927914984489484328: '41kprx', 324909654864035851: '4odcqs', 960207221617201223: '8yjtev', 940798725679382568: '947pgm', 1031022873671913524: 'joty2w', 287378474497343488: 't1xjku', 381092710343507969: '8zceny', 397844749324910593: 'pwxmq3', 920358138505465888: 'z9jtor', 935241483840262184: '58gs8e', 364454049036369930: '7xj4y9', 408128790510698498: 'ythbof', 646909221014601748: 'y1qyzp', 769195942552666202: 'c9wd9e', 932274676527403088: 'tsgg7s', 879426265768153098: 'ow1ik3', 295054211828154371: 'g7quu5', 902276379129810944: '2w5gsr', 562419641075630090: 's2k2fy', 533990926662631445: 'qqbv37', 900293815414423572: 'wiaxnj', 970478084723716096: '3qe2iz', 236882112081297409: 'rg6hz2', 915674954924712007: '1oft48', 761860041702899723: '26wqa8', 524931156840546314: 'btb2kt', 885611634196881470: 'bsu1py', 944946943103205416: '4wbigy', 936125509803311204: '45kns3', 918567007958466590: 'oaif4e', 927156447421300847: '624rnx', 842623038038212638: 'd55jio', 823476634304774187: 'itoo1p', 912920494301388800: 'g7gmvj', 813658029349273630: 'w25t5u', 907824445211672618: 'fiqycq', 847981997191462912: 'tpnwd4', 921604497950777375: '5xisuj', 951862684528308244: '9mdoig', 576086070182019072: '3mqsf2', 956693874947022908: '9ocdon', 793547078495895625: 'tadpat', 155149108183695360: '8cnr79', 932276205456080956: 'ouc82k', 930540514825080943: 'zwib3k', 129379459491954692: '69mk8k', 375668356994301954: 'psquwu', 997445397544964116: '66b8jg', 294353552057303040: 'dysm1n', 949641655898755072: '7wpt63', 926416069743247370: '94sjg7', 867791093939961866: 'pu7rt8', 968186125875282001: 'pogi1y', 1034137364534132747: 'yd73fs', 652094552374509592: 'jqh6tn', 870112078797631498: 'nzv8s6', 947415166771945502: '3734i4', 920230309948166195: 'i4yqzv', 933665274299822080: '355hqq', 228894231630970881: 'eh19uj', 904408696619151381: 'fjgr3m', 837901274187694111: 'd8k6b9', 941397120236290078: '5riibc', 918045980186771466: 'g3just', 788992689239752748: 'c1df8i', 932270912907128852: 'mtr2pu', 951946149055569940: 'qg3t5v', 801018216192147488: 'hzhvgv', 881878475626119209: 'njdrja', 852035400491204639: '98j8at', 390841699657580544: 'zgbru8', 436839798569959426: '848b2p', 977325810413342730: 'otvyda', 900365100655976458: '3w5z12', 955814019028094996: 'hcwg23', 742161869657341974: 'dajvr1', 959047274934181908: 'p3hss7', 848382450328797236: 'onrq6p', 937778324493713478: 'djc1zu', 726403775773802527: 'psbfjv', 902663067022790727: '94xwi6', 313319095779065866: '12froi', 935480255827832852: 'wmh74e', 859675755427921955: '43g7g7', 405340782611136532: 'vy8vbr', 764842596421074954: 'mk3fh5', 961301510527021127: 'oqs94d', 885269054686892062: 'n8218w', 981823020681273374: 'i9agvd', 767481270548299837: 'au9nqm', 304930060320768000: 'x9pto2', 770635462921945108: 'dr11ja', 885645739970162718: 'bnaq56', 793853718902472724: 'i8c9w6', 258330453726068736: 'i5xja7', 922133299470688287: '5hpgwv', 945599835527086100: 'oimire', 1005747416957456404: '55vkup', 934556738156392468: 'wfp7w6', 932275809937399858: 'iow784', 940173219103666182: 'fpktkj', 913781078559457303: 'mdehok', 983733403251789865: '2w2to2', 425250979496067083: 'krsy4w', 333515024087777281: 'huagyg', 1041765559399878707: 'mptd1h', 989848566384181248: 'tze9r8', 975570318464806932: 'ugko97', 816695328253542450: 'werw6f', 689779624443641960: 'amc3br', 1048832200738611240: '6hb1dk', 836821662984962118: 'ikis9d', 783404169339338752: 'ye3cso', 163322557938925568: 'p8ejog', 905113058102370304: '35rdbo', 956100688323174431: 'kwjrm8', 932271821150117899: '326vzi', 996329629822488667: 'ni4ab8', 334741821940957186: 'pqaw31', 917766960253640714: '4xhnes', 898478233849303080: 'x3u322', 955745509098815540: '8azytc', 700299479399792800: 'dhbim2', 934816611259547669: 'jhwcr7', 898080304063975434: 'u439q1', 440821644488081408: 'ogrnw9', 907590248601645077: 'dzkdeh', 397153549609467905: 'xcau53', 915675799632375888: '2ckd72', 861607937985609758: 'iercgd', 246856483243950081: '2n6qh9', 932261918968799264: 'mjdrci', 771614394983251978: 'szpzzw', 660452594375852037: 'auq6io', 1049930460622508072: '9p8t4i', 956469158680350760: 'k5gmor', 367454099886702594: 'ze276u', 896491182186709022: '66pdd3', 896983987954786315: '99mnfw', 891110860410470421: 'srt8yz', 442499633160257546: '9td83w', 886135894216695859: 'a7dmti', 955814022857519164: 'vaytc2', 408204817815699458: 'ardr3i', 852810755081633793: 'ch294q', 869410195678314527: 'vwdusk', 864114538135945246: 'qadyb2', 829902236217638962: 'ea9vhk', 943837929111978025: 'k9rvs2', 829909193779576893: 'co51ta', 1006969711176732883: 't1nowv', 1045902179732561991: 'zzzyta', 810922497507459112: 'fhpwg8', 980041157767733288: 'n27364', 904575721429663785: '4i551b', 351210609636802571: 'mgytq5', 781543791584083998: 'upzfmu', 813152237802749982: 'ptvxav', 947696734367264848: 'uwm9j1', 985426831073247302: '8oky3g', 921181493563359264: '83u19z', 442572024624185344: 'jy1pbg', 954995710053462028: 'serjpk', 830775147552047115: 'x53y2u', 635550126987018290: 'qx55xh', 969003103473000508: 'gc1ptn', 697891749191745596: 'j2maxe', 449551896122753024: '8gnutv', 921883568144252989: 'd6ccsi', 967994695110254653: 'ex6hde', 575454072950226945: '5t3nkj', 350435982618918913: 'uqds7m', 382843539232653312: 'xs61if', 273860220378284032: 'mijt3m', 848348105354903573: 'icf59e', 982123901310099486: 'jsun9n', 953226891085631498: '3csyqt', 581143151582904387: 'ayizyy', 968794214123048960: '7vuou4', 857425598166990868: 'cu78y1', 513623058104451072: 't5vqu2', 932298035499773972: '7g1kn3', 899212668756426774: 'zh3zkn', 932294027657752647: 'mdrgz1', 861479703969136640: '75vt3y', 282117661540745216: 'bjdez5', 949575613470089266: 'xmp25q', 859110114287026188: 'umgb95', 949207954232578048: 'nzc823', 474937339840299009: 'zzjfuw', 948463904009388052: '4xm7ih', 995999059288535050: '2mj59p', 250265647584509955: 'g3vjzu', 948305917181591552: 'pffdzo', 894003907515281459: 'jetd9w', 735487516605546546: '724vrv', 973185647428902932: 'p8w6b5', 366962832442654720: 'gyt1ey', 867070534696042497: 'aqfak5', 734545948994174978: '57fjhy', 693460435168395284: '3x5265', 957602940032528445: 'c5dj9w', 768366787259400212: 'kd24mp', 996394673105023027: '7kc8a2', 494646371765321749: 'u1h37h', 924329121310453780: 'ydvqff', 956133660178923541: 'kpfd55', 1018472954444660778: '2pz895', 232150429419569152: '9emijn', 885315650371870720: 'mgkb3w', 380302654531960834: '4edyua', 1023157532430172190: '7prq31', 1024373687643811910: 'fxh2xq', 1050628782089846794: 'pt1779', 906886221161173012: '5tfyhk', 986256549116801085: '1hwtx9', 932524177318105178: '276c6m', 872453616521342997: 'k14swn', 849210290222792784: 'wy5krb', 941375915269685298: 'fh98e8', 944986320156123156: 'ycstsz', 1011246037429653545: '6mhwdc', 961960538370355220: 'ddfcmu', 409640753367875586: 'nzdhz9', 411268651795218442: 'osq2g1', 945901201071947907: '4fcia6', 814302894353940480: 'ovm9m4', 884416554320691240: 'xfck7d', 693871076152836126: 's8mes6', 402123517161898005: 'a9imsf', 880285492376129578: 'dikz3p', 944462218911711313: 'ffxx38', 763717679176613938: 'c2po5z', 1037618592520339498: 'oyr5we', 652559941449809932: '2upjm9', 228424422183272448: '8hpicv', 922080219790196786: 'hgv5d8', 993920014480580749: 'fwnjfk', 812287138200420362: 'z86zv8', 1006783433294495784: 'drvgeg', 915908183149641788: 'ewznhu', 752901623746920448: '93qiy4', 519078121564012545: 'msued4', 870140522533105705: 'tgvate', 934152536284344350: '7itjm7', 949522768460910623: '8s3mto', 984717063203459142: '3it91u', 918414211586097172: 'bmkay6', 684820705350910049: 'mnncid', 899305721693368340: 'dnuuwi', 573261870606057497: '1diy8m', 703651750728564777: '1yt92y', 922370440561840130: 'jygd1c', 464789440418807808: 'skq8hz', 934628647241932900: '3th7vr', 1017314018853134366: '1jr9rj', 964445143484755998: 'b2powg'}
# GenesisCodeSet = set(og_dt.values())


async def send_genesis_code_msg(ctx, channel):
    text = f"The first 300 Producers who give the reaction will receive a Producer Code"
    embed = discord.Embed(description=text)

    embed.set_image(url="https://cdn.discordapp.com/attachments/997037889995165706/1051694200871211028/20221212-105643.jpeg")
    view = discord.ui.View()
    item = account_itmes.GenesisCodeItem()
    view.add_item(item)
    # key = get_key.get_genesis_code_list_key()
    # redis_ctl.redis_lpush()
    await channel.send(embed=embed, view=view)


async def send_genesis_code(interaction: discord.Interaction):

    code = get_code234(interaction.user.id)
    if not code:
        return
    await interaction.response.send_message(
        code + ", you can apply for Producer List:https://question.producerc.xyz/",
        ephemeral=True)
    team_channel = interaction.guild.get_channel(config.config.cfg[Cache.bot_cfg_Key]['team_channel_id'])
    await team_channel.send(f"{interaction.user} get {code} ")


async def send_last_genesis_code(interaction: discord.Interaction):
    text = "The first 300 Producers who give the reaction will receive a Producer Code"
    embed = discord.Embed(description=text)
    embed.set_image(url="https://cdn.discordapp.com/attachments/997037889995165706/1051694200871211028/20221212-105643.jpeg")
    embed.add_field(name="total", value=f"0", inline=False)
    view = discord.ui.View()
    item = account_itmes.GenesisCodeItem(disable=True)
    view.add_item(item)
    # print("inter", interaction.user)
    await interaction.message.edit(embed=embed, view=view)


def init_code(ctx):
    pass
    # role = ctx.guild.get_role(1051843859153420388)
    # members = role.members
    #
    # lt = GenesisCodeList
    # members = [m for m in members if m.id not in og_dt]
    #
    # # for i in range(len(members)):
    # #     if members[i].id in og_dt:
    # #         continue
    # #     if lt[i] in GenesisCodeSet:
    # #         continue
    # #     og_dt[members[i].id] = lt[i]
    # #     GenesisCodeSet.add(lt[i])
    #
    #
    # for m in members:
    #     if m.id in og_dt:
    #         continue
    #     for code in lt:
    #         if code not in GenesisCodeSet:
    #             og_dt[m.id] = code
    #             GenesisCodeSet.add(code)
    #             break
    #
    # print("og_dt", og_dt)
    # print("GenesisCodeSet", GenesisCodeSet)
    # return len(og_dt)


def get_code234(user_id):
    pass
    # return og_dt.get(user_id)


async def send_alpha_role_msg(ctx):
    channel = ctx.guild.get_channel(config.config.cfg[Cache.bot_cfg_Key]['members_channel_id'])

    embed = discord.Embed(title=_alpha_role_txt)
    msg = await channel.send(embed=embed)
    await msg.add_reaction(_alpha_role_emoji)
    global _alpha_role_msg_id
    _alpha_role_msg_id = msg.id
    # print("msg", msg.id)


async def listen_alpha_role_add(guild: discord.Guild, payload: discord.RawReactionActionEvent):
    if payload.channel_id != config.config.cfg[Cache.bot_cfg_Key]['members_channel_id']:
        return
    if payload.emoji.name != _alpha_role_emoji:
        return

    if _alpha_role_msg_id == 0:
        ok = await init_alpha_role_msg_id(guild, payload.message_id)
        if not ok:
            return
    elif payload.message_id != _alpha_role_msg_id:
        return

    role = guild.get_role(config.config.cfg[Cache.bot_cfg_Key]['alpha_call_role_id'])

    await payload.member.add_roles(role)


async def listen_alpha_role_remove(guild: discord.Guild, payload: discord.RawReactionActionEvent):
    # print("_alpha_role_msg_id", _alpha_role_msg_id)
    # print("payload", payload.message_id)
    if payload.channel_id != config.config.cfg[Cache.bot_cfg_Key]['members_channel_id']:
        return
    if payload.emoji.name != _alpha_role_emoji:
        return

    if _alpha_role_msg_id == 0:
        ok = await init_alpha_role_msg_id(guild, payload.message_id)
        print("ok", ok)
        if not ok:
            return
    elif payload.message_id != _alpha_role_msg_id:
        return

    role = guild.get_role(config.config.cfg[Cache.bot_cfg_Key]['alpha_call_role_id'])
    # print("payload.member", payload.user_id)
    await guild.get_member(payload.user_id).remove_roles(role)


async def init_alpha_role_msg_id(guild: discord.Guild, msg_id):
    channel = guild.get_channel(config.config.cfg[Cache.bot_cfg_Key]['members_channel_id'])
    try:
        msg = await channel.fetch_message(msg_id)
    except:
        print("msg not found")
        return False
    if msg.embeds and msg.embeds[0].title == _alpha_role_txt:
        global _alpha_role_msg_id
        _alpha_role_msg_id = msg_id
        return True

    return False
