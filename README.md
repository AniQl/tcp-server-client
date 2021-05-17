# tcp-server-client
How to run?
run server.py
run client.py
Observe STDOUT and created files.

Task (it will be formatted later)
BLK-5

RCV-5

87541

12093

10911

12094

99801

ACK-checksum

BLK-100

RCV-100

...

ACK-checksum

EOT

 

BLK-x – x to liczba, którą sender zapowiada, że zaraz przyśle 5 4-bajtowych słów

RCV-x – x ta sama liczba, którą receiver odsyła do sendera potwierdzając, że jest gotowy do przyjęcia

ACK-checksum – checksum to suma tych słów obliczona w ten sposób, że z każdego słowa jest odrzucona pierwsza cyfra, a pozostałe są dodane do sumy; jeśli suma ma więcej cyfr niż 5, cyfra na 6-tym miejscu licząc od prawej i kolejne są odrzucone

Jeśli suma przysłana przez receivera zgadza się z tą obliczoną wewnętrznie przez sendera, przystępuje do tranmisji kolejnego bloku (który może mieć niż liczbę słów inną, niż poprzedni blok).

Jeśli suma się nie zgadza, sender przesyła EOT, co kończy transmisję.

Jeśli wyśle wszystkie bloki, sender również przesyła EOT.

 

Liczba bloków niech będzie losową liczbą z zakresu <5-10>, a słów w bloku – z zakresu <5-100>.

Sender może logować każde wysłane i otrzymane słowo do pliku.