# 🚁 Helimac

**Jednoosobowy śmigłowiec elektryczny — projekt open source**
*Single-seat electric helicopter — open-source hardware project* ([English summary below](#english-summary))

> ⚠️ **Projekt w fazie koncepcyjnej.** Nic w tym repozytorium nie jest jeszcze zweryfikowaną, gotową do budowy konstrukcją. Przed czymkolwiek przeczytaj [SAFETY.md](SAFETY.md).

---

## Cel projektu

Zaprojektować — otwarcie i wspólnie — lekki, jednoosobowy śmigłowiec z napędem w pełni elektrycznym, który:

- ma szansę mieścić się w kategorii statków powietrznych z **Aneksu I rozporządzenia (UE) 2018/1139** (jednomiejscowy śmigłowiec, MTOM ≤ 300 kg), czyli podlega przepisom krajowym, a nie certyfikacji EASA — szczegóły w [docs/przepisy.md](docs/przepisy.md),
- da się zbudować w dobrze wyposażonym warsztacie z dostępnych komponentów,
- ma **w pełni jawną dokumentację**: rysunki, obliczenia, oprogramowanie, wyniki testów i błędy.

## Parametry

Parametry konstrukcji będą uzupełniane w miarę postępu prac — aktualny stan zawsze w [docs/parametry.md](docs/parametry.md), a przebieg prac w [DZIENNIK.md](DZIENNIK.md).

Do wstępnych szacunków (moc w zawisie, czas lotu, średnica wirnika) służy [kalkulator osiągów](calc/).

## Struktura repozytorium

```
helimac/
├── DZIENNIK.md           dziennik budowy – bieżące postępy
├── docs/                 dokumentacja: parametry, przepisy, decyzje (ADR)
├── calc/                 obliczenia i narzędzia (Python) + testy
├── hardware/             konstrukcja mechaniczna (CAD, rysunki, BOM)
│   ├── rama/  wirnik-glowny/  wirnik-ogonowy/  przekladnia/  podwozie/
├── electronics/          napęd, bateria + BMS, awionika
├── firmware/             oprogramowanie (monitoring, wskaźniki, logowanie)
├── LICENSES/             pełne teksty licencji
└── .github/              szablony zgłoszeń, dyskusji, CI
```

## Jak dołączyć

1. **Przywitaj się** w zakładce [Discussions → Przedstaw się](../../discussions).
2. **Przeczytaj** [CONTRIBUTING.md](CONTRIBUTING.md) i [SAFETY.md](SAFETY.md).
3. **Wybierz zadanie** z [Issues](../../issues) z etykietą `dobry-pierwszy-krok` albo zaproponuj własne.
4. **Szukamy szczególnie:** konstruktorów lotniczych, specjalistów od wirników i dynamiki lotu, elektroników mocy, specjalistów od baterii, pilotów śmigłowcowych, mechaników lotniczych, osób znających polskie przepisy (ULC).

## Komunikacja

| Kanał | Do czego |
|---|---|
| **Discussions** | pomysły, pytania, dyskusje techniczne, przedstawienie się |
| **Issues** | konkretne zadania, błędy w obliczeniach/dokumentacji, propozycje zmian |
| **Pull Requests** | wkład w pliki projektu |
| **Releases** | paczki plików do pobrania (rysunki, PDF, BOM) dla każdej wersji |

## Plan

Zobacz [ROADMAP.md](ROADMAP.md) — etapy będą odhaczane i uzupełniane na bieżąco.

## Licencje

| Co | Licencja |
|---|---|
| Sprzęt (CAD, rysunki, schematy, BOM) | [CERN-OHL-S-2.0](LICENSES/CERN-OHL-S-2.0.txt) |
| Oprogramowanie (`calc/`, `firmware/`) | [GPL-3.0-or-later](LICENSES/GPL-3.0-or-later.txt) |
| Dokumentacja (`docs/`, pliki .md) | [CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt) |

Szczegóły w [LICENSE](LICENSE). Projekt dostarczany jest **bez jakiejkolwiek gwarancji**.

---

## English summary

Helimac is an open-source effort to design and build a **single-seat, fully electric light helicopter**. Files and specs are published progressively as the build advances. It is at the **concept stage**. Working language is Polish, but English contributions in Issues and Discussions are very welcome. Hardware: CERN-OHL-S-2.0, software: GPL-3.0-or-later, docs: CC-BY-SA-4.0. Please read [SAFETY.md](SAFETY.md) first.
