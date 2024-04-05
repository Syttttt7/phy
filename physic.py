import tkinter as tk


class PhysicsFormulasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("High School Physics Formulas")
        self.master.geometry("500x400")  # 设置窗口大小

        # 创建一个字典来存储物理学公式和相关信息
        self.formulas = {
            "运动学": {
                "平均速度": "v = Δx / Δt",
                "加速度": "a = Δv / Δt",
                "等加速度运动位移": "x = v0 * t + 0.5 * a * t^2",
                "等加速度运动速度": "v = v0 + at",
                "等加速度运动末速度平方": "v^2 - v0^2 = 2aΔx"
            },
            "力学": {
                "牛顿第二定律": "F = ma",
                "功": "W = Fd",
                "动能": "K = 0.5 * mv^2",
                "能量守恒定律": "Ei = Ef",
                "动量守恒定律": "m1v1 + m2v2 = m1v1' + m2v2'",
                "弹簧弹性势能": "U = 0.5 * k * x^2",
                "重力势能": "U = mgh",
                "万有引力定律": "F = G * (m1 * m2) / r^2",
                "万有引力势能": "U = - G * (m1 * m2) / r"
            },
            "热学": {
                "热力学第一定律": "Q = ΔU + W",
                "理想气体状态方程": "PV = nRT",
                "气体内能": "ΔU = 3/2 * nRT",
                "热容": "Q = mcΔT",
                "等体积变化吸热": "Q = nCvΔT",
                "等压变化吸热": "Q = nCpΔT",
                "Cp和Cv关系": "Cp = Cv + R"
            },
            "波动学": {
                "频率": "f = 1/T",
                "波速": "v = λf",
                "光速": "c = λf",
                "反射公式": "θi = θr",
                "折射公式": "n1*sin(θ1) = n2*sin(θ2) , n1*v1 = n2*v2 , n1*λ1 = n2*λ2"
            },
            "电磁学": {
                "库仑定律": "F = k * |q1 * q2| / r^2",
                "电场强度": "E = F / q",
                "电流": "I = Q / t",
                "磁感应强度": "B = μ * I / (2 * π * r)"
            }
            # 其他物理学领域的公式...
        }

        # 创建主界面
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True,padx=20, pady=20)

        # 创建标签和滚动文本框用于显示公式
        self.formula_label = tk.Label(self.main_frame, text="选择一个物理学领域：", font=("Helvetica", 16))
        self.formula_label.pack(pady=(0, 5))

        self.category_var = tk.StringVar()
        self.category_var.set("运动学")  # 默认选择运动学
        self.category_menu = tk.OptionMenu(self.main_frame, self.category_var, *self.formulas.keys(),
                                           command=self.display_formulas)
        self.category_menu.config(width=25, font=("Helvetica", 14))
        self.category_menu.pack()

        self.formula_text = tk.Text(self.main_frame)
        self.formula_text.config(font=("Helvetica", 14))
        self.formula_text.pack(fill=tk.BOTH, expand=True)

        # 初始化显示第一个物理学领域的公式
        self.display_formulas("运动学")

    def display_formulas(self, category):
        self.formula_text.delete('1.0', tk.END)  # 清空文本框内容
        for formula, equation in self.formulas[category].items():
            self.formula_text.insert(tk.END, f"{formula}: {equation}\n\n")


# 创建主窗口并运行程序
root = tk.Tk()
app = PhysicsFormulasApp(root)
root.mainloop()
