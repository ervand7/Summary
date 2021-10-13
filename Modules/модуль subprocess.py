# основная статья: https://pyneng.readthedocs.io/ru/latest/book/12_useful_modules/subprocess.html
import subprocess

result = subprocess.run('ls')
print(result)
print('________________________________________')

print(type(result))
print('________________________________________')

print(result.returncode)
print('________________________________________')

result2 = subprocess.run(['ls', '-ls'])
print(result2)
print('________________________________________')

result3 = subprocess.run('ls -ls *py', shell=True)
print(result3)
print('________________________________________')

result4 = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'])
print(result4)
print('________________________________________')

result5 = subprocess.run(['ls', '-ls'], stdout=subprocess.PIPE)
print(result5.stdout.decode())
