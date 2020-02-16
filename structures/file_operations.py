import gzip
import tarfile

if __name__ == '__main__':
    f = open('test.txt', 'w')
    f.write('Ala ma kota')
    f.close()

    try:
        f = open('test1.txt', 'x')
        f.write('kkkk')
    except FileExistsError:
        print('File exists')
    finally:
        f.close()
        f = open('test1.txt', 'r')  # It's only to print the file content. Normally we use rather line above.
        print(f.read())  # It's only to print the file content.

    f = open('test.txt', 'r')
    print(f.read())  # read all file

    f = open('test.txt', 'a')
    f.write(' A Ola ma psa')
    f.close()

    f = open('test.txt', 'r')
    print(f.read(4))  # read 4 bytes
    print(f.read(4))  # read 4 bytes
    print(f.tell())
    print(f.read())  # will read rest whole file starting after 8 bytes
    print('empty string: ',
          f.read())  # When the reading cursor is on the end the file another read operations return the empty string

    with open('test.txt', 'a') as f:
        f.write(' Dom jest biały')
        f.write(' Hotel jest niebeski')

    with open('test.txt', 'r') as f:
        print(f.read())

    with open('test.txt', 'a') as f:
        f.write(' Rower jest jego')

    with open('test.txt', 'r') as f:
        print(f.read())

    with open('test.txt', 'r') as f:
        f.seek(30)
        print(f.tell())
        print(f.read())
    print('************************************')
    with open('test.txt', 'w') as f:
        f.write('Dom jest biały\n')
        f.write('Hotel jest niebeski\n')
        f.write('Ala ma kota\n')
        f.write('Ola ma psa\n')
        f.write('Jemy sniadanie\n')

    with open('test.txt', 'r') as f:
        line = f.readline()
        print('first line :', line)
        while True:
            line = f.readline()
            if not line:
                break
            print(line, end='')

    with open('test.txt', 'r') as f:
        lines = f.readlines()
        print(lines)
        for line in lines:
            print(line)

    with open('test.txt', 'r') as f:
        for line in f:  # Use lazy iterator is preferred
            print(line, end='')
    print('gzip*************gzip**************gzip')
    with gzip.open('test.txt.gz', 'wt') as f:
        f.write('Dom jest biały\n')
        f.write('Hotel jest niebeski\n')
        f.write('Ala ma kota\n')
        f.write('Ola ma psa\n')
        f.write('Jemy sniadanie\n')

    with gzip.open('test.txt.gz', 'rt') as f:
        for line in f:
            print(line, end='')

    with tarfile.open('sample.tar', 'w') as tar:
        for name in ['foo.txt', 'bar.txt', 'guu.txt']:
            tar.add(name)

    with tarfile.open('sample.tar') as tar:
        tar.extractall('\ext')
