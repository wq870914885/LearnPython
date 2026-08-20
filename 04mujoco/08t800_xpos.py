from pathlib import Path

import mujoco

# 打印 T800 每个 body 的 xpos（世界坐标系下的位置）
XML_PATH = Path(__file__).resolve().parent / "assest_t800" / "t800.xml"

model = mujoco.MjModel.from_xml_path(str(XML_PATH))
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)  # 根据 qpos 算出 xpos，才能读到世界坐标

LINK_CN = {
    "world": "世界坐标系（不是机器人连杆）",
    "LINK_BASE": "基座 / 骨盆",
    "LINK_HIP_PITCH_L": "左髋俯仰连杆",
    "LINK_HIP_ROLL_L": "左髋滚转连杆",
    "LINK_HIP_YAW_L": "左髋偏航连杆",
    "LINK_KNEE_PITCH_L": "左膝俯仰连杆（大腿）",
    "LINK_ANKLE_PITCH_L": "左踝俯仰连杆（小腿）",
    "LINK_ANKLE_ROLL_L": "左踝滚转连杆",
    "LINK_FOOT_L": "左脚",
    "LINK_HIP_PITCH_R": "右髋俯仰连杆",
    "LINK_HIP_ROLL_R": "右髋滚转连杆",
    "LINK_HIP_YAW_R": "右髋偏航连杆",
    "LINK_KNEE_PITCH_R": "右膝俯仰连杆（大腿）",
    "LINK_ANKLE_PITCH_R": "右踝俯仰连杆（小腿）",
    "LINK_ANKLE_ROLL_R": "右踝滚转连杆",
    "LINK_FOOT_R": "右脚",
    "LINK_WAIST_YAW": "腰偏航连杆",
    "LINK_SHOULDER_PITCH_L": "左肩俯仰连杆",
    "LINK_SHOULDER_ROLL_L": "左肩滚转连杆",
    "LINK_SHOULDER_YAW_L": "左肩偏航连杆",
    "LINK_ELBOW_PITCH_L": "左肘俯仰连杆（上臂）",
    "LINK_ELBOW_YAW_L": "左肘偏航连杆（前臂）",
    "LINK_WRIST_END_L": "左腕末端",
    "LINK_SHOULDER_PITCH_R": "右肩俯仰连杆",
    "LINK_SHOULDER_ROLL_R": "右肩滚转连杆",
    "LINK_SHOULDER_YAW_R": "右肩偏航连杆",
    "LINK_ELBOW_PITCH_R": "右肘俯仰连杆（上臂）",
    "LINK_ELBOW_YAW_R": "右肘偏航连杆（前臂）",
    "LINK_WRIST_END_R": "右腕末端",
    "LINK_HEAD_PITCH": "头俯仰连杆",
    "LINK_HEAD_YAW": "头偏航连杆",
}

print(f"T800 body 数量 nbody = {model.nbody}")
print("xpos：世界坐标系下 body 原点位置（存在 MjData 里，关节一动就会变）")
print(f"{'id':>3}  {'name':<24} {'含义':<18} {'x':>9} {'y':>9} {'z':>9}")
print("-" * 80)

for i in range(model.nbody):
    name = model.body(i).name
    cn = LINK_CN.get(name, "")
    x, y, z = data.xpos[i]
    print(f"{i:3d}  {name:<24} {cn:<18} {x:9.4f} {y:9.4f} {z:9.4f}")

# T800 body 数量 nbody = 31
# xpos：世界坐标系下 body 原点位置（存在 MjData 里，关节一动就会变）
#  id  name                     含义                         x         y         z
# --------------------------------------------------------------------------------
#   0  world                    世界坐标系（不是机器人连杆）        0.0000    0.0000    0.0000
#   1  LINK_BASE                基座 / 骨盆               0.0000    0.0000    1.0300
#   2  LINK_HIP_PITCH_L         左髋俯仰连杆                0.0000    0.0792    1.0300
#   3  LINK_HIP_ROLL_L          左髋滚转连杆                0.0047    0.1195    0.9225
#   4  LINK_HIP_YAW_L           左髋偏航连杆                0.0141    0.1195    0.8420
#   5  LINK_KNEE_PITCH_L        左膝俯仰连杆（大腿）           -0.0236    0.1195    0.5540
#   6  LINK_ANKLE_PITCH_L       左踝俯仰连杆（小腿）           -0.0263    0.1195    0.1154
#   7  LINK_ANKLE_ROLL_L        左踝滚转连杆               -0.0252    0.1195    0.0774
#   8  LINK_FOOT_L              左脚                   -0.0252    0.1195    0.0774
#   9  LINK_HIP_PITCH_R         右髋俯仰连杆                0.0000   -0.0792    1.0300
#  10  LINK_HIP_ROLL_R          右髋滚转连杆                0.0047   -0.1195    0.9225
#  11  LINK_HIP_YAW_R           右髋偏航连杆                0.0141   -0.1195    0.8420
#  12  LINK_KNEE_PITCH_R        右膝俯仰连杆（大腿）           -0.0236   -0.1195    0.5540
#  13  LINK_ANKLE_PITCH_R       右踝俯仰连杆（小腿）           -0.0263   -0.1195    0.1154
#  14  LINK_ANKLE_ROLL_R        右踝滚转连杆               -0.0252   -0.1195    0.0774
#  15  LINK_FOOT_R              右脚                   -0.0252   -0.1195    0.0774
#  16  LINK_WAIST_YAW           腰偏航连杆                 0.0000    0.0000    1.1338
#  17  LINK_SHOULDER_PITCH_L    左肩俯仰连杆               -0.0110    0.1630    1.4127
#  18  LINK_SHOULDER_ROLL_L     左肩滚转连杆               -0.0110    0.2256    1.3973
#  19  LINK_SHOULDER_YAW_L      左肩偏航连杆               -0.0110    0.2341    1.3146
#  20  LINK_ELBOW_PITCH_L       左肘俯仰连杆（上臂）           -0.0090    0.2477    1.1638
#  21  LINK_ELBOW_YAW_L         左肘偏航连杆（前臂）           -0.0112    0.2571    1.0320
#  22  LINK_WRIST_END_L         左腕末端                  0.0182    0.2696    0.8998
#  23  LINK_SHOULDER_PITCH_R    右肩俯仰连杆               -0.0110   -0.1630    1.4127
#  24  LINK_SHOULDER_ROLL_R     右肩滚转连杆               -0.0110   -0.2256    1.3973
#  25  LINK_SHOULDER_YAW_R      右肩偏航连杆               -0.0110   -0.2341    1.3146
#  26  LINK_ELBOW_PITCH_R       右肘俯仰连杆（上臂）           -0.0090   -0.2477    1.1638
#  27  LINK_ELBOW_YAW_R         右肘偏航连杆（前臂）           -0.0112   -0.2571    1.0320
#  28  LINK_WRIST_END_R         右腕末端                  0.0182   -0.2696    0.8998
#  29  LINK_HEAD_PITCH          头俯仰连杆                -0.0113    0.0000    1.5199
#  30  LINK_HEAD_YAW            头偏航连杆                -0.0113    0.0000    1.5601
