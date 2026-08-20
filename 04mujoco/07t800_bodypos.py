from pathlib import Path

import mujoco

# 打印 T800 每个 body 的 body_pos（相对父连杆，XML 里的 pos）
XML_PATH = Path(__file__).resolve().parent / "assest_t800" / "t800.xml"

model = mujoco.MjModel.from_xml_path(str(XML_PATH))

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
print("body_pos：相对父连杆的位置（XML 里的 pos，存在 MjModel 里）")
print(f"{'id':>3}  {'name':<24} {'含义':<18} {'x':>9} {'y':>9} {'z':>9}")
print("-" * 80)

for i in range(model.nbody):
    name = model.body(i).name
    cn = LINK_CN.get(name, "")
    x, y, z = model.body_pos[i]
    print(f"{i:3d}  {name:<24} {cn:<18} {x:9.4f} {y:9.4f} {z:9.4f}")

# body_pos 相对父连杆，不随仿真变化
#   1  LINK_BASE          0.0000   0.0000   1.0300   （相对 world）
#   8  LINK_FOOT_L        0.0000   0.0000   0.0000   （贴在踝上）
#  30  LINK_HEAD_YAW      0.0000   0.0000   0.0402
