# Calculations

`helimac_calc.py` — early estimate of hover power and flight time (momentum theory).

```bash
python3 calc/helimac_calc.py --mtom 225 --d 4.5 --bat-kwh 8.06 --sweep
pytest -q calc/tests
```

Defaults = HELIMAC rev J2 (coaxial, no tail rotor: `--tail 0`). Results are rough estimates only — see comments in the code.
