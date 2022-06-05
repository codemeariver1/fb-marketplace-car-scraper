# Page defining constants used within the bot
# Leaving an empty string, denoted as '', will leave the default parameter 
# Capitalization matters! Pay attention to details!

# Define your facebook credentials here:
MY_USERNAME = ''
MY_PASSWORD = ''

# Define your desired vehicle make or make and model
CAR_MAKE = '27' # Leave empty to set all as default or enter the corresponding number: 
                    # ( A )
                    # Acura-(1), Alfa Romeo-(2), Aston Martin-(2), Audi-(4)
                    # ( B )
                    # BMW-(5),  Bentley-(6), Buick-(7)
                    # ( C )
                    # CODA-(8), Cadillac-(9), Chevrolet-(10), Chrysler-(11)
                    # ( D )
                    # Daewoo-(12), Daihatsu-(13), Dodge-(14)
                    # ( E )
                    # Eagle-(15)
                    # ( F )
                    # Ferrari-(15), Fiat-(17), Fisker-(18), Ford-(19), Freightliner-(20)
                    # ( G )
                    # GMC-(21), Genesis-(21), Geo-(23)
                    # ( H )
                    # Honda-(24), Hummer-(25), Hyundai-(26)
                    # ( I )
                    # Infiniti-(27), Isuzu-(28)
                    # ( J )
                    # Jaguar-(29), Jeep-(30)
                    # ( K )
                    # Kia-(31)
                    # ( L )
                    # Lamborghini-(32), Land Rover-(33), Lexus-(34), Lincoln-(35), Lotus-(36)
                    # ( M )
                    # Maserati-(37), Maybach-(38), Mazda-(39), Mclaren-(40), Mercedes-Benz-(41), Mercury-(42), Mini-(43), 
                        # Mitsubitshi-(44)
                    # ( N )
                    # Nissan-(45)
                    # ( O )
                    # Oldsmobile-(46)
                    # ( P )
                    # Panoz-(47), Plymouth-(48), Pontiac-(49), Porsche-(50)
                    # ( Q ) 
                    # Ram-(51), Rivian-(52), Rolls-Royce-(53)
                    # ( S )
                    # Saab-(54), Saturn-(55), Scion-(56), Smart-(57), Srt-(58), Subaru-(59), Suzuki-(60)
                    # ( T )
                    # Tesla-(61), Toyota-(62)
                    # ( V )
                    # Volkswagen-(63), Volvo-(64)
CAR_MODEL = '27h' # Leave empty to set all as default or enter the corresponding number-letter combination: 
                    # Acura:
                        # CL-(1a), ILX-(1b), Integra-(1c), Acura Legend-(1d), MDX-(1e), NSX-(1f), RDX-(1g), RL-(1h), RLX-(1i), 
                        # RSX-(1j), Acura SLX-(1k)
                    # Alfa Romeo:
                        # 164-(2a), 4C-(2b), 8C-(2c), Giulia-(2d), Spider-(2e), Stelvio-(2f) 
                    # Aston Martin:
                        # DB11-(3a), DB7-(3b), DB9-(3c), DBS-(3d), Rapide-(3e), Rapide S-(3f), Vanquish-(3g), Vantage-(3h), 
                        # Virage-(3i) 
                    # Audi:
                        # 100-(4a), 80-(4b), 90-(4c), A3-(4d), Audi A3 Sportback e-tron-(4e), A4-(4f), A4 Allroad Quattro-(4g), 
                        # A5-(4h), A6-(4i), A7-(4j), A8-(4k), allroad-(4l), Cabriolet-(4m), e-tron-(4n), Q3-(4o), Q5-(4p), 
                        # Q7-(4q), Q8-(4r), Quattro-(4s), R8-(4t), Audi RS5-(4u), RS3-(4v), RS4-(4w), RS6-(4x), Audi Rs7-(4y), 
                        # S3-(4z), S4-(4aa), S5-(4ab), S6-(4ac), Audi S7-(4ad), S8-(4ae), SQ5-(4af), TT-(4ag), TT RS-(4ah) 
                    # BMW:
                        # Series 4-(5a), i3-(5b), i8-(5c), M-(5d), M2-(5e), M3-(5f), M4-(5g), M5-(5h), M6-(5i), Series 1-(5j), 
                        # Series 2-(5k), Series 3-(5l), Series 4-(5m), Series 5-(5n), Series 6-(5o), Series 7-(5p), Series 8-(5q), 
                        # X1-(5r), X2-(5s), X3-(5t), X4-(5u), X5-(5v), X6-(5w), X7-(5x), Z1-(5y), Z3-(5z), Z4-(5aa), Z8-(5ab)  
                    # Bentley:
                        # Arnage-(6a), Azure-(6b), Bentayga-(6c), Brooklands-(6d), Continental-(6e), Flying Spur-(6f), 
                        # Mulsanne-(6g)
                    # Buick:
                        # Buick Cascada-(7a), Century-(7b), Electra-(7c), Enclave-(7d), Encore-(7e), Envision-(7f), 
                        # LaCrosse-(7g), LeSabre-(7h), Buick Lucerne-(7i), Park Avenue-(7j), Buick Ranier-(7k), Regal-(7l), 
                        # Rendezvous-(7m), Riviera-(7n), Roadmaster-(7o), Buick Skylark-(7p), Terraza-(7q), Verano-(7r)
                    # CODA:
                        # CODA Sedan-(8a), 
                    # Cadillac:
                        # -(9), 
                    # Chevrolet:
                        # -(10), 
                    # Chrysler:
                        # -(11), 
                    # Daewoo:
                        # -(12), 
                    # Daihatsu:
                        # -(13), 
                    # Dodge:
                        # -(14), 
                    # Eagle:
                        # -(15), 
                    # Ferrari:
                        # -(15), 
                    # Fiat:
                        # -(17), 
                    # Fisker:
                        # -(18), 
                    # Ford:
                        # -(19), 
                    # Freightliner:
                        # -(20), 
                    # GMC:
                        # -(21), 
                    # Genesis:
                        # -(21), 
                    # Geo:
                        # -(23), 
                    # Honda:
                        # -(24), 
                    # Hummer:
                        # -(25), 
                    # Hyundai:
                        # -(26), 
                    # Infiniti:
                        # EX-(27a), FX-(27b), G-(27c), JX-(27d), M-(27e), Q-(27f), Q40-(27g), Q50-(27h), Q60-(27i), Q70-(27j), 
                        # QX-(27k), QX30-(27l), QX50-(27m), QX60-(27n), QX70-(27o), QX80-(27p)
                    # Isuzu:
                        # -(28), 
                    # Jaguar:
                        # -(29), 
                    # Jeep:
                        # -(30), 
                    # Kia:
                        # -(31), 
                    # Lamborghini:
                        # -(32), 
                    # Land Rover:
                        # -(33), 
                    # Lexus:
                        # -(34), 
                    # Lincoln:
                        # -(35), 
                    # Lotus:
                        # -(36), 
                    # Maserati:
                        # -(37), 
                    # Maybach:
                        # -(38), 
                    # Mazda:
                        # -(39), 
                    # Mclaren:
                        # -(40), 
                    # Mercedes-Benz:
                        # -(41), 
                    # Mercury:
                        # -(42), 
                    # Mini:
                        # -(43), 
                    # Mitsubitshi:
                        # -(44), 
                    # Nissan:
                        # 200SX-(45a), 240 SX-(45b), 300ZX-(45c), 350Z-(45d), 370Z-(45d), Almera-(45e), Altima-(45f), 
                        # Armada-(45g), cube-(45h), Frontier-(45i), GT-R-(45j), JUKE-(45k), Kicks-(45l), LEAF-(45m), 
                        # Maxima-(45n), Murano-(45o), NX-(45p), NV-(45q), NV200-(45r), Pathfinder-(45s), Pathfinder Armada-(45t), 
                        # Quest-(45u), Rogue-(45v), Sentra-(45w), Nissan Stanza-(45x), 
                    # Oldsmobile:
                        # -(46), 
                    # Panoz:
                        # -(47), 
                    # Plymouth:
                        # -(48), 
                    # Pontiac:
                        # -(49), 
                    # Porsche:
                        # -(50), 
                    # Ram:
                        # -(51), 
                    # Rivian:
                        # R1S-(52a), R1T-(52b) 
                    # Rolls-Royce:
                        # Dawn-(53a), Ghost-(53b), Phantom-(53c), Silver Spur-(53d), Wraith-(53e)
                    # Saab:
                        # 9-2X-(54a), 43711-(54b), 9-3X-(54c), 9-4X-(54d), 43713-(54e), Saab 9-7X-(54f), 900-(54g), 9000-(54h) 
                    # Saturn:
                        # Astra-(55a), Aura-(55b), Ion-(55c), Saturn L-Series-(55d), Outlook-(55e), Saturn Relay-(55f), 
                        # Saturn S-Series-(55g), SKY-(55h), VUE-(55i)
                    # Scion:
                        # -(56), 
                    # Smart:
                        # Fortwo-(57a), Roadster-(57b) 
                    # Srt:
                        # -(58), 
                    # Subaru:
                        # -(59), 
                    # Suzuki:
                        # -(60), 
                    # Tesla:
                        # Model 3-(61a), Model S-(61b), Model X-(61c), 
                    # Toyota:
                        # -(62), 
                    # Volkswagen:
                        # -(63), 
                    # Volvo:
                        # -(64)

# Define the rest of your search parameters
SELLER = '2' # Leave empty for all or enter a number: Dealer Only-(1), Private Only-(2)
MIN_PRICE = ''
MAX_PRICE = ''
MIN_YEAR = '2017'
MAX_YEAR = ''



# STATIC URLS: DO NOT TOUCH!!
BASE_URL = 'https://www.facebook.com/'
FB_MARKETPLACE_URL = 'https://www.facebook.com/marketplace/category/vehicles'
