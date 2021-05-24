from datetime import date


class Contact:
    def __init__(self, id, first_name, last_name, birth_date, profession):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.profession = profession

    def get_information(self):
        list_name = [self.first_name, self.last_name]
        full_name = ' '.join(list_name)
        print(f'ID - {self.id}\n'
              f'Full name - {full_name}\n'
              f'Birth Date - {self.birth_date}\n'
              f'Profession - {self.profession}')


c = Contact(id=1,
            first_name='John',
            last_name='Dow',
            birth_date=date(day=21, month=4, year=1996),
            profession='Python developer')
c.get_information()
