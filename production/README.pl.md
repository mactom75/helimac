# HELIMAC — pliki produkcyjne (rev J2)

English: [README.md](README.md)

> 🛑 **Rev J2 to wersja archiwalna — nie produkować J1, J2 ani J3.** Obowiązuje **rev K** (w projektowaniu, [docs/design-rev-K.md](../docs/design-rev-K.md)); paczki produkcyjne rev K po etapie 3 (model CAD i rysunki). **Wyjątek: falownik MC-P rev D1 jest aktualny** i zostaje w rev K.

Komplet do wykonania konstrukcji rev J2 (wersja archiwalna; pilot do 110 kg, masa startowa 225 kg): rysunki, pliki DXF do cięcia, modele STEP, pliki STL do druku 3D, dane CNC łopat oraz pełny projekt KiCad falownika MC-P z gerberami, BOM i plikami pozycji.

> ⚠️ **Prototyp, a nie certyfikowany statek powietrzny.** Wszystkie wartości są obliczone, jeszcze nie zmierzone. Przed budową przeczytaj [SAFETY.pl.md](../SAFETY.pl.md). Budujemy i badamy etapami: najpierw napęd na hamowni (395 N·m przez 30 min, potem 50 h), potem wirniki na uwięzi, potem loty bez pilota. Rysunki i elektronikę 400 V daj do przeglądu doświadczonym inżynierom, zanim zamówisz części.

## Pobieranie

Cztery pliki ZIP to kompletne pakiety, razem z plikami STEP i STL:

| Pakiet | Zawartość | Plik |
|---|---|---|
| **J1 – Zespół napędowy rev J2** | silnik, przekładnia cykloidalna 10:1, przekładnia nawrotna, piasty wirników, kolektyw górny, łożyska | [HELIMAC_J1_drive_revJ2.zip](downloads/HELIMAC_J1_drive_revJ2.zip) (32 MB) |
| **J2 – Łopaty wirników rev J** | 4 łopaty (dolne D i lustrzane górne G), rdzenie z ASA do druku, przyrządy, przekroje CNC | [HELIMAC_J2_blades_revJ.zip](downloads/HELIMAC_J2_blades_revJ.zip) (16 MB) |
| **J3 – Rama, siedzisko, pierścień PK, kolektyw dolny rev J2** | rama, siedzisko z punktami uprzęży, segmenty pierścienia PK, kolektyw dolny | [HELIMAC_J3_frame_seat_revJ2.zip](downloads/HELIMAC_J3_frame_seat_revJ2.zip) (0,6 MB) |
| **MC-P – falownik 3-fazowy SiC rev D1** | projekt KiCad 7, gerbery, BOM, CPL, schemat, rysunek mechaniczny, STEP | [HELIMAC_MC-P_inverter_revD1.zip](downloads/HELIMAC_MC-P_inverter_revD1.zip) (2,6 MB) |

Aby pobrać ZIP: otwórz link i kliknij **Download raw file** (↓). Całe repozytorium: na stronie głównej **Code → Download ZIP**.

Rysunki, pliki DXF, gerbery i projekt KiCad są też w folderach poniżej, więc można je przeglądać na GitHubie. Pliki STEP i STL są tylko w paczkach ZIP; sam model złożenia napędu ma 107 MB.

Oznaczenia części: K – kolumna, P – przekładnia cykloidalna, N – przekładnia nawrotna i piasta górna, S – silnik, C – kolektyw, R – rama i siedzisko, PK – pierścień kierujący powietrze, L / W / J – segmenty łopat, rysunki łopat, przyrządy.

## Mechanika — [mechanical/](mechanical/)

### J1 – Zespół napędowy rev J2
- `drawings/ZS-00_zlozeniowy_revJ.pdf` – rysunek złożeniowy ze spisem części (materiały, ilości, części znormalizowane, łożyska).
- `drawings/Helimac_revJ_rysunki_czesci.pdf` – rysunki wykonawcze: wymiary, tolerancje, obróbka cieplna, chropowatość.
- `drawings/MT_rysunki_montazowe_revJ.pdf` – kolejność montażu.
- `drawings/ECN-J01…`, `ECN-J03…` – karty zmian rev H → J → J2.
- `dxf/` – pliki do cięcia (materiał i ilość w nazwie): blachy silnika S01/S02 (NO20 0,20 mm, 280 + 280 szt., zamawiać 285 + 285), krzywki P01 (100Cr6), płyty i pierścienie (Al 7075-T651), podkładki (CuSn8), wkładka sprzęgła P11.
- Tylko w ZIP: `step/` – 41 modeli części i złożenie całego napędu.

### J2 – Łopaty rev J
- `Helimac_WL-01_lopaty_dokumentacja_revJ.pdf` – technologia: rdzenie, laminowanie węglem, wyważanie, nasada, kontrola.
- `01_RYSUNKI/` – rysunki W-00…W-05, łopata D i G; `03_DANE_CNC/` – przekroje (CSV), płytka W-07 (DXF); `04_ANALIZA/` – DY-02; `05_INTERFEJS_PIASTY/` – P07, N05, C03, C04.
- Tylko w ZIP: `02_STL_DO_DRUKU/` – rdzenie L00–L09, łoża J1, sprawdziany kąta J2, przyrząd wiercenia nasady J3.

### J3 – Rama, siedzisko, PK, kolektyw dolny rev J2
- `01_RYSUNKI/` – rysunki ramy, siedziska, kolektywu dolnego; karty ECN-J02, ECN-J03.
- Tylko w ZIP: `02_STEP/`, `03_STL_PK_DO_DRUKU/` (pierścień PK w 6 segmentach).
- ⚠️ **Układ ramy może się zmienić.** Trwa przeliczanie nowego układu (trójkąt jak w lotni z przodu i jedna noga z tyłu). Nie zamawiać jeszcze rur ramy; siedziska i kolektywu to nie dotyczy.

## Elektronika — [electronics/](electronics/)

### MC-P – falownik SiC rev D1
400 V DC, 6 × SiC C3M0016120K (1200 V, 16 mΩ), izolowane sterowniki bramek z zabezpieczeniem zwarciowym DESAT. Płytka 215 × 116 mm, 4 warstwy, miedź 2 oz.
- `kicad/` – projekt KiCad 7 (schemat, płytka, reguły z odstępami 400 V, własne footprinty).
- `fabrication/` – gerbery, BOM i pozycje (numery LCSC), opis produkcji i montażu `CZYTAJ_produkcja_i_montaz_revD1.txt`.
- `docs/` – schemat PDF, rysunek mechaniczny (radiator, klipsy), warstwy miedzi, model `MC-P.step`, raport DRC, obliczenia radiatora.
- Przed zasileniem: próba izolacji 1,5 kV DC (< 1 mA), pierwsze uruchomienie z zasilacza z ograniczeniem prądu.

## Sprawy otwarte
Nowy układ ramy; skok ogólny wirnika dolnego (do decyzji – wpływa na kolektyw dolny w J3); płytka sterująca MC-C; akumulator i BMS; linki do modeli Onshape.

## Licencja
Sprzęt: CERN-OHL-S-2.0 · dokumentacja: CC-BY-SA-4.0 · © Tomasz Maciąg i współtwórcy HELIMAC. Nazwa i logo HELIMAC poza licencjami ([branding/](../branding/)).
