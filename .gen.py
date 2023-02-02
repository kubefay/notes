import os

# for one dir, the sub dir should 


os.remove('ReadMe.md')

result = []
for root, dirs, files in os.walk("."):
    # if root == '.git':
    #     continue
    if root.startswith('./.git') or root == '.':
        continue
    if not files:
        continue
    result.append(f'## {root[2:]}\n')

    for name in files:
        file_name = os.path.basename(name)
        file_name = file_name.strip()[:-3]
        
        # result.append(f'[{file_name}]({root[2:]}/{name})\n')
        result.append(f'''<a href="{root[2:]}/{name}">{file_name}</a>\n\n''')

with open ('ReadMe.md','w') as f:
    f.write('# Tech笔记\n')
    f.write(''.join(result))