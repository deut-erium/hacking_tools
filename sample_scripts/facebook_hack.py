# This super duper leet hacking script will gain access to any facebook account in 2ms.
# PLease do not share this this is made by the 'anonymous mouse' group and is proprietary.
# Very dangerous

from time import sleep
import random


def print_logo():
    logo = """
 ********     **       ******  ******** *******   ****  **       ** ****     **
/**/////     ****     **////**/**///// /**////** *///**/**      /**/**/**   /**
/**         **//**   **    // /**      /**   /**/*  */*/**   *  /**/**//**  /**
/*******   **  //** /**       /******* /******* /* * /*/**  *** /**/** //** /**
/**////   **********/**       /**////  /**////  /**  /*/** **/**/**/**  //**/**
/**      /**//////**//**    **/**      /**      /*   /*/**** //****/**   //****
/**      /**     /** //****** /********/**      / **** /**/   ///**/**    //***
//       //      //   //////  //////// //        ////  //       // //      ///
  """
    print(logo)


def start(username):
    print("Starting hack on {}".format(username))
    sleep(3)
    print("Connecting to http://facebook.com/login via telnet...")
    sleep(4)
    print("Telnet connection opened on port 1337. Uploading the CSS Mainframe to avoid detection.")
    sleep(5)
    print("Mainframe deployed with sleath statistic set to 0.9 (90%) for faster data retrieval.")
    print("Proceeding to filter database.")
    sleep(4)

# wtf even is this lol


def sqlbinary(username):
    print(
        "Compiling sql statement with gcc: 'SELECT * from main_db.users where 'username' = '{}';".format(username))
    sleep(6)
    print("[-] GCC FATAL ERROR. Trying g++...")
    print(
        "Compiling sql statement with g++: 'SELECT * from main_db.users where 'username' = '{}';".format(username))
    sleep(4)
    print("Binary created. Deploying to retrieve data...")

def upload():
  for i in range(100):
    if i == 20:
        print(
            "Facebook servers are currently overloaded. Data retrieval speeds may be affected.")
    elif i == 50:
        print("Halfway there. Looks like the servers are under less load now.")
    elif i == 90:
        print("Almost done with the data retrieval.")
    print("{}/100% done".format(i))
    sleep(4)

def gethash():
  print("Successful data retrieval. Using the help of Jonathan to crack the hash.")
  hash = "$2y${}${}".format(
      random.getrandbits(20), random.getrandbits(128))
  print("Found hash {}".format(hash))
  print("Identifying hash format. This may take a while. ")
  sleep(1)
  hashes = hashes = ["BLAKE-256","BLAKE-512","BLAKE2s","BLAKE2b","BLAKE2X","BLAKE3","ECOH","FSB","GOST","Grøstl","HAS-160","HAVAL","JH","LSH[15]","MD2","MD4","MD5","MD6","RadioGatún","RIPEMD","RIPEMD-128","RIPEMD-160","RIPEMD-320","SHA-1","SHA-224","SHA-256","SHA-384","SHA-512","SHA-3 (subset of Keccak)","Skein","Snefru","Spectral Hash","Streebog","SWIFFT","Tiger","Whirlpool","BLAKE-256","BLAKE-512","BLAKE2s","BLAKE2b","BLAKE2X","BLAKE3","ECOH","FSB","GOST","Grøstl","HAS-160","HAVAL","JH","LSH[15]","MD2","MD4","MD5","MD6","RadioGatún","RIPEMD","RIPEMD-128","RIPEMD-160","RIPEMD-320","SHA-1","SHA-224","SHA-256","SHA-384","SHA-512","SHA-3 (subset of Keccak)","Skein","Snefru","Spectral Hash","Streebog","SWIFFT","Tiger","Whirlpool","BLAKE-256","BLAKE-512","BLAKE2s","BLAKE2b","BLAKE2X","BLAKE3","ECOH","FSB","GOST","Grøstl","HAS-160","HAVAL","JH","LSH[15]","MD2","MD4","MD5","MD6","RadioGatún","RIPEMD","RIPEMD-128","RIPEMD-160","RIPEMD-320","SHA-1","SHA-224","SHA-256","SHA-384","SHA-512","SHA-3 (subset of Keccak)","Skein","Snefru","Spectral Hash","Streebog","SWIFFT","Tiger","Whirlpool"]
  correct_hash = random.choice(hashes)
  for h in hashes:
    print("Matching our hash with {}".format(h))
    sleep(1)
    if h == correct_hash:
      print("Found correct hash type: {}.".format(correct_hash))
      break

def decrypt():
  print("Decrypting...")
  passwords = ["123456","12345","123456789","password","iloveyou","princess","1234567","rockyou","12345678","abc123","nicole","daniel","babygirl","monkey","lovely","jessica","654321","michael","ashley","qwerty","111111","iloveu","000000","michelle","tigger","sunshine","chocolate","password1","soccer","anthony","friends","butterfly","purple","angel","jordan","liverpool","justin","loveme","fuckyou","123123","football","secret","andrea","carlos","jennifer","joshua","bubbles","1234567890","superman","hannah","amanda","loveyou","pretty","basketball","andrew","angels","tweety","flower","playboy","hello","elizabeth","hottie","tinkerbell","charlie","samantha","barbie","chelsea","lovers","teamo","jasmine","brandon","666666","shadow","melissa","eminem","matthew","robert","danielle","forever","family","jonathan","987654321","computer","whatever","dragon","vanessa","cookie","naruto","summer","sweety","spongebob","joseph","junior","softball","taylor","yellow","daniela","lauren","mickey","princesa","alexandra","alexis","jesus","estrella","miguel","william","thomas","beautiful","mylove","angela","poohbear","patrick","iloveme","sakura","adrian","alexander","destiny","christian","121212","sayang","america","dancer","monica","richard","112233","princess1","555555","diamond","carolina","steven","rangers","louise","orange","789456","999999","shorty","11111","nathan","snoopy","gabriel","hunter","cherry","killer","sandra","alejandro","buster","george","brittany","alejandra","patricia","rachel","tequiero","7777777","cheese","159753","arsenal","dolphin","antonio","heather","david","ginger","stephanie","peanut","blink182","sweetie","222222","beauty","987654","victoria","honey","00000","fernando","pokemon","maggie","corazon","chicken","pepper","cristina","rainbow","kisses","manuel","myspace","rebelde","angel1","ricardo","babygurl","heaven","55555","baseball","martin","greenday","november","alyssa","madison","mother","123321","123abc","mahalkita","batman","september","december","morgan","mariposa","maria","gabriela","iloveyou2","bailey","jeremy","pamela","kimberly","gemini","shannon","pictures","asshole","sophie","jessie","hellokitty","claudia","babygirl1","angelica","austin","mahalko","victor","horses","tiffany","mariana","eduardo","andres","courtney","booboo","kissme","harley","ronaldo","iloveyou1","precious","october","inuyasha","peaches","veronica","chris","888888","adriana","cutie","james","banana","prince","friend","jesus1","crystal","celtic","zxcvbnm","edward","oliver","diana","samsung","freedom","angelo","kenneth","master","scooby","carmen","456789","sebastian","rebecca","jackie","spiderman","christopher","karina","johnny","hotmail","0123456789","school","barcelona","august","orlando","samuel","cameron","slipknot","cutiepie","monkey1","50cent","bonita","kevin","bitch","maganda","babyboy","casper","brenda","adidas","kitten","karen","mustang","isabel","natalie","cuteako","javier","789456123","123654","sarah","bowwow","portugal","laura","777777","marvin","denise","tigers","volleyball","jasper","rockstar","january","fuckoff","alicia","nicholas","flowers","cristian","tintin","bianca","chrisbrown","chester","101010","smokey","silver","internet","sweet","strawberry","garfield","dennis","panget","francis","cassie","benfica","love123","696969","asdfgh","lollipop","olivia","cancer","camila","qwertyuiop","superstar","harrypotter","ihateyou","charles","monique","midnight","vincent","christine","apples","scorpio","jordan23","lorena","andreea","mercedes","katherine","charmed","abigail","rafael","icecream","mexico","brianna","nirvana","aaliyah","pookie","johncena","lovelove","fucker","abcdef","benjamin","131313","gangsta","brooke","333333","hiphop","aaaaaa","mybaby","sergio","welcome","metallica","julian","travis","myspace1","babyblue","sabrina","michael1","jeffrey","stephen","love","dakota","catherine","badboy","fernanda","westlife","blondie","sasuke","smiley","jackson","simple","melanie","steaua","dolphins","roberto","fluffy","teresa","piglet","ronald","slideshow","asdfghjkl","minnie","newyork","jason","raymond","santiago","jayson","88888888","5201314","jerome","gandako","muffin","gatita","babyko","246810","sweetheart","chivas","ladybug","kitty","popcorn","alberto","valeria","cookies","leslie","jenny","nicole1","12345678910","leonardo","jayjay","liliana","dexter","sexygirl","232323","amores","rockon","christ","babydoll","anthony1","marcus","bitch1","fatima","miamor","lover","chris1","single","eeyore","lalala","252525","scooter","natasha","skittles","brooklyn","colombia","159357","teddybear","winnie","happy","manutd","123456a","britney","katrina","christina","pasaway","cocacola","mahal","grace","linda","albert","tatiana","london","cantik","0123456","lakers","marie","teiubesc","147258369","charlotte","natalia","francisco","amorcito","smile","paola","angelito","manchester","hahaha","elephant","mommy1","shelby","147258","kelsey","genesis","amigos","snickers","xavier","turtle","marlon","linkinpark","claire","stupid","147852","marina","garcia","fuckyou1","diego","brandy","letmein","hockey","444444","sharon","bonnie","spider","iverson","andrei","justine","frankie","pimpin","disney","rabbit","54321","fashion","soccer1","red123","bestfriend","england","hermosa","456123","qazwsx","bandit","danny","allison","emily","102030","lucky1","sporting","miranda","dallas","hearts","camille","wilson","potter","pumpkin","iloveu2","number1","katie","guitar","212121","truelove","jayden","savannah","hottie1","phoenix","monster","player","ganda","people","scotland","nelson","jasmin","timothy","onelove","ilovehim","shakira","estrellita","bubble","smiles","brandon1","sparky","barney","sweets","parola","evelyn","familia","love12","nikki","motorola","florida","omarion","monkeys","loverboy","elijah","joanna","canada","ronnie","mamita","emmanuel","thunder","999999999","broken","rodrigo","maryjane","westside","california","lucky","mauricio","yankees","jackass","jamaica","justin1","amigas","preciosa","shopping","flores","mariah","matrix","isabella","tennis","trinity","jorge","sunflower","kathleen","bradley","cupcake","hector","martinez","elaine","robbie","friendster","cheche","gracie","connor","hello1","valentina","melody","darling","sammy","jamie","santos","abcdefg","joanne","candy","fuckyou2","loser","dominic","pebbles","sunshine1","swimming","millie","loving","gangster","blessed","compaq","taurus","gloria","tyler","aaron","darkangel","kitkat","megan","dreams","sweetpea","bettyboop","jessica1","cynthia","cheyenne","ferrari","dustin","iubire","a123456","snowball","purple1","violet","darren","starwars","bestfriends","inlove","kelly","batista","karla","sophia","chacha","biteme","marian","sydney","sexyme","pogiako","gerald","jordan1","010203","daddy1","zachary","daddysgirl","billabong","carebear","froggy","pinky","erika","oscar","skater","raiders","nenita","tigger1","ashley1","charlie1","gatito","lokita","maldita","buttercup","nichole","bambam","nothing","glitter","bella","amber","apple","123789","sister","zacefron","tokiohotel","loveya","lindsey","money","lovebug","bubblegum","marissa","dreamer","darkness","cecilia","lollypop","nicolas","google","lindsay","cooper","passion","kristine","green","puppies","ariana","fuckme","chubby","raquel","lonely","anderson","sammie","sexybitch","mario","butter","willow","roxana","mememe","caroline","susana","kristen","baller","hotstuff","carter","stacey","babylove","angelina","miller","scorpion","sierra","playgirl","sweet16","012345","rocker","bhebhe","gustavo","marcos","chance","123qwe","kayla","james1","football1","eagles","loveme1","milagros","stella","lilmama","beyonce","lovely1","rocky","daddy","catdog","armando","margarita","151515","loves","lolita","202020","gerard","undertaker","amistad","williams","qwerty1","freddy","capricorn","caitlin","bryan","delfin","dance","cheerleader","password2","PASSWORD","martha","lizzie","georgia","matthew1","enrique","zxcvbn","badgirl","andrew1","141414","11111111","dancing","cuteme","booger","amelia","vampire","skyline","chiquita","angeles","scoobydoo","janine","tamara","carlitos","money1","sheila","justme","ireland","kittycat","hotdog","yamaha","tristan","harvey","israel","legolas","michelle1","maddie","angie","cinderella","jesuschrist","lester","ashton","ilovejesus","tazmania","remember","xxxxxx","tekiero","thebest","princesita","lucky7","jesucristo","peewee","paloma","buddy1","deedee","miriam","april","patches","regina","janice","cowboys","myself","lipgloss","jazmin","rosita","happy1","felipe","chichi","pangit","mierda","genius","741852963","hernandez","awesome","walter","tinker","arturo","silvia","melvin","celeste","pussycat","gorgeous","david1","molly","honeyko","mylife","animal","penguin","babyboo","loveu","simpsons","lupita","boomer","panthers","hollywood","alfredo","musica","johnson","ilovegod","hawaii","sparkle","kristina","sexymama","crazy","valerie","spencer","scarface","hardcore","098765","00000000","winter","hailey","trixie","hayden","micheal","wesley","242424","0987654321","marisol","nikita","daisy","jeremiah","pineapple","mhine","isaiah","christmas","cesar","lolipop","butterfly1","chloe","lawrence","xbox360","sheena","murphy","madalina","anamaria","gateway","debbie","yourmom","blonde","jasmine1","please","bubbles1","jimmy","beatriz","poopoo","diamonds","whitney","friendship","sweetness","pauline","desiree","trouble","741852","united","marley","brian","barbara","hannah1","bananas","julius","leanne","sandy","marie1","anita","lover1","chicago","twinkle","pantera","february","birthday","shadow1","qwert","bebita","87654321","twilight","imissyou","pollito","ashlee","tucker","cookie1","shelly","catalina","147852369","beckham","simone","nursing","iloveyou!","eugene","torres","damian","123123123","joshua1","bobby","babyface","andre","donald","daniel1","panther","dinamo","mommy","juliana","cassandra","trustno1","sexylady","14344","autumn","mendoza","animals","perfect","mariel","bullshit","bitches","852456","marcela","drpepper","gerardo","titanic","robert1","alison","moomoo","paulina","blossom","simpleplan"]
  rpass = random.choice(passwords)
  sleep(25) # sleep for 25 sec why not. Cracking takes time
  print("Found password: {}".format(rpass))


def hack(n):
    # Facebook l33t hacking script
    if n == 1:
        username = input("Enter facebook identifier(username, email, phone): ")
      
        start(username)
        sqlbinary(username)
        #upload()
        gethash()
        decrypt()
        
        print("Thank you for using facep0wn3r. Created by the 'anonymous mouse' group for illegal purposes.")
    else:
        print("Not implemented...")
def choice():
    choice = 1
    try:
        choice = int(input("""
            1 - Crack facebook hash
            2 - Crack instagram hash
            3 - Crack twitter hash
            >"""))
    except:
        print("You cannot even follow simple instructions...")
        exit()
    return choice


print_logo()

n = choice()
hack(n)
