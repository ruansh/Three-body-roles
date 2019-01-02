import matplotlib.pyplot as plt


class Novel():
    """创建一个小说的类"""

    def __init__(self, novel_name, roles_name):
        """初始化类的属性"""

        self.novel_name = novel_name
        self.roles_name = roles_name

    def one_role_nums(self, role_name):
        """统计一个人物名字出现的次数"""

        with open(self.novel_name, encoding='utf-8') as f:
            content = f.read()

        count = 0
        n = len(role_name)
        for i in range(len(content)):
            if content[i: i + n] == role_name:
                count += 1
        return count

    def main_roles_nums(self):
        """统计主要人物名字出现的次数"""

        with open(self.roles_name, encoding='utf-8') as f:
            names = [line.strip() for line in f.readlines()]

        dic = {}
        for name in names:
            num = self.one_role_nums(name)
            if num:
                dic[name] = num
        dic = sorted(dic.items(), key=lambda k: k[1], reverse=True)
        return dic

    def show_datas(self):
        """输出人物名字及出现次数"""

        dic = self.main_roles_nums()
        for x in dic:
            print(x[0], x[1])

    def draw_picture(self, title=""):
        """可视化数据"""

        dic = self.main_roles_nums()
        names, nums = [], []
        for x in dic:
            names.append(x[0])
            nums.append(x[1])

        n = list(range(len(names)))
        plt.figure(figsize=(12, 6))
        plt.bar(n, nums, alpha=0.5)
        plt.xlim((0, len(names)))
        plt.xticks(n, names, rotation=30, fontproperties="SimHei", fontsize=12)
        plt.title(title, fontproperties="SimHei", fontsize=20)

        plt.show()