# Calculations

`helimac_calc.py` — early estimate of hover power and flight time (momentum theory).

```bash
python3 calc/helimac_calc.py --mtom 300 --d 6.5 --bat-kwh 16 --sweep
pytest -q calc/tests
```

Results are rough estimates only — see comments in the code.
