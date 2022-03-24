# password-generator
Simple Password Generator:
A random password generator is software program or hardware device that takes input from a random or pseudo-random number generator and automatically generates a password.

## Help
- -c, --count, Count for password loop method ( Optional )
- -l, --length, Length for password ( Optional )
- -t, --type, Type for password ( Optional ) [ All / Lower / Upper / Numbers / Symbols ]
- -hp, --hashpassword, Hashed password ( Optional ) [ True / Flase ]

## Example
```python
python password-generator.py -c 10 -l 64
python password-generator.py -l 64 -t lower
python password-generator.py -l 64 -hp true
```
