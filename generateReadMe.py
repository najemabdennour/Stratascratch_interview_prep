"""
| # | Title | Solution | Difficulty | 
|---| ----- | -------- | ---------- |
|1|[Salaries Differences](https://platform.stratascratch.com/coding/10308-salaries-differences?python=)| [MySQL](./salariesDifferences.sql)|Easy|
"""

print('| # | Title | Solution | Difficulty | ')
print('|---| ----- | -------- | ---------- |')

from os import listdir

index = 1

fileNames=[f for f in listdir('.') if f.endswith('.sql')]
write_file=open("README.md", "w")
write_file.write('| # | Title | Solution | Difficulty | ')
write_file.write('\n')
write_file.write('|---| ----- | -------- | ---------- |')
write_file.write('\n')

for filename in fileNames:
    with open(filename,'r') as f:
        
        title = f.readline().split('--TITLE: ')[1].strip()
        link = f.readline().split('--LINK: ')[1].strip()
        
        print(f'|{index}|[{title}]({link})|[MySQL](./{filename})|Easy|')
        write_file.writelines(f'|{index}|[{title}]({link})|[MySQL](./{filename})|Easy|')        
        write_file.write('\n')
        index += 1