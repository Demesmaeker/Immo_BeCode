import re
import Data

a = 0
b = 1

list_function = [ "a = 10", "b = 10"]

for i in list_function:
    exec(i)

print(a)
print(b)

rend = "maison.available_date = df[\"Available date\"]", "maison.property_name = df[\"Property name\"]"

patern = "(maison\.)(\w*)"
for i in rend:

    print(re.search(i,patern))

def get_str_from_req_content(pattern, fct_content):
    """
    Get str from getFilestring_from_an exiting request url
    """
    if not pattern:
        return None

    print(str(pattern))

    prog = re.compile(pattern)
    fstr = prog.search(str(fct_content))

    return fstr



url = "https://www.immoweb.be/fr/annonce/villa/a-vendre/uccle/1180/8892317"

clean_content = rend

regex = "(maison\.)(\w*)"

result = get_str_from_req_content(regex, clean_content)

detail = get_str_from_req_content(regex, i).group(2)

maison = Data.estate()

print("maison." + detail)

truc = "maison." + detail
print(truc)
tric = truc + " == \"Not found\""
print(tric)
print(bool(exec(tric)))

if maison.energy_class != "Not found":
    print("ah bin mince")
else:
    print("new")

print(str(result))
print('str(result.group(1))' )
print(str(result.group(1)) )
print('str(result.group(2))' )
print(str(result.group(2)) )