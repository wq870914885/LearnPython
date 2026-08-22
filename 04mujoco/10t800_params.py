from pathlib import Path

import mujoco

# 打印 T800 关键状态：nq / nv / nu，以及 qpos、qvel、ctrl 的数量和当前值
XML_PATH = Path(__file__).resolve().parent / "assest_t800" / "t800.xml"

model = mujoco.MjModel.from_xml_path(str(XML_PATH))
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)

QPOS_N = {
    mujoco.mjtJoint.mjJNT_FREE: 7,
    mujoco.mjtJoint.mjJNT_BALL: 4,
    mujoco.mjtJoint.mjJNT_SLIDE: 1,
    mujoco.mjtJoint.mjJNT_HINGE: 1,
}
QVEL_N = {
    mujoco.mjtJoint.mjJNT_FREE: 6,
    mujoco.mjtJoint.mjJNT_BALL: 3,
    mujoco.mjtJoint.mjJNT_SLIDE: 1,
    mujoco.mjtJoint.mjJNT_HINGE: 1,
}

print("=" * 72)
print("数量（存在 MjModel 里，模型定了就不变）")
print("=" * 72)
print(f"nq   = {model.nq:3d}   qpos 长度，广义坐标")
print(f"nv   = {model.nv:3d}   qvel 长度，自由度")
print(f"nu   = {model.nu:3d}   ctrl 长度，执行器")
print(f"njnt = {model.njnt:3d}   关节个数")
print()
print("关系：free 关节占 qpos 7 个数、qvel 6 个数；每个 hinge 各占 1 个。")
print("T800：1 个 free + 25 个 hinge → nq=7+25=32，nv=6+25=31，nu=25（基座没有电机）")
print()

print("=" * 72)
print(f"qpos  长度 {model.nq}（关节位置 / 姿态）")
print("=" * 72)
print(f"{'idx':>4}  {'joint':<22} {'qpos':>10}")
print("-" * 42)
for i in range(model.njnt):
    name = model.joint(i).name or "(unnamed free)"
    adr = int(model.jnt_qposadr[i])
    n = QPOS_N[int(model.jnt_type[i])]
    for k in range(n):
        tag = name if n == 1 else f"{name}[{k}]"
        print(f"{adr + k:4d}  {tag:<22} {data.qpos[adr + k]:10.4f}")
print("向量:", " ".join(f"{v:.4f}" for v in data.qpos))
print()

print("=" * 72)
print(f"qvel  长度 {model.nv}（关节速度）")
print("=" * 72)
print(f"{'idx':>4}  {'joint':<22} {'qvel':>10}")
print("-" * 42)
for i in range(model.njnt):
    name = model.joint(i).name or "(unnamed free)"
    adr = int(model.jnt_dofadr[i])
    n = QVEL_N[int(model.jnt_type[i])]
    for k in range(n):
        tag = name if n == 1 else f"{name}[{k}]"
        print(f"{adr + k:4d}  {tag:<22} {data.qvel[adr + k]:10.4f}")
print("向量:", " ".join(f"{v:.4f}" for v in data.qvel))
print()

print("=" * 72)
print(f"ctrl  长度 {model.nu}（执行器控制量，这里是力矩）")
print("=" * 72)
print(f"{'idx':>4}  {'actuator':<28} {'ctrl':>10}")
print("-" * 48)
for i in range(model.nu):
    name = model.actuator(i).name
    print(f"{i:4d}  {name:<28} {data.ctrl[i]:10.4f}")
print("向量:", " ".join(f"{v:.4f}" for v in data.ctrl))

# nq   =  32   qpos 长度，广义坐标
# nv   =  31   qvel 长度，自由度
# nu   =  25   ctrl 长度，执行器
# njnt =  26   关节个数
#
# 关系：free 关节占 qpos 7 个数、qvel 6 个数；每个 hinge 各占 1 个。
# T800：1 个 free + 25 个 hinge → nq=7+25=32，nv=6+25=31，nu=25（基座没有电机）
#
# ========================================================================
# qpos  长度 32（关节位置 / 姿态）
# ========================================================================
#  idx  joint                        qpos
# ------------------------------------------
#    0  (unnamed free)[0]          0.0000
#    1  (unnamed free)[1]          0.0000
#    2  (unnamed free)[2]          1.0300
#    3  (unnamed free)[3]          1.0000
#    4  (unnamed free)[4]          0.0000
#    5  (unnamed free)[5]          0.0000
#    6  (unnamed free)[6]          0.0000
#    7  J00_HIP_PITCH_L            0.0000
#    8  J01_HIP_ROLL_L             0.0000
#    9  J02_HIP_YAW_L              0.0000
#   10  J03_KNEE_PITCH_L           0.0000
#   11  J04_ANKLE_PITCH_L          0.0000
#   12  J05_ANKLE_ROLL_L           0.0000
#   13  J06_HIP_PITCH_R            0.0000
#   14  J07_HIP_ROLL_R             0.0000
#   15  J08_HIP_YAW_R              0.0000
#   16  J09_KNEE_PITCH_R           0.0000
#   17  J10_ANKLE_PITCH_R          0.0000
#   18  J11_ANKLE_ROLL_R           0.0000
#   19  J12_TORSO_YAW              0.0000
#   20  J13_SHOULDER_PITCH_L       0.0000
#   21  J14_SHOULDER_ROLL_L        0.0000
#   22  J15_SHOULDER_YAW_L         0.0000
#   23  J16_ELBOW_PITCH_L          0.0000
#   24  J17_ELBOW_YAW_L            0.0000
#   25  J18_SHOULDER_PITCH_R       0.0000
#   26  J19_SHOULDER_ROLL_R        0.0000
#   27  J20_SHOULDER_YAW_R         0.0000
#   28  J21_ELBOW_PITCH_R          0.0000
#   29  J22_ELBOW_YAW_R            0.0000
#   30  J23_HEAD_PITCH             0.0000
#   31  J24_HEAD_YAW               0.0000
# 向量: 0.0000 0.0000 1.0300 1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
#
# ========================================================================
# qvel  长度 31（关节速度）
# ========================================================================
#  idx  joint                        qvel
# ------------------------------------------
#    0  (unnamed free)[0]          0.0000
#    1  (unnamed free)[1]          0.0000
#    2  (unnamed free)[2]          0.0000
#    3  (unnamed free)[3]          0.0000
#    4  (unnamed free)[4]          0.0000
#    5  (unnamed free)[5]          0.0000
#    6  J00_HIP_PITCH_L            0.0000
#    7  J01_HIP_ROLL_L             0.0000
#    8  J02_HIP_YAW_L              0.0000
#    9  J03_KNEE_PITCH_L           0.0000
#   10  J04_ANKLE_PITCH_L          0.0000
#   11  J05_ANKLE_ROLL_L           0.0000
#   12  J06_HIP_PITCH_R            0.0000
#   13  J07_HIP_ROLL_R             0.0000
#   14  J08_HIP_YAW_R              0.0000
#   15  J09_KNEE_PITCH_R           0.0000
#   16  J10_ANKLE_PITCH_R          0.0000
#   17  J11_ANKLE_ROLL_R           0.0000
#   18  J12_TORSO_YAW              0.0000
#   19  J13_SHOULDER_PITCH_L       0.0000
#   20  J14_SHOULDER_ROLL_L        0.0000
#   21  J15_SHOULDER_YAW_L         0.0000
#   22  J16_ELBOW_PITCH_L          0.0000
#   23  J17_ELBOW_YAW_L            0.0000
#   24  J18_SHOULDER_PITCH_R       0.0000
#   25  J19_SHOULDER_ROLL_R        0.0000
#   26  J20_SHOULDER_YAW_R         0.0000
#   27  J21_ELBOW_PITCH_R          0.0000
#   28  J22_ELBOW_YAW_R            0.0000
#   29  J23_HEAD_PITCH             0.0000
#   30  J24_HEAD_YAW               0.0000
# 向量: 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
#
# ========================================================================
# ctrl  长度 25（执行器控制量，这里是力矩）
# ========================================================================
#  idx  actuator                           ctrl
# ------------------------------------------------
#    0  motor_J00_HIP_PITCH_L            0.0000
#    1  motor_J01_HIP_ROLL_L             0.0000
#    2  motor_J02_HIP_YAW_L              0.0000
#    3  motor_J03_KNEE_PITCH_L           0.0000
#    4  motor_J04_ANKLE_PITCH_L          0.0000
#    5  motor_J05_ANKLE_ROLL_L           0.0000
#    6  motor_J06_HIP_PITCH_R            0.0000
#    7  motor_J07_HIP_ROLL_R             0.0000
#    8  motor_J08_HIP_YAW_R              0.0000
#    9  motor_J09_KNEE_PITCH_R           0.0000
#   10  motor_J10_ANKLE_PITCH_R          0.0000
#   11  motor_J11_ANKLE_ROLL_R           0.0000
#   12  motor_J12_TORSO_YAW              0.0000
#   13  motor_J13_SHOULDER_PITCH_L       0.0000
#   14  motor_J14_SHOULDER_ROLL_L        0.0000
#   15  motor_J15_SHOULDER_YAW_L         0.0000
#   16  motor_J16_ELBOW_PITCH_L          0.0000
#   17  motor_J17_ELBOW_YAW_L            0.0000
#   18  motor_J18_SHOULDER_PITCH_R       0.0000
#   19  motor_J19_SHOULDER_ROLL_R        0.0000
#   20  motor_J20_SHOULDER_YAW_R         0.0000
#   21  motor_J21_ELBOW_PITCH_R          0.0000
#   22  motor_J22_ELBOW_YAW_R            0.0000
#   23  motor_J23_HEAD_PITCH             0.0000
#   24  motor_J24_HEAD_YAW               0.0000
# 向量: 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000