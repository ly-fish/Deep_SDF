import numpy as np
import matplotlib.pyplot as plt
 
def plot_npz():
    with np.load('./sample.npz') as data:
       points = data['neg']
    x, y, z, sdf = points[:, 0], points[:, 1], points[:, 2], points[:, 3]
 
    sample_size = int(len(x) * 0.09)  # 选择50%的点
    random_indices = np.random.choice(len(x), sample_size, replace=False)
    x, y, z = x[random_indices], y[random_indices], z[random_indices]
 
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
 
   # 初始化一个形状和points相同的RGBA颜色数组
    colors = np.zeros((x.shape[0], 4))
   # SDF > 0 的点设置为蓝色且不透明
    colors[:] = [0, 0, 1, 1]  # 蓝色
 
    sc = ax.scatter(x, y, z, c=colors, marker='o', alpha=0.1)
 
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('3D Scatter Plot of Points by SDF Value')
 
    plt.show()
 
if __name__=="__main__":
    plot_npz()