from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane
from parameterization import Parameterization

getcontext().prec = 30


class LinearSystem():

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        """planes是一个数组"""
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        # 交换row1和row2的位置
        m = self[row1]
        n = self[row2]
        self[row1] = n
        self[row2] = m

    def multiply_coefficient_and_row(self, coefficient, row):
        # 根据row值，找到相应的序列，normal_vector、constant_term乘以coefficient
        n = self[row].normal_vector
        c = self[row].constant_term

        new_normal_vector = n.times_scalar(coefficient)
        new_constant_term = c * coefficient

        self[row] = Plane(new_normal_vector, new_constant_term)



    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        # 根据 row_to_add值，找到相应的序列，normal_vector、constant_term乘以coefficient加上 row_to_be_added_to序列
        n1 = self[row_to_add].normal_vector
        c1 = self[row_to_add].constant_term
        n2 = self[row_to_be_added_to].normal_vector
        c2 = self[row_to_be_added_to].constant_term

        new_normal_vector = n1.times_scalar(coefficient).plus(n2)
        new_constant_term = c1 * coefficient + c2

        self[row_to_be_added_to]  = Plane(new_normal_vector, new_constant_term)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e
        return indices

    def compute_triangular_form(self):
        """变化为三角形矩阵"""
        # 复制之前的矩阵
        system = deepcopy(self)
        # 行数
        num_equations = len(system)
        # 列数
        num_variables = system.dimension
        # 表示变化的列
        j = 0
        for i in range(num_equations):
            # 每行循环
            while j < num_variables:
                c = MyDecimal(system[i].normal_vector.coordinates[j])
                if c.is_near_zero():
                    swap_succeeded = system.swap_with_row_below(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue
                system.clear_coeff_below(i, j)
                j += 1
                break
        return system

    def swap_with_row_below(self, row, col):
        """切换row下边非0的行"""
        num_equations = len(self)
        for k in range(row+1, num_equations):
            coefficient = MyDecimal(self[k].normal_vector.coordinates[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row, k)
                return True
            return False

    def clear_coeff_below(self, row, col):
        """清除row行col列下的所有的非0系数"""
        num_equations = len(self)
        beta = MyDecimal(self[row].normal_vector.coordinates[col])
        # 循环消除row下的非零系统
        for k in range(row+1, num_equations):
            n = self[k].normal_vector.coordinates
            gamma = n[col]
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha, row, k)

    def compute_rref(self):
        """方程组转换为RREF"""
        # tf转换后的三角变量
        tf = self.compute_triangular_form()
        num_equations = len(tf)
        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()

        for i in range(num_equations)[::-1]:
            j = pivot_indices[i]
            if j < 0:
                continue
            tf.scale_row_to_make_one(i, j)
            tf.clear_coefficients_above(i, j)

        return tf

    def scale_row_to_make_one(self, row, col):
        """是row行col列的值系数变为1"""
        n = self[row].normal_vector.coordinates
        beta = Decimal('1.0') / n[col]
        self.multiply_coefficient_and_row(beta, row)

    def clear_coefficients_above(self, row, col):
        """消除上边的所有系数"""
        for k in range(row)[::1]:
            n = self[k].normal_vector.coordinates
            alpha = -(n[col])
            self.add_multiple_times_row_to_row(alpha, row, k)

    def computer_solution(self):
        """计算方程式解的情况，高斯消去法求解函数"""
        try:
            return self.do_gaussian_elimination_and_parameterization_solution()

        except Exception as e:
            if (str(e) == self.NO_SOLUTIONS_MSG or
                str(e) == self.INF_SOLUTIONS_MSG ):
                return str(e)
            else:
                raise e

    def do_gaussian_elimination_and_parameterization_solution(self):
        """高斯求解，判断无解、无数解、单一解"""
        rref = self.compute_rref()
        # 判断是否无解
        rref.raise_exception_if_contradictory_equation()
        # 判断是否多解
        # rref.raise_exception_if_too_few_pivots()
        # num_variables = rref.dimension
        # solution_coordinates = [rref.planes[i].constant_term for i in
        #                         range(num_variables)]
        # return Vector(solution_coordinates)
        # 多个解，参数化解集
        # 方向向量
        direction_vectors = rref.extract_direction_vectors_for_parametrization()
        # 基准点
        basepoint = rref.extract_basepoint_for_parametrization()
        # 输出结果
        return Parameterization(basepoint, direction_vectors)

    def extract_direction_vectors_for_parametrization(self):
        """参数化解集,计算方向向量"""
        # 方程的位数
        num_variables = self.dimension
        # 主变量的位置
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        # 差集反应出需要参数化表示的位置
        free_variable_indices = set(range(num_variables)) - set(pivot_indices)
        # 返回值 每个主变量参数化的值
        direction_vectors = []

        for free_var in free_variable_indices:
            vector_coords = [0] * num_variables
            vector_coords[free_var] = 1
            for i,p in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                if pivot_var < 0:
                    break
                vector_coords[pivot_var] = -p.normal_vector.coordinates[free_var
                ]
            direction_vectors.append(Vector(vector_coords))
        return direction_vectors

    def extract_basepoint_for_parametrization(self):
        """计算基准点"""
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()

        basepoint_coods = [0] * num_variables

        for i,p in enumerate(self.planes):
            pivot_var = pivot_indices[i]
            if pivot_var < 0 :
                break
            basepoint_coods[pivot_var] = p.constant_term

        return Vector(basepoint_coods)


    def raise_exception_if_contradictory_equation(self):
        """如果有矛盾引发异常"""
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == 'No nonzero elements found':
                    constant_term = MyDecimal(p.constant_term)
                    if not constant_term.is_near_zero():
                        raise Exception(self.NO_SOLUTIONS_MSG)
                else:
                    raise e

    def raise_exception_if_too_few_pivots(self):
        """判断为多个解"""
        pivote_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >=0 else 0 for index in pivote_indices])
        num_variables = self.dimension
        if num_pivots < num_variables:
            raise Exception(self.INF_SOLUTIONS_MSG)







    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
#
# s = LinearSystem([p0,p1,p2,p3])
#
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
