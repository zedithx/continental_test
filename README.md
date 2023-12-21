## Setup
```bash
pip install -r requirements.txt
```

## Information
CSV files can be found in 'csvgeneration/files' <br />
Command handler can be found under 'csvgeneration/management/commands' <br />
Functions that are referenced from the command handler are found in 'csvgeneration/functions' <br />
Files output will be in the root directory at the continental_test level

## How to run the commands

To generate vehicular_data.csv:
```bash
python manage.py csv_command -b [insert absolute filepath here]
```
To generate mag_high.csv:
```bash
python manage.py csv_command -u [insert absolute filepath here]
```
To generate mag_low.csv:
```bash
python manage.py csv_command -l [insert absolute filepath here]
```
## Example
```bash
python manage.py csv_command -b /Users/abc/continental_test/vehicular_data.csv
```