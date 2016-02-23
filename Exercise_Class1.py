class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise ValueError('width must be a integer!')
        if value <= 0 or value > 100000:
            raise ValueError('Data is out of range')
        self._width = value
        
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be a integer!')
        if value <= 0 or value > 100000:
            raise ValueError('Data is out of range')
        self._height = value
        
    @property
    def resolution(self):
        return self._height * self._width
    pass

#test
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
