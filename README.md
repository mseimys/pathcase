# Guess path case in Linux

In Linux your paths are case sensitive, if you have Windows users who deal with case insensitive paths you might have a problem. While communicating with Windows users and handling their file requests you need to be able to "guess" which case is the correct one. This is a simple Python function to deal with such cases.

Sample usage:
```
>>> from pathcase import guess_path_case
>>> guess_path_case('/TMP')
'/tmp'
>>> guess_path_case('/var/Log/DMESG')
'/var/log/dmesg'
>>> guess_path_case('/VAR/log/non-Existing/CaSe')
'/var/log/non-Existing/CaSe'
```
