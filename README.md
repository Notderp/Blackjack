# Blackjack
Gra w blackjacka napisana w Pythonie z wykorzystaniem podstawowych bibliotek, gra ma uwzględnioną różną liczbę graczy i przedstawia poprawnie działającą logikę, przypisanie kart, wartości kart w zależności od ręki, uwzględnia obsługę błędów w inpucie na etapie grania. Szczegóły na temat skryptu:
-skrypt zawiera klasę gracza, klasa zawiera metodę statyczną, zmienną na poziomie klasy, która jest inkrementowana przy tworzeniu instancji i wykorzystywana w logicę odpowiadającej za ciąg gry.
-Na każdego gracza przypada instancja gracza, gracz ma przypisowane parametry typu imię, posiadane karty. Klasa zawiera metody pozwalające graczowi na podjęcie decyzji i na wyliczenie wartości kart u gracza. 
-talia jest przygotowana za pomocą listy tupletów, mieszanie talii i wyciąganie kart jest zasymulowane z wykorzystaniem modułu random
-na każdym z etapów, w których użytkownik ma przekazać wartości jako input, wartości te są sprawdzane, a potencjalne błędy wynikające z niepoprawnych lub powielających się wartości są obsługiwane.
