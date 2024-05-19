class BF:
    def __init__(self):
        self.l = [0]
        self.id = 0
        self.s = ""
        self.i = ""
        self.o = ""
    
    def script(self, s):
        self.s = s

    def input(self, i):
        self.i = i

    def output(self):
        return self.o

    def PList(self):
        print(self.l)

    def run(self):
        pos = 0
        pos_i = 0
        loop_init = 0
        loop_fim = 0
        loop_id = 0
        while True:
            match self.s[pos]:
                case "+":
                    self.l[self.id] += 1
                case "-":
                    self.l[self.id] -= 1
                case ">":
                    self.id += 1
                    if self.id == len(self.l):
                        self.l.append(0)
                case "<":
                    self.id = len(self.l)-1 if self.id == 0 else self.id-1
                case ".":
                    self.o += chr(self.l[self.id])
                case ",":
                    self.l[self.id] += ord(self.i[pos_i])
                    pos_i = 0 if len(self.i)-1 == pos_i else pos_i+1
                case "[":
                    loop_init = pos
                    loop_id = self.id
                    while True:
                        pos += 1
                        if self.s[pos] == "]":
                            loop_fim = pos
                            break
                    pos = loop_init+1
                case "]":
                    pos = loop_init+1 if self.l[loop_id] > 0 else loop_fim+1
            pos += 1
            if len(self.s) <= pos:
                break

bf = BF()

bf.script("+++[>++<-]")
bf.run()

bf.PList()
