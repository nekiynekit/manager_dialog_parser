from scripts.company import extract_companies
from scripts.firewell import mark_firewells
from scripts.greeting import mark_greetings
from scripts.introduce import mark_introduces
from scripts.naming import extract_names

import pandas as pd
import click


@click.command()
@click.option('--fread', default='test_data.csv', help='Name of CSV-file for parsing')
@click.option('--frite', default='updated_dat.csv', help='Result will be saved in file with this name')
def mark_csv_file(fread, frite):
    data = pd.read_csv(fread)
    dialog_text = data['text']
    
    greetings = [item & (role == 'manager') for item, role in zip(mark_greetings(dialog_text), data['role'])]
    firewells = [item & (role == 'manager') for item, role in zip(mark_firewells(dialog_text), data['role'])]
    introduces = [item & (role == 'manager') for item, role in zip(mark_introduces(dialog_text), data['role'])]
    data['greeting'] = greetings
    data['firewell'] = firewells
    data['introduce'] = introduces

    last = len(data) - 1
    greet = [False for _ in range(data['dlg_id'][last] + 1)]
    byes = [False for _ in range(data['dlg_id'][last] + 1)]
    for dlg_idx, greet_, role in zip(data['dlg_id'], greetings, data['role']):
        if greet_ and role == 'manager':
            greet[dlg_idx] = True
    for dlg_idx, greet_, role in zip(data['dlg_id'], firewells, data['role']):
        if greet_ and role == 'manager':
            byes[dlg_idx] = True
    hi_and_bye = [greet[data['dlg_id'][idx]] & byes[data['dlg_id'][idx]] \
        for idx in range(len(data))]
    data['hi_and_bye'] = hi_and_bye

    intros = [data['text'][idx] for idx, intro in enumerate(introduces) if intro]
    indicies = [idx for idx, intro in enumerate(introduces) if intro]
    names = extract_names(intros)
    companies = extract_companies(intros)
    names_column = [None for _ in range(len(data))]
    companies_column = [None for _ in range(len(data))]
    for idx, company, name in zip(indicies, companies, names):
        companies_column[idx] = company
        names_column[idx] = name
    data['company_name'] = companies_column
    data['manager_name'] = names_column

    data.to_csv(frite)
    
if __name__ == '__main__':
    mark_csv_file()