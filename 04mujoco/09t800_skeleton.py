from pathlib import Path

import matplotlib
# Cursor / 终端常默认 Agg（只出静态图）。必须在 import pyplot 之前切到可交互后端。
matplotlib.use("TkAgg", force=True)
import matplotlib.pyplot as plt
import mujoco
import numpy as np

# 用每个 body 的 xpos + 父子关系，画出 T800 骨架
XML_PATH = Path(__file__).resolve().parent / "assest_t800" / "t800.xml"

model = mujoco.MjModel.from_xml_path(str(XML_PATH))
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)

# Windows 下显示中文
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

LABEL = {
    "LINK_BASE": "基座",
    "LINK_FOOT_L": "左脚",
    "LINK_FOOT_R": "右脚",
    "LINK_WRIST_END_L": "左腕",
    "LINK_WRIST_END_R": "右腕",
    "LINK_HEAD_YAW": "头",
    "LINK_WAIST_YAW": "腰",
}


def limb_color(name):
    if name.endswith("_L"):
        return "C0"  # 左蓝
    if name.endswith("_R"):
        return "C3"  # 右红
    return "0.25"  # 躯干 / 头


def set_axes_equal(ax):
    limits = np.array([ax.get_xlim3d(), ax.get_ylim3d(), ax.get_zlim3d()])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    ax.set_xlim3d(origin[0] - radius, origin[0] + radius)
    ax.set_ylim3d(origin[1] - radius, origin[1] + radius)
    ax.set_zlim3d(origin[2] - radius, origin[2] + radius)


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

# 地面参考（z = 0）
g = 0.4
ax.plot_surface(
    np.array([[-g, g], [-g, g]]),
    np.array([[-g, -g], [g, g]]),
    np.zeros((2, 2)),
    color="0.85",
    alpha=0.35,
    zorder=0,
)

# 从父 body 连到子 body：这就是骨架
for i in range(1, model.nbody):  # 跳过 world
    name = model.body(i).name
    color = limb_color(name)
    child = data.xpos[i]
    parent_id = int(model.body_parentid[i])
    if parent_id != 0:
        parent = data.xpos[parent_id]
        ax.plot(
            [parent[0], child[0]],
            [parent[1], child[1]],
            [parent[2], child[2]],
            color=color,
            linewidth=2.5,
        )
    ax.scatter(child[0], child[1], child[2], color=color, s=25, depthshade=False)

    if name in LABEL:
        ax.text(child[0], child[1], child[2] + 0.03, LABEL[name], fontsize=9)

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("z (m)")
ax.set_title("T800 骨架（由 data.xpos 连父子 body）")
ax.view_init(elev=15, azim=-70)
set_axes_equal(ax)
plt.tight_layout()
print("弹出独立窗口后：按住鼠标左键拖动即可旋转，滚轮缩放。关闭窗口结束。")
plt.show(block=True)
