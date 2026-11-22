# 🚁 HELIMAC

**Jednoosobowy śmigłowiec elektryczny — projekt open source**

[🇬🇧 English](README.md) · 🇵🇱 Polski

> ⚠️ **Wczesna faza koncepcyjna.** Nic w tym repozytorium nie jest jeszcze zweryfikowaną, gotową do budowy konstrukcją. Przed czymkolwiek przeczytaj [SAFETY.pl.md](SAFETY.pl.md).

---

## O projekcie

**HELIMAC** to międzynarodowy projekt open source, którego celem jest zaprojektowanie i zbudowanie lekkiego, jednoosobowego śmigłowca z napędem w pełni elektrycznym.

Nazwa łączy słowa **HELI**kopter i **MAC**iąg — nazwisko założyciela projektu, **Tomasza Maciąga** z Bydgoszczy. To nawiązanie do jego pierwszego projektu **HeliMac** (2013–2015), dziś zaprojektowanego od nowa z pomocą narzędzi AI. **[Przeczytaj historię →](ABOUT.pl.md)**

### Cele

- Zaprojektować jednoosobowy śmigłowiec elektryczny otwarcie, razem z osobami z całego świata.
- Zmieścić się w kategorii lekkich statków powietrznych z **Aneksu I rozporządzenia (UE) 2018/1139** (jednomiejscowy śmigłowiec, MTOM ≤ 300 kg), która podlega przepisom krajowym, a nie certyfikacji EASA — patrz [docs/regulations.md](docs/regulations.md).
- Korzystać z części i technologii dostępnych w dobrze wyposażonym warsztacie.
- Publikować wszystko: rysunki, obliczenia, oprogramowanie, wyniki testów — i błędy.

## Aktualna konstrukcja — rev J2

| | |
|---|---|
| Układ | współosiowy, 2 wirniki Ø 4,5 m, 500 obr/min |
| Pilot | do 110 kg |
| Masa startowa | 225,2 kg (maszyna 74,9 kg, bateria 40,3 kg) |
| Moc zawisu | 20,7 kW |
| Napęd | silnik promieniowy → przekładnia cykloidalna; własny falownik SiC MC-P |
| Bateria | 112S, ≈ 400 V |
| Obecny etap | **Etap 1 — napęd + zasilanie** (hamownia) |

Szczegóły (EN): [docs/design-rev-J2.md](docs/design-rev-J2.md).

## Aktualny stan

Pliki i parametry są publikowane **stopniowo, w miarę postępu projektu i budowy maszyny**.

- Postępy: [BUILD_LOG.md](BUILD_LOG.md)
- Aktualne parametry: [docs/parameters.md](docs/parameters.md)
- Plan prac: [ROADMAP.md](ROADMAP.md)
- Kalkulator wstępnych szacunków: [calc/](calc/)

## Jak dołączyć

1. **Przywitaj się** w [Discussions → Introductions](../../discussions).
2. **Przeczytaj** [CONTRIBUTING.md](CONTRIBUTING.md) i [SAFETY.pl.md](SAFETY.pl.md).
3. **Wybierz zadanie** z [Issues](../../issues) albo zaproponuj własne.

**Języki:** głównym językiem projektu jest angielski, ale po polsku piszemy równie chętnie.

## Licencje

Sprzęt: CERN-OHL-S-2.0 · Oprogramowanie: GPL-3.0-or-later · Dokumentacja: CC-BY-SA-4.0. Szczegóły w [LICENSE](LICENSE). Bez jakiejkolwiek gwarancji.

---

**Założyciel i opiekun projektu:** Tomasz Maciąg · Bydgoszcz, Polska
