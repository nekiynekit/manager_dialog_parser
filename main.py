from scripts.firewell import mark_firewells
from scripts.greeting import mark_greetings
from scripts.introduce import mark_introduces

import pandas as pd
import click


@click.command()
@click.option('--fname', default='test_data.csv', help='Name of CSV-file for parsing')
def mark_csv_file(fname):
    data = pd.read_csv(fname)
    manager_phases = [text for text, role in zip(data['text'], data['role']) if role == 'manager']
    greetings = mark_greetings(manager_phases)
    introduces = mark_introduces(manager_phases)
    firewells = mark_firewells(manager_phases)
    print(('-' * 20) + 'Greetings' + ('-' * 20))
    for text, label in zip(manager_phases, greetings):
        if label:
            print(text)
    print(('-' * 20) + 'Introduces' + ('-' * 20))
    for text, label in zip(manager_phases, introduces):
        if label:
            print(text)
    print(('-' * 20) + 'Firewells' + ('-' * 20))
    for text, label in zip(manager_phases, firewells):
        if label:
            print(text)
    
if __name__ == '__main__':
    mark_csv_file()