
# 用于处理训练用的csv数据
def data_preprocess():
    f = open("./phase1/trace1_train1/dex.txt")
    f1 = open("./phase1/trace1_train1/sandbox_behaviorlist.txt")
    f2 = open("./phase1/trace1_train1/safetype.txt")
    line = f.readline()
    line1 = f1.readline()
    line2 = f2.readline()

    dex_dict = {}

    line = f.readline()
    line1 = f1.readline()
    line2 = f2.readline()
    while line:
        # print(line)
        line = line.strip('\n')
        tmp = str.split(line,";")
        # print(tmp[0],tmp[1:])
        tmp_append = str.split(tmp[8],",")
        # print(tmp_append)
        # print(len(tmp_append))
        # print(tmp[1:])
        del tmp[8]
        # tmp_append1 = str.split(tmp[8], ",")
        del tmp[8]
        dex_dict[tmp[0]] = tmp[1:] + tmp_append
        # print(len(dex_dict[tmp[0]]))
        line = f.readline()
    f.close()

    # while line1:
    #     line1 = line1.strip('\n')
    #     tmp = str.split(line1,";")
    #     # print(dex_dict[tmp[0]])
    #     dex_dict[tmp[0]] = dex_dict[tmp[0]]+(tmp[1:])
    #     # print(dex_dict[tmp[0]])
    #     line1 = f1.readline()
    #
    # f1.close()

    while line2:
        line2 = line2.strip('\n')
        tmp = str.split(line2, ";")
        # print(tmp[0], tmp[1:], dex_dict[tmp[0]])
        dex_dict[tmp[0]] = dex_dict[tmp[0]]+(tmp[1:])
        line2 = f2.readline()

    f2.close()

    # for k in dex_dict.keys():
    #     print(len(dex_dict[k]))

    f = open("./phase1/trace1_train2/dex.txt")
    f1 = open("./phase1/trace1_train2/sandbox_behaviorlist.txt")
    f2 = open("./phase1/trace1_train2/safetype.txt")
    line = f.readline()
    line1 = f1.readline()
    line2 = f2.readline()

    line = f.readline()
    line1 = f1.readline()
    line2 = f2.readline()
    while line:
        # print(line)
        line = line.strip('\n')
        tmp = str.split(line, ";")
        # print(tmp[0],tmp[1:])
        tmp_append = str.split(tmp[8], ",")
        # print(tmp_append)
        # print(len(tmp_append))
        # print(tmp[1:])
        del tmp[8]
        # tmp_append1 = str.split(tmp[8], ",")
        del tmp[8]
        dex_dict[tmp[0]] = tmp[1:] + tmp_append
        # print(len(dex_dict[tmp[0]]))
        line = f.readline()
    f.close()

    # while line1:
    #     line1 = line1.strip('\n')
    #     tmp = str.split(line1,";")
    #     # print(dex_dict[tmp[0]])
    #     dex_dict[tmp[0]] = dex_dict[tmp[0]]+(tmp[1:])
    #     # print(dex_dict[tmp[0]])
    #     line1 = f1.readline()
    #
    # f1.close()

    while line2:
        line2 = line2.strip('\n')
        tmp = str.split(line2, ";")
        # print(tmp[0], tmp[1:], dex_dict[tmp[0]])
        dex_dict[tmp[0]] = dex_dict[tmp[0]] + (tmp[1:])
        line2 = f2.readline()

    f2.close()



    return dex_dict

# 用于处理测试用的csv数据
def test_data_preprocess():
    f = open("./phase2/trace1_test/dex.txt")
    f1 = open("./phase2/trace1_test/sandbox_behaviorlist.txt")
    f2 = open("./phase2/trace1_test/safetype.txt")
    line = f.readline()
    line1 = f1.readline()
    line2 = f2.readline()

    dex_dict = {}

    line = f.readline()
    line1 = f1.readline()
    line2 = f2.readline()
    while line:
        # print(line)
        line = line.strip('\n')
        tmp = str.split(line,";")
        # print(tmp[0],tmp[1:])
        tmp_append = str.split(tmp[8],",")
        # print(tmp_append)
        # print(len(tmp_append))
        # print(tmp[1:])
        del tmp[8]
        # tmp_append1 = str.split(tmp[8], ",")
        del tmp[8]
        dex_dict[tmp[0]] = tmp[1:] + tmp_append
        # print(len(dex_dict[tmp[0]]))
        line = f.readline()
    f.close()

    return dex_dict

# 用于转换测试数据成可用形式
def test_data_transform(test_data_dict):

    X= []

    for k in test_data_dict.keys():
        tmp_list = []
        len1 = len(test_data_dict[k])
        for i in range(len1):
            tmp_list.append(float(test_data_dict[k][i]))
        X.append(tmp_list)

    print("Finish test data processing...")

    return X

# 用于转换训练数据成可用形式
def data_transform(data_dict):

    X, y = [],[]

    for k in data_dict.keys():
        tmp_list = []
        len1 = len(data_dict[k])
        for i in range(len1-2):
            tmp_list.append(float(data_dict[k][i]))
        X.append(tmp_list)
        y.append(int(data_dict[k][-1]))

    print("Finish data processing...Start to train")

    return X, y
    # print(X, y)

from sklearn.datasets import load_iris
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


data = data_preprocess()
X, y = data_transform(data)


test_data = test_data_preprocess()
test_X = test_data_transform(test_data)


# iris = load_iris()

# X = iris.data
# y = iris.target



# print(X, y)
#
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234565)

# xgboost参数设置
params = {
    'booster': 'gbtree',
    'objective': 'multi:softmax',
    'num_class':6,
    'gamma': 0.1,
    'max_depth': 6,
    'lambda': 2,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 3,
    'silent': 1,
    'eta': 0.1,
    'seed': 1000,
    'nthread': 8,
}

plst = params.items()
dtrain = xgb.DMatrix(X_train, y_train)
num_round = 2000
# 模型训练
# model = xgb.train(plst, dtrain, num_round)
# 加载模型
model = xgb.Booster(model_file="xgb.model")
# dtest = xgb.DMatrix(X_test)
# ans = model.predict(dtest)
#
# print(ans)
dtest_test = xgb.DMatrix(test_X)
ans1 = model.predict(dtest_test)
print(ans1)

import pandas as pd
name_list, type_list, id_list = [], [], []
count_num = 0
for k in test_data.keys():
    name_list.append(k)
    id = int(ans1[count_num])
    type = 0 if id == 0 else 1
    type_list.append(type)
    id_list.append(id)
    count_num += 1

print(name_list, type_list, id_list)
dataframe = pd.DataFrame({"family_id":id_list,"safe_type":type_list,
                          "sha1": name_list})

dataframe.to_csv("trace1-phase2.csv",index=False,sep=",")


# model.save_model('xgb-2000.model')

# cnt1 = 0
# cnt2 = 0
# for i in range(len(y_test)):
#     if ans[i] == y_test[i]:
#         cnt1 += 1
#     else:
#         cnt2 += 1
#
# print("Accuracy: %.2f %%" % (100 * cnt1 / (cnt1 + cnt2)))
# plot_importance(model)
# plt.show()