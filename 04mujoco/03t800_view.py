from pathlib import Path
import time

import mujoco
import mujoco.viewer

# 加载 T800 场景（机器人 + 地面），用 viewer 展示
XML_PATH = Path(__file__).resolve().parent / "assest_t800" / "t800.xml"

model = mujoco.MjModel.from_xml_path(str(XML_PATH))
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)

print(f"已加载 T800  |  body={model.nbody}  nq={model.nq}")
print("关闭窗口结束")

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        step_start = time.time()

        mujoco.mj_step(model, data)  # 推进物理一步；没有控制器时机器人会倒下
        viewer.sync()

        leftover = model.opt.timestep - (time.time() - step_start)
        if leftover > 0:
            time.sleep(leftover)
