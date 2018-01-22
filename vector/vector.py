from math import sqrt, acos, pi
from decimal import Decimal, getcontext

# 定义decimal的保留位数。
getcontext().prec = 5
class Vector():
    """创建向量的类,参数是coordinates,是一个数组"""
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError()
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise  TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector:{}'.format([x for x in self.coordinates])

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def plus(self, other):
        """向量加法运算"""
        new_coordinates = [x+y for x,y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coordinates)

    def minus(self, other):
        """向量的减法运算"""
        new_coordinates = [x-y for x,y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, other):
        """向量乘以标量"""
        new_coordiantes = [x*other for x in self.coordinates]
        return Vector(new_coordiantes)

    def magnitude(self):
        """计算向量的大小，标量"""
        coordinates_squared = [x**2 for x in self.coordinates]
        result = Decimal.sqrt(sum(coordinates_squared))
        return result

    def normalized(self):
        """计算单位向量"""
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0') / magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, other):
        """计算点积"""
        return sum([x*y for x,y in zip(self.coordinates, other.coordinates)])

    def angle_with(self, other, in_degrees=False):
        """计算角度，in_degrees=False,输出为角度，否则输出"""
        try:
            u1 = self.normalized()
            u2 = other.normalized()
            angle_in_radians = acos(Decimal(u1.dot(u2)))
            if in_degrees:
                return angle_in_radians * 180. / pi
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def is_orthogonal_to(self, other, tolerance=1e-10):
        """判断是否为垂直，判断依据为cos值为0，由于误差所以判断结果是否小于1e-10"""
        return abs(self.dot(other)) < tolerance

    def is_parallel_to(self, other):
        """判断是否为平行，依据角度为0或180，或者其中包含0向量"""
        return (self.angle_with(other) == 0 or self.angle_with(other) == pi or self.is_zero() or other.is_zero())

    def is_zero(self):
        """判断是否为零向量"""
        return self.magnitude() <= 0

    def component_orthogonal_to(self, other):
        """计算投影向量"""
        try:
            # other方向的计算单位向量
            other_one = other.normalized()
            w = self.dot(other_one)
            # other方向的投影向量
            return other_one.times_scalar(w)
        except Exception as e:
            raise e


    def component_parallel_to(self, other):
        """计算other垂直方向的向量"""
        try:
            # 投影方向的向量
            shadow_other = self.component_orthogonal_to(other)
            # 垂直方向的向量
            return self.minus(shadow_other)
        except Exception as e:
            raise e

    def cross(self, other):
        """计算向量积"""
        try:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = other.coordinates
            cross_j = [(y1*z2-y2*z1), -(x1*z2-x2*z1), x1*y2 - x2*y1]
            return Vector(cross_j)
        except Exception as e:
            raise e

    def area_of_triangle_with(self, other):
        """计算三角形的面积"""
        try:
            return self.area_of_parallelogram_with_(other) / Decimal('2.0')
        except Exception as e:
            raise e



    def area_of_parallelogram_with_(self, other):
        """计算平行四边形的面积"""
        try:
            # 计算向量积
            guo = self.cross(other)
            # 返回平行四边形的面积
            return guo.magnitude()
        except Exception as e:
            raise e


# one = Vector([7.887, 4.138])
# two = Vector([-8.802, 6.776])
# thr = Vector([-5.955, -4.904, -1.874])
# four = Vector([-4.496, -8.755, 7.103])

# five = Vector([3.183, -7.627])
# six = Vector([-2.668, 5.319])
# seven = Vector([7.35, 0.221, 5.188])
# eight = Vector([2.751, 8.259, 3.985])

# one = Vector([-7.579, -7.88])
# two = Vector([22.737, 23.64])
# thr = Vector([-2.029, 9.97, 4.172])
# four = Vector([-9.231, -6.639, -7.245])
#
# five = Vector([-2.328, -7.284, -1.214])
# six = Vector([-1.821, 1.072, -2.94])
# seven = Vector([2.118, 4.827])
# eight = Vector([0, 0])

# print(one.dot(two))                    #点积
# print(thr.dot(four))                   #点积
# print(five.angle_with(six))            #角度
# print(seven.angle_with(eight, True))         #角度


# print('判断是否平行')
# print(one.is_orthogonal_to(two))
# print(thr.is_orthogonal_to(four))
# print(five.is_orthogonal_to(six))
# print(eight.is_orthogonal_to(seven))
#
#
# print('判断是否垂直')
# print(one.is_parallel_to(two))
# print(thr.is_parallel_to(four))
# print(five.is_parallel_to(six))
# print(eight.is_parallel_to(seven))


# print(one.magnitude())
# print(two.magnitude())
# print(thr.normalized())
# print(four.normalized())
# print(one.plus(two))
# print(one.minus(two))
# print(one.times_scalar(6))


# one = Vector([3.039, 1.879])
# two = Vector([0.825, 2.036])
# thr = Vector([-9.88, -3.264, -8.159])
# four = Vector([-2.155, -9.353, -9.473])
# five = Vector([3.009, -6.172, 3.692, -2.51])
# six = Vector([6.404, -9.144, 2.759, 8.718])
#
# print(one)
# print('two方向的投影：', end='')
# print(one.component_orthogonal_to(two))
#
# print('four方向的垂直向量：', end='')
# print(thr.component_parallel_to(four))
#
#
# print('投影：', end='')
# print(five.component_orthogonal_to(six))
#
# print('垂直向量：', end='')
# print(five.component_parallel_to(six))


# one = Vector([8.462, 7.893, -8.187])
# two = Vector([6.984, -5.975, 4.778])
# thr = Vector([-8.987, -9.838, 5.031])
# four = Vector([-4.268, -1.861, -8.866])
# five = Vector([1.5, 9.547, 3.691])
# six = Vector([-6.007, 0.124, 5.772])
#
# print('向量积：', end='')
# print(one.cross(two))
# print('平行四边形面积：', end='')
# print(thr.area_of_parallelogram_with_(four))
# print('三角形的面积', end='')
# print(five.area_of_triangle_with(six))

