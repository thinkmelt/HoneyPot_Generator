import random
import openpyxl
from openpyxl import Workbook

class honeypot_generator():
    def __init__(self):
        self.fname_file = 'first-names.txt'
        self.mname_file = 'middle-names.txt'
        self.lname_file = 'names.txt'
        self.cstate_file = 'us_cities_states_counties.csv'
        self.output_dir = 'zip'

        self.fname_obj = open(self.fname_file, 'r')
        self.fnames = self.fname_obj.read().split('\n')
        self.fname_count = len(self.fnames)

        self.mname_obj = open(self.mname_file, 'r')
        self.mnames = self.mname_obj.read().split('\n')
        self.mname_count = len(self.mnames)

        self.lname_obj = open(self.lname_file, 'r')
        self.lnames = self.lname_obj.read().split('\n')
        self.lname_count = len(self.lnames)

        self.cstate_list = []
        self.cityState_obj = open(self.cstate_file, 'r')
        self.cityStates = self.cityState_obj.read().split('\n')
        for item in self.cityStates[1:]:
            split_list = item.split('|')
            self.cstate_list.append(split_list)

        self.cstat_count = len(self.cstate_list)
    def gen_rand_maleName(self):
        offset = random.randrange(0, self.mname_count-1)
        return self.mnames[offset]
    def gen_rand_femaleName(self):
        offset = random.randrange(0, self.fname_count-1)
        return self.fnames[offset]
    def gen_rand_lastName(self):
        offset = random.randrange(0, self.lname_count-1)
        return self.lnames[offset]
    def gen_rand_fullMaleName(self):
        lastName = self.gen_rand_lastName()
        firstName = self.gen_rand_maleName()
        return f"{lastName}, {firstName}"
    def gen_rand_fullFemaleName(self):
        lastName = self.gen_rand_lastName()
        firstName = self.gen_rand_femaleName()
        return f"{lastName}, {firstName}"
    def gen_rand_Number(self, size):
        if size <= 9:
            return random.randint(1,9)
        if size <= 99:
            return random.randint(1, 99)
        if size <= 999:
            return random.randint(1, 999)
        if size <= 9999:
            return random.randint(1, 9999)
    def gen_rand_series(self, series):
        returnset = []
        for set in series:
            returnset.append(self.gen_rand_Number(set))

        a = random.randint(0, 9)
        if a == 0:
            returnset.append("St")
        if a == 1:
            returnset.append("Street")
        if a == 2:
            returnset.append("St.")
        if a == 3:
            returnset.append("Cl")
        if a == 4:
            returnset.append("Close")
        if a == 5:
            returnset.append("Av")
        if a == 6:
            returnset.append("Ave.")
        if a == 7:
            returnset.append("Avenue")
        if a == 8:
            returnset.append("Way")
        if a == 9:
            returnset.append("Wy")
        return returnset
    def gen_rand_streetAddress(self):
        pos = random.randint(0, 30)
        if 0 <= pos < 3:
            return self.gen_rand_series([9, 99])
        if 4 <= pos <= 9:
            return self.gen_rand_series([99])
        if 10 <= pos <= 15:
            return self.gen_rand_series([9, 999])
        if 16 <= pos <= 22:
            return self.gen_rand_series([9999])
        if pos > 22:
            return self.gen_rand_series([99,99])
    def gen_random_Suite(self):
        pos = random.randint(1,99)
        suite_type = ""
        ptype = random.randint(0, 99)
        if 0 <= ptype <= 33:
            suite_type = "Suite"
        if 34 <= ptype <= 66:
            suite_type = "Apt"
        if 67 <= ptype <= 99:
            suite_type = "Apt."
        return f"{suite_type} {pos},"
    def gen_rand_USAddress(self):
        fake_addr = ""
        while fake_addr == "":
            pos = random.randrange(self.cstat_count)
            ref_addr = self.cstate_list[pos]
            ref_pos = self.gen_rand_streetAddress()
            suite_type = self.gen_random_Suite()
            if ref_pos and ref_addr:
                ref_addr_count = len(ref_addr)
                ref_pos_count = len(ref_pos)
                pos = random.randint(0, 24)
                fake_addr = ""
                if 0 <= pos <= 3:
                    if ref_pos_count > 0 and ref_addr_count > 2:
                        fake_addr = f"{ref_pos[0]} {ref_addr[0]}, {ref_addr[1]}"
                if 4 <= pos <= 5:
                    if ref_pos_count > 0 and ref_addr_count >= 4:
                        fake_addr = f"{ref_pos[0]} {ref_addr[0]}, {ref_addr[1]}"
                if 6 <= pos <= 8:
                    if ref_pos_count > 1 and ref_addr_count >= 1:
                        fake_addr = f"{ref_pos[0]}-{ref_pos[1]} {ref_addr[0]}, {ref_addr[1]}"
                if 9 <= pos <= 10:
                    if ref_pos_count > 1 and ref_addr_count > 0:
                        fake_addr = f"{ref_pos[0]} {ref_addr[0]} {ref_addr[1]}"
                if pos == 11:
                    fake_addr = ""  # User did not disclose an address..
                if 12 <= pos <= 24:
                    if ref_pos_count > 1 and ref_addr_count > 2:
                        fake_addr = f"{suite_type} {ref_pos[0]} {ref_addr[0]}, {ref_addr[1]}"

            print(f"{fake_addr}")
    def gen_rand_Excel(self, tfile):
        wb = Workbook()
        wb.create_sheet('testsheet')
        wb['testsheet'].title = 'bob'
        wb['A1'].value = 'bob'
        wb.save(tfile)

hp_gen = honeypot_generator()
for x in range(100):
    a = hp_gen.gen_rand_USAddress()





