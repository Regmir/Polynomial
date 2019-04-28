class Polynomial(object):

    def __init__(self, coeffs):
        if isinstance(coeffs, Polynomial):
            self.coeffs = list(coeffs.coeffs)
        else:
            self.coeffs = list(coeffs)

    @property
    def coeffs(self):
        return self._coeffs

    @coeffs.setter
    def coeffs(self, coeffs):
        self._coeffs = coeffs

    @coeffs.setter
    def coeffs(self, coeffs):
        if isinstance(coeffs, list) or isinstance(coeffs, tuple):
            for coeff in coeffs:
                if not isinstance(coeff, int):
                    raise TypeError("Polynomial coefficient should be int")
            if not coeffs:
                self._coeffs=[0,]
            else:
                self._coeffs = coeffs
        else:
            raise TypeError("Polynomisl coefficients should be tuple or list")

    def __add__(self, other):
        res=(self)
        if isinstance(other, Polynomial):
            if len(res.coeffs) > len(other.coeffs):
                s = len(res.coeffs)
                for c in range(s-len(other.coeffs)):
                    other.coeffs=[0]+other.coeffs
            else:
                s = len(other.coeffs)
                for c in range(s - len(res.coeffs)):
                    res.coeffs = [0] + res.coeffs
            for c in range(s):
                res.coeffs[c]= res.coeffs[c] + other.coeffs[c]
        else:
            if isinstance(other, int):
                res.coeffs[len(res.coeffs)-1] = res.coeffs[len(res.coeffs)-1] + other
            else:
                raise TypeError("Incorrect argument")
        return res

    def __radd__(self, other):
        res=(self)
        if isinstance(other, Polynomial):
            if len(res.coeffs) > len(other.coeffs):
                s = len(res.coeffs)
                for c in range(s-len(other.coeffs)):
                    other.coeffs=[0]+other.coeffs
            else:
                s = len(other.coeffs)
                for c in range(s - len(res.coeffs)):
                    res.coeffs = [0] + res.coeffs
            for c in range(s):
                res.coeffs[c]= res.coeffs[c] + other.coeffs[c]
        else:
            if isinstance(other, int):
                res.coeffs[len(res.coeffs)-1] = res.coeffs[len(res.coeffs)-1] + other
            else:
                raise TypeError("Incorrect argument")
        return res

    def __sub__(self, other):
        res=(self)
        if isinstance(other, Polynomial):
            if len(res.coeffs) > len(other.coeffs):
                s = len(res.coeffs)
                for c in range(s-len(other.coeffs)):
                    other.coeffs=[0]+other.coeffs
            else:
                s = len(other.coeffs)
                for c in range(s - len(res.coeffs)):
                    res.coeffs = [0] + res.coeffs
            for c in range(s):
                res.coeffs[c]= res.coeffs[c] - other.coeffs[c]
        else:
            if isinstance(other, int):
                res.coeffs[len(res.coeffs) - 1] = res.coeffs[len(res.coeffs) - 1] - other
            else:
                raise TypeError("Incorrect argument")
        return res

    def __rsub__(self, other):
        res=(self)
        if isinstance(other, Polynomial):
            if len(res.coeffs) > len(other.coeffs):
                s = len(res.coeffs)
                for c in range(s-len(other.coeffs)):
                    other.coeffs=[0]+other.coeffs
            else:
                s = len(other.coeffs)
                for c in range(s - len(res.coeffs)):
                    res.coeffs = [0] + res.coeffs
            for c in range(s):
                res.coeffs[c]= other.coeffs[c] - res.coeffs[c]
        else:
            if isinstance(other, int):
                for c in range(0,len(res.coeffs)-1):
                    res.coeffs[c] = - res.coeffs[c]
                res.coeffs[len(res.coeffs)-1] =other - res.coeffs[len(res.coeffs)-1]
            else:
                raise TypeError("Incorrect argument")
        return res

    def __mul__(self, other):
        res = Polynomial([0])
        if isinstance(other, Polynomial):
            o = (other)
            e = (self)
            lenself=len(self.coeffs)
            lenother=len(other.coeffs)
            if lenself > lenother:
                s = len(self.coeffs)
                i = len(other.coeffs)
                for c in range(s+i-2):
                    res.coeffs = [0] + res.coeffs
                for c in range(s-1, -1, -1):
                    for k in range(i-1, -1, -1):
                        res.coeffs[c+k] += e.coeffs[c] * o.coeffs[k]
            else:
                s = len(other.coeffs)
                i = len(self.coeffs)
                for c in range(s+i-2):
                    res.coeffs = [0] + res.coeffs
                for c in range(s-1, -1, -1):
                    for k in range(i-1, -1, -1):
                        res.coeffs[c+k] += o.coeffs[c] * e.coeffs[k]
        else:
            if isinstance(other, int):
                res=Polynomial(self)
                for c in range(len(res.coeffs)):
                    res.coeffs[c]= res.coeffs[c] * other
            else:
                raise TypeError("Incorrect argument")
        return res

    def __rmul__(self,other):
        return self.__mul__(other)

    def __str__(self):
        s=''
        for c in range(len(self.coeffs)):
            if (self.coeffs[c]!=0):
                if (c == len(self.coeffs) - 2):
                    if (self.coeffs[c]) > 0:
                        if (self.coeffs[c] != 1):
                            s = s + str(self.coeffs[c]) + 'x+'
                        else:
                            s = s + 'x^' + str(len(self.coeffs) - 1 - c) + '+'
                    if self.coeffs[c] < 0:
                        if (self.coeffs[c] == -1):
                            s = s[:len(s) - 1]
                            s = s + '-x+'
                        else:
                            s = s[:len(s) - 1]
                            s = s + str(self.coeffs[c]) + 'x+'
                else:
                    if (c == len(self.coeffs) - 1):
                        if (self.coeffs[c]) > 0:
                            if (self.coeffs[c] != 1):
                                s = s + str(self.coeffs[c]) + '+'
                            else:
                                s = s + str(len(self.coeffs) - 1 - c) + '+'
                        if self.coeffs[c] < 0:
                            if (self.coeffs[c] == -1):
                                s = s[:len(s) - 1]
                                s = s + str(self.coeffs[c]) + '+'
                            else:
                                s = s[:len(s) - 1]
                                s = s + str(self.coeffs[c]) + '+'
                    else:
                        if (self.coeffs[c]) > 0:
                            if (self.coeffs[c] != 1):
                                s = s + str(self.coeffs[c]) + 'x^' + str(len(self.coeffs) - 1 - c) + '+'
                            else:
                                s = s + 'x^' + str(len(self.coeffs) - 1 - c) + '+'
                        if self.coeffs[c] < 0:
                            if (self.coeffs[c] == -1):
                                s = s[:len(s) - 1]
                                s = s + '-x^' + str(len(self.coeffs) - 1 - c) + '+'
                            else:
                                s = s[:len(s) - 1]
                                s = s + str(self.coeffs[c]) + 'x^' + str(len(self.coeffs) - 1 - c) + '+'
        s=s[:len(s)-1]
        if (s==''):
            s='0'
        return s

    def __repr__(self):
        return 'Polynomial{}'.format(list(self.coeffs))

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        return False

    def __lt__(self, other):
        if isinstance(other, Polynomial):
            if len(self.coeffs) == len(other.coeffs):
                return self.coeffs < other.coeffs
            else:
                return len(self.coeffs) < len(other.coeffs)
        raise TypeError("Incorrect argument")

    def __le__(self, other):
        if isinstance(other, Polynomial):
            return self.__lt__(other) or self.coeffs == other.coeffs
        raise TypeError("Incorrect argument")

    def __ne__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs != other.coeffs
        raise TypeError("Incorrect argument")

    def __gt__(self, other):
        if isinstance(other, Polynomial):
            return not self.__le__(other)
        raise TypeError("Incorrect argument")

    def __ge__(self, other):
        if isinstance(other, Polynomial):
            return not self.__lt__(other)
        raise TypeError("Incorrect argument")



        
