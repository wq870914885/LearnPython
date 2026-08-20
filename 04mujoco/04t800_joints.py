from pathlib import Path

import mujoco

# 打印 T800 的全部关节（名称、中文含义、类型、所属 body、当前 qpos）
XML_PATH = Path(__file__).resolve().parent / "assest_t800" / "t800.xml"

model = mujoco.MjModel.from_xml_path(str(XML_PATH))
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)

JOINT_TYPE = {
    mujoco.mjtJoint.mjJNT_FREE: "free",
    mujoco.mjtJoint.mjJNT_BALL: "ball",
    mujoco.mjtJoint.mjJNT_SLIDE: "slide",
    mujoco.mjtJoint.mjJNT_HINGE: "hinge",
}

# pitch 俯仰 / roll 滚转 / yaw 偏航；L 左 / R 右
JOINT_CN = {
    "(unnamed)": "基座自由关节：整机平移 + 转动",
    "J00_HIP_PITCH_L": "左髋俯仰：大腿前后摆",
    "J01_HIP_ROLL_L": "左髋滚转：大腿左右摆",
    "J02_HIP_YAW_L": "左髋偏航：大腿内外旋",
    "J03_KNEE_PITCH_L": "左膝俯仰：小腿屈伸",
    "J04_ANKLE_PITCH_L": "左踝俯仰：脚尖上下",
    "J05_ANKLE_ROLL_L": "左踝滚转：脚掌内外翻",
    "J06_HIP_PITCH_R": "右髋俯仰：大腿前后摆",
    "J07_HIP_ROLL_R": "右髋滚转：大腿左右摆",
    "J08_HIP_YAW_R": "右髋偏航：大腿内外旋",
    "J09_KNEE_PITCH_R": "右膝俯仰：小腿屈伸",
    "J10_ANKLE_PITCH_R": "右踝俯仰：脚尖上下",
    "J11_ANKLE_ROLL_R": "右踝滚转：脚掌内外翻",
    "J12_TORSO_YAW": "腰偏航：躯干左右转",
    "J13_SHOULDER_PITCH_L": "左肩俯仰：手臂前后摆",
    "J14_SHOULDER_ROLL_L": "左肩滚转：手臂左右抬",
    "J15_SHOULDER_YAW_L": "左肩偏航：上臂内外旋",
    "J16_ELBOW_PITCH_L": "左肘俯仰：前臂屈伸",
    "J17_ELBOW_YAW_L": "左肘偏航：前臂旋转",
    "J18_SHOULDER_PITCH_R": "右肩俯仰：手臂前后摆",
    "J19_SHOULDER_ROLL_R": "右肩滚转：手臂左右抬",
    "J20_SHOULDER_YAW_R": "右肩偏航：上臂内外旋",
    "J21_ELBOW_PITCH_R": "右肘俯仰：前臂屈伸",
    "J22_ELBOW_YAW_R": "右肘偏航：前臂旋转",
    "J23_HEAD_PITCH": "头俯仰：点头",
    "J24_HEAD_YAW": "头偏航：摇头",
}

print(f"T800 关节数量 njnt = {model.njnt}")
print(f"{'id':>3}  {'name':<22} {'type':<6} {'含义':<22} {'qposadr':>7}  qpos")
print("-" * 90)

for i in range(model.njnt):
    name = model.joint(i).name or "(unnamed)"
    jtype = JOINT_TYPE[int(model.jnt_type[i])]
    cn = JOINT_CN.get(name, "")
    adr = int(model.jnt_qposadr[i])
    nq = 7 if model.jnt_type[i] == mujoco.mjtJoint.mjJNT_FREE else 1
    qpos = data.qpos[adr : adr + nq]
    qpos_str = " ".join(f"{v:.4f}" for v in qpos)
    print(f"{i:3d}  {name:<22} {jtype:<6} {cn:<22} {adr:7d}  {qpos_str}")

# T800 关节数量 njnt = 26
#  id  name                   type   含义                      qposadr  qpos
# ------------------------------------------------------------------------------------------
#   0  (unnamed)              free   基座自由关节：整机平移 + 转动      0  0.0000 0.0000 1.0300 1.0000 0.0000 0.0000 0.0000
#   1  J00_HIP_PITCH_L        hinge  左髋俯仰：大腿前后摆             7  0.0000
#   2  J01_HIP_ROLL_L         hinge  左髋滚转：大腿左右摆             8  0.0000
#   3  J02_HIP_YAW_L          hinge  左髋偏航：大腿内外旋             9  0.0000
#   4  J03_KNEE_PITCH_L       hinge  左膝俯仰：小腿屈伸              10  0.0000
#   5  J04_ANKLE_PITCH_L      hinge  左踝俯仰：脚尖上下              11  0.0000
#   6  J05_ANKLE_ROLL_L       hinge  左踝滚转：脚掌内外翻             12  0.0000
#   7  J06_HIP_PITCH_R        hinge  右髋俯仰：大腿前后摆            13  0.0000
#   8  J07_HIP_ROLL_R         hinge  右髋滚转：大腿左右摆            14  0.0000
#   9  J08_HIP_YAW_R          hinge  右髋偏航：大腿内外旋            15  0.0000
#  10  J09_KNEE_PITCH_R       hinge  右膝俯仰：小腿屈伸              16  0.0000
#  11  J10_ANKLE_PITCH_R      hinge  右踝俯仰：脚尖上下              17  0.0000
#  12  J11_ANKLE_ROLL_R       hinge  右踝滚转：脚掌内外翻             18  0.0000
#  13  J12_TORSO_YAW          hinge  腰偏航：躯干左右转              19  0.0000
#  14  J13_SHOULDER_PITCH_L   hinge  左肩俯仰：手臂前后摆            20  0.0000
#  15  J14_SHOULDER_ROLL_L    hinge  左肩滚转：手臂左右抬            21  0.0000
#  16  J15_SHOULDER_YAW_L     hinge  左肩偏航：上臂内外旋            22  0.0000
#  17  J16_ELBOW_PITCH_L      hinge  左肘俯仰：前臂屈伸              23  0.0000
#  18  J17_ELBOW_YAW_L        hinge  左肘偏航：前臂旋转              24  0.0000
#  19  J18_SHOULDER_PITCH_R   hinge  右肩俯仰：手臂前后摆            25  0.0000
#  20  J19_SHOULDER_ROLL_R    hinge  右肩滚转：手臂左右抬            26  0.0000
#  21  J20_SHOULDER_YAW_R     hinge  右肩偏航：上臂内外旋            27  0.0000
#  22  J21_ELBOW_PITCH_R      hinge  右肘俯仰：前臂屈伸              28  0.0000
#  23  J22_ELBOW_YAW_R        hinge  右肘偏航：前臂旋转              29  0.0000
#  24  J23_HEAD_PITCH         hinge  头俯仰：点头                   30  0.0000
#  25  J24_HEAD_YAW           hinge  头偏航：摇头                   31  0.0000
