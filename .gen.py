import os

# for one dir, the sub dir should 

'''
[this subtext](subpro/subtext.md)
'''

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
        file_name = file_name.split('.')[1].strip()
        
        # result.append(f'[{file_name}]({root[2:]}/{name})\n')
        result.append(f'''<a href="{root[2:]}/{name}">{file_name}</a>\n''')

print(''.join(result))