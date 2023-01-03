"""
| # | ID | Title | SQL Solution | Python Solution | Difficulty | 
|---|----| ----- | ------------ | --------------- | ---------- |
|1|[Salaries Differences](https://platform.stratascratch.com/coding/10308-salaries-differences?python=)| [MySQL](./salariesDifferences.sql)| [Python(Pandas)](./salariesDifferences.py)|Easy|
"""

import os
index = 1

write_file=open("README.md", "w")
write_file.write('<style type="text/css">body{font-size: 10pt;}</style> ')
write_file.write('\n')
write_file.write('| # | ID | Title | SQL Solution | Python Solution | Difficulty | ')
write_file.write('\n')
write_file.write('|---|----| ----- | ------------ | --------------- | ---------- |')
write_file.write('\n')

for dir in os.listdir('.'):
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            if file.endswith('SQL'):
                sql_file = file.strip()
            elif file.endswith('.py'):
                python_file = file.strip()
        if dir not in ["unfinished",".git"]:
            file_path = os.path.join(dir,'question.md')
            with open(file_path,'r') as f:
                title = f.readline().split('# ')[1].strip()
                link = f.read().split("]")[1].strip().strip('()')
                diffuculty = dir.split('-')[1]
                question_id = dir.split('-')[0].strip()
                try:
                    write_file.writelines(f'|{index}|{question_id}|[{title}]({link})|[MySQL]({dir}/{sql_file})|[Python(pandas)]({dir}/{python_file})|{diffuculty}|')        
                    write_file.write('\n')
                    index += 1
                except NameError:
                    print("Not finished No SQL or python file")
