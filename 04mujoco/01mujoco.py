import time

import mujoco
import mujoco.viewer

# 木块自由落体：初始高度 1 m，重力 -9.81 m/s²，每 200 ms 打印一次高度
XML = """
<mujoco model="falling_block">
  <option gravity="0 0 -9.81" timestep="0.002"/>

  <asset>
    <texture name="grid" type="2d" builtin="checker"
             rgb1="0.2 0.3 0.2" rgb2="0.3 0.4 0.3"
             width="256" height="256"/>
    <material name="grid" texture="grid" texrepeat="8 8" reflectance="0.2"/>
    <material name="wood" rgba="0.76 0.54 0.32 1"/>
  </asset>

  <worldbody>
    <light pos="0 0 4"/>
    <geom name="floor" type="plane" size="2 2 0.1" material="grid"/>

    <body name="block" pos="0 0 1">
      <freejoint/>
      <geom type="box" size="0.05 0.05 0.05" material="wood" mass="0.5"/>
    </body>
  </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(XML)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)  # 根据初始 qpos 算出 xpos，才能立刻读到高度

block_id = model.body("block").id
print_dt = 0.2          # 200 ms
sim_duration = 1.5      # 仿真时长（秒）
next_print_t = 0.0

print("木块自由落体  |  初始高度 1 m  |  每 200 ms 打印一次")
print("-" * 42)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running() and data.time < sim_duration:
        step_start = time.time()

        if data.time + 1e-9 >= next_print_t:
            height = data.xpos[block_id, 2]
            print(f"t = {data.time * 1000:6.0f} ms  |  高度 = {height:.4f} m")
            next_print_t += print_dt

        mujoco.mj_step(model, data)
        viewer.sync()

        # 按物理步长对齐真实时间，方便肉眼看掉落
        leftover = model.opt.timestep - (time.time() - step_start)
        if leftover > 0:
            time.sleep(leftover)
