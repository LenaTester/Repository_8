from pythonProject.Repository_7.proxy_pattern.proxy_txt_reader import TxtProxyReader
from pythonProject.Repository_7.proxy_pattern.txt_reader import TxtReader
from pythonProject.Repository_7.proxy_pattern.txt_writer import TxtWriter

txt_reader = TxtReader('users.txt')
proxy_reader = TxtProxyReader(txt_reader)
txt_writer = TxtWriter('users.txt')

print(proxy_reader.read_file())
print('\n')
print(proxy_reader.read_file())
print(txt_writer.write_file('Randy,Marsh,45,7000'))
