
with open("input.txt", "rt") as fi:
    s=fi.read().strip()

def hex2bin(s):
    m = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    return "".join([m[c] for c in s])

b = hex2bin(s)

def bin2int(b):
    return sum([int(bit) * 2**i for i, bit in enumerate(reversed(b))])


class packet(object):
    def __init__(self):
        self.pos = 0
        self.version_str = ""
        self.type_str = ""
        self.body = ""
        self.group_pos = 0
        self.has_next = False
        self.length_type = None
        self.length_str = ""
        self.length = None
        self.subpackets = []
        self.currpacket = None

    def __repr__(self):
        return f"<T: {self.type_str} V: {self.version_str}>"

    def sumver(self):
        s = bin2int(self.version_str)
        s += sum([p.sumver() for p in self.subpackets])
        return s

    def value(self):
        t = bin2int(self.type_str)
        if t == 4:
            return bin2int(self.body)
        if t == 0:
            return sum([p.value() for p in subpackets])
        if t == 1:
            pr = 1
            for x in [p.value() for p in subpackets]:
                pr *= x
            return pr
        if t == 2:
            return min([p.value() for p in subpackets])
        if t == 3:
            return max([p.value() for p in subpackets])
        if t == 5:
            return 1 if subpackets[0].value() > subpackets[1].value() else 0
        if t == 6:
            return 1 if subpackets[0].value() > subpackets[1].value() else 0
        if t == 6:
            return 1 if subpackets[0].value() > subpackets[1].value() else 0



    def add(self, c):
        if self.pos < 3:
            self.version_str += c
            self.pos +=1
            return False
        if self.pos < 6:
            self.type_str += c
            self.pos +=1
            return False

        if self.type_str == '100':
            if self.group_pos == 0:
                self.has_next = c == "1"
                self.group_pos +=1
                self.pos += 1
                return False

            self.body += c

            if self.group_pos == 4:
                if not self.has_next:
                    return True

                self.group_pos = 0
                self.pos += 1
                return False

            self.group_pos +=1
            self.pos += 1
            return False
        else:
            if self.length_type is None:
                self.length_type = c
                self.group_pos = 0
                return False

            if self.length == None:
                self.length_str += c
                self.group_pos += 1
                self.pos += 1

                if self.length_type == '0' and self.group_pos == 15:
                    self.length = bin2int(self.length_str)
                    self.group_pos  = 0
                    return False

                if self.length_type == '1' and self.group_pos == 11:
                    self.length = bin2int(self.length_str)
                    self.group_pos = 0
                    return False

                return False

            if self.group_pos < self.length:
                if self.currpacket == None:
                    self.currpacket = packet()

                if self.length_type == '0':
                    self.group_pos += 1
                self.pos += 1

                if self.currpacket.add(c):
                    if self.length_type == '1':
                        self.group_pos += 1
                    self.subpackets.append(self.currpacket)
                    self.currpacket = None
                    return self.group_pos == self.length

                return self.group_pos == self.length

            return "oops"


def parse(b):
    packets = []
    p = None
    for c in b:
        if p is None:
            p = packet()
        if p.add(c):
            packets.append(p)
            p = None

    print(packets)

    return sum([p.sumver() for p in packets])


print(parse(b))
