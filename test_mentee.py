from mentee import Mentee

def test_import_Mentee():
    "Class Mentee can be imported"
    from mentee import Mentee


test_csv = "test_list.csv"
users = Mentee(test_csv)


class TestMentee():
    
    def test_initial_value(self):
        """Testing of __init__ method"""
        assert users.num_of_mentees == 5
        assert users.languages == {'English', 'Romanian'}
        assert users.full_names[0] == 'Lacy Keefe'
        assert users.full_names[1] == 'Luisa Nagy'
        assert users.full_names[3] != 'Aileen Olvera'
        assert users.full_names[4] == 'Aileen Olvera'


    # def test_get_average(self):
    #     "Return an average length of metees full names"
    #     mt = Mentee()
    #     assert mt.get_average(test_names) == 11

    # def test_get_longest(self):
    #     "Return a longest full name"
    #     mt = Mentee()
    #     assert mt.get_longest(test_names) == (15, ['Kristina Pfeifer'])

    # def test_get_shortest(self):
    #     mt = Mentee()
    #     assert mt.get_shortest(test_names) == (9, ['Lacy Keefe', 'Luisa Nagy'])
