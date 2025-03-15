# dictionary = A changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing,allow us to access a value quickly

capitals ={'USA':'Washington DC',
           'Nepal':'Kathmandu',
           'India':'Delhi',
           'China':'Beijing',
           'Russia':'Moscow'
           }
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
#capitals.clear()

#print(capitals['Nepal'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for x in capitals:
 #   print(x)
for key, value in capitals.items():
    print(key, value)
