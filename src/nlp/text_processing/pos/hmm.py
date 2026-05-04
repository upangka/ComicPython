class HMM:
    """隐马尔科夫模型"""

    def __init__(self):
        # 用于存取算法中间结果，不需要每次都训练模型
        self.model_file = './data/hmm_model.pkl'
        # 状态列表
        self.state_list = ['B', 'M', 'E', 'S']
        # 用于判断是否需要重新加载模型
        self.load_para = False

    def try_load_model(self, trained):
        if trained:
            import pickle
            with open(self.model_file, 'rb') as f:
                self.A_dic = pickle.load(f)
                self.B_dic = pickle.load(f)
                self.Pi_dic = pickle.load(f)
                self.load_para = True
        else:
            # 转移概率 (状态->状态的条件概率)
            self.A_dic = {}
            # 发射概率 (状态->词语的条件概率)
            self.B_dic = {}
            # 初始概率 (状态的初始条件概率)
            self.Pi_dic = {}
            self.load_para = False

    def train(self, path):
        self.try_load_model(trained=False)

        # 统计状态出现次数
        Count_dic = {}

        def init_parameters():
            """初始化参数"""
            for state in self.state_list:
                self.Pi_dic[state] = 0.0
                self.A_dic[state] = {s: 0.0 for s in self.state_list}
                self.B_dic[state] = {}
                Count_dic[state] = 0

        def make_label(text):
            """为训练材料的每个词划分BMES列表"""
            out_text = []
            if len(text) == 1:
                out_text.append('S')
            else:
                out_text += ['B'] + ['M'] * (len(text) - 2) + ['E']
            return out_text

        init_parameters()
        line_num = 0

        # 观察者集合，主要是字、标点
        words = set()
        with open(path, encoding='utf-8') as f:
            for line in f:
                line_num += 1
                line = line.strip()
                if not line:
                    continue
                word_list = [i for i in line if i != ' ']
                # 更新字的集合
                words |= set(word_list)
                linelist = line.split()
                line_state = []
                for w in linelist:
                    line_state.extend(make_label(w))
                assert len(line_state) == len(word_list)

                for k, v in enumerate(line_state):
                    Count_dic[v] += 1
                    if k == 0:
                        # 每个句子中第一个字的状态，用于计算初始状态概率
                        self.Pi_dic[v] += 1
                    else:
                        # 计算转移概率
                        self.A_dic[line_state[k - 1]][v] += 1
                    # 计算发射概率
                    self.B_dic[line_state[k]][word_list[k]] = self.B_dic[line_state[k]].get(word_list[k], 0) + 1.0

        self.Pi_dic = {k: v / line_num for k, v in self.Pi_dic.items()}
        # P(当前状态 | 上一个状态) = 转移次数 / 上一个状态的总出现次数
        self.A_dic = {
            k: {k1: v1 / Count_dic[k] for k1, v1 in v.items()}
            for k, v in self.A_dic.items()
        }
        #  加1平滑：分子 v1 + 1，防止未登录词概率为0
        self.B_dic = {
            k: {k1: (v1 + 1) / (Count_dic[k] + len(words)) for k1, v1 in v.items()}
            for k, v in self.B_dic.items()
        }

        # 序列化
        with open(self.model_file, 'wb') as f:
            # pickle.dump(self.A_dic, f)
            # pickle.dump(self.B_dic, f)
            # pickle.dump(self.Pi_dic, f)
            print(self.B_dic)
            print(self.Pi_dic)
            print(self.A_dic)
        return self


if __name__ == '__main__':
    hmm = HMM()
    hmm.train('./data/train_data.txt')
