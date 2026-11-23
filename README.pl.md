<p align="center">
  <a href="https://helimac.pl/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="website/assets/img/logo-dark-600.webp">
      <img src="website/assets/img/logo-600.png" alt="HELIMAC" width="420">
    </picture>
  </a>
</p>

<p align="center"><b>Jednoosobowy śmigłowiec elektryczny — projekt open source</b><br>
wirniki współosiowe · sterowanie balansem ciała · napęd elektryczny 400 V · budowany otwarcie</p>

<p align="center">
  <a href="README.md">🇬🇧 English</a> · 🇵🇱 Polski · 🌐 <a href="https://helimac.pl/">helimac.pl</a> · ▶️ <a href="https://www.youtube.com/@Helimac-pl">YouTube</a> · ☕ <a href="https://buycoffee.to/helimac">Wesprzyj</a>
</p>

> **Aktualna konstrukcja: rev K — w projektowaniu (koncepcja, etap 2, 23.11.2026).** Maszynę przeliczono od zera, żeby zmniejszyć masę z 74,9 do ok. 43,7 kg. Pliki w [`production/`](production/README.pl.md) to **rev J2 — wersja archiwalna, nie budować** (wyjątek: falownik MC-P rev D1 jest aktualny). Paczki produkcyjne rev K pojawią się po etapie 3 (model CAD i rysunki).

---

## Od czego zacząć

| Chcę… | Przejdź do |
|---|---|
| 👀 **zobaczyć konstrukcję** | [Konstrukcja rev K](docs/design-rev-K.md) (EN) · [grafiki](docs/graphics/revK/) · [szkic układu](docs/graphics/HELIMAC_revK_szkic_ukladu.pdf) · [parametry](docs/parameters.md) (EN) · [strona](https://helimac.pl/) |
| 📦 **pobrać pliki** | rev K: [obliczenia](calc/revK/) · rev J2 (archiwalna): [wydanie](../../releases/latest), [pliki produkcyjne](production/README.pl.md) · falownik MC-P rev D1 (aktualny): [pliki](production/electronics/MC-P-inverter-revD1/) |
| 🛠️ **pomóc w budowie** | [Otwarte zadania (Issues)](../../issues) · [Discussions](../../discussions) · [Jak współtworzyć](CONTRIBUTING.md) |
| ▶️ **śledzić budowę** | [YouTube @Helimac-pl](https://www.youtube.com/@Helimac-pl) · [dziennik budowy](BUILD_LOG.md) · [plan prac](ROADMAP.md) |
| ☕ **wesprzeć projekt** | [buycoffee.to/helimac](https://buycoffee.to/helimac) — każda kawa to wkład w części i próby na hamowni |

> ⚠️ **Prototyp w fazie projektu — nie jest to dopuszczony statek powietrzny.** Wszystkie wartości są obliczone, jeszcze nie zmierzone. Przed budową przeczytaj [SAFETY.pl.md](SAFETY.pl.md).

<p align="center">
  <a href="docs/graphics/revK/"><img src="docs/graphics/revK/helimac_K01_maszyna.webp" alt="HELIMAC rev K — cała maszyna, model koncepcyjny" width="720"></a><br>
  <sub>HELIMAC rev K — cała maszyna (model koncepcyjny): wirniki współosiowe Ø 4,5 m, przekładnia pasowa 16:1 nad głową pilota, rama z trzech rur aluminiowych · <a href="docs/graphics/HELIMAC_revK_szkic_ukladu.pdf">szkic układu z wymiarami</a> · <a href="docs/graphics/revK/">wszystkie grafiki rev K</a></sub>
</p>

## Czym jest HELIMAC?

Lekki, jednoosobowy śmigłowiec z napędem w pełni elektrycznym, projektowany otwarcie razem z ludźmi z całego świata. Publikujemy wszystko: rysunki, obliczenia, oprogramowanie, wyniki prób — i błędy.

Nazwa łączy słowa **HELI**kopter i **MAC**iąg — nazwisko założyciela, **Tomasza Maciąga** z Bydgoszczy. To nawiązanie do jego pierwszego projektu **HeliMac** (2013–2015), dziś zaprojektowanego od nowa z pomocą narzędzi AI. **[Przeczytaj historię →](ABOUT.pl.md)**

Docelowa kategoria: jednomiejscowy śmigłowiec ultralekki, MTOM ≤ 300 kg ([Aneks I do rozporządzenia (UE) 2018/1139](docs/regulations.md) — przepisy krajowe zamiast certyfikacji EASA).

## Aktualna konstrukcja — rev K (w projektowaniu)

| | |
|---|---|
| Układ | współosiowy, 2 wirniki dwułopatowe Ø 4,5 m, 500 obr/min, bez wirnika ogonowego |
| Sterowanie | kierunek – balans ciała pilota (bez skoku cyklicznego) · skok ogólny – siłowniki elektryczne · kurs – różnica skoku wirnika górnego i dolnego |
| Pilot | do 110 kg |
| Masa startowa | ok. 194 kg (maszyna bez akumulatora ok. 43,7 kg, akumulator 40 kg) |
| Moc zawisu | 17,3 kW (1,3 g w upalny dzień: 26 kW) |
| Napęd | silnik PMSM z wirnikiem zewnętrznym, 8000 obr/min, ok. 7 kg → **przekładnia pasowa 16:1** (pasy zębate z włóknem węglowym, koła z 10 szprychami, bez oleju) → wały współosiowe |
| Łopaty | rdzeń z pianki PMI, dźwigar i pokrycie z włókna węglowego, ok. 2,2 kg |
| Rama | trzy rury Al 7075-T6: dwie nogi przednie (trójkąt) + jedna wygięta tylna z siodełkiem, podnóżkiem i akumulatorem |
| Elektronika | własny falownik SiC **MC-P** rev D1 (KiCad) · płytka sterująca **MC-C** w projekcie |
| Akumulator | 112S4P Li-ion, ≈ 400 V, ok. 8 kWh, 40 kg |
| Czas lotu (obliczony) | ok. 20 min zawis / ok. 26 min lot mieszany |
| **Obecny etap** | **rev K, etap 3 — model CAD i rysunki**, potem paczki produkcyjne i hamownia |

Poprzednia wersja: [rev J2](docs/design-rev-J2.md) (archiwalna) — 74,9 kg bez akumulatora, przekładnia cykloidalna i stożkowa.

## Co gdzie jest

| Folder | Zawartość |
|---|---|
| [production/](production/README.pl.md) | pliki produkcyjne — **rev J2 archiwalna** (J1, J2, J3: nie budować) i **falownik MC-P rev D1 (aktualny)** |
| [hardware/](hardware/) | opisy zespołów z grafikami CAD: rama, siedzisko, głowica i sterowanie, łopaty, przekładnia, silnik |
| [electronics/](electronics/) | falownik MC-P, sterownik MC-C, akumulator + BMS, awionika |
| [docs/](docs/) | [konstrukcja rev K](docs/design-rev-K.md), [rev J2 (archiwalna)](docs/design-rev-J2.md), parametry, przepisy, [grafiki (PDF)](docs/graphics/) |
| [calc/](calc/) | kalkulator osiągów i [obliczenia projektowe rev K](calc/revK/) (Python) |
| [firmware/](firmware/) | oprogramowanie (w przyszłości) |

## Jak dołączyć

Szukamy szczególnie: konstruktorów lotniczych, specjalistów od wirników i dynamiki lotu, energoelektroników i specjalistów od akumulatorów, pilotów śmigłowcowych, mechaników lotniczych, majsterkowiczów z drukarkami 3D i CNC oraz osób znających przepisy dla lekkich statków powietrznych.

1. **Przywitaj się** w [Discussions](../../discussions).
2. **Wybierz zadanie** z [Issues](../../issues) — np. [#1 przegląd falownika 400 V](../../issues/1) albo [#6 kalkulator](../../issues/6) (dobre na start).
3. **Przeczytaj** [CONTRIBUTING.md](CONTRIBUTING.md) i [SAFETY.pl.md](SAFETY.pl.md).

Głównym językiem projektu jest angielski, ale po polsku piszemy równie chętnie.

## Licencje

Sprzęt: [CERN-OHL-S-2.0](LICENSES/CERN-OHL-S-2.0.txt) · Oprogramowanie: [GPL-3.0-or-later](LICENSES/GPL-3.0-or-later.txt) · Dokumentacja: [CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt) · Nazwa i logo HELIMAC nie są objęte tymi licencjami ([branding/](branding/)). Bez jakiejkolwiek gwarancji — patrz [LICENSE](LICENSE).

---

**Założyciel i opiekun projektu:** Tomasz Maciąg · Bydgoszcz, Polska · [helimac.pl](https://helimac.pl/)
