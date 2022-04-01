packages = []
output_file = open('reqs.txt', 'w')
with open('requirements.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        package_only = line.split('==')[0]
        output_file.write(package_only + '\n')
output_file.close()

