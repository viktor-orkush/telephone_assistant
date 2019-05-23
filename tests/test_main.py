import pytest

import main_app

numbers = [380673406767, 180673406767, 380673406767, 380673406767, 380675156060, 380675156262, 380675156264,
               380675156265, 380675156266, 380675156267, 380675156268, 380675156269, 38067515626212, 38067515626213,
               38067515626214, 38067515626215, 38067515626217]

class Tests:
    def test_check_string_value(self):
        assert main_app.check_telephones('qwe', numbers) == []

    def test_check_max_matches(self):
        assert main_app.check_telephones(380, numbers) == [380673406767, 380673406767, 380673406767, 380675156060, 380675156262, 380675156264,
               380675156265, 380675156266, 380675156267, 380675156268]

    def test_check_one_full_matches(self):
        assert main_app.check_telephones(1, numbers) == [180673406767]

    def test_check_one_matches(self):
        assert main_app.check_telephones(38067515626213, numbers) == [38067515626213]

    def test_check_null_matches(self):
        assert main_app.check_telephones('', numbers) == []