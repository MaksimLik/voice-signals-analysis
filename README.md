# voice-analysis
 A primitive python program for voice recognition.
####
Ten program jest skryptem do rozpoznawania płci mówcy na podstawie sygnału 
dźwiękowego jego głosu. Skrypt odczytuje pliki WAV z katalogu " train/", 
przetwarza sygnał, a następnie próbuje sklasyfikować mówcę jako 
mężczyznę ("M") lub kobietę ("K").
####
Główna funkcja iteruje po każdym pliku w katalogu 'train/', odczytuje plik za 
pomocą wavfile scipy.funkcja odczytu zmniejsza próbkowanie sygnału o 
współczynnik 10 za pomocą odcięcia, a następnie przesyła sygnał i nową 
częstotliwość próbkowania do funkcji function_signal. Funkcja 
function_signal przetwarza następnie sygnał i zwraca klasyfikację " M " lub 
"K", która jest porównywana z piątym znakiem nazwy pliku. Jeśli klasyfikacja 
pasuje do nazwy pliku, liczba good_answer wzrasta. Liczba pełnych 
odpowiedzi rośnie niezależnie od tego. Pod koniec pętli skrypt wyświetla 
całkowitą liczbę przetworzonych plików, liczbę poprawnych klasyfikacji i 
procent poprawnych klasyfikacji.
###
Funkcja fundamental_frequency pobiera sygnał i częstotliwość próbkowania 
jako dane wejściowe i zwraca oszacowanie częstotliwości podstawowej 
sygnału. Robi to, najpierw stosując szybką transformatę Fouriera (FFT) do 
sygnału, a następnie odfiltrowując wszystkie składowe częstotliwości z 
wyjątkiem tych w zakresie 70 Hz do częstotliwości Nyquista (połowa 
częstotliwości próbkowania). Następnie iteracyjnie mnoży amplitudy 
pozostałych składowych częstotliwości przez Amplitudy ich harmonicznych 
(wielokrotności całkowitej) aż do piątej harmonicznej. Na koniec zwraca 
częstotliwość składowej częstotliwości o największej wynikowej amplitudzie.
###
Funkcja recognize_gender przyjmuje indeks jako dane wejściowe i zwraca 
"M", jeśli indeks jest mniejszy lub równy 165 - " K " w przeciwnym razie.
Wreszcie skrypt ma na dole klauzulę ochronną, która wywołuje główną 
funkcję z katalogiem " train/", jeśli skrypt jest uruchamiany jako moduł 
główny.
####
Raport końcowy: 
####
All audio files: 91 (ilość całego zbioru)
####
Accepted files: 87 (ilość poprawnie rozpoznanych elementów)
####
Percent good answer: 95.6043956043956 (% od całej ilości)
####

Man: 45 (rozpoznano mężczyzn)

Woman: 42 (rozpoznano kobiet)

####
Recognized woman: 4 (nie rozpoznano kobiet)
####
Recognized man: 0 (nie rozpoznano mężczyzn)
