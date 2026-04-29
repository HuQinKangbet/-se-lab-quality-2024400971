# 包含代码坏味道：重复代码、未使用变量、冗余逻辑
def calculate_student_score(score_list):
    # 未使用变量（坏味道）
    unused_var = "test"
    total = 0
    count = 0
    for score in score_list:
        if score >= 0:
            total = total + score
            count = count + 1
    if count == 0:
        return 0
    avg = total / count
    # 重复打印逻辑
    print("学生分数计算完成")
    print("总分：", total)
    print("平均分：", avg)
    return avg

def calculate_teacher_score(score_list):
    # 未使用变量（坏味道）
    unused_var = "test"
    total = 0
    count = 0
    for score in score_list:
        if score >= 0:
            total = total + score
            count = count + 1
    if count == 0:
        return 0
    avg = total / count
    # 重复打印逻辑
    print("教师分数计算完成")
    print("总分：", total)
    print("平均分：", avg)
    return avg

# 调用测试
if __name__ == "__main__":
    student_scores = [85, 92, 78, 90]
    teacher_scores = [95, 88, 96]
    calculate_student_score(student_scores)
    calculate_teacher_score(teacher_scores)
