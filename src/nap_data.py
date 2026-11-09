# (vnb, NAP-Datum, Netzebene, Zeitraum, Art, Menge, Einheit, Mio€)
# Zeitraum: T5=bis 2028, T10=2029-33, Z=bis 2045
R=[]
def a(v,d,rows):
    for r in rows: R.append((v,d)+tuple(r))
a("AVU Netz","2024-04-29",[
("HS","T5","Leitung",14,"km",11.8),("HS","T5","Anlage",2,"UW",13.4),
("HS","T10","Leitung",1,"km",0.9),("HS","T10","Anlage",3,"UW",20.5),
("HS","Z","Leitung",7,"km",10.0),("HS","Z","Anlage",5,"UW",37.0),
("MS+NS","T5","Leitung",103,"km",15.3),("MS+NS","T5","Anlage",129,"St",13.1),
("MS","T10","Leitung",17,"km",2.9),("NS","T10","Leitung",104,"km",14.7),
("MS","Z","Leitung",38,"km",7.3),("NS","Z","Leitung",250,"km",35.4),("MS/NS","Z","Anlage",345,"ONS",16.9)])
a("AllgäuNetz","2025-07-01",[
("HS","T5","Leitung",29,"km",10.79),("HS","T5","Anlage",5,"UW",22.96),
("HS","T10","Leitung",44,"km",19.29),("HS","T10","Anlage",4,"UW",21.38),
("HS","Z","Leitung",60,"km",27.66),("HS","Z","Anlage",15,"UW",56.76),
("MS","T5","Leitung",158,"km",22.79),("MS/NS","T5","Anlage",875,"ONS",32.21),
("MS","T10","Leitung",243,"km",34.13),("MS/NS","T10","Anlage",1630,"ONS",48.89),
("MS","Z","Leitung",288,"km",34.97),("MS/NS","Z","Anlage",1420,"ONS",63.43),
("NS","T5","Leitung",446,"km",49.71),("NS","T10","Leitung",590,"km",55.10),("NS","Z","Leitung",1179,"km",103.35)])
a("Avacon Netz","2024-06-24",[
("HS","T5","Leitung",4168,"km",4618),("HS","T5","Anlage",175,"UW",1952),
("HS","T10","Leitung",1588,"km",2542),("HS","T10","Anlage",64,"UW",1037),
("HS","Z","Leitung",899,"km",1618),("HS","Z","Anlage",35,"UW",279),
("MS","T5","Leitung",2518,"km",544),("MS/NS","T5","Anlage",3752,"ONS",137),
("MS","T10","Leitung",2433,"km",526),("MS/NS","T10","Anlage",2965,"ONS",157),
("MS","Z","Leitung",3194,"km",690),("MS/NS","Z","Anlage",3379,"ONS",259),
("NS","T5","Leitung",1472,"km",361),("NS","T10","Leitung",2733,"km",670),("NS","Z","Leitung",2102,"km",515)])
a("badenovaNETZE","2024-05-01",[
("HS","T5","Leitung",16.7,"km",31),("HS","T5","Anlage",10,"UW",106),
("HS","T10","Leitung",22.7,"km",33),("HS","T10","Anlage",7,"UW",89),("HS","Z","Leitung",26,"km",66),
("MS","T5","Leitung",142,"km",43.5),("MS/NS","T5","Anlage",317,"ONS",44.3),
("MS","T10","Leitung",140,"km",43),("MS/NS","T10","Anlage",529,"ONS",46.5),
("MS","Z","Leitung",355,"km",110),("MS/NS","Z","Anlage",450,"ONS",20),
("NS","T5","Leitung",130,"km",12),("NS","T10","Leitung",202,"km",20.5),("NS","Z","Leitung",340,"km",30)])
a("Bayernwerk Netz","2024-04-30",[
("HS","T5","Leitung",2419,"km",4275),("HS","T10","Leitung",1786,"km",3620),("HS","Z","Leitung",805,"km",1464),
("HS/MS","T5","Anlage",203,"UW",2358),("HS/MS","T10","Anlage",115,"UW",1819),("HS/MS","Z","Anlage",152,"UW",1306),
("MS","T5","Leitung",12247,"km",1748),("MS","T10","Leitung",15710,"km",2133),("MS","Z","Leitung",28973,"km",4267),
("NS","T5","Leitung",11894,"km",1348),("NS","T10","Leitung",15960,"km",1885),("NS","Z","Leitung",27519,"km",3303)])
a("Bonn-Netz","2025-06-30",[
("MS+NS","T5","Leitung",98.6,"km",36.6),("MS+NS","T5","Anlage",92,"St",6.4),
("MS+NS","T10","Leitung",48,"km",16.8),("MS+NS","T10","Anlage",125,"St",9.4),
("MS+NS","Z","Leitung",120,"km",41.9),("MS+NS","Z","Anlage",304,"St",35)])
a("Dortmunder Netz","2024-04-30",[
("HS/MS","T5","Anlage",5,"UW",43),("HS/MS","T10","Anlage",5,"UW",43),("HS/MS","Z","Anlage",13,"UW",95),
("MS","T5","Leitung",169,"km",45.5),("MS/NS","T5","Anlage",200,"ONS",23),
("MS","T10","Leitung",162,"km",42.5),("MS/NS","T10","Anlage",270,"ONS",31.8),
("MS","Z","Leitung",369,"km",97),("MS/NS","Z","Anlage",670,"ONS",73),
("NS","T5","Leitung",73,"km",17.4),("NS","T10","Leitung",93,"km",22.2),("NS","Z","Leitung",219,"km",50.5)])
a("Braunschweiger Netz","2024-09-13",[
("HS","T5","Leitung",11,"km",29.1),("HS/MS","T5","Anlage",4,"UW",9.4),
("HS","T10","Leitung",2,"km",6),("HS/MS","T10","Anlage",12,"UW",69.2),("HS/MS","Z","Anlage",3,"UW",12),
("MS","T5","Leitung",50,"km",20.3),("MS/NS","T5","Anlage",159,"ONS",17.9),
("MS","T10","Leitung",93,"km",36.7),("MS/NS","T10","Anlage",155,"ONS",11.6),
("MS","Z","Leitung",104,"km",41),("MS/NS","Z","Anlage",86,"ONS",7.1),
("NS","T5","Leitung",66,"km",22.6),("NS","T10","Leitung",68,"km",23.1),("NS","Z","Leitung",99,"km",81.4)])
a("E-Werk Netze","2024-09-20",[
("HS","T5","Leitung",6.9,"km",10.4),("HS/MS","T5","Anlage",6,"UW",52),("HS/MS","T10","Anlage",7,"UW",54),
("MS","T5","Leitung",551,"km",151),("MS/NS","T5","Anlage",646,"ONS",43),
("MS","T10","Leitung",526,"km",126),("MS/NS","T10","Anlage",617,"ONS",38)])
a("ELE Verteilnetz","2024-08-09",[
("MS","T5","Leitung",102,"km",24.84),("MS/NS","T5","Anlage",221,"ONS",16.73),
("MS","T10","Leitung",147,"km",39.68),("MS/NS","T10","Anlage",308,"ONS",27.34),
("MS","Z","Leitung",353,"km",116.83),("MS/NS","Z","Anlage",738,"ONS",80.50),
("NS","T5","Leitung",152.28,"km",35.71),("NS","T10","Leitung",203,"km",54.28),("NS","Z","Leitung",487,"km",159.81)])
a("ENERVIE Vernetzt","2024-04-24",[
("HS","Z","Leitung",202,"km",28.55),("HS/MS","Z","Anlage",8,"UW",40.93),
("MS","T10","Leitung",291,"km",76.83),("MS","Z","Leitung",778,"km",208.02),
("MS/NS","T10","Anlage",608,"ONS",43.20),("MS/NS","Z","Anlage",961,"ONS",70.42),
("NS","T10","Leitung",542,"km",112.37),("NS","Z","Leitung",1720,"km",359.60)])
a("E.DIS Netz (TNG Brandenburg)","2024-06-17",[
("HS","T5","Leitung",423,"km",414),("HS","T5","Anlage",100,"UW",563),("HS","T10","Leitung",961,"km",1068),("HS","T10","Anlage",158,"UW",1045),("HS","Z","Leitung",1940,"km",1808),("HS","Z","Anlage",327,"UW",1361),
("MS","T5","Leitung",2723,"km",281),("MS/NS","T5","Anlage",4305,"ONS",389),("MS","T10","Leitung",2155,"km",216),("MS/NS","T10","Anlage",2293,"ONS",201),("MS","Z","Leitung",2375,"km",240),("MS/NS","Z","Anlage",2490,"ONS",211),
("NS","T5","Leitung",357,"km",50),("NS","T10","Leitung",1168,"km",164),("NS","Z","Leitung",2815,"km",394)])
a("E.DIS Netz (TNG Mecklenburg-Vorpommern)","2024-06-17",[
("HS","T5","Leitung",214,"km",172),("HS","T5","Anlage",40,"UW",264),("HS","T10","Leitung",713,"km",546),("HS","T10","Anlage",120,"UW",714),("HS","Z","Leitung",939,"km",876),("HS","Z","Anlage",193,"UW",684),
("MS","T5","Leitung",2119,"km",215),("MS/NS","T5","Anlage",2833,"ONS",261),("MS","T10","Leitung",1292,"km",131),("MS/NS","T10","Anlage",1149,"ONS",108),("MS","Z","Leitung",1206,"km",122),("MS/NS","Z","Anlage",1194,"ONS",106),
("NS","T5","Leitung",179,"km",25),("NS","T10","Leitung",530,"km",75),("NS","Z","Leitung",1408,"km",197)])
a("EAM Netz (Summe 11 Teilnetze, MS-Leitungen)","2024-06-09",[
("HS","T5","Leitung",3.7,"km",7.4),("MS","T5","Leitung",931.9,"km",191.6)])
a("EWE NETZ","2024-08-23",[
("HS/MS","T5","Anlage",100,"UW",483),("HS/MS","T10","Anlage",57,"UW",174),("HS/MS","Z","Anlage",69,"UW",250),
("MS","T5","Leitung",2152,"km",330),("MS/NS","T5","Anlage",8866,"ONS",292),("NS","T5","Leitung",1010,"km",102),
("MS","T10","Leitung",1636,"km",287),("MS/NS","T10","Anlage",4513,"ONS",148),("NS","T10","Leitung",929,"km",94),
("MS","Z","Leitung",2982,"km",499)])
a("EWR Netz","2024-09-13",[
("HS","T5","Leitung",9,"km",8),("HS/MS","T5","Anlage",6,"UW",17),("HS/MS","T10","Anlage",7,"UW",20),("HS/MS","Z","Anlage",6,"UW",30),
("MS","T5","Leitung",76,"km",12),("MS/NS","T5","Anlage",200,"ONS",24),("MS","T10","Leitung",178,"km",36),("MS/NS","T10","Anlage",460,"ONS",34),
("MS","Z","Leitung",360,"km",90),("MS/NS","Z","Anlage",1380,"ONS",138),
("NS","T5","Leitung",70,"km",13),("NS","T10","Leitung",210,"km",37),("NS","Z","Leitung",744,"km",112)])
a("Stadtwerke Hamm","2024-04-30",[
("MS","T10","Leitung",61,"km",10.0),("MS/NS","T10","Anlage",41,"ONS",4.0),
("HS/MS","Z","Anlage",5,"UW",5.0),("MS","Z","Leitung",160,"km",24.0)])
a("Energienetze Offenbach (ENO)","2024-08-29",[
("HS","T5","Leitung",73,"km",99),("HS/MS","T5","Anlage",11,"UW",183),("HS","T10","Leitung",38,"km",79),("HS/MS","T10","Anlage",2,"UW",33),
("MS","T5","Leitung",104,"km",55),("MS/NS","T5","Anlage",104,"ONS",9),("MS","T10","Leitung",241,"km",127),("MS/NS","T10","Anlage",216,"ONS",20),
("MS","Z","Leitung",183,"km",96),("MS/NS","Z","Anlage",204,"ONS",19),
("NS","T5","Leitung",156,"km",52),("NS","T10","Leitung",320,"km",104),("NS","Z","Leitung",260,"km",85)])
a("FairNetz","2024-08-28",[
("HS","T5","Leitung",2,"km",6.1),("HS/MS","T5","Anlage",8,"UW",216),("HS/MS","T10","Anlage",1,"UW",15),("HS","Z","Leitung",5,"km",13.2),("HS/MS","Z","Anlage",4,"UW",111)])
a("Energienetze Mittelrhein","2025-04-30",[
("MS","T10","Leitung",214,"km",67.16),("NS","T10","Leitung",122,"km",36.78),("MS/NS","T10","Anlage",379,"ONS",25.16),
("MS","Z","Leitung",451,"km",110.04),("NS","Z","Leitung",1536,"km",505.69),("MS/NS","Z","Anlage",475,"ONS",23.88),("HS/MS","Z","Anlage",15,"UW",105)])
a("Stromnetz Hamburg (inkl. Erneuerung lt. 10-Jahresplanung)","2024-07-04",[
("HS","T5","Leitung",192,"km",750),("HS/MS","T5","Anlage",23,"UW",241),("HS","T10","Leitung",184,"km",722),("HS/MS","T10","Anlage",13,"UW",192),
("HS","Z","Leitung",270,"km",1078),("HS/MS","Z","Anlage",50,"UW",730),
("MS","T5","Leitung",1091,"km",573),("MS/NS","T5","Anlage",1065,"ONS",172),("MS","T10","Leitung",1006,"km",528),("MS/NS","T10","Anlage",935,"ONS",152),
("MS","Z","Leitung",2639,"km",1386),("MS/NS","Z","Anlage",7443,"ONS",1058),
("NS","T5","Leitung",973,"km",365),("NS","T10","Leitung",946,"km",355),("NS","Z","Leitung",2270,"km",851)])
a("Harz Energie Netz","2024-09-06",[
("HS","T5","Leitung",130.7,"km",12.7),
("MS","T5","Leitung",100,"km",23.9),("MS/NS","T5","Anlage",585,"ONS",35.7),("MS","T10","Leitung",96,"km",21.5),("MS/NS","T10","Anlage",457,"ONS",16.7),
("MS","Z","Leitung",248,"km",50.9),("MS/NS","Z","Anlage",402,"ONS",19.4),
("NS","T5","Leitung",315,"km",79.9),("NS","T10","Leitung",288,"km",73.22),("NS","Z","Leitung",682,"km",173.32)])
a("LSW Netz","2024-08-22",[
("HS","T5","Leitung",52,"km",29.5),("HS/MS","T5","Anlage",5,"UW",40.4),("HS","T10","Leitung",46,"km",114.5),("HS/MS","T10","Anlage",7,"UW",30.5),
("HS","Z","Leitung",91,"km",201.3),("HS/MS","Z","Anlage",7,"UW",94.3),
("MS","T5","Leitung",182,"km",29.1),("MS/NS","T5","Anlage",254,"ONS",20.8),("MS","T10","Leitung",346,"km",55.2),("MS/NS","T10","Anlage",303,"ONS",24.5),
("MS","Z","Leitung",214,"km",34.2),("MS/NS","Z","Anlage",295,"ONS",22.3),
("NS","T5","Leitung",129,"km",26.1),("NS","T10","Leitung",226,"km",45.9),("NS","Z","Leitung",323,"km",66.2)])
a("Mainfranken Netze","2024-04-30",[
("MS","T5","Leitung",92,"km",15.80),("MS/NS","T5","Anlage",25,"St",10.25),("MS","T10","Leitung",54,"km",9.63),("MS/NS","T10","Anlage",59,"St",12.46),
("NS","T5","Leitung",85,"km",14.54),("NS","T10","Leitung",110,"km",18.82),("NS","Z","Leitung",284,"km",68.90)])
a("MITNETZ Strom","2024-04-30",[
("MS","T5","Leitung",3632,"km",544),("MS/NS","T5","Anlage",5575,"ONS",612),("MS","T10","Leitung",4328,"km",650),("MS/NS","T10","Anlage",4414,"ONS",470),
("MS","Z","Leitung",10700,"km",1600),("MS/NS","Z","Anlage",11000,"ONS",1180)])
a("LEW Verteilnetz","2024-08-01",[
("HS","T5","Leitung",297,"km",467),("HS/MS","T5","Anlage",50,"UW",265),("HS","T10","Leitung",302,"km",628),("HS/MS","T10","Anlage",62,"UW",388),
("HS","Z","Leitung",326,"km",563),("HS/MS","Z","Anlage",72,"UW",456),
("MS","T5","Leitung",2162,"km",486),("MS/NS","T5","Anlage",4918,"ONS",427),("MS","T10","Leitung",842,"km",191),("MS/NS","T10","Anlage",3402,"ONS",348),
("MS","Z","Leitung",1230,"km",288),("MS/NS","Z","Anlage",3468,"ONS",444),
("NS","T5","Leitung",709,"km",117),("NS","T10","Leitung",1279,"km",211),("NS","Z","Leitung",2321,"km",383)])
a("MVV Netze","2024-09-09",[
("HS","T5","Leitung",45,"km",57),("HS/MS","T5","Anlage",7,"UW",57),("HS","T10","Leitung",13,"km",43),("HS/MS","T10","Anlage",9,"UW",129),
("MS","T5","Leitung",88,"km",40),("MS/NS","T5","Anlage",95,"ONS",9),("MS","T10","Leitung",208,"km",93),("MS/NS","T10","Anlage",224,"ONS",20),
("MS","Z","Leitung",123,"km",55),("MS/NS","Z","Anlage",132,"ONS",12),
("NS","T5","Leitung",197,"km",59),("NS","T10","Leitung",464,"km",139),("NS","Z","Leitung",275,"km",83)])
a("N-ERGIE Netz","2024-09-13",[
("HS","T5","Leitung",168,"km",161),("HS","T10","Leitung",419,"km",625),
("MS","T5","Leitung",343,"km",87)])
a("NGN Netzgesellschaft Niederrhein","2024-04-29",[
("HS","T5","Leitung",71,"km",62),("HS","T5","Anlage",12,"UW",35),("HS","T10","Leitung",10,"km",8),("HS","Z","Leitung",48,"km",36),("HS","Z","Anlage",2,"UW",11),
("MS","T5","Leitung",17,"km",6),("MS","T10","Leitung",89,"km",30),("MS/NS","T10","Anlage",153,"ONS",13),("MS","Z","Leitung",183,"km",64),("MS/NS","Z","Anlage",473,"ONS",39)])
a("NRM Netzdienste Rhein-Main","2024-09-04",[
("MS","T5","Leitung",160,"km",94),("MS/NS","T5","Anlage",161,"ONS",28),("MS/NS","T10","Anlage",300,"ONS",29),
("MS","Z","Leitung",610,"km",244),("MS/NS","Z","Anlage",590,"ONS",56),
("NS","T5","Leitung",146,"km",78),("NS","T10","Leitung",146,"km",78),("NS","Z","Leitung",462,"km",182)])
a("Netze BW","2024-09-09",[
("HS","T5","Leitung",700,"km",1100),("HS/MS","T5","Anlage",219,"UW",3600),("HS","T10","Leitung",2300,"km",3500),("HS/MS","T10","Anlage",61,"UW",1000),("HS/MS","Z","Anlage",40,"UW",700),
("MS","T5","Leitung",22500,"km",5300),("MS/NS","T5","Anlage",8800,"ONS",800),("NS","T5","Leitung",18000,"km",2600),
("MS","T10","Leitung",9400,"km",2200),("MS/NS","T10","Anlage",11000,"ONS",900),("NS","T10","Leitung",8400,"km",1200),
("MS","Z","Leitung",7700,"km",1800),("MS/NS","Z","Anlage",13000,"ONS",1000),("NS","Z","Leitung",10900,"km",1600)])
a("Netze Duisburg","2024-04-25",[
("HS","T5","Leitung",17,"km",37),("HS/MS","T5","Anlage",6,"UW",94),("HS","T10","Leitung",24,"km",76),("HS/MS","T10","Anlage",7,"UW",72),("HS","Z","Leitung",34,"km",102),("HS/MS","Z","Anlage",8,"UW",36),
("MS","T5","Leitung",116,"km",38),("MS/NS","T5","Anlage",255,"ONS",21),("MS","T10","Leitung",135,"km",47),("MS/NS","T10","Anlage",285,"ONS",24),("MS","Z","Leitung",324,"km",113),("MS/NS","Z","Anlage",684,"ONS",57)])
a("Netze ODR","2024-08-28",[
("MS","T5","Leitung",884,"km",167),("MS/NS","T5","Anlage",607,"ONS",36.4),("NS","T5","Leitung",944,"km",188.8),
("MS","T10","Leitung",928,"km",182),("MS/NS","T10","Anlage",607,"ONS",36.4),("NS","T10","Leitung",1326,"km",199.5),
("MS","Z","Leitung",1801,"km",360),("MS/NS","Z","Anlage",1456,"ONS",87.4),("NS","Z","Leitung",3176,"km",477.6)])
a("Oberhausener Netzgesellschaft","2024-04-30",[
("MS","T5","Leitung",43,"km",11),("MS/NS","T5","Anlage",26,"ONS",1),("MS","T10","Leitung",45,"km",11),("MS/NS","T10","Anlage",26,"ONS",1),("MS","Z","Leitung",107,"km",27),("MS/NS","Z","Anlage",63,"ONS",2)])
a("OsthessenNetz","2024-08-16",[
("MS","T5","Leitung",50,"km",8),("MS","T10","Leitung",100,"km",16),("MS","Z","Leitung",240,"km",36),
("NS","T5","Leitung",60,"km",4.5),("NS","T10","Leitung",75,"km",4.75),("NS","Z","Leitung",155,"km",11.5),
("MS/NS","T5","Anlage",150,"ONS",3),("MS/NS","T10","Anlage",250,"ONS",5)])
a("Netze Magdeburg","2024-04-29",[("MS","T10","Leitung",47,"km",19.8),("NS","T10","Leitung",74,"km",32.7)])
a("Netzgesellschaft Potsdam","2024-04-30",[
("HS","T5","Leitung",6.84,"km",10.5),("HS","T10","Leitung",23.9,"km",48.4),("HS","Z","Leitung",28.2,"km",66.0),
("MS","T5","Leitung",223,"km",58.0),("MS/NS","T5","Anlage",133,"ONS",17.3),("MS","T10","Leitung",98,"km",25.6),("MS/NS","T10","Anlage",100,"ONS",13.0),
("MS","Z","Leitung",147,"km",38.3),("MS/NS","Z","Anlage",179,"ONS",23.3)])
a("Pfalzwerke Netz","2024-08-07",[
("MS","T10","Leitung",402,"km",129.8),("NS","T10","Leitung",305,"km",52.9),("HS","Z","Leitung",362,"km",262.87),("HS/MS","Z","Anlage",40,"UW",149.63)])
a("Regensburg Netz","2024-04-30",[("MS","T5","Leitung",12,"km",4.8),("MS/NS","T5","Anlage",70,"ONS",6.3)])
a("Regionetz","2024-06-21",[
("MS","T5","Leitung",177,"km",55),("MS/NS","T5","Anlage",342,"ONS",27),("MS","T10","Leitung",109,"km",33),("MS/NS","T10","Anlage",945,"ONS",76),
("MS","Z","Leitung",322,"km",97),("MS/NS","Z","Anlage",897,"ONS",72),
("NS","T5","Leitung",191,"km",56),("NS","T10","Leitung",224,"km",65),("NS","Z","Leitung",487,"km",141)])
a("RheinNetz","2024-08-26",[
("MS","T5","Leitung",286,"km",96),("MS/NS","T5","Anlage",1413,"ONS",93),("MS","T10","Leitung",355,"km",114.9),("MS/NS","T10","Anlage",1098,"ONS",70.45),
("MS","Z","Leitung",851,"km",282),("MS/NS","Z","Anlage",2640,"ONS",168.05)])
a("SVO Netz / Celle-Uelzen Netz","2024-09-12",[
("MS","T5","Leitung",162.91,"km",37.56),("MS/NS","T5","Anlage",366,"ONS",20.15),("MS","T10","Leitung",427,"km",88.2),("MS/NS","T10","Anlage",387,"ONS",28.64),
("NS","T5","Leitung",14.6,"km",2.29),("NS","T10","Leitung",153,"km",19.89),("NS","Z","Leitung",147,"km",23.5)])
a("SWE Netz (Erfurt)","2024-09-03",[
("HS/MS","T10","Anlage",2,"UW",6),("HS/MS","Z","Anlage",6,"UW",18),
("MS","T5","Leitung",9.9,"km",5.1),("MS/NS","T5","Anlage",107,"ONS",8.0),("MS","T10","Leitung",11.3,"km",5.8),("MS/NS","T10","Anlage",140,"ONS",13.9),
("NS","T5","Leitung",10,"km",2.3),("NS","T10","Leitung",16,"km",3.8),("NS","Z","Leitung",43,"km",9.2)])
a("SWKiel Netz","2024-07-30",[
("HS","T5","Leitung",38,"km",38),("HS/MS","T5","Anlage",2,"UW",15),("HS/MS","T10","Anlage",1,"UW",3),("HS","Z","Leitung",13,"km",19),("HS/MS","Z","Anlage",7,"UW",17),
("MS","T5","Leitung",31,"km",12),("MS/NS","T5","Anlage",40,"ONS",6),("MS","T10","Leitung",21,"km",8),("MS/NS","T10","Anlage",52,"ONS",8),("MS","Z","Leitung",140,"km",67),("MS/NS","Z","Anlage",144,"ONS",20),
("NS","T5","Leitung",67,"km",26),("NS","T10","Leitung",125,"km",49),("NS","Z","Leitung",561,"km",208)])
a("SWM Infrastruktur","2024-06-28",[
("MS","T5","Leitung",350,"km",105),("MS/NS","T5","Anlage",750,"ONS",150),("NS","T5","Leitung",250,"km",62.5),
("MS","T10","Leitung",475,"km",142.5),("MS/NS","T10","Anlage",750,"ONS",187.5),("NS","T10","Leitung",475,"km",118.75)])
a("SWO Netz (Osnabrück)","2024-08-29",[
("MS","T5","Leitung",202,"km",27),("MS/NS","T5","Anlage",100,"ONS",10),("MS","T10","Leitung",202,"km",27),("MS/NS","T10","Anlage",100,"ONS",10),
("MS","Z","Leitung",484,"km",65.5),("MS/NS","Z","Anlage",240,"ONS",24.5),
("NS","T5","Leitung",120,"km",16.3),("NS","T10","Leitung",120,"km",16.3),("NS","Z","Leitung",288,"km",39.2)])
a("SWS Netze Solingen (nur assetbedingt)","2024-09-17",[
("MS","T5","Leitung",20.3,"km",4.427),("MS/NS","T5","Anlage",13,"ONS",0.675),("MS","T10","Leitung",18,"km",3.96),("MS","Z","Leitung",60,"km",13.2)])
a("SachsenNetze (Dresden)","2024-08-23",[
("HS/MS","T5","Anlage",5,"UW",40),("HS/MS","T10","Anlage",7,"UW",50),("HS/MS","Z","Anlage",2,"UW",20),
("MS","T5","Leitung",115,"km",31),("MS/NS","T5","Anlage",220,"ONS",19),("MS","T10","Leitung",125,"km",33),("MS/NS","T10","Anlage",375,"ONS",33),
("MS","Z","Leitung",230,"km",61),("MS/NS","Z","Anlage",550,"ONS",48),
("NS","T5","Leitung",270,"km",65),("NS","T10","Leitung",290,"km",69),("NS","Z","Leitung",520,"km",128)])
a("SachsenNetze HS.HD","2024-08-23",[
("HS","T5","Leitung",170,"km",240),("HS","T5","Anlage",20,"UW",120),("HS","T10","Leitung",125,"km",250),("HS","T10","Anlage",29,"UW",180),("HS","Z","Leitung",280,"km",350),("HS","Z","Anlage",25,"UW",190),
("MS","T5","Leitung",730,"km",110),("MS/NS","T5","Anlage",1810,"ONS",127),("MS","T10","Leitung",615,"km",90),("MS/NS","T10","Anlage",1190,"ONS",83),
("MS","Z","Leitung",1030,"km",155),("MS/NS","Z","Anlage",1275,"ONS",90),
("NS","T5","Leitung",1110,"km",113),("NS","T10","Leitung",1025,"km",105),("NS","Z","Leitung",1675,"km",199)])
a("Schleswig-Holstein Netz","2024-06-21",[
("HS","T5","Leitung",282,"km",552),("HS","T5","Anlage",61,"UW",379),("HS","T10","Leitung",553,"km",1064),("HS","T10","Anlage",54,"UW",314),("HS","Z","Leitung",229,"km",458),("HS","Z","Anlage",91,"UW",680),
("MS","T5","Leitung",4808,"km",546),("MS/NS","T5","Anlage",4428,"ONS",206),("MS","T10","Leitung",1362,"km",163),("MS/NS","T10","Anlage",1743,"ONS",95),
("MS","Z","Leitung",1363,"km",163),("MS/NS","Z","Anlage",1305,"ONS",61),
("NS","T5","Leitung",655,"km",87),("NS","T10","Leitung",204,"km",28),("NS","Z","Leitung",204,"km",28)])
a("Stadtwerke Jena Netze","2025-07-09",[
("MS","T5","Leitung",32,"km",8.75),("MS/NS","T5","Anlage",80,"ONS",18.125),("NS","T5","Leitung",52,"km",14.45),
("MS","T10","Leitung",103,"km",19.23),("MS/NS","T10","Anlage",135,"ONS",30.5),("NS","T10","Leitung",216,"km",58.325),
("MS","Z","Leitung",222,"km",62.325),("MS/NS","Z","Anlage",216,"ONS",48.72),("NS","Z","Leitung",515,"km",139.35)])
a("Stadtwerke Karlsruhe Netzservice","2024-04-30",[
("HS","T5","Leitung",18.9,"km",24),("HS/MS","T5","Anlage",2,"UW",14),("HS","T10","Leitung",24.3,"km",30),("HS/MS","T10","Anlage",2,"UW",13),("HS","Z","Leitung",9,"km",11),("HS/MS","Z","Anlage",5,"UW",46),
("MS","T5","Leitung",34,"km",14),("MS/NS","T5","Anlage",125,"ONS",13),("MS","T10","Leitung",123,"km",43),("MS/NS","T10","Anlage",179,"ONS",19),("MS","Z","Leitung",255,"km",89),("MS/NS","Z","Anlage",369,"ONS",40),
("NS","T5","Leitung",249,"km",62),("NS","T10","Leitung",300,"km",60),("NS","Z","Leitung",721,"km",148)])
a("Stadtwerke Rostock Netzgesellschaft","2024-04-30",[
("MS","T5","Leitung",108,"km",25.3),("MS/NS","T5","Anlage",187,"ONS",18.7),("NS","T5","Leitung",178,"km",26.7),
("MS","T10","Leitung",80,"km",17.9),("MS/NS","T10","Anlage",120,"ONS",12.0),("NS","T10","Leitung",131,"km",19.7),
("MS","Z","Leitung",123,"km",27.7),("MS/NS","Z","Anlage",236,"ONS",23.6),("NS","Z","Leitung",198,"km",29.8)])
a("Stadtwerke Saarbrücken Netz","2025-04-28",[
("HS","T5","Leitung",3.6,"km",11),("HS","T5","Anlage",1,"UW",14.4),("HS","T10","Leitung",3.7,"km",11),("HS","T10","Anlage",1,"UW",15),
("MS","T5","Leitung",20.4,"km",7.2),("MS/NS","T5","Anlage",53,"ONS",5.1),("MS","T10","Leitung",52,"km",21),("MS/NS","T10","Anlage",101,"ONS",7.4),("MS","Z","Leitung",140,"km",89),("MS/NS","Z","Anlage",158,"ONS",16),
("NS","T5","Leitung",41,"km",10.6),("NS","T10","Leitung",176,"km",32),("NS","Z","Leitung",420,"km",123)])
a("Stuttgart Netze","2024-04-30",[
("HS","T5","Leitung",30,"km",45),("HS","T5","Anlage",10,"UW",183),("HS","T10","Leitung",68,"km",113),("HS","T10","Anlage",3,"UW",37),("HS","Z","Leitung",70,"km",97),("HS","Z","Anlage",9,"UW",145),
("MS","T5","Leitung",147,"km",73.5),("MS/NS","T5","Anlage",137,"ONS",8.3),("MS","T10","Leitung",268,"km",134),("MS/NS","T10","Anlage",161,"ONS",8.5),("MS","Z","Leitung",423,"km",211.5),("MS/NS","Z","Anlage",185,"ONS",10),
("NS","T5","Leitung",198,"km",99),("NS","T10","Leitung",358,"km",179),("NS","Z","Leitung",840,"km",420)])
a("SWU Netze (Ulm/Neu-Ulm)","2024-09-19",[
("HS","T5","Leitung",50,"km",39.8),("HS/MS","T5","Anlage",3,"UW",65),("HS/MS","T10","Anlage",2,"UW",35),
("MS","Z","Leitung",341,"km",143.22),("MS/NS","Z","Anlage",324,"ONS",42.12),("NS","Z","Leitung",712,"km",270.56)])
a("Städtische Werke Netz+Service (Kassel)","2025-07-02",[
("HS/MS","T5","Anlage",2,"UW",14.2),("HS/MS","T10","Anlage",2,"UW",18.1),
("MS","T10","Leitung",83,"km",38.0),("MS","Z","Leitung",198,"km",89.0),("MS/NS","T5","Anlage",96,"ONS",5.0),("MS/NS","T10","Anlage",61,"ONS",3.0),("MS/NS","Z","Anlage",44,"ONS",2.2),
("NS","T5","Leitung",15,"km",3.5),("NS","T10","Leitung",75,"km",22.5)])
a("Syna","2024-08-19",[
("MS","T10","Leitung",6014,"km",421),("MS/NS","T10","Anlage",2604,"ONS",248),("NS","T10","Leitung",3944,"km",670),
("MS","Z","Leitung",7729,"km",541),("MS/NS","Z","Anlage",3256,"ONS",309)])
a("TEN Thüringer Energienetze","2024-06-26",[
("HS","T5","Leitung",881,"km",290),("HS","T10","Leitung",533,"km",354),("HS","Z","Leitung",345,"km",206),
("MS","T5","Leitung",670,"km",133),("NS","T5","Leitung",587,"km",92),("MS/NS","T5","Anlage",576,"ONS",58),
("MS","T10","Leitung",711,"km",155),("NS","T10","Leitung",639,"km",110),("MS/NS","T10","Anlage",719,"ONS",80),
("MS","Z","Leitung",1390,"km",357),("NS","Z","Leitung",1298,"km",264),("MS/NS","Z","Anlage",1461,"ONS",192)])
a("TraveNetz","2024-09-16",[
("HS","T5","Leitung",5,"km",9.0),("HS/MS","T5","Anlage",14,"UW",59.0),("HS","T10","Leitung",6,"km",10.5),("HS/MS","T10","Anlage",12,"UW",43.8),
("MS","T5","Leitung",110,"km",31.6),("NS","T5","Leitung",126,"km",32.3),("MS/NS","T5","Anlage",450,"ONS",26.6),
("MS","T10","Leitung",118,"km",37.5),("NS","T10","Leitung",120,"km",31.8),("MS/NS","T10","Anlage",390,"ONS",23.0)])
a("VSE Verteilnetz","2024-04-30",[
("HS","T5","Leitung",44,"km",35.8),("HS","T5","Anlage",19,"UW",68.6),("HS","T10","Leitung",77,"km",222),("HS","T10","Anlage",9,"UW",32.9),("HS","Z","Leitung",16,"km",80)])
a("WSW Netz (Wuppertal)","2024-09-23",[
("HS","T5","Leitung",6.7,"km",4.4),("HS/MS","T5","Anlage",1,"UW",3.1),("MS","T5","Leitung",161.7,"km",56.6),("NS","T5","Leitung",117.3,"km",29.3),
("HS","T10","Leitung",48.4,"km",32.0),("HS/MS","T10","Anlage",1,"UW",3.1),("MS","T10","Leitung",269.5,"km",94.3),("NS","T10","Leitung",195.5,"km",48.9)])
a("Westnetz","2024-08-23",[
("HS","T5","Leitung",1813,"km",1684),("HS","T5","Anlage",254,"UW",1801),("HS","T10","Leitung",1688,"km",1963),("HS","T10","Anlage",124,"UW",814),("HS","Z","Leitung",5623,"km",4851),("HS","Z","Anlage",454,"UW",2157),
("MS","T5","Leitung",8914,"km",1070),("MS/NS","T5","Anlage",7500,"ONS",750),("MS","T10","Leitung",5710,"km",686),("MS/NS","T10","Anlage",19680,"ONS",1968),
("MS","Z","Leitung",10083,"km",1211),("MS/NS","Z","Anlage",19377,"ONS",1937),("NS","T10","Leitung",7643,"km",622.4)])
a("WEMAG Netz","2025-07-04",[
("HS","T5","Leitung",237,"km",277),("HS","T5","Anlage",31,"UW",159),("HS","T10","Leitung",239,"km",292),("HS","T10","Anlage",2,"UW",191),("HS","Z","Leitung",143,"km",143),("HS","Z","Anlage",2,"UW",121),
("MS","T5","Leitung",37,"km",10),("NS","T5","Leitung",184,"km",26.7),("MS","T10","Leitung",126,"km",28.4),("NS","T10","Leitung",141,"km",34.9)])
a("e-netz Südhessen","2024-09-27",[
("HS/MS","T5","Anlage",6,"UW",39.5),("HS/MS","T10","Anlage",10,"UW",77.0),("HS/MS","Z","Anlage",5,"UW",44),
("MS","T5","Leitung",128,"km",19.6),("MS","T10","Leitung",220,"km",30.1),("MS","Z","Leitung",216,"km",29.7),
("MS/NS","T5","Anlage",223,"ONS",16.6),("MS/NS","T10","Anlage",1913,"ONS",149.6),("MS/NS","Z","Anlage",327,"ONS",30.4),
("NS","T5","Leitung",679,"km",40.5),("NS","T10","Leitung",679,"km",40.5),("NS","Z","Leitung",476,"km",27.2)])
a("enercity Netz","2024-08-30",[
("MS","T5","Leitung",164,"km",72),("MS/NS","T5","Anlage",300,"ONS",42.8),("NS","T5","Leitung",256,"km",80),
("MS","T10","Leitung",291,"km",128),("MS/NS","T10","Anlage",400,"ONS",49.5),("NS","T10","Leitung",375,"km",115),
("MS","Z","Leitung",1509,"km",664),("MS/NS","Z","Anlage",700,"ONS",121.4),("NS","Z","Leitung",1470,"km",452)])
a("energis-Netzgesellschaft","2024-08-29",[
("MS","T5","Leitung",665,"km",166),("MS/NS","T5","Anlage",522,"ONS",22),("MS","T10","Leitung",286,"km",72),("MS/NS","T10","Anlage",1009,"ONS",66),
("MS","Z","Leitung",1138,"km",284),("MS/NS","Z","Anlage",325,"ONS",21)])
a("inetz (Chemnitz)","2025-07-08",[
("HS","T10","Leitung",27,"km",31),("HS/MS","T5","Anlage",3,"UW",10),("HS/MS","T10","Anlage",2,"UW",17),("HS/MS","Z","Anlage",14,"UW",49),
("MS","T5","Leitung",177,"km",18.9),("MS/NS","T5","Anlage",227,"ONS",22.1),("MS","T10","Leitung",98,"km",18.85),("MS/NS","T10","Anlage",196,"ONS",21.3),
("MS","Z","Leitung",173,"km",36.4),("MS/NS","Z","Anlage",322,"ONS",36.3)])
a("naturenergie netze","2024-04-30",[
("HS","T5","Leitung",1.1,"km",1.65),("HS/MS","T5","Anlage",6,"UW",59),("HS","T10","Leitung",26.8,"km",40.2),("HS/MS","T10","Anlage",5,"UW",8),("HS","Z","Leitung",35.6,"km",53.4),("HS/MS","Z","Anlage",3,"UW",35),
("MS","T5","Leitung",175,"km",61.25),("MS/NS","T5","Anlage",100,"ONS",5.32),("MS","T10","Leitung",140,"km",49),("MS/NS","T10","Anlage",80,"ONS",4.256),
("MS","Z","Leitung",385,"km",134.75),("MS/NS","Z","Anlage",220,"ONS",11.7)])
a("ovag Netz","2024-08-09",[
("MS","T5","Leitung",505,"km",170),("MS/NS","T5","Anlage",499,"ONS",25),("MS","T10","Leitung",277,"km",80),("MS/NS","T10","Anlage",794,"ONS",38),
("MS","Z","Leitung",710,"km",200),("MS/NS","Z","Anlage",1462,"ONS",90),("NS","T5","Leitung",136,"km",18.6),("NS","T10","Leitung",247,"km",33.9)])
a("swa Netze","2025-07-16",[
("HS/MS","T5","Anlage",1,"UW",1),("HS","T10","Leitung",6,"km",8),("HS/MS","T10","Anlage",1,"UW",10),("HS","Z","Leitung",29,"km",43),("HS/MS","Z","Anlage",9,"UW",60),
("MS","T5","Leitung",40,"km",18),("MS/NS","T5","Anlage",70,"ONS",24),("NS","T5","Leitung",45,"km",28),
("MS","T10","Leitung",40,"km",18),("MS/NS","T10","Anlage",150,"ONS",19),("NS","T10","Leitung",44,"km",26),
("MS","Z","Leitung",96,"km",43),("MS/NS","Z","Anlage",360,"ONS",46),("NS","Z","Leitung",106,"km",62)])
a("wesernetz Bremen","2024-05-02",[
("HS","T5","Leitung",38,"km",50),("HS","T5","Anlage",11,"UW",141),("HS","T10","Leitung",35,"km",27),("HS","T10","Anlage",8,"UW",104),
("MS","T5","Leitung",252,"km",80),("MS/NS","T5","Anlage",140,"ONS",8),("MS","T10","Leitung",290,"km",87),("MS/NS","T10","Anlage",750,"ONS",45),
("MS","Z","Leitung",540,"km",162),("MS/NS","Z","Anlage",1100,"ONS",66)])
