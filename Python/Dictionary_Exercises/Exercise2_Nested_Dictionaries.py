# Functional Spec's:
# 1. Write a Python expression that gets the email address of Ramit.
# 2. Write a Python expression that gets the first of Ramit's interest.
# 3. Write a Python expression that gets the email address of Jasmine.
# 4. Write a Python expression that gets the second of Jan's two interests.

# Imports

# Functions

# Main

if __name__ == "__main__":

    ramit = {
            'name': 'Ramit',
            'email': 'ramit@gmail.com',
            'interests': ['movies', 'tennis'],
            'friends': [{
                'name': 'Jasmine',
                'email': 'jasmine@yahoo.com',
                'interests': ['photography', 'tennis']
            },
            {
                'name': 'Jan',
                'email': 'jan@hotmail.com',
                'interests': ['movies', 'tv']
            }]
    }

    # Satisfy Functional Spec #1
    ramit_email = ramit['email']
    print(ramit_email)

    # Satisfy Functional Spec #2
    ramit_interest1 = ramit['interests'][0]
    print(ramit_interest1)

    # Satisfy Functional Spec #3
    jasmines_email = ramit['friends'][0]['email']
    print(jasmines_email)

    # Satisfy Functional Spec #4
    jans_2nd_interest = ramit['friends'][1]['interests'][1]
    print(jans_2nd_interest)
