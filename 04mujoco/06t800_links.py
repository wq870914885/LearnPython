from pathlib import Path

import numpy as np
import mujoco

# 打印 T800 连杆：名字、尺寸（网格包围盒）、重量
XML_PATH = Path(__file__).resolve().parent / "assest_t800" / "t800.xml"

model = mujoco.MjModel.from_xml_path(str(XML_PATH))
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)

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


def _rotate(points, quat, pos):
    mat = np.zeros(9)
    mujoco.mju_quat2Mat(mat, np.asarray(quat, dtype=np.float64))
    return points @ mat.reshape(3, 3).T + pos


def geom_points(model, gid):
    """几何体在连杆坐标系下的采样点，用来算包围盒。"""
    gtype = model.geom_type[gid]
    pos = model.geom_pos[gid]
    quat = model.geom_quat[gid]
    size = model.geom_size[gid]

    if gtype == mujoco.mjtGeom.mjGEOM_MESH:
        mid = int(model.geom_dataid[gid])
        adr = int(model.mesh_vertadr[mid])
        num = int(model.mesh_vertnum[mid])
        pts = np.array(model.mesh_vert[adr : adr + num], dtype=np.float64)
        return _rotate(pts, quat, pos)

    if gtype == mujoco.mjtGeom.mjGEOM_BOX:
        sx, sy, sz = size
        corners = np.array(
            [[x, y, z] for x in (-sx, sx) for y in (-sy, sy) for z in (-sz, sz)],
            dtype=np.float64,
        )
        return _rotate(corners, quat, pos)

    if gtype == mujoco.mjtGeom.mjGEOM_SPHERE:
        r = float(size[0])
        corners = np.array(
            [[x, y, z] for x in (-r, r) for y in (-r, r) for z in (-r, r)],
            dtype=np.float64,
        )
        return _rotate(corners, quat, pos)

    if gtype == mujoco.mjtGeom.mjGEOM_CYLINDER:
        r, h = float(size[0]), float(size[1])
        corners = np.array(
            [[x, y, z] for x in (-r, r) for y in (-r, r) for z in (-h, h)],
            dtype=np.float64,
        )
        return _rotate(corners, quat, pos)

    return None


def body_size_xyz(model, body_id):
    """连杆尺寸：优先用视觉网格包围盒；没有网格（脚、腕）则用碰撞体。"""
    visual, other = [], []
    for g in range(model.ngeom):
        if int(model.geom_bodyid[g]) != body_id:
            continue
        if model.geom_type[g] == mujoco.mjtGeom.mjGEOM_PLANE:
            continue
        (visual if model.geom_group[g] == 2 else other).append(g)

    chunks = []
    for g in visual or other:
        pts = geom_points(model, g)
        if pts is not None and len(pts):
            chunks.append(pts)
    if not chunks:
        return None
    pts = np.vstack(chunks)
    return pts.max(axis=0) - pts.min(axis=0)


print(f"T800 连杆数量 nbody = {model.nbody}（含 world）")
print(f"{'id':>3}  {'name':<24} {'含义':<22} {'尺寸 xyz (m)':<28} {'重量(kg)':>8}")
print("-" * 95)

total_mass = 0.0
for i in range(model.nbody):
    name = model.body(i).name
    cn = LINK_CN.get(name, "")
    mass = float(model.body_mass[i])
    total_mass += mass
    size = body_size_xyz(model, i)
    if size is None:
        size_str = "—"
    else:
        size_str = f"{size[0]:.3f} x {size[1]:.3f} x {size[2]:.3f}"
    print(f"{i:3d}  {name:<24} {cn:<22} {size_str:<28} {mass:8.3f}")

print("-" * 95)
print(f"整机重量合计: {total_mass:.3f} kg")

# 尺寸来自视觉网格包围盒；脚 / 腕没有网格，用碰撞体近似
#  T800 连杆数量 nbody = 31（含 world）
#  id  name                     含义                     尺寸 xyz (m)                     重量(kg)
# -----------------------------------------------------------------------------------------------
#   0  world                    世界坐标系（不是机器人连杆）         —                               0.000
#   1  LINK_BASE                基座 / 骨盆                0.207 x 0.194 x 0.198          10.083
#   2  LINK_HIP_PITCH_L         左髋俯仰连杆                 0.151 x 0.131 x 0.241           3.536
#   3  LINK_HIP_ROLL_L          左髋滚转连杆                 0.146 x 0.141 x 0.144           0.851
#   4  LINK_HIP_YAW_L           左髋偏航连杆                 0.188 x 0.152 x 0.356           7.195
#   5  LINK_KNEE_PITCH_L        左膝俯仰连杆（大腿）             0.182 x 0.134 x 0.538           5.995
#   6  LINK_ANKLE_PITCH_L       左踝俯仰连杆（小腿）             0.071 x 0.047 x 0.073           0.144
#   7  LINK_ANKLE_ROLL_L        左踝滚转连杆                 0.269 x 0.118 x 0.112           1.494
#   8  LINK_FOOT_L              左脚                     0.270 x 0.110 x 0.037           0.001
#   9  LINK_HIP_PITCH_R         右髋俯仰连杆                 0.151 x 0.131 x 0.241           3.536
#  10  LINK_HIP_ROLL_R          右髋滚转连杆                 0.146 x 0.141 x 0.144           0.851
#  11  LINK_HIP_YAW_R           右髋偏航连杆                 0.188 x 0.152 x 0.356           7.195
#  12  LINK_KNEE_PITCH_R        右膝俯仰连杆（大腿）             0.182 x 0.134 x 0.538           5.995
#  13  LINK_ANKLE_PITCH_R       右踝俯仰连杆（小腿）             0.071 x 0.047 x 0.073           0.144
#  14  LINK_ANKLE_ROLL_R        右踝滚转连杆                 0.269 x 0.118 x 0.112           1.494
#  15  LINK_FOOT_R              右脚                     0.270 x 0.110 x 0.037           0.001
#  16  LINK_WAIST_YAW           腰偏航连杆                  0.268 x 0.334 x 0.442          19.411
#  17  LINK_SHOULDER_PITCH_L    左肩俯仰连杆                 0.130 x 0.131 x 0.142           1.769
#  18  LINK_SHOULDER_ROLL_L     左肩滚转连杆                 0.122 x 0.106 x 0.139           0.683
#  19  LINK_SHOULDER_YAW_L      左肩偏航连杆                 0.099 x 0.096 x 0.200           2.552
#  20  LINK_ELBOW_PITCH_L       左肘俯仰连杆（上臂）             0.102 x 0.106 x 0.189           1.195
#  21  LINK_ELBOW_YAW_L         左肘偏航连杆（前臂）             0.137 x 0.102 x 0.256           1.079
#  22  LINK_WRIST_END_L         左腕末端                   0.100 x 0.100 x 0.100           0.001
#  23  LINK_SHOULDER_PITCH_R    右肩俯仰连杆                 0.130 x 0.131 x 0.142           1.769
#  24  LINK_SHOULDER_ROLL_R     右肩滚转连杆                 0.122 x 0.106 x 0.139           0.683
#  25  LINK_SHOULDER_YAW_R      右肩偏航连杆                 0.099 x 0.096 x 0.200           2.552
#  26  LINK_ELBOW_PITCH_R       右肘俯仰连杆（上臂）             0.102 x 0.106 x 0.189           1.195
#  27  LINK_ELBOW_YAW_R         右肘偏航连杆（前臂）             0.137 x 0.102 x 0.256           1.079
#  28  LINK_WRIST_END_R         右腕末端                   0.100 x 0.100 x 0.100           0.001
#  29  LINK_HEAD_PITCH          头俯仰连杆                  0.039 x 0.065 x 0.039           0.708
#  30  LINK_HEAD_YAW            头偏航连杆                  0.210 x 0.164 x 0.217           1.724
# -----------------------------------------------------------------------------------------------
# 整机重量合计: 84.917 kg