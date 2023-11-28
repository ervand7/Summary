print('this will be printed while file <second> will run')
print(__name__)
res = 'This will NOT be printed while file <second> will run. ' \
      'This will be printed ONLY if this file (<first>) will run.'
if __name__ == '__main__':
    print(res)
