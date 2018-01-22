from decimal import Decimal
from line import Line
from vector import Vector
from plane import Plane
from linsys import LinearSystem
from linsys import MyDecimal


# line =Line(Vector([7.204, 3.182]), 8.68)
# line2 = Line(Vector([8.172, 4.114]), 9.883)
# plane = Plane(Vector([8.172, 4.114, 3.454]), 9.883)
# plane2 = Plane(Vector([8.172, 4.114, 3.454]), 9.883)
# print(line.intersection_with(line2))
# print(plane)
# linearsystem = LinearSystem([plane, plane2])
# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
#
# s = LinearSystem([p0,p1,p2,p3])

# print(s.indices_of_first_nonzero_terms_in_each_row())
# print('{},{},{},{}'.format(s[0],s[1],s[2],s[3]))
# print(len(s))
# print(s)
#
# s[0] = p1
# print(s)
#
# print(MyDecimal('1e-9').is_near_zero())
# print(MyDecimal('1e-11').is_near_zero())
# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
#
# s = LinearSystem([p0,p1,p2,p3])
#
#
# s.swap_rows(0,1)
# if not (s[3] == p3):# s[0] == p1 and s[1] == p0 and s[2] == p2 and
#     print('test case 1 failed')
# #
# s.swap_rows(1,3)
# if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
#     print('test case 2 failed')
#
# s.swap_rows(3,1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print('test case 3 failed')
#
#
# s.multiply_coefficient_and_row(1,0)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print('test case 4 failed')
#
# s.multiply_coefficient_and_row(-1,2)
# if not (s[0] == p1 and
#         s[1] == p0 and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 5 failed')
#
# s.multiply_coefficient_and_row(10,1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 6 failed')
#
# s.add_multiple_times_row_to_row(0,0,1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 7 failed')
#
# s.add_multiple_times_row_to_row(1,0,1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 8 failed')
#
# s.add_multiple_times_row_to_row(-1,1,0)
# if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
#         s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 9 failed')
#
# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and t[1] == p2):
#     print('test case 1 failed')
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == Plane(constant_term='1')):
#     print('test case 2 failed')
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2 and
#         t[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
#         t[3] == Plane()):
#     print('test case 3 failed')
#
# p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# t = s.compute_triangular_form()
# if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
#         t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
#         t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
#     print('test case 4 failed')
#
#
p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
s = LinearSystem([p1,p2])
r = s.compute_rref()
if not (r[0] == Plane(Vector(['1','0','0']), '-1') and r[1] == p2):
    print('test case 1 failed')

p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
s = LinearSystem([p1,p2])
r = s.compute_rref()
if not (r[0] == p1 and
        r[1] == Plane(constant_term='1')):
    print('test case 2 failed')

p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
s = LinearSystem([p1,p2,p3,p4])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='0') and
        r[1] == p2 and
        r[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
        r[3] == Plane()):
    print('test case 3 failed')

p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
s = LinearSystem([p1,p2,p3])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')) and
        r[1] == Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')) and
        r[2] == Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9'))):
    print('test case 4 failed')