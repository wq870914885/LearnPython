import mujoco
import mujoco.viewer

XML = """
"""

model = mujoco.MjModel.from_xml_string(XML)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
