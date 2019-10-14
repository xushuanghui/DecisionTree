from sklearn.datasets import load_iris, load_boston, fetch_20newsgroups
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def decision():
    """
    决策树预测乘客数据
    :return:
    """
    #1、获取决策树预测乘客生存分类
    titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")

    # 2、确定特征值和目标值，缺失值处理，特征类别数据 -->one-hot编码
    x = titan[['pclass', 'age', 'sex']]

    y = titan[['survived']]

    #填充
    x['age'].fillna(x['age'].mean(),inplace=True)

    dic = DictVectorizer(sparse=False)

    # [["1st","2","female"],[]]--->[{"pclass":, "age":2, "sex: female"}, ]


    return  None




if __name__ == '__main__':
    decision()