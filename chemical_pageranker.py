# Public domain

import requests


manifest = ["Q101497", 
"Q102769", 
"Q1038", 
"Q104085", 
"Q1053", 
"Q10749005", 
"Q10876", 
"Q1089", 
"Q1090", 
"Q1091", 
"Q1094", 
"Q1096", 
"Q1099", 
"Q1100", 
"Q1103", 
"Q1112", 
"Q1123", 
"Q1136648", 
"Q11426", 
"Q11450699", 
"Q114675", 
"Q1147539", 
"Q116269", 
"Q1193660", 
"Q12144", 
"Q12269575", 
"Q126625", 
"Q1287838", 
"Q129163", 
"Q130336", 
"Q130971", 
"Q131656", 
"Q132298", 
"Q132501", 
"Q13848921", 
"Q1388", 
"Q1484569", 
"Q14982", 
"Q14985", 
"Q150429", 
"Q150440", 
"Q150681", 
"Q150694", 
"Q150717", 
"Q150731", 
"Q150744", 
"Q151797", 
"Q153", 
"Q1562648", 
"Q15779", 
"Q15975449", 
"Q161210", 
"Q161233", 
"Q161268", 
"Q161271", 
"Q161275", 
"Q161276", 
"Q161280", 
"Q161282", 
"Q161284", 
"Q161287", 
"Q161296", 
"Q161301", 
"Q161471", 
"Q161475", 
"Q161478", 
"Q161480", 
"Q161495", 
"Q161496", 
"Q161503", 
"Q161529", 
"Q161532", 
"Q161589", 
"Q161655", 
"Q162867", 
"Q16391", 
"Q16392", 
"Q1688256", 
"Q170591", 
"Q1706418", 
"Q172275", 
"Q177342", 
"Q1778575", 
"Q178266", 
"Q179452", 
"Q179724", 
"Q1801", 
"Q181559", 
"Q182040", 
"Q18216", 
"Q182849", 
"Q18351604", 
"Q1838431", 
"Q184782", 
"Q185006", 
"Q185076", 
"Q1853255", 
"Q18555422", 
"Q186414", 
"Q1864653", 
"Q1876830", 
"Q1880736", 
"Q1884806", 
"Q18882035", 
"Q190020", 
"Q190077", 
"Q191924", 
"Q192470", 
"Q193414", 
"Q193521", 
"Q19414", 
"Q194207", 
"Q194309", 
"Q194406", 
"Q1950418", 
"Q1953551", 
"Q19563", 
"Q195823", 
"Q1959597", 
"Q1960244", 
"Q196661", 
"Q1976186", 
"Q1987204", 
"Q1997", 
"Q20054517", 
"Q20054533", 
"Q2007270", 
"Q2013804", 
"Q201382", 
"Q2020228", 
"Q202218", 
"Q202251", 
"Q2025", 
"Q2043499", 
"Q2048380", 
"Q204923", 
"Q204980", 
"Q2051705", 
"Q207843", 
"Q207877", 
"Q207895", 
"Q2080990", 
"Q208366", 
"Q209188", 
"Q209195", 
"Q209222", 
"Q209323", 
"Q209332", 
"Q209354", 
"Q209373", 
"Q209376", 
"Q209381", 
"Q209404", 
"Q209450", 
"Q209453", 
"Q209460", 
"Q2095629", 
"Q20963640", 
"Q20963647", 
"Q20963648", 
"Q20963650", 
"Q20963679", 
"Q20963681", 
"Q20963908", 
"Q20963940", 
"Q20964244", 
"Q20964363", 
"Q20965030", 
"Q20965073", 
"Q20965201", 
"Q20965240", 
"Q20965319", 
"Q20965962", 
"Q20966042", 
"Q20966400", 
"Q20966410", 
"Q20966474", 
"Q20966491", 
"Q20966917", 
"Q20966927", 
"Q20968563", 
"Q20968579", 
"Q20972145", 
"Q20983235", 
"Q210385", 
"Q21042439", 
"Q21057305", 
"Q21057310", 
"Q21057311", 
"Q21057316", 
"Q21057320", 
"Q21057847", 
"Q21058099", 
"Q21059832", 
"Q21060412", 
"Q21060492", 
"Q21060906", 
"Q21060907", 
"Q211086", 
"Q211171", 
"Q211433", 
"Q21167741", 
"Q21175367", 
"Q212364", 
"Q214769", 
"Q214863", 
"Q2170375", 
"Q2179668", 
"Q2180922", 
"Q2194382", 
"Q219626", 
"Q220410", 
"Q22082729", 
"Q22082745", 
"Q22082750", 
"Q221307", 
"Q22132784", 
"Q22132798", 
"Q22132817", 
"Q22133107", 
"Q22133309", 
"Q22133386", 
"Q22133393", 
"Q22133399", 
"Q22133404", 
"Q22137005", 
"Q22137013", 
"Q22137016", 
"Q22137036", 
"Q22137042", 
"Q22137046", 
"Q22137047", 
"Q22137048", 
"Q22137050", 
"Q22137062", 
"Q22137069", 
"Q22137070", 
"Q22137078", 
"Q22138333", 
"Q22138343", 
"Q22138388", 
"Q22138395", 
"Q22138402", 
"Q22138414", 
"Q22138417", 
"Q22138421", 
"Q22157170", 
"Q22157957", 
"Q22158401", 
"Q22159020", 
"Q22159079", 
"Q222936", 
"Q222968", 
"Q222991", 
"Q223011", 
"Q223083", 
"Q223101", 
"Q22329230", 
"Q22329266", 
"Q22329336", 
"Q22330060", 
"Q22330219", 
"Q22330463", 
"Q22330487", 
"Q225045", 
"Q2257129", 
"Q2257591", 
"Q2270", 
"Q2275328", 
"Q229848", 
"Q2362625", 
"Q23757", 
"Q23767", 
"Q2380192", 
"Q2404344", 
"Q2404890", 
"Q2409", 
"Q2415195", 
"Q2416556", 
"Q243354", 
"Q2442512", 
"Q2447", 
"Q2452578", 
"Q2467070", 
"Q2468", 
"Q2506823", 
"Q2509768", 
"Q2528979", 
"Q2533785", 
"Q2557079", 
"Q26075", 
"Q2609815", 
"Q263958", 
"Q2645019", 
"Q2660666", 
"Q266210", 
"Q26963", 
"Q273169", 
"Q27335", 
"Q274988", 
"Q278332", 
"Q2786152", 
"Q278809", 
"Q2788153", 
"Q279055", 
"Q2803610", 
"Q2806545", 
"Q2806548", 
"Q2816005", 
"Q282003", 
"Q284549", 
"Q285657", 
"Q285790", 
"Q285878", 
"Q28917", 
"Q290862", 
"Q2914590", 
"Q2926003", 
"Q2954819", 
"Q2988108", 
"Q300852", 
"Q300928", 
"Q306051", 
"Q308976", 
"Q309038", 
"Q310473", 
"Q310957", 
"Q311695", 
"Q312240", 
"Q312251", 
"Q312708", 
"Q3234708", 
"Q32693", 
"Q3295808", 
"Q33103", 
"Q3314420", 
"Q3333299", 
"Q334599", 
"Q336041", 
"Q338869", 
"Q342790", 
"Q342968", 
"Q343014", 
"Q343028", 
"Q367994", 
"Q372291", 
"Q372524", 
"Q377339", 
"Q382897", 
"Q399771", 
"Q401952", 
"Q4024614", 
"Q4027534", 
"Q402846", 
"Q407153", 
"Q407212", 
"Q407258", 
"Q407270", 
"Q407290", 
"Q407324", 
"Q407350", 
"Q407431", 
"Q407473", 
"Q407520", 
"Q407613", 
"Q407658", 
"Q407666", 
"Q407684", 
"Q407733", 
"Q407768", 
"Q407775", 
"Q407867", 
"Q407891", 
"Q407905", 
"Q407918", 
"Q407936", 
"Q408022", 
"Q408047", 
"Q408345", 
"Q408365", 
"Q40861", 
"Q408652", 
"Q408683", 
"Q4087", 
"Q408767", 
"Q408865", 
"Q408916", 
"Q408998", 
"Q409013", 
"Q409021", 
"Q409054", 
"Q409133", 
"Q409141", 
"Q409156", 
"Q409173", 
"Q409178", 
"Q409184", 
"Q409298", 
"Q409309", 
"Q409367", 
"Q409536", 
"Q409554", 
"Q409598", 
"Q409669", 
"Q409707", 
"Q409799", 
"Q409836", 
"Q410066", 
"Q410107", 
"Q410116", 
"Q410185", 
"Q410387", 
"Q410603", 
"Q410772", 
"Q410871", 
"Q410893", 
"Q410915", 
"Q410985", 
"Q411073", 
"Q411076", 
"Q411202", 
"Q411303", 
"Q411314", 
"Q411362", 
"Q411424", 
"Q411436", 
"Q411452", 
"Q411496", 
"Q411748", 
"Q411754", 
"Q4118", 
"Q412241", 
"Q412245", 
"Q412260", 
"Q412346", 
"Q412356", 
"Q412377", 
"Q412388", 
"Q412429", 
"Q412441", 
"Q412460", 
"Q412556", 
"Q412645", 
"Q412803", 
"Q413018", 
"Q413147", 
"Q413328", 
"Q413421", 
"Q413500", 
"Q413504", 
"Q413524", 
"Q413540", 
"Q413683", 
"Q413719", 
"Q413779", 
"Q413904", 
"Q4140494", 
"Q414189", 
"Q414195", 
"Q414196", 
"Q414303", 
"Q414394", 
"Q414458", 
"Q414537", 
"Q414553", 
"Q414555", 
"Q414724", 
"Q414915", 
"Q414986", 
"Q415090", 
"Q415103", 
"Q415128", 
"Q415183", 
"Q415256", 
"Q41534", 
"Q415415", 
"Q415465", 
"Q415519", 
"Q415612", 
"Q415723", 
"Q415750", 
"Q415988", 
"Q416036", 
"Q416160", 
"Q416206", 
"Q416365", 
"Q416393", 
"Q416399", 
"Q416475", 
"Q416572", 
"Q416728", 
"Q416972", 
"Q417134", 
"Q417157", 
"Q417316", 
"Q417347", 
"Q417399", 
"Q417435", 
"Q417646", 
"Q417934", 
"Q417958", 
"Q418031", 
"Q418104", 
"Q418157", 
"Q418163", 
"Q418164", 
"Q418197", 
"Q418265", 
"Q418386", 
"Q418437", 
"Q418492", 
"Q418504", 
"Q418573", 
"Q418607", 
"Q418989", 
"Q419096", 
"Q419164", 
"Q419170", 
"Q419330", 
"Q419453", 
"Q419668", 
"Q419799", 
"Q419842", 
"Q420172", 
"Q420380", 
"Q420390", 
"Q420473", 
"Q420630", 
"Q420652", 
"Q420657", 
"Q420680", 
"Q420698", 
"Q420835", 
"Q421035", 
"Q421041", 
"Q421055", 
"Q421143", 
"Q421197", 
"Q421204", 
"Q421486", 
"Q421557", 
"Q421693", 
"Q421729", 
"Q421748", 
"Q421751", 
"Q421758", 
"Q421787", 
"Q421828", 
"Q421862", 
"Q421902", 
"Q422037", 
"Q422075", 
"Q422152", 
"Q422416", 
"Q422642", 
"Q422709", 
"Q422777", 
"Q422909", 
"Q422994", 
"Q423000", 
"Q423005", 
"Q423021", 
"Q423083", 
"Q423136", 
"Q423145", 
"Q423245", 
"Q423282", 
"Q423314", 
"Q423354", 
"Q423398", 
"Q423462", 
"Q423633", 
"Q423797", 
"Q423892", 
"Q423922", 
"Q424314", 
"Q424390", 
"Q424662", 
"Q424811", 
"Q424848", 
"Q425214", 
"Q425350", 
"Q425378", 
"Q425389", 
"Q425450", 
"Q425468", 
"Q425668", 
"Q425777", 
"Q425827", 
"Q426535", 
"Q43010", 
"Q4314639", 
"Q4348652", 
"Q4392804", 
"Q4545799", 
"Q457515", 
"Q4596780", 
"Q4634173", 
"Q4637187", 
"Q47512", 
"Q4890780", 
"Q4890819", 
"Q49546", 
"Q5135111", 
"Q517266", 
"Q5276422", 
"Q5282", 
"Q5309", 
"Q5319", 
"Q550039", 
"Q568", 
"Q569", 
"Q572774", 
"Q584276", 
"Q58447", 
"Q5861", 
"Q59712", 
"Q60235", 
"Q611617", 
"Q613394", 
"Q61457", 
"Q618", 
"Q623", 
"Q629", 
"Q631266", 
"Q6456100", 
"Q655819", 
"Q658", 
"Q660", 
"Q663", 
"Q670", 
"Q674", 
"Q677", 
"Q688", 
"Q69488", 
"Q6985085", 
"Q703", 
"Q704203", 
"Q706", 
"Q707896", 
"Q708", 
"Q716", 
"Q7178974", 
"Q722", 
"Q7224880", 
"Q725", 
"Q727742", 
"Q731", 
"Q740", 
"Q743", 
"Q744", 
"Q753", 
"Q758", 
"Q764", 
"Q764245", 
"Q76904", 
"Q7739", 
"Q7842224", 
"Q80294", 
"Q82658", 
"Q83320", 
"Q844123", 
"Q861", 
"Q871", 
"Q876", 
"Q879", 
"Q880", 
"Q897", 
"Q903362", 
"Q904901", 
"Q905027", 
"Q905750", 
"Q908663", 
"Q910267", 
"Q925", 
"Q927885", 
"Q932", 
"Q933664", 
"Q938", 
"Q941", 
"Q942"]

result = []

for item in manifest:
    print("Processing: " + item)
    wikidata_url = "https://www.wikidata.org/wiki/Special:EntityData/{0}.json"
    pageviews_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"
    pageviews_url += "/en.wikipedia/all-access/user/{0}/daily/20151001/20160101"
    
    # Get article name from Wikidata item number
    r = requests.get(wikidata_url.format(item))
    blob = r.json()
    
    if "sitelinks" in blob["entities"][item]:
        if "enwiki" in blob["entities"][item]["sitelinks"]:
            article_title = blob["entities"][item]["sitelinks"]["enwiki"]["title"]
        else:
            continue
    else:
        continue
        
    article_title = article_title.replace(" ", "_")  # normalizing
    
    r = requests.get(pageviews_url.format(article_title))
    blob = r.json()
    
    views = 0
    for daily_views in blob["items"]:
        views += daily_views["views"]
    
    article_title = article_title.replace("_", " ")  # un-normalizing
    
    result.append((article_title, views))


for pair in result:
    print(pair[0] + "|" + str(pair[1]))  # will sort output in Excel; am lazy