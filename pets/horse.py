# -*- coding: utf-8 -*-

from pets import Pet

class Horse (Pet):
    breeds = [ "Abaco Barb", "Abstang", "Abtenauer", "Abyssinian", "Adaev",
    "Aegidienberger", "Ainos Pony", "Akhal-Teke", "Albanian Horse", "Altai",
    "Alter Real", "Altmarkisches Kaltblut", "Altwurttemberg", "American Albino",
    "American Bashkir", "American Cream Draft", "American Drum Horse",
    "American Indian Horse", "American Mammoth Jack", "American Miniature Horse",
    "American Mustang", "American Paint Horse", "American Quarter Horse",
    "American Saddlebred", "American Shetland", "American Sport Pony",
    "American Spotted Paso", "American Standardbred", "American Thoroughbred",
    "American Walking Pony", "American Warmblood", "Amur", "Anadolu Pony",
    "Andalusian", "Andean", "Andino Pony", "Andravida", "Anglo-Arabian",
    "Anglo-Arabo-Sardo", "Anglo-Kabarda", "Anglo-Karachai", "Anglo-Luso",
    "Anglo-Norman", "Appaloosa", "Appaloosa Sport Horse", "Appendix Quarter Horse", "AraAppaloosa", "Arabian",
    "Arabian-Berber", "Arabian-Haflinger", "Arabo-Friesian", "Araboulonnais", "Aralusian", "Ardahan", "Ardennes",
    "Arenberg-Nordkirchener", "Argentine Anglo", "Argentine Criollo", "Argentine Polo Pony", "Argentinean Modepony", "Argentinian Ranch Horse", "Ariegeois Pony", "Arravani", "Asiatic Wild Horse", "Asil", "Assateague Pony", "Astrakhan", "Asturcón", "Asturian", "Australian Brumby", "Australian Draught", "Australian Pony",
    "Australian Stock horse", "Australian Warmblood", "Austrian Warmblood", "Autre Que Pur Sang", "Auxois", "Avelignese", "Azerbaijan",
    "Azores", "Azteca", "Baguales", "Baguio Light Horse", "Baguio Pony", "Bahr-El-Ghazal", "Baikal", "Baise", "Baixadeiro Horse", "Bajau Pony", "Bakhtiari", "Baladi", "Balearic Horse", "Bali Pony", "Balikun Horse", "Baluchi Horse", "Ban-ei", "Banamba", "Banat", "Bandiagara", "Banker Pony", "Barb", "Bardigiano", "Barra", "Bara Pony", "Barthais Pony", "Bashkir Horse", "Basotho Pony", "Basuto Pony", "Basque Pony", "Batak Pony", 
    "Bavarian Warmblood", "Beledougou", "Belgian Ardennais", "Belgian Draft", "Belgian Sport Horse", "Belgian Halfblood", "Belgian Warmblood", "Bergmann Pony", "Bhorum Pony", "Bhotia Pony", "Bhutia Pony", "Bidet Horse", "Bigourdan Horse", "Bitcuk", "Black Forest Horse", "Black Sea Horse", "Blazer Horse", "Boerperd", "Bolivian Pony", "Borneo Pony", "Bose Pony", "Bosnian Pony", "Boulonnais", "Brabant", "Barbancon", "Brandenburger", "Brazilian Pony", "Brazilian Sport Horse", 
    "Breton", "British Appaloosa", "British Riding Pony", "British Shetland", "British Spotted Pony", "British Thoroughbred", "British Warmblood", "Brumby", "Buckskin", "Bucovina", "Budyonny", "Bulgarian Native Horse", "Buohai", "Burmese Pony",
    "Buryat", "Busak Posavec", "Byelorussian Harness Horse", "Calabrese", "Calvinia Horse", "Camargue Horse", "Camarillo White Horse", "Campeiro", "Campolina", "Canadian Cutting Horse", "Canadian Horse", 
    "Canadian Pacer", "Canadian Rustic Pony", "Canadian Sport Horse", "Canadian Hunter", "Canadian Warmblood", "Canik", "Cape Harness", "Cape Horse", "Carolina Marsh Tacky", "Carpathian Pony", "Carthusian Horse", "Caspian", "Castilian Horse", "Catria Horse", "Cayuse Pony", "Celtic Pony", "Cerbat Mustang", "Certisino", "Chahou Post Pony", "Chaidamu Pony", "Chakouyi", "Chalosse Pony", "Champagne Horse", "Chamurthi", 
    "Chapman Horse", "Charentais", "Charollais", "Charysh", "Chara", "Cheju Pony", "Cheval de Corlay", "Cheval Demi sang du Centre", "Cheval d’Auvergne", "Chickasaw Horse", "Chicksaw Pony", "Chilean Corralero", "Chilkow", "Chilote Pony", "Chincoteague Pony", "Choctaw Horse", "Chumbivilcas Horse", "Chumysh Horse", "Chyanta Pony", "Cimarron Horse", "Cleveland Bay", "Clydesdale", "Cob", "Coffin Bay Pony", "Coldblooded Trotter", "Colonial Spanish", "Colorado Ranger",
    "Comtois horse", "Conestoga Horse", "Connemara Pony", "Corajoso", "Corolla Island Pony", "Corsican Horse", "Cossak Horse", "Costa Rican Saddle Horse", "Country Saddle Horse", "Cretan Horse", "Criollo", "Crioulo", "Crioulo Brasileiro", "Croatian Hladnokrvnjak", "Croatian Posavac", "Cuban Paso", "Cuban Pinto", "Cukurova", "Curly Haired Fox Trotter", "Curly Horse", "Cutchi", "Czech Coldblood", "Czech Warmblood", 
    "Czechoslovakian Small Riding Horse", "Dagestan Pony", "Dahoman", "Dales Pony", "Daliboz Horse", "Deliboz", "Danish Sport Pony", "Danish Wamblood", "Danube Delta Horse", "Danubian", "Dunav", "Darashouri", "Darashouli", "Darfur Pony", "Dartmoor Pony", "Datong Horse", "Debao Pony", "Deli Pony", "Deliorman", "Deliormanski", "Desert Norman Horse", "Deutsches Reitpony", "Dilbaz", "Deliboz", 
    "Daliboz", "Delibozskaya", "Djamoi", "Djamonský Pony", "Djerma Horse", "Dolny-Iskar", "Don", "Donskaya", "Dongola", "Dongolah", "Dongolawi", "Dosanko Horse", "Drum Horse", "Dutch Draft", "Dutch Harness Horse", "Dutch Warmblood", "Dzhabe", "Døle Gudbrandsdal", "Dølehest", "Døle Trotter", "Dülmen Pony", "East Bulgarian Horse", "East Friesian Horse – Old Type", "East Friesian Warmblood", "East Prussian", "Edelbluthaflinger", 
    "Ege Midillisi", "Egyptian Arabian", "Egyptian Horse", "Einsiedler", "Eleia", "English Thoroughbred", "Equus Kinsky", "Equus Przewalskii", "Eriskay Pony", "Erlanbach", "Erlunchun", "Esperia Pony", "Estonian Draft", "Estonian Arden", "Estonian Native", "Exmoor Pony", "Faca Galizana", "Falabella", "Faroe Pony", "Faeroes Pony", "Faeroe Island Horse", "Fell Pony", "Finnhorse", "Finnish Universal", "Finnish Warmblood", "Fjord horse", "Flemish Horse", 
    "Fleuve", "Flores Pony", "Florida Cracker Horse", "Florida Horse", "Florida Cow Pony", "Foundation Quarter Horse", "Fouta Horse", "Foutanké",
    "Frederiksborg Horse", "Freiberger horse", "Franches Montagnes", "Freiberger", "French Anglo Arab", "French Ardennais", "French Cob", "French Saddle Pony", "French Saddlebred", "Halfblood", "French Sport Horse", "French Trotter", "Friesian", "Friesian Sporthorse", "Furioso Horse", "Gala Horse", 
    "Galiceño Pony", "Galician Pony", "Gallego", "Galaga", "Galloway Pony", "Galshar", "Garrano", "Garrano do Minho",
    "Gayoe Pony", "Gelderlander", "Gelderland", "Geogrgian Grand", "German Coach Horse", "German Cold-Blooded", "German Riding Pony", "Gharbaui", "Gharkawi", "Ghazi", "Giara", "Gidran", "Glasinacki", "Goklan", "Golden American Saddlebred", "Golden Horse of Bohemia", "Gotland Pony", "Grand Noir du Berry Donkey", "Great Black Berry Ass", "Great Poland Horse", "Greek Pony", 
    "Greyson Highlands Ponies", "Groningen Horse", "Groninger", "Guangxi Horse", "Guanxi", "Guanzhong", "Guba", "Guizhou Pony", "Guoxia Pony", "Gutsul", "Guculs", "Guzuls", "Gypsy Vanner", "Hackney Horse", "Hackney Pony", "Haflinger", "Half-Saddlebred", "Handachine Horse", "Hanoverian", "Hantam Horse", "Harddraver", "Holländischer", "Hardtdraver", "Harna", "Hazziz", "Hebridean Pony", "Heck Horse", "Heihe Horse", "Heilongkiang", "Henson Horse", "Hequ", "Hequl", "Hessen Horse", 
    "Hessischer", "Highland Pony", "Highlander Horse", "Hinis Horse", "Hinisin Kolu Kisasi Ati", "Hirzai", "Hispano", "Hispano Arabe", "Hmong Horse", "Hokkaido Pony", "Holsteiner",
    "Holsteiner Coldblood", "Horse of the Americas", "Hrvatski Hladnokrvnjak", "Hrvatski Posavac", "Hucul", "Huçul", "Hutsul", "Hutul", "Huculska", "Huzul ", "Hungarian Draft", "Hungarian Coldblood", "Hungarian Dun", "Hungarian Horse", "Hungarian Felver", "Ibérian Warmblood", "Icelandic Horse", "Ilia", "Indian Country Bred Horse", "Indian Horse", "Indian Pony", "International Striped Horse", "Iomud", "Iomudskaya", "Irish Cob", "Irish Draft", 
    "Irish Draught", "Irish Hobby", "Irish Hunter", "Irish Sport Horse", "Israeli Horse", "Italian Heavy Draft", "Italian Working Horse", "Italian Trotter", "Jabe", "Jaca Gallega", "Java Pony", "Jeju Pony", "Jennet", "Jianchang Pony", "Jielin Horse", "Jinhong Horse", "Jinzhou", "Jura", "Jutland", "Kabarda", "Kabardian", "Kabardinskaya", "Kagoshima", "Kuyshu", "Kaimanawa Horse", "Kaju Pony", "Kaldblodstraver", "Kalmyk", "Kalmykskaya", "Kandachi", "Kandachime",
    "Karabair", "Karabairskaya", "Karabakh", "Karabakhskaya", "Karacabey", "Karachai", "Karakachan Pony", "Karatschai Pony", "Karatschaever", "Karatschaewsker", "Karachaier", "Karakacan", "Kathiawari", "Kathi", "Kutchi", "Kazakh Horse", "Kazakhskaya", "Ke-Er-Qin", "Kentucky Mountain Saddle Horse", "Kerry Bog Pony", "Khani", "Kiger Mustang", "Kinsky Horse", 
    "Kirdi Pony", "Kirghiz", "Kirgizskaya", "Kisber Halfbred", "Kisber Felver", "Kiso Horse", 
    "Kladruby Horse", "Kladruber", "Kladrubsky", "Kleines Deutsches Reitpferd", "Klepper", "Knabstrupper", "Konik Horse", "Kordofani", "Kuda-Gayo", "Kumingan", "Kundudo", "Kushum", "Kushumakaya", "Kustanai", "Kustanair", "Kustanaiskaya", "Kuznetsk Horse", "KWPN", "Kyrgyz Horse", "Labem Horse", "Lac la Croix Indian Pony", "LLCIP", "Lakka", "Logone", "Landais Pony",
    "Latgale Trotter", "Latvian", "Latviiskaya", "Lehmkuhlener Pony", "Leutstetten", "Leutstettener", "Lewitzer Pony", "Lewitz Pony", "Lichuan", "Lijiang Pony",
    "Limousin Horse", "Lipizzan", "Lipizzaner", "Lippit Morgan", "Lithuanian Heavy Draft", "Lithuanian Landrace", "Little Poland Horse", "Ljutomer Trotter", "Llanero", "Lokai", "Lokaiskaya", "Lombok", "Losino", "Lundy Pony", "Lusitano", "Lyngen Horse", "Macassar", "Magyar Hidegveru", "Malakan Horse", "Mallorquin Horse", "Malopolski", "Mangalarga Marchador",
    "Mangalarga Paulista", "Manipuri Pony", "Marajoara", "Marajo", "Maremmano", "Maremmana Horse", "Marquesas Islands Horse", "Marsh Tacky", "Marwari", "Masuren", "Mazury", "Mecklenburg", "Mecklenburger Horse", "Megezh", "Megrel", "Mingrelian", "Megrelskaya", "Menorca", "Menorquin Horse", "Merens Pony", 
    "Messara Horse", "Metis Trotter", "Mezen", "Mezenskaya", "Mezohegyes Sport Horse", "Mimoseano",
    "Minho", "Miniature Horse", "Minusin Horse", "Misaki Pony", "Miyazaki", "Missouri Fox Trotting Horse", "Miyako Horse", "Miyazaki", "Mogod Pony", "Mongolian", "Mongolian Wild Horse", "Montana Travler", "Monterufoli Pony", "Morab", "Morgan Horse", "Morna", "Moroccan Barb", "Morochuco", "Mountain Pleasure Horse", "Mousseye Pony", "Mbai", "M’baye", "Mussey", "Moyle Horse", "Mulassier Horse", "Mura", "Mur Island", "Medjimurski", "Murakoz", "Murakosi", 
    "Murgese", "Murge Horse", "Musey Pony", "Mustang", "Mytilene Horse", "M’Bayar", "Namaqua Pony", "Nambu Horse",
    "Namib Desert Horse", "Nanfan", "Narragansett Pacer", "Narym", "Narymskaya", "National Show Horse", "Navarra", "Navarran", "Navarrais", "Navarre Pony", "Neapolitan", "Napolitan", "Napolitano Horse", "Nederlands Appaloosa Pony", "Nederlands Mini Paarden", "Dutch Mini Horse", "Nederlands Trekpaard", "Nefza", "New Forest Pony", "New Kirgiz Horse", "Novokirgizskaya", "Newfoundland Pony", "Nez Perce Horse", "Nigerian", "Nogai Horse", "Nokota Horse", "Noma Horse", "Nonius", "Noniusz", 
    "Nooitgedacht Pony", "Nordland Horse", "Norfolk Roadster", "Norfolk Trotter", "Noriker", "Noric", "Norman Cob", "Normandy Cob", "Norman Trotter", "North African Barb", "North Swedish Horse", "Nordsvensk Hast", "Northeastern", "Nordestino", "Northern Ardennais", "Northern Draft Horse", "Norwegian Fjord", "Norwegian Dun", "Norwegian Pony", "Northern Dun", "Norwegian Riding Pony",
    "Northlands", "Nordland-Lyngen", "Norwegian Trotter", "Novokirghiz", "Ob Pony", "Oberlander Horse", "Ocracoke",
    "Old Austrian Warmblood", "Old English Black Horse", "Old Kladruby Horse", "Oldenburger", "Oldenburg", "Orlov Trotter", "Orlovskaya Rysistaya",
    "Orlov-Rostopchin", "Oromo Horse", "Ostlandhester", "Outer Banks Ponies", "Padang Pony", "Paint Horse", "Paint Pony", "Palomino", "Pampa Horse", "Panela", "Peneia", "Pinia |Peneia", "Pineia", "Panje", "Panjeskaya", "Pantaneiro", "Poconeano", "Paso Fino", "Patibarcina Horse", "Pechora", "Pechorskaya", "Pentro", "Percheron", "Periangan Pony", "Perkehner Horse", "Persano Horse",
    "Peruvian Paso", "Petiso Pony", "Petiso Argentino", "Pindos Pony", "Pinkafo", "Pinkafeld Horse",
    "Pintabian", "Pinzgauer Horse", "Piquira Pony", "Pleven", "Plevna", "Plevenska", "Poitevin", "Polesian", "Polessakya", "Polish Konik", "Polish Primitive Horse", "Poney Gallego", "Poni Galaga", "Poney Mousseye", "Poneys Landais", "Pony of the Americas", "Posavina Horse", "Pottok", "Poznan Horse", "Prairie Horse", "Prairie Pony", "Priob", "Przewalski’s Horse", "Qatgani Horse", 
    "Quarab", "Quarter horse", "Quarter Pony", "Racking Horse", "Rahvan", "West Black Sea Rahvan Horse", "Rangerbred horse", 
    "Rhineland Heavy draft", "Rhenish Cold Blood", "Riwoche Pony", "Roadster", "Rocky Mountain Horse", "Romanian Saddle Horse", "Romanian Trotter", "Rottaler", "Rottal", "Rottaler Warmblut", "Russ", "Russian Don", "Russian Heavy Draft", "Russian Riding Horse", "Russian Trotter", "Sable Island Pony",
    "Sachsen Warmblood", "Sachsen Anhaltiner Warmblut", "Saddlebred", "Sadecki", "Salerno Horse", "Salernitano", "Samolaco", "San Fratello Horse", "Sanfratellani", "Sicilian Horse", "Sandalwood Pony", "Sandal", "Sandan Horse", "Sanhe", "Sardinian", "Sarcidano", "Sarvar", "Saxon-Turinga Coldblood", "Sächsisch-Thüringisches Kaltblut", "Saxony Warmblood", "Saxony-Thuringian Warmbloods", "Schleswiger Heavy Draft", 
    "Schleswiger Kaltblut", "Schwarzwälder Fuchs", "Scottish Galloway", "Selle Français", "Selle Français Pony", "Seminole Pony", "Senne Horse", "Senner", "Sertanejo",
    "Shackleford Banks Horse", "Shagya Arabian", "Shan Pony", "Sheehan", "Shetland Pony", "Shire Horse", "Silesian", "Slaski Horse", "Single-Footing Horse", "Sini", "Sining Horse",
    "Skogsruss", "Skyros Pony", "Slovak Sport Pony", "Slovak", "Slovakian Warmblood", "Sokolsky", "Sokolski", "Somali Pony", "Somme Bay Horse", "Sorraia", "South African Miniature", "South African Vlaamperd", "South African Warmblood", 
    "South German Coldblood", "Suddeutsches Kaltblut", "Soviet Heavy Draft", "Spanish Anglo-Arabian", "Spanish Barb", "Spanish Colonial Horse", "Spanish Jennet", "Spanish Mustang", "Spanish Norman", "Spiti Pony", "Spotted Saddle Horse", "Standardbred", "Strelets Horse", "Sudan Country-Bred", "Suffolk Punch", 
    "Sugarbush Draft", "Sulawesi", "Sumba Pony", "Sumbawa Pony", "Sunicho", "Swedish Ardennes", "Svensk Ardenner", "Swedish Warmblood", "Swedish Halfbred", "Swiss Warmblood", "Swiss Halfbred", "Süddeutsches Kaltblut", "Taishuh", "Taishu Horse", "Takhi Horse", "Tarbes", "Tarbais", "Tarpan", "Tavda", "Tavdinka", "Tavdinskaya",
    "Tawleed", "Tchenarani", "Tennessee Walking Horse", "Tennuvian", "Tersk", "Tersky", "Terskaya", "Thai Pony", "Thai Country Bred", "Thessalian", "Thessalonian", "Thoroughbred", "Thüringen Warmblood", "Tibetan Pony", "Tiger Horse", "Timor Pony", "Tinker Horse", "Tokara Pony", "Tokara Kyushu", "Tolfetano Horse", "Tori", "Tory", "Toric", "Toriiskaya", "Trait Du Nord", "Trakehner", "Trakya", "Tres Sangres", 
    "Three Blood", "Trote en Gallope", "Trote y Galope", "Trochador", "Trocha Horse", "Trottatore Italiano", "Trotteur Francais",
    "Tuigpaard", "Tuigpaarden", "Tunisian Pony", "Turk", "Turkoman", "Turkmene", "Turkmen", "Turkmenian", "Tushin", "Tuva", "Tuvan", "Tuvinskaya", "Tyrol Pesante Rapido", "Ukrainian Saddle-Riding Horse", "Unmol", "Upper Yenisei", "Uzunyayla Horse", "Venezuelan Criollo", "Ventasso Horse", "Vietnamese Hmong", "Virginia Highlander", "Vlaamperd", "Vladimir Heavy Draft",
    "Voronezh Coach", "Vyatka", "Viatka", "Waler", "Walkaloosa", "Washu Horse", "Welara Pony", "Welsh Cob ", "Welsh Mountain Pony ", "Welsh Pony", "Welsh Pony of Cob Type", "Weser-Ems Pony", "West African Barb", "West Norwegian", "West Norway",
    "Westland", "Western Sudan Pony", "Westfalen Pony", "Westfalen", "Westphalian", "Wielkopolski", "Wild Horses of the Namib", "Württemberger", "Xilingol", "Yabou", "Yaboo", "Yakut Horse", "Yamud", "Yanqi Horse", "Yemeni Horse", "Yili Horse", "Yonaguni Horse", "Yorkshire Coach Horse", "Yugoslav Mountain Pony", "Yunnan", "Yururi Island horse", "Zangersheide", "Zaniskari Pony",
    "Zeeland", "Zemaituka", "Zemaitukai", "Žemaitukas", "Zemaituka", "Zhumd", "Zhemaichu", "Zhmudk", "Zweibrucker"]
    
    species = "Horse"

    max_age = 30

    def __init__(self, name=None, age=None, breed=None):
        super(Horse, self).__init__(Horse.species, name=name, age=age, breed=breed)
    
    @property
    def sound(self):
       return "Neigh"

if __name__ == "__main__":
    pixie = Horse("Pixie", 6, "Arabian")
    pixie.speak()