# This file is part of CardStock.
#     https://github.com/benjie-git/CardStock
#
# Copyright Ben Levitt 2020-2023
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.  If a copy
# of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

try:
    from browser import window as context
except:
    from browser import self as context

import math


class Size(object):
    def __init__(self, *args):
        super().__init__()
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            self._width = round(float(args[0][0]))
            self._height = round(float(args[0][1]))
        elif len(args) == 1 and isinstance(args[0], Size):
            self._width = round(args[0]._width)
            self._height = round(args[0]._height)
        elif len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            self._width = round(args[0])
            self._height = round(args[1])
        else:
            raise TypeError("Size() requires 2 numbers or a Size")

    def __eq__(self, other):
        if isinstance(other, (list, tuple)) and len(other) != 2:
            return False
        if isinstance(other, (Size, list, tuple)):
            return (self[0] == other[0] and self[1] == other[1])
        return False

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("width must be a number")
        self._width = round(val)

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("height must be a number")
        self._height = round(val)

    @property
    def Width(self):
        return self._width
    @Width.setter
    def Width(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("width must be a number")
        self._width = round(val)

    @property
    def Height(self):
        return self._height
    @Height.setter
    def Height(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("height must be a number")
        self._height = round(val)

    def __str__(self):
        return f"({self._width}, {self._height})"

    def __getitem__(self, key):
        if key == 0:
            return self._width
        elif key == 1:
            return self._height
        else:
            raise KeyError("Size has 2 elements")

    def __setitem__(self, key, val):
        if key == 0:
            self.width = round(val)
        elif key == 1:
            self.height = round(val)
        else:
            raise KeyError("Size has 2 elements")

    def __iadd__(self, other):
        if isinstance(other, (tuple, list, Point, Size)):
            self._width = round(self._width + other[0])
            self._height = round(self._height + other[1])
        else:
            raise TypeError()
        return self

    def __isub__(self, other):
        if isinstance(other, (tuple, list, Point, Size)):
            self._width = round(self._width - other[0])
            self._height = round(self._height - other[1])
        else:
            raise TypeError()
        return self

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self._width = round(self._width * other[0])
            self._height = round(self._height * other[1])
        else:
            raise TypeError()
        return self

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self._width = round(self._width / other[0])
            self._height = round(self._height / other[1])
        else:
            raise TypeError()
        return self

    def __add__(self, other):
        if isinstance(other, (Point, RealPoint, Size,tuple,list)):
            return Size(self._width + other[0], self._height + other[1])
        else:
            raise TypeError()

    def __sub__(self, other):
        if isinstance(other, (Point, RealPoint, Size, tuple, list)):
            return Size(self._width - other[0], self._height - other[1])
        else:
            raise TypeError()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Size(self._width * other, self._height * other)
        else:
            raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Size(self._width / other, self._height / other)
        else:
            raise TypeError()

    def __iter__(self):
        return (self.__getitem__(k) for k in (0, 1))

    def __len__(self):
        return 2


class Point(object):
    def __init__(self, *args):
        super().__init__()
        if len(args) == 1 and isinstance(args[0], (list, tuple, Point, RealPoint)):
            self._x = round(float(args[0][0]))
            self._y = round(float(args[0][1]))
        elif len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            self._x = round(args[0])
            self._y = round(args[1])
        else:
            raise TypeError(f"Point() requires 2 numbers or a Point {args}")

    def __eq__(self, other):
        if isinstance(other, (list, tuple)) and len(other) != 2:
            return False
        if isinstance(other, (Point, list, tuple)):
            return (self[0] == other[0] and self[1] == other[1])
        return False

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("x must be a number")
        self._x = round(val)

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("y must be a number")
        self._y = round(val)

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __getitem__(self, key):
        if key == 0:
            return self._x
        elif key == 1:
            return self._y
        else:
            raise KeyError("Point has 2 elements")

    def __setitem__(self, key, val):
        if key == 0:
            self._x = round(val)
        elif key == 1:
            self._y = round(val)
        else:
            raise KeyError("Point has 2 elements")

    def __iadd__(self, other):
        if isinstance(other, (tuple, list, Point, Size)):
            self._x += round(other[0])
            self._y += round(other[1])
        else:
            raise TypeError()
        return self

    def __isub__(self, other):
        if isinstance(other, (tuple, list, Point, Size)):
            self._x -= round(other[0])
            self._y -= round(other[1])
        else:
            raise TypeError()
        return self

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self._x = round(self._x * other)
            self._y = round(self._y * other)
        else:
            raise TypeError()
        return self

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self._x = round(self._x / other)
            self._y = round(self._y / other)
        else:
            raise TypeError()
        return self

    def __add__(self, other):
        if isinstance(other, (Point, Size, tuple, list)):
            return Point(self._x + other[0], self._y + other[1])
        else:
            raise TypeError()

    def __sub__(self, other):
        if isinstance(other, (Point, RealPoint, Size, tuple, list)):
            return Point(self._x - other[0], self._y - other[1])
        else:
            raise TypeError()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point(self._x * other, self._y * other)
        else:
            raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Point(self._x / other, self._y / other)
        else:
            raise TypeError()

    def __iter__(self):
        return (self.__getitem__(k) for k in (0, 1))

    def __len__(self):
        return 2


class RealPoint(object):
    def __init__(self, *args):
        super().__init__()
        if len(args) == 1 and isinstance(args[0], (list, tuple, Point, RealPoint)):
            self._x = args[0][0]
            self._y = args[0][1]
        elif len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            self._x = args[0]
            self._y = args[1]
        else:
            raise TypeError(f"Point() requires 2 numbers or a Point {args}")

    def __eq__(self, other):
        if isinstance(other, (list, tuple)) and len(other) != 2:
            return False
        if isinstance(other, (Point, list, tuple)):
            return (self[0] == other[0] and self[1] == other[1])
        return False

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("x must be a number")
        self._x = val

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("y must be a number")
        self._y = val

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __getitem__(self, key):
        if key == 0:
            return self._x
        elif key == 1:
            return self._y
        else:
            raise KeyError("Point has 2 elements")

    def __setitem__(self, key, val):
        if key == 0:
            self._x = val
        elif key == 1:
            self._y = val
        else:
            raise KeyError("Point has 2 elements")

    def __iadd__(self, other):
        if isinstance(other, (tuple, list, Point, Size)):
            self._x += other[0]
            self._y += other[1]
        else:
            raise TypeError()
        return self

    def __isub__(self, other):
        if isinstance(other, (tuple, list, Point, Size)):
            self._x -= other[0]
            self._y -= other[1]
        else:
            raise TypeError()
        return self

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self._x *= other
            self._y *= other
        else:
            raise TypeError()
        return self

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self._x /= other
            self._y /= other
        else:
            raise TypeError()
        return self

    def __add__(self, other):
        if isinstance(other, (Point, Size, tuple, list)):
            return Point(self._x + other[0], self._y + other[1])
        else:
            raise TypeError()

    def __sub__(self, other):
        if isinstance(other, (Point, RealPoint, Size, tuple, list)):
            return Point(self._x - other[0], self._y - other[1])
        else:
            raise TypeError()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point(self._x * other, self._y * other)
        else:
            raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Point(self._x / other, self._y / other)
        else:
            raise TypeError()

    def __iter__(self):
        return (self.__getitem__(k) for k in (0, 1))

    def __len__(self):
        return 2


class Rect(object):
    def __init__(self, *args):
        super().__init__()
        if len(args) == 4:
            self.Left = args[0]
            self.Top = args[1]
            self.Width = args[2]
            self.Height = args[3]
        elif len(args) == 2:
            self.Left = args[0][0]
            self.Top = args[0][1]
            if isinstance(args[1], Point):
                self.Width = args[1][0] - args[0][0]
                self.Height = args[1][1] - args[0][1]
            else:
                self.Width = args[1][0]
                self.Height = args[1][1]

        else:
            raise TypeError

    def Union(self, other):
        if other.Top < self.Top:
            diff = other.Top - self.Top
            self.Top += diff
            self.Height -= diff
        if other.Left < self.Left:
            diff = other.Left - self.Left
            self.Left += diff
            self.Width -= diff
        if other.Bottom > self.Bottom:
            diff = other.Bottom - self.Bottom
            self.Height += diff
        if other.Right > self.Right:
            diff = other.Right - self.Right
            self.Width += diff
        return self

    def Contains(self, pt):
        return (self.Left <= pt[0] <= self.Right and self.Top <= pt[1] <= self.Bottom)

    def __eq__(self, other):
        if isinstance(other, Rect):
            return (self.Left == other.Left and self.Top == other.Top and
                    self.Right == other.Right and self.Bottom == other.Bottom)
        return False

    def __str__(self):
        return f"(({self.Left}, {self.Top}), ({self.Width}, {self.Height}))"

    @property
    def Right(self):
        return self.Left + self.Width
    @Right.setter
    def Right(self, r):
        self.Width = r-self.Left

    @property
    def Bottom(self):
        return self.Top + self.Height
    @Bottom.setter
    def Bottom(self, b):
        self.Height = b-self.Top

    @property
    def Position(self):
        return RealPoint(self.Left, self.Top)
    @Position.setter
    def Position(self, pos):
        self.Left = pos[0]
        self.Top = pos[1]

    @property
    def TopLeft(self):
        return RealPoint(self.Left, self.Top)

    @property
    def TopRight(self):
        return RealPoint(self.Right, self.Top)

    @property
    def BottomLeft(self):
        return RealPoint(self.Left, self.Bottom)

    @property
    def BottomRight(self):
        return RealPoint(self.Right, self.Bottom)

    @property
    def Size(self):
        return Size(self.Width, self.Height)
    @Size.setter
    def Size(self, s):
        self.Width = s[0]
        self.Height = s[1]


class Colour(object):
    def __init__(self, *a):
        if len(a) == 1 and isinstance(a[0], str):
            self.fabCol = context.fabric.Color.new(a[0])
        elif len(a) == 1 and isinstance(a[0], (list, tuple)):
            colorStr = self.PartsToHex(*a[0])
            self.fabCol = context.fabric.Color.new(colorStr)
        else:
            colorStr = self.PartsToHex(*a)
            self.fabCol = context.fabric.Color.new(colorStr)

    def PartsToHex(self, r, g, b, a=1.0):
        r = round(r*255)
        g = round(g*255)
        b = round(b*255)
        if a == 1.0:
            colorStr = '#'+''.join('{:02X}'.format(n) for n in (r, g, b, 255))
            return colorStr
        else:
            a = round(a*255)
            colorStr = '#'+''.join('{:02X}'.format(n) for n in (r, g, b, a))
            return colorStr

    def ToHex(self):
        parts = self.fabCol.getSource()
        scaledParts = list((p/255.0 for p in (parts)))
        scaledParts[3] *= 255
        return self.PartsToHex(*scaledParts)

    def Red(self):   return self.fabCol.getSource()[0]/255.0
    def Green(self): return self.fabCol.getSource()[1]/255.0
    def Blue(self):  return self.fabCol.getSource()[2]/255.0
    def Alpha(self):
        parts = self.fabCol.getSource()
        if len(parts) > 3:
            return parts[3]
        else:
            return 1.0


class AffineMatrix2D(object):
    nextMat = 1
    def __init__(self, other=None):
        super().__init__()

        self.id = AffineMatrix2D.nextMat
        AffineMatrix2D.nextMat += 1

        if other:
            self.matrix = context.fabric.util.composeMatrix(other.matrix)
        else:
            d = {'angle': 0,
                 'scaleX': 1.0, 'scaleY': 1.0,
                 'flipX': False, 'flipY': False,
                 'skewX': 0.0, 'skewY': 0.0,
                 'translateX': 0, 'translateY': 0}
            self.matrix = context.fabric.util.composeMatrix(d)

    def Translate(self, x, y):
        newMat = context.fabric.util.composeMatrix({'translateX':x, 'translateY':y})
        newMat = context.fabric.util.multiplyTransformMatrices(self.matrix, newMat, False)
        self.matrix = newMat

    def Rotate(self, angle):
        angle = math.degrees(angle)
        newMat = context.fabric.util.composeMatrix({'angle': angle})
        newMat = context.fabric.util.multiplyTransformMatrices(self.matrix, newMat, False)
        self.matrix = newMat

    def Invert(self):
        newMat = context.fabric.util.invertTransform(self.matrix)
        self.matrix = newMat

    def TransformPoint(self, x, y):
        pos = context.fabric.util.transformPoint({'x':x, 'y':y}, self.matrix)
        return RealPoint(pos.x, pos.y)


# CardStock-specific Point, Size, RealPoint subclasses
# These notify their model when their components are changed, so that, for example:
# button.center.x = 100  will notify the button's model that the center changed.


class CDSPoint(Point):
    def __init__(self, *args, **kwargs):
        model = kwargs.pop("model")
        role = kwargs.pop("role")
        super().__init__(*args, **kwargs)
        self.model = model
        self.role = role

    def __setitem__(self, key, val):
        if not isinstance(val, (int, float)):
            raise TypeError("value must be a number")
        super().__setitem__(key, val)

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("x must be a number")
        self._x = val
        self.model.FramePartChanged(self)

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("y must be a number")
        self._y = val
        self.model.FramePartChanged(self)


class CDSRealPoint(RealPoint):
    def __init__(self, *args, **kwargs):
        model = kwargs.pop("model")
        role = kwargs.pop("role")
        super().__init__(*args, **kwargs)
        self.model = model
        self.role = role

    def __setitem__(self, key, val):
        if not isinstance(val, (int, float)):
            raise TypeError("value must be a number")
        super().__setitem__(key, val)

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("x must be a number")
        self._x = val
        self.model.FramePartChanged(self)

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("y must be a number")
        self._y = val
        self.model.FramePartChanged(self)


class CDSSize(Size):
    def __init__(self, *args, **kwargs):
        model = kwargs.pop("model")
        role = kwargs.pop("role")
        super().__init__(*args, **kwargs)
        self.model = model
        self.role = role

    def __setitem__(self, key, val):
        if not isinstance(val, (int, float)):
            raise TypeError("size must be a number")
        super().__setitem__(key, val)

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("width must be a number")
        self._width = val
        self.model.FramePartChanged(self)

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("height must be a number")
        self._height = val
        self.model.FramePartChanged(self)
