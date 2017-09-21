class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def __str__(self):
        return 'This is the {oname} object'.format(oname=self.name)

    def greet(self, other_person):
        print ('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

    def print_contact_info(self):
        print('{pname}\'s email: {pemail}, {pname}\'s phone number: {pphone}'.format
        (pname = self.name, pemail = self.email, pphone = self.phone))

    def add_friend(self, friend):
        self.friends.append(friend)
        for afriend in self.friends:
            print(afriend.name)

    def get_num_friends(self):
        nfriends = len(self.friends)
        return nfriends


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_contact_info()

jordan.friends.append(sonny)
print(len(jordan.friends))

jordan.add_friend(sonny)
nfriends = jordan.get_num_friends()
print(nfriends)

print('Sonny\'s greeting count is {count}.'.format(count=sonny.greeting_count))
sonny.greet(jordan)
print('Sonny\'s greeting count is {count}.'.format(count=sonny.greeting_count))
sonny.greet(jordan)
print('Sonny\'s greeting count is {count}.'.format(count=sonny.greeting_count))
sonny.greet(jordan)
print('Sonny\'s greeting count is {count}.'.format(count=sonny.greeting_count))

objectname = str(sonny)
print(objectname)
objectname = str(jordan)
print(objectname)
