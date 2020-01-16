# # Przykład 1.
# handle = open('tmp/random_data.txt', 'w', encoding='utf-8')
# handle.write('success\nand\nnew\nlines')
# handle.close()
# handle = open('tmp/random_data.txt')  # Może spowodować zgłoszenie wyjątku IOError.
# try:
#     data = handle.read()  # Może spowodować zgłoszenie wyjątku UnicodeDecodeError.
# finally:
#     handle.close()        # Zawsze wykonywane po bloku try.

# Przykład 2.
import json

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # Może spowodować zgłoszenie wyjątku ValueError.
        print(result_dict)
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]         # Może spowodować zgłoszenie wyjątku KeyError.

# Dekodowanie JSON zakończone powodzeniem.
assert load_json_key('{"foo": "bar"}', 'foo') == 'bar'
try:
    load_json_key('{"foo": "bar"}', 'foo1') # use 'foo' or 'foo1' to testing
    print('assert error')
    assert False
except KeyError: # using an exception such as ValueError will cause the program to crash.
    print('bad key')
    # pass

# Dekodowanie JSON zakończone niepowodzeniem.
try:
    load_json_key('{"foo": bad value"}', 'foo') # add ->"<- before the bad value to testing
    print('assert2 error')
    assert False
except KeyError:
   print('value error')
